#!/usr/bin/env python3
"""Render a weekly digest edition from the daily scan files in digest/data.

Uses only the Python standard library. Writes docs/digest/YYYY-MM-DD-edition-N.md
and prints its path. Never overwrites an existing edition.

  python3 digest/render.py            # render for the newest data file
  python3 digest/render.py --if-due   # only if 7+ days since the last edition
  python3 digest/render.py --force    # render now, even if not due
"""

import argparse
import collections
import datetime as dt
import json
import os
import re
import sys
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from scan import DATA_DIR, parse_time  # noqa: E402

OUT_DIR = os.path.join(HERE, "..", "docs", "digest")
WEEK = 7
MAX_NON_OK = 0.2  # skip the edition if more repos than this failed to scan
MAX_BUILDERS = 10
MAX_PEOPLE = 5
MAX_PRS = 3
ISSUE_6 = "https://github.com/Erriccc/jappa-labs/issues/6"
DATA_FILE = re.compile(r"^(\d{4}-\d{2}-\d{2})\.json$")
EDITION_FILE = re.compile(r"^(\d{4}-\d{2}-\d{2})-edition-(\d+)\.md$")

# Repo text is untrusted and edition pages are rendered by Liquid and kramdown,
# so every character that could start a tag, a link or a table is neutralised.
_ESC = {"\\": "\\\\", "&": "&amp;", "<": "&lt;", ">": "&gt;", "{": "&#123;", "}": "&#125;",
        "$": "&#36;", "~": "&#126;", "`": "&#96;", "|": " ", "\n": " ", "\r": " ", "\t": " "}
_ESC.update({c: "\\" + c for c in "[]()*_#"})


def esc(text):
    if text is None:
        return ""
    return " ".join("".join(_ESC.get(ch, ch) for ch in str(text)).split())


def day(s):
    return dt.date.fromisoformat(s)


def long_date(d):
    return f"{d.day} {d.strftime('%B %Y')}"


def load_scans(data_dir):
    """Sorted list of (date, scan) from the YYYY-MM-DD.json files."""
    out = []
    for name in sorted(os.listdir(data_dir)):
        m = DATA_FILE.match(name)
        if m:
            with open(os.path.join(data_dir, name), encoding="utf-8") as f:
                out.append((day(m.group(1)), json.load(f)))
    return out


def window(scans, end, days=WEEK):
    """Scans dated in the `days` days up to and including `end`."""
    return [(d, s) for d, s in scans if end - dt.timedelta(days=days) < d <= end]


def baseline(scans, end, days=WEEK):
    """The newest scan at least `days` days before `end`, or None."""
    older = [(d, s) for d, s in scans if d <= end - dt.timedelta(days=days)]
    return older[-1] if older else None


def is_bot(name):
    return bool(name) and name.endswith("[bot]")


def by_repo(scan):
    return {r["repo"]: r for r in scan.get("repos", [])}


def safe_url(u):
    """A link target safe for kramdown and Liquid, or None if it is not a GitHub URL.
    Keeps URL syntax and existing %-escapes; encodes ( ) < > { } | " and whitespace."""
    if not isinstance(u, str) or not re.match(r"^https://github\.com/", u):
        return None
    return urllib.parse.quote(u, safe=":/?#[]@!$&'*+,;=%~")


def link(label, url):
    """Markdown link with an already-escaped label; plain label when the URL is unsafe."""
    target = safe_url(url)
    return f"[{label}]({target})" if target else label


def person(name, login=None):
    """Markdown credit for a person: a profile link when the GitHub login is known."""
    if login:
        return link(esc(login), f"https://github.com/{urllib.parse.quote(login, safe='')}")
    return esc(name)


def count(n, word):
    return f"{n:,} {word}{'' if n == 1 else 's'}"


def repo_link(r):
    return link(esc(r['repo']), r.get('url'))


def join(items):
    items = list(items)
    if len(items) <= 1:
        return "".join(items)
    return ", ".join(items[:-1]) + " and " + items[-1]


def week_activity(name, scans):
    """Commits (deduped by sha), merged PRs (deduped by URL) and releases
    (deduped by URL) recorded for one repo across the week's scan files."""
    commits, prs, releases = {}, {}, {}
    for _, scan in scans:
        r = by_repo(scan).get(name)
        if not r or r.get("status") != "ok":
            continue
        for c in (r.get("commits") or {}).get("items", []):
            commits.setdefault(c.get("sha") or (c.get("date"), c.get("message")), c)
        for p in (r.get("pull_requests") or {}).get("merged", []):
            prs.setdefault(p.get("url") or p.get("number"), p)
        for rel in r.get("releases") or []:
            releases.setdefault(rel.get("url") or rel.get("tag"), rel)
    human = [c for c in commits.values() if not is_bot(c.get("author"))]
    human.sort(key=lambda c: (c.get("date") or "", c.get("sha") or ""), reverse=True)
    merged = [p for p in prs.values() if not is_bot(p.get("author"))]
    merged.sort(key=lambda p: p.get("number") or 0, reverse=True)
    return human, merged, list(releases.values())


