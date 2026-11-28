"""Site checks: on-site links resolve, and content rules hold.

Run: python3 -m unittest discover -s digest/tests

docs/guide/ is copied in from the plugin at build time (see
.github/workflows/pages.yml). Links into it are checked against the plugin's
references folder, so the tests pass with or without the copy.
"""

import glob
import os
import re
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DOCS = os.path.join(ROOT, "docs")
GUIDE_SRC = os.path.join(ROOT, "plugins", "send-to-nigeria", "skills", "send-to-nigeria", "references")
sys.path.insert(0, HERE)
from test_render import fixture_edition  # noqa: E402

LINK = re.compile(r"\]\(([^)\s]+)\)|href=\"([^\"]+)\"")
FENCE = re.compile(r"^```.*?^```", re.M | re.S)
PRIVATE_ISSUE = re.compile(r"jappa-labs/issues/(5|10|13|14|15)\b")
BARE_PRIVATE_ISSUE = re.compile(r"(?<![\w&/])#(5|10|13|14|15)\b")
PRICE = re.compile(r"[$₦£]\s?\d")
BANNED_NAME = re.compile("ogirac"[::-1], re.I)  # a private name, spelled backwards so it never appears in the repo
ATTRIBUTION = ("Co-" + "Authored", "Generated " + "with")


def rel(path):
    return os.path.relpath(path, DOCS)


def site_pages():
    """(path, text) for every markdown page in docs/, plus the guide pages and
    a rendered fixture edition."""
    pages = []
    for path in glob.glob(os.path.join(DOCS, "**", "*.md"), recursive=True):
        if rel(path).startswith("guide" + os.sep):
            continue  # checked from the plugin source below
        with open(path, encoding="utf-8") as f:
            pages.append((path, f.read()))
    for path in glob.glob(os.path.join(GUIDE_SRC, "**", "*.md"), recursive=True):
        if os.path.relpath(path, GUIDE_SRC).startswith("templates" + os.sep):
            continue  # not copied to the site
        with open(path, encoding="utf-8") as f:
            pages.append((os.path.join(DOCS, "guide", os.path.relpath(path, GUIDE_SRC)), f.read()))
    pages.append((os.path.join(DOCS, "digest", "2026-12-02-edition-2.md"), fixture_edition()))
    return pages


def exists_on_site(path):
    """True if a docs/ path is a file, a folder with an index, or a guide page."""
    r = rel(path)
    if r.startswith("guide" + os.sep):
        src = os.path.join(GUIDE_SRC, os.path.relpath(r, "guide"))
        if os.path.relpath(src, GUIDE_SRC).startswith("templates"):
            return False
        return os.path.isfile(src) or os.path.isfile(os.path.join(src, "README.md"))
    return os.path.isfile(path) or os.path.isfile(os.path.join(path, "index.md"))


class TestLinks(unittest.TestCase):
    def test_on_site_links_resolve(self):
        broken = []
        for path, text in site_pages():
            in_guide = rel(path).startswith("guide" + os.sep)
            for m in LINK.finditer(FENCE.sub("", text)):
                target = m.group(1) or m.group(2)
                if re.match(r"^(https?:|mailto:|#)", target) or "{{" in target:
                    continue
                if in_guide and "templates/" in target:
                    continue  # model-facing link to the scenario template, not published
                dest = os.path.normpath(os.path.join(os.path.dirname(path), target.split("#")[0]))
                if not (dest + os.sep).startswith(DOCS + os.sep):
                    broken.append(f"{rel(path)}: {target} leaves docs/")
                elif not exists_on_site(dest):
                    broken.append(f"{rel(path)}: {target} not found")
        self.assertEqual(broken, [])

    def test_site_pages_link_only_public_guide_pages(self):
        for path, text in site_pages():
            if rel(path).startswith("guide" + os.sep):
                continue
            for name in ("recheck-live.md", "research-method.md", "templates/"):
                self.assertNotIn(name, text, rel(path))


class TestContentRules(unittest.TestCase):
    def test_banned_text(self):
        for path, text in site_pages():
            r = rel(path)
            self.assertNotRegex(text, BANNED_NAME, r)
            self.assertNotRegex(text, PRIVATE_ISSUE, r)
            for banned in ATTRIBUTION:
                self.assertNotIn(banned, text, r)
            self.assertNotRegex(text, re.compile(r"^##\s+Private", re.M), r)

    def test_no_liquid_outside_index(self):
        for path, text in site_pages():
            r = rel(path)
            if r.startswith(("digest", "research", "guide")) or r in ("send-to-nigeria.md", "about.md"):
                self.assertNotIn("{{", text, r)
                self.assertNotIn("{%", text, r)

    def test_research_posts(self):
        posts = glob.glob(os.path.join(DOCS, "research", "_posts", "*.md"))
        self.assertGreaterEqual(len(posts), 3)
        for path in posts:
            self.assertRegex(os.path.basename(path), r"^\d{4}-\d{2}-\d{2}-[a-z0-9-]+\.md$")
            with open(path, encoding="utf-8") as f:
                text = f.read()
            front = text.split("---")[1]
            for key in ("title:", "date:", "status:", "sources:"):
                self.assertIn(key, front, rel(path))
            self.assertNotRegex(text, BARE_PRIVATE_ISSUE, rel(path))
            self.assertIn("not legal, customs or tax advice", text, rel(path))
            self.assertIn("*As of ", text, rel(path))

    def test_no_prices_outside_the_guide(self):
        paths = glob.glob(os.path.join(DOCS, "research", "_posts", "*.md"))
        paths += [os.path.join(DOCS, "index.md"), os.path.join(DOCS, "send-to-nigeria.md")]
        for path in paths:
            with open(path, encoding="utf-8") as f:
                self.assertNotRegex(f.read(), PRICE, rel(path))


if __name__ == "__main__":
    unittest.main()
