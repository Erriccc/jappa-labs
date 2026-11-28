"""Write the repo's open issues to docs/_data/issues.json for the "Open work" page.

Run by .github/workflows/pages.yml before the Jekyll build. Writes [] on any
failure so the site still builds. docs/_data/issues.json is gitignored.
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from scan import paginate  # noqa: E402

OUT = os.path.join(os.path.dirname(HERE), "docs", "_data", "issues.json")
# Internal research issues, never shown or linked on the site. The site tests
# (tests/test_site.py) check committed pages against the same list.
PRIVATE_ISSUES = (5, 10, 13, 14, 15)
PRIVATE_NUMBER = "(" + "|".join(map(str, PRIVATE_ISSUES)) + r")\b"
BANNED_NAME = re.compile("ogirac"[::-1], re.I)  # a private name, spelled backwards so it never appears in the repo
HIDDEN_LABELS = {"private", "security"}


def hide_private_numbers(text):
    return re.sub("#" + PRIVATE_NUMBER, "a private note", text or "")


def plain(text):
    text = re.sub(r"```.*?```", " ", text or "", flags=re.S)
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)  # links -> text
    text = re.sub(r"https?://\S+", " ", text)
    text = hide_private_numbers(text)
    text = re.sub(r"[#*_`>|~]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def public_issues(items, repo):
    issues = []
    for item in items:
        labels = [label.get("name", "") for label in item.get("labels", [])]
        if ("pull_request" in item or item["number"] in PRIVATE_ISSUES
                or HIDDEN_LABELS & {label.lower() for label in labels}
                or any(BANNED_NAME.search(text) for text in
                       [item.get("title") or "", item.get("body") or ""] + labels)):
            continue
        issues.append({
            "number": item["number"],
            "title": hide_private_numbers(item.get("title")),
            "labels": labels,
            "created_at": item.get("created_at") or "",
            "body": plain(item.get("body")),
            "url": f"https://github.com/{repo}/issues/{item['number']}",
        })
    return issues


def main():
    repo = os.environ["REPO"]
    try:
        issues = public_issues(paginate(f"/repos/{repo}/issues", {"state": "open", "per_page": 100}), repo)
    except Exception as exc:  # the page shows "No open work right now." instead
        print(f"Could not fetch issues, writing an empty list: {exc}")
        issues = []
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(issues, f, indent=2)
    print(f"Wrote {len(issues)} issues to {os.path.relpath(OUT)}")


if __name__ == "__main__":
    main()
