#!/usr/bin/env python3
"""Scan public GitHub activity for the repos in digest/watchlist.yml.

Uses only the Python standard library. Reads GITHUB_TOKEN or GH_TOKEN from the
environment if set; otherwise makes unauthenticated calls (lower rate limit).

Writes digest/data/YYYY-MM-DD.json and prints a short markdown summary.
"""

import argparse
import collections
import datetime as dt
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.github.com"
DEPS = "https://api.deps.dev"
HERE = os.path.dirname(os.path.abspath(__file__))
MAX_PAGES = 10
ISO = "%Y-%m-%dT%H:%M:%SZ"


class NotFound(Exception):
    pass


class RateLimited(Exception):
    pass


def token():
    return os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""


def request(path, params=None):
    """GET a GitHub API path. Returns (json, headers)."""
    url = path if path.startswith("http") else API + path
    if params:
        url += ("&" if "?" in url else "?") + urllib.parse.urlencode(params)
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "jappa-labs-digest-scan",
    }
    tok = token()
    for attempt in range(3):
        req = urllib.request.Request(url, headers=headers)
        if tok and url.startswith(API + "/"):  # never send the GitHub token elsewhere
            req.add_unredirected_header("Authorization", "Bearer " + tok)  # not forwarded on redirects
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                body = resp.read().decode("utf-8")
                return (json.loads(body) if body else None), resp.headers
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise NotFound(url)
            if e.code == 409:  # empty repository
                return [], e.headers
            if e.code in (403, 429):
                raise RateLimited(url)
            if e.code < 500 or attempt == 2:
                raise
        except urllib.error.URLError:
            if attempt == 2:
                raise
        time.sleep(2 * (attempt + 1))  # transient server or network error


def next_link(headers):
    link = headers.get("Link") if headers else None
    if not link:
        return None
    for part in link.split(","):
        seg = part.split(";")
        if len(seg) >= 2 and 'rel="next"' in seg[1]:
            return seg[0].strip()[1:-1]
    return None


def paginate(path, params, stop=None):
    """Yield items across pages. `stop(item)` returning True ends iteration."""
    data, headers = request(path, params)
    pages = 1
    while True:
        for item in data or []:
            if stop and stop(item):
                return
            yield item
        url = next_link(headers)
        if not url or pages >= MAX_PAGES:
            return
        data, headers = request(url)
        pages += 1


def parse_time(s):
    if not s:
        return None
    return dt.datetime.strptime(s, ISO).replace(tzinfo=dt.timezone.utc)


def load_watchlist(path):
    """Minimal parser for the watchlist format (no third-party YAML needed)."""
    repos, group, current = [], None, None
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.split(" #")[0].rstrip() if not raw.lstrip().startswith("#") else ""
            if not line.strip():
                continue
            if not line.startswith(" ") and line.endswith(":"):
                group = line[:-1].strip()
                continue
            stripped = line.strip()
            if stripped.startswith("- "):
                current = {"group": group}
                repos.append(current)
                stripped = stripped[2:]
            if ":" in stripped and current is not None:
                key, val = stripped.split(":", 1)
                current[key.strip()] = val.strip().strip("'\"")
    return [r for r in repos if r.get("repo")]


def fork_history(name, created_at):
    """Forks created per month (YYYY-MM -> count), from repo creation to now.

    Only forks that still exist are listed by GitHub, and at most MAX_PAGES
    pages are read (newest first, so recent months stay exact), so the total
    can be below the repo's fork count.
    """
    months = collections.Counter()
    for f in paginate(f"/repos/{name}/forks", {"sort": "newest", "per_page": 100}):
        if f.get("created_at"):
            months[f["created_at"][:7]] += 1
    now = dt.datetime.now(dt.timezone.utc)
    start = parse_time(created_at) or now
    y, m = start.year, start.month
    out = {}
    while (y, m) <= (now.year, now.month):
        key = f"{y:04d}-{m:02d}"
        out[key] = months.get(key, 0)
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    return out