def credits(commits, prs):
    """People ranked by commits plus merged PRs this week, as markdown credits."""
    counts, logins = collections.Counter(), {}
    for c in commits:
        key = c.get("login") or c.get("author")
        if not key:
            continue
        counts[key] += 1
        if c.get("login"):
            logins[key] = c["login"]
    for p in prs:
        if p.get("author"):
            counts[p["author"]] += 1
            logins[p["author"]] = p["author"]  # PR authors are always logins
    ranked = sorted(counts, key=lambda k: (-counts[k], k.lower()))
    return [person(k, logins.get(k)) for k in ranked]


def credit_line(people):
    shown = people[:MAX_PEOPLE]
    rest = len(people) - len(shown)
    if rest:
        return ", ".join(shown) + f" and {rest} more"
    return join(shown)


def stars_line(repo, base):
    if repo.get("stars") is None:
        return None
    line = count(repo["stars"], "star")
    if base is not None:
        old = by_repo(base[1]).get(repo["repo"])
        if old and old.get("status") == "ok" and old.get("stars") is not None:
            diff = repo["stars"] - old["stars"]
            line += f" ({diff:+,d} since {long_date(base[0])})"
    return line


def in_window(stamp, start, end):
    t = parse_time(stamp) if stamp else None
    return t is not None and start < t.date() <= end


def render_edition(current, scans, n, end):
    """Markdown for edition `n`, built from the scan for `end` and the week before it."""
    week = window(scans, end)
    base = baseline(scans, end)
    start = end - dt.timedelta(days=WEEK)
    dates = [d for d, _ in week]
    if len({(d.year, d.month) for d in dates}) == 1:
        covered = join([str(d.day) for d in dates[:-1]] + [long_date(dates[-1])])
    else:
        covered = join([long_date(d) for d in dates])

    builders, shipped, own = [], [], []
    for r in current.get("repos", []):
        if r.get("status") != "ok" or r.get("archived"):
            continue
        commits, prs, releases = week_activity(r["repo"], week)
        releases = [x for x in releases if in_window(x.get("published_at"), start, end)]
        if r.get("group") == "own":
            own.append((r, commits, prs))
            continue
        if commits or prs:
            builders.append((r, commits, prs))
        if releases or prs:
            shipped.append((r, releases, prs))
    # Projects built for West Africa lead, as in edition 1; building blocks follow.
    builders.sort(key=lambda b: (b[0].get("group") != "built_for_west_africa",
                                 -(len(b[1]) + len(b[2])), b[0]["repo"].lower()))
    shipped.sort(key=lambda s: s[0]["repo"].lower())

    out = [f"# Builders to watch: open source for West Africa, edition {n}", "",
           f"*{long_date(end)}*", "",
           "This digest shines a light on open-source projects that serve Nigerians and West Africans, "
           "at home and in the diaspora. Each edition credits the people building them, shares what they "
           f"have shipped, and points to ways you can help. This edition covers the daily scans of {covered}, "
           "gathered from public GitHub data. See [About](../about.md) for how it works."]
    if base is None:
        out.append("")
        out.append("Star changes appear once there is a scan from a week earlier to compare against.")

    out += ["", "## Builders this week", ""]
    if builders:
        out.append("The people behind the projects with the most recorded activity this week. "
                   "Commit counts are on the default branch; automated accounts are left out.")
        for r, commits, prs in builders[:MAX_BUILDERS]:
            people = credits(commits, prs)
            out += ["", f"### {repo_link(r)}" + (f", by {credit_line(people)}" if people else ""), ""]
            out.append(f"{repo_link(r)}: {esc(r.get('description') or r.get('github_description'))}")
            out.append("")
            facts = [f"{count(len(commits), 'commit')} recorded this week"
                     + (f", and {count(len(prs), 'merged pull request')}" if prs else "")]
            stars = stars_line(r, base)
            if stars:
                facts.append(stars)
            last = parse_time((r.get("commits") or {}).get("last_commit_at"))
            if last:
                facts.append(f"Last activity: {long_date(last.date())}")
            facts.append(f"Licence: {esc(r['license'])}" if r.get("license") else "Licence: none yet")
            out += [f"- {f}" for f in facts]
            help_line = "**How you can help:** try it, star the repo, and open an issue with your feedback."
            if not r.get("license"):
                help_line += " Adding an open-source licence would make it easier for others to use the project and contribute."
            out += ["", help_line]
        if len(builders) > MAX_BUILDERS:
            out += ["", "### And more", "", f"Activity was also recorded on {len(builders) - MAX_BUILDERS} more projects in the "
                        "[watchlist](https://github.com/Erriccc/jappa-labs/blob/main/digest/watchlist.yml)."]
    else:
        out.append("No commits or merged pull requests were recorded this week.")

    out += ["", "## Shipped", ""]
    if shipped:
        out.append("Releases and merged pull requests recorded this week, with the people who made them.")
        out.append("")
        for r, releases, prs in shipped:
            parts = []
            for rel in sorted(releases, key=lambda x: x.get("published_at") or "", reverse=True):
                label = esc(rel.get("name") or rel.get("tag"))
                when = parse_time(rel.get("published_at"))
                parts.append(f"released {link(label, rel.get('url'))}" + (f" on {long_date(when.date())}" if when else ""))
            if prs:
                shown = [f"{link(esc(p.get('title')), p['url'])} by {person(p['author'], p['author'])}"
                         for p in prs[:MAX_PRS] if p.get("url") and p.get("author")]
                more = len(prs) - len(shown)
                text = f"merged {count(len(prs), 'pull request')}"
                if shown:
                    text += (", including " if more else ": ") + "; ".join(shown)
                    if more:
                        text += f"; and {more} more"
                parts.append(text)
            out.append(f"- {repo_link(r)} " + "; ".join(parts) + ".")
    else:
        out.append("No releases or merged pull requests were recorded this week.")

    if own:
        out += ["", "## From Jappa Labs", "",
                "Our own open-source work. It is listed here and not ranked with the projects above."]
        for r, commits, prs in own:
            out += ["", f"### {repo_link(r)}", "",
                    f"{repo_link(r)}: {esc(r.get('description') or r.get('github_description'))}", ""]
            stars = stars_line(r, base)
            if stars:
                out.append(f"- {stars}")
            if commits:
                out.append(f"- {count(len(commits), 'commit')} recorded this week, "
                           "not counting the daily scan updates:")
                for c in commits[:MAX_PEOPLE]:
                    commit_url = f"{r.get('url')}/commit/{urllib.parse.quote(c.get('sha') or '')}"
                    out.append(f"  - {link(esc(c.get('sha')), commit_url)} "
                               f"{esc(c.get('message'))}")
            else:
                out.append("- No commits this week apart from the daily scan updates.")
        out += ["", "Read the [research](../research/index.md) behind the "
                    "[send-to-nigeria guide](../send-to-nigeria.md)."]

    out += ["", "## Know a project we missed?", "",
            f"Open an issue. Suggestions and corrections are welcome in [issue #6]({ISSUE_6})."]
    return "\n".join(out) + "\n"


