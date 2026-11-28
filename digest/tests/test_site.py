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
sys.path[:0] = [HERE, os.path.dirname(HERE)]
from test_render import fixture_edition  # noqa: E402
from site_issues import BANNED_NAME, PRIVATE_NUMBER, public_issues  # noqa: E402

LINK = re.compile(r"\]\(([^)\s]+)\)|href=\"([^\"]+)\"")
FENCE = re.compile(r"^```.*?^```", re.M | re.S)
PRIVATE_ISSUE = re.compile(r"jappa-labs/issues/" + PRIVATE_NUMBER)
BARE_PRIVATE_ISSUE = re.compile(r"(?<![\w&/])#" + PRIVATE_NUMBER)
PRICE = re.compile(r"[$₦£]\s?\d")
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
            if r == os.path.join("digest", "index.md"):
                continue  # lists the editions with Liquid
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
        paths += [os.path.join(DOCS, name) for name in ("index.md", "send-to-nigeria.md", "guides.md", "skill.md")]
        for path in paths:
            with open(path, encoding="utf-8") as f:
                self.assertNotRegex(f.read(), PRICE, rel(path))


def read(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
        return f.read()


NOT_PUBLISHED = ("recheck-live.md", "research-method.md", "README.md")


class TestNavigation(unittest.TestCase):
    PAGES = ["send-to-nigeria.md", "guides.md", "research/index.md", "digest/index.md",
             "open-work.md", "skill.md", "about.md"]

    def test_header_pages(self):
        config = read("docs", "_config.yml")
        block = config.split("header_pages:", 1)[1]
        listed = re.findall(r"^\s+-\s+(\S+)\s*$", block, re.M)
        self.assertEqual(listed[:len(self.PAGES)], self.PAGES)
        for page in self.PAGES:
            self.assertTrue(os.path.isfile(os.path.join(DOCS, page)), page)

    def test_guides_links_every_guide_page(self):
        text = read("docs", "guides.md")
        for folder, prefix in ((GUIDE_SRC, "guide/"), (os.path.join(GUIDE_SRC, "scenarios"), "guide/scenarios/")):
            for path in glob.glob(os.path.join(folder, "*.md")):
                name = os.path.basename(path)
                if name in NOT_PUBLISHED:
                    continue
                self.assertIn(f"]({prefix}{name})", text, name)

    def test_open_work_escapes_untrusted_text(self):
        text = read("docs", "open-work.md")
        outputs = re.findall(r"\{\{(.*?)\}\}", text)
        self.assertTrue(outputs)
        for out in outputs:
            self.assertRegex(out, r"\|\s*escape\s*$", out)
        self.assertIn("strip_html | truncate: 200 | escape", text)
        self.assertIn("No open work right now.", text)

    def test_pages_workflow_fetches_issues(self):
        workflow = read(".github", "workflows", "pages.yml")
        build = workflow.split("\n  build:", 1)[1].split("\n  deploy:", 1)[0]
        self.assertRegex(build, r"permissions:\n(\s+\w[\w-]*: \w+\n)*\s+issues: read")
        self.assertIn("docs/_data/issues.json", build)
        self.assertLess(build.index("docs/_data/issues.json"), build.index("jekyll-build-pages"))
        self.assertIn("docs/_data/issues.json", read(".gitignore").splitlines())

    def test_open_issues_hide_private_ones(self):
        items = [
            {"number": 5, "title": "internal", "body": ""},
            {"number": 30, "title": "PR", "body": "", "pull_request": {}},
            {"number": 31, "title": "labelled", "body": "", "labels": [{"name": "Private"}]},
            {"number": 32, "title": "x", "body": "ogirac"[::-1]},
            {"number": 33, "title": "Help wanted", "body": "See #13 and #50, [docs](https://x.test/a)."},
        ]
        issues = public_issues(items, "o/r")
        self.assertEqual([i["number"] for i in issues], [33])
        self.assertEqual(issues[0]["body"], "See a private note and 50, docs.")

    def test_open_issues_title_hides_private_numbers(self):
        issues = public_issues([{"number": 34, "title": "Follow up #13 and #130", "body": ""}], "o/r")
        self.assertEqual(issues[0]["title"], "Follow up a private note and #130")

    def test_open_issues_banned_name_in_label(self):
        items = [{"number": 35, "title": "x", "body": "", "labels": [{"name": "ogirac"[::-1].title()}]}]
        self.assertEqual(public_issues(items, "o/r"), [])

    def test_where_exp_single_condition(self):
        # Jekyll 3 (jekyll-build-pages) does not support and/or inside where_exp.
        paths = glob.glob(os.path.join(DOCS, "**", "*.html"), recursive=True)
        paths += glob.glob(os.path.join(DOCS, "**", "*.md"), recursive=True)
        found = 0
        for path in paths:
            with open(path, encoding="utf-8") as f:
                for m in re.finditer(r"where_exp:\s*\"[^\"]*\"\s*,\s*\"([^\"]*)\"", f.read()):
                    found += 1
                    self.assertNotRegex(m.group(1), r" (and|or) ", rel(path))
        self.assertTrue(found)

    def test_install_moved_to_skill_page(self):
        guide = read("docs", "send-to-nigeria.md")
        self.assertNotIn("/plugin install", guide)
        self.assertNotIn("/plugin marketplace add", guide)
        self.assertIn("](skill.md)", guide)
        skill = read("docs", "skill.md")
        self.assertIn("/plugin install send-to-nigeria@jappa-labs", skill)
        self.assertIn("issues/22", skill)


if __name__ == "__main__":
    unittest.main()