def dependents(name):
    """Dependents of the repo's published package, from deps.dev; None if unknown.

    Picks the non-Go package that deps.dev links to this repo most often (Go
    entries are skipped: deps.dev lists every GitHub repo as a Go module) and
    returns the dependent count of its default version. Any package can claim a
    repo in its metadata, so an unverified link counts only if the package name
    ends in the repo name.
    """
    def norm(s):
        return s.lower().replace("-", "").replace("_", "")

    try:
        q = urllib.parse.quote
        data, _ = request(f"{DEPS}/v3alpha/projects/{q('github.com/' + name, safe='')}:packageversions")
        pkgs = collections.Counter((k["system"], k["name"]) for v in (data or {}).get("versions", [])
                                   for k in [v["versionKey"]] if k["system"] != "GO"
                                   and (v.get("relationProvenance") != "UNVERIFIED_METADATA"
                                        or norm(k["name"].replace(":", "/").rsplit("/", 1)[-1]) == norm(name.split("/")[-1])))
        if not pkgs:
            return None
        system, pkg = pkgs.most_common(1)[0][0]
        info, _ = request(f"{DEPS}/v3/systems/{system}/packages/{q(pkg, safe='')}")
        version = next((v["versionKey"]["version"] for v in (info or {}).get("versions", []) if v.get("isDefault")), None)
        if not version:
            return None
        deps, _ = request(f"{DEPS}/v3alpha/systems/{system}/packages/{q(pkg, safe='')}/versions/{q(version, safe='')}:dependents")
        return {"system": system.lower(), "package": pkg, "version": version, "count": (deps or {}).get("dependentCount")}
    except (NotFound, RateLimited, OSError, ValueError, KeyError):  # OSError covers URLError and timeouts
        return None


def scan_repo(entry, since, detail_since):
    """Counts cover `since` onwards; item lists keep only items created or
    updated since `detail_since`."""
    name = entry["repo"]

    def recent(*stamps):
        return any(parse_time(t) >= detail_since for t in stamps if t)
    since_iso = since.strftime(ISO)
    out = {
        "repo": name,
        "url": "https://github.com/" + name,
        "group": entry.get("group"),
        "category": entry.get("category"),
        "description": entry.get("description"),
        "status": "ok",
    }
    try:
        meta, _ = request(f"/repos/{name}")
    except NotFound:
        out["status"] = "not_found"
        return out
    except RateLimited:
        out["status"] = "rate_limited"
        return out

    lic = meta.get("license") or {}
    branch = meta.get("default_branch")
    out.update({
        "default_branch": branch,
        "stars": meta.get("stargazers_count"),
        "forks": meta.get("forks_count"),
        "open_issues": meta.get("open_issues_count"),
        "license": lic.get("spdx_id") if lic.get("spdx_id") not in (None, "NOASSERTION") else (lic.get("name") or None),
        "archived": meta.get("archived"),
        "created_at": meta.get("created_at"),
        "pushed_at": meta.get("pushed_at"),
        "github_description": meta.get("description"),
    })

    try:
        # Commits on the default branch (solo repos often push straight to main).
        commits = []
        for c in paginate(f"/repos/{name}/commits", {"sha": branch, "since": since_iso, "per_page": 100}):
            author = (c.get("author") or {}).get("login") or ((c.get("commit") or {}).get("author") or {}).get("name")
            msg = ((c.get("commit") or {}).get("message") or "").split("\n", 1)[0]
            date = ((c.get("commit") or {}).get("committer") or {}).get("date")
            commits.append({"sha": c.get("sha", "")[:7], "author": author, "message": msg, "date": date})
        authors = sorted({c["author"] for c in commits if c["author"]})
        latest, _ = request(f"/repos/{name}/commits", {"sha": branch, "per_page": 1})
        last_commit = None
        if latest:
            last_commit = ((latest[0].get("commit") or {}).get("committer") or {}).get("date")
        out["commits"] = {"count": len(commits), "authors": authors, "last_commit_at": last_commit,
                          "items": [c for c in commits if recent(c["date"])]}

        # Pull requests opened and merged in the window.
        opened, merged, n_opened, n_merged = [], [], 0, 0
        for p in paginate(f"/repos/{name}/pulls", {"state": "all", "sort": "updated", "direction": "desc", "per_page": 100},
                          stop=lambda p: (parse_time(p.get("updated_at")) or since) < since):
            info = {"number": p.get("number"), "title": p.get("title"), "author": (p.get("user") or {}).get("login"), "url": p.get("html_url")}
            keep = recent(p.get("created_at"), p.get("updated_at"))
            if (parse_time(p.get("created_at")) or since) >= since and p.get("created_at"):
                n_opened += 1
                if keep:
                    opened.append(info)
            if p.get("merged_at") and parse_time(p["merged_at"]) >= since:
                n_merged += 1
                if keep:
                    merged.append(info)
        out["pull_requests"] = {"opened": opened, "merged": merged, "opened_count": n_opened, "merged_count": n_merged}

        # Issues opened and closed in the window (excluding PRs).
        iopened, iclosed, n_iopened, n_iclosed = [], [], 0, 0
        for i in paginate(f"/repos/{name}/issues", {"state": "all", "since": since_iso, "per_page": 100}):
            if "pull_request" in i:
                continue
            info = {"number": i.get("number"), "title": i.get("title"), "author": (i.get("user") or {}).get("login"), "url": i.get("html_url")}
            keep = recent(i.get("created_at"), i.get("updated_at"))
            if i.get("created_at") and parse_time(i["created_at"]) >= since:
                n_iopened += 1
                if keep:
                    iopened.append(info)
            if i.get("closed_at") and parse_time(i["closed_at"]) >= since:
                n_iclosed += 1
                if keep:
                    iclosed.append(info)
        out["issues"] = {"opened": iopened, "closed": iclosed, "opened_count": n_iopened, "closed_count": n_iclosed}

        # Releases published in the window.
        rels = []
        for r in paginate(f"/repos/{name}/releases", {"per_page": 100},
                          stop=lambda r: (parse_time(r.get("published_at") or r.get("created_at")) or since) < since):
            if r.get("draft"):
                continue
            rels.append({"tag": r.get("tag_name"), "name": r.get("name"), "published_at": r.get("published_at"), "url": r.get("html_url")})
        out["releases_count"] = len(rels)
        out["releases"] = [r for r in rels if recent(r["published_at"])]

        out["fork_history"] = fork_history(name, meta.get("created_at"))
        out["dependents"] = dependents(name)
    except RateLimited:
        out["status"] = "rate_limited"
    except NotFound:
        out["status"] = "partial_not_found"
    return out