def last_edition(out_dir):
    """(date, number) of the newest edition file in out_dir, or (None, 0)."""
    best = (None, 0)
    if os.path.isdir(out_dir):
        for name in os.listdir(out_dir):
            m = EDITION_FILE.match(name)
            if m:
                d, n = day(m.group(1)), int(m.group(2))
                if best[0] is None or (d, n) > best:
                    best = (d, n)
    return best


def is_due(today, last_date, days=WEEK):
    return last_date is None or (today - last_date).days >= days


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--date", help="edition date, YYYY-MM-DD (default: the newest data file)")
    ap.add_argument("--data-dir", default=DATA_DIR)
    ap.add_argument("--out-dir", default=OUT_DIR)
    ap.add_argument("--if-due", action="store_true", help=f"render only if {WEEK}+ days since the last edition")
    ap.add_argument("--force", action="store_true", help="render even if not due")
    args = ap.parse_args(argv)

    scans = load_scans(args.data_dir)
    if not scans:
        print("No data files in " + args.data_dir, file=sys.stderr)
        return 1
    end = day(args.date) if args.date else scans[-1][0]
    current = dict(scans).get(end)
    if current is None:
        print(f"No data file for {end}", file=sys.stderr)
        return 1

    for name in os.listdir(args.out_dir) if os.path.isdir(args.out_dir) else []:
        if name.startswith(f"{end}-edition-"):
            print(f"Edition for {end} already exists: {name}")
            return 0
    last_date, last_n = last_edition(args.out_dir)
    if args.if_due and not args.force and not is_due(end, last_date):
        print(f"Not due: last edition {last_date}, next due {last_date + dt.timedelta(days=WEEK)}")
        return 0
    repos = current.get("repos", [])
    bad = sum(1 for r in repos if r.get("status") != "ok")
    if not repos or bad / len(repos) > MAX_NON_OK:
        print(f"Skipping: {bad} of {len(repos)} repos did not scan cleanly on {end}")
        return 0

    n = last_n + 1
    path = os.path.join(args.out_dir, f"{end}-edition-{n}.md")
    os.makedirs(args.out_dir, exist_ok=True)
    with open(path, "x", encoding="utf-8") as f:
        f.write(render_edition(current, scans, n, end))
    print(os.path.relpath(path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