def summary(result):
    lines = [f"# Digest scan {result['date']} (last {result['days']} days)", ""]
    lines.append("| Repo | Commits | Authors | PRs opened/merged | Issues opened/closed | Releases | Stars | Forks |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for r in result["repos"]:
        if r["status"] != "ok":
            lines.append(f"| [{r['repo']}]({r['url']}) | {r['status']} | | | | | | |")
            continue
        c, p, i = r["commits"], r["pull_requests"], r["issues"]
        lines.append(
            f"| [{r['repo']}]({r['url']}) | {c['count']} | {len(c['authors'])} | "
            f"{p['opened_count']}/{p['merged_count']} | {i['opened_count']}/{i['closed_count']} | "
            f"{r['releases_count']} | {r['stars']} | {r['forks']} |"
        )
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--days", type=int, default=90, help="look-back window for counts in days (default 90)")
    ap.add_argument("--detail-days", type=int, default=1,
                    help="keep per-item lists only for items created or updated in this many days (default 1; "
                         "use 90 for a full edition scan)")
    args = ap.parse_args()

    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    since = now - dt.timedelta(days=args.days)
    detail_since = max(since, now - dt.timedelta(days=args.detail_days))
    watchlist = os.path.join(HERE, "watchlist.yml")
    repos = load_watchlist(watchlist)
    if not repos:
        sys.exit("no repos found in " + watchlist)

    result = {
        "date": now.strftime("%Y-%m-%d"),
        "generated_at": now.strftime(ISO),
        "days": args.days,
        "since": since.strftime(ISO),
        "detail_days": min(args.detail_days, args.days),
        "detail_since": detail_since.strftime(ISO),
        "authenticated": bool(token()),
        "repos": [],
    }
    for entry in repos:
        print("scanning " + entry["repo"], file=sys.stderr)
        result["repos"].append(scan_repo(entry, since, detail_since))

    path = os.path.join(HERE, "data", result["date"] + ".json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(summary(result))
    print("\nWrote " + os.path.relpath(path), file=sys.stderr)


if __name__ == "__main__":
    main()
