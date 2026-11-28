"""Tests for digest/render.py. Run: python3 -m unittest discover -s digest/tests"""

import contextlib
import datetime as dt
import io
import json
import os
import re
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import render  # noqa: E402

FIXTURES = os.path.join(HERE, "fixtures", "data")
END = dt.date(2026, 12, 2)


def fixture_edition(n=2, end=END):
    scans = render.load_scans(FIXTURES)
    return render.render_edition(dict(scans)[end], scans, n, end)


def section(text, title):
    start = text.index(f"## {title}")
    nxt = text.find("\n## ", start + 1)
    return text[start:nxt if nxt != -1 else None]


def run_main(*args):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = render.main(list(args))
    return code, buf.getvalue()


class TestScans(unittest.TestCase):
    def test_window_and_baseline(self):
        scans = render.load_scans(FIXTURES)
        self.assertEqual([d for d, _ in render.window(scans, END)], [dt.date(2026, 11, 29), END])
        self.assertEqual(render.baseline(scans, END)[0], dt.date(2026, 11, 25))
        self.assertIsNone(render.baseline(scans, dt.date(2026, 11, 29)))

    def test_week_activity_dedupes_and_drops_bots(self):
        week = render.window(render.load_scans(FIXTURES), END)
        commits, prs, releases = render.week_activity("alpha/mover", week)
        self.assertEqual(sorted(c["sha"] for c in commits), ["aaa0001", "aaa0002", "aaa0003"])
        commits, prs, releases = render.week_activity("beta/release", week)
        self.assertEqual([p["number"] for p in prs], [7])
        self.assertEqual(len(releases), 2)  # date filtering happens in render_edition


class TestEdition(unittest.TestCase):
    def setUp(self):
        self.text = fixture_edition()

    def test_heading_and_date(self):
        lines = self.text.splitlines()
        self.assertEqual(lines[0], "# Builders to watch: open source for West Africa, edition 2")
        self.assertEqual(lines[2], "*2 December 2026*")
        self.assertIn("daily scans of 29 November 2026 and 2 December 2026", self.text)
        self.assertTrue(self.text.endswith("\n"))
        self.assertFalse(self.text.startswith("---"))

    def test_builder_order_is_deterministic_and_excludes_own(self):
        builders = section(self.text, "Builders this week")
        order = [line.split("](")[0][5:] for line in builders.splitlines() if line.startswith("### ")]
        self.assertEqual(order, ["alpha/mover", "gamma/hostile", "beta/release", "epsilon/new"])
        self.assertNotIn("jappa-labs", builders)
        self.assertEqual(fixture_edition(), self.text)

    def test_people_credited(self):
        builders = section(self.text, "Builders this week")
        self.assertIn("by [ada](https://github.com/ada) and Jane Doe", builders)  # no login: plain text
        self.assertNotIn("dependabot", self.text)
        self.assertNotIn("renovate", self.text)
        self.assertIn("3 commits recorded this week", builders)
        self.assertIn("[kemi](https://github.com/kemi)", builders)

    def test_star_changes(self):
        builders = section(self.text, "Builders this week")
        self.assertIn("10 stars (+5 since 25 November 2026)", builders)
        self.assertIn("120 stars (+20 since 25 November 2026)", builders)
        self.assertIn("- 40 stars\n", builders)  # epsilon/new is missing from the baseline

    def test_no_licence_note(self):
        alpha = self.text.split("### [alpha/mover]")[1].split("### ")[0]
        self.assertIn("Licence: none yet", alpha)
        self.assertIn("Adding an open-source licence", alpha)

    def test_shipped(self):
        shipped = section(self.text, "Shipped")
        self.assertIn("[Version 2](https://github.com/beta/release/releases/tag/v2.0.0) on 1 December 2026", shipped)
        self.assertNotIn("Ancient", shipped)
        self.assertIn("[Ship 2.0](https://github.com/beta/release/pull/7) by [kemi](https://github.com/kemi)", shipped)
        self.assertNotIn("jappa-labs", shipped)

    def test_not_found_skipped(self):
        self.assertNotIn("delta/missing", self.text)

    def test_own_section_drops_bot_commits(self):
        own = section(self.text, "From Jappa Labs")
        self.assertIn("[Erriccc/jappa-labs](https://github.com/Erriccc/jappa-labs)", own)
        self.assertIn("Add research posts", own)
        self.assertIn("1 commit recorded this week", own)
        self.assertNotIn("Digest scan data", own)
        self.assertIn("(../research/index.md)", own)

    def test_no_baseline_text(self):
        text = fixture_edition(1, dt.date(2026, 11, 29))
        self.assertIn("Star changes appear once there is a scan from a week earlier", text)
        self.assertNotIn(" since ", section(text, "Builders this week"))


class TestEscape(unittest.TestCase):
    def test_esc(self):
        out = render.esc("{{ x }} {% y %} {# z #} | [a](http://b) <i>&</i> *_`$~\n")
        for bad in ("{", "}", "|", "<i>", "[a](", "\n", "`", "$", "~"):
            self.assertNotIn(bad, out)
        self.assertIn("&amp;", out)
        self.assertEqual(render.esc(None), "")

    def test_hostile_fixture(self):
        text = fixture_edition()
        for bad in ("{{", "{%", "<script", "[x](http", "](http://evil"):
            self.assertNotIn(bad, text)
        self.assertEqual(text.count("\n|"), 0)

    def test_safe_url(self):
        self.assertEqual(render.safe_url("https://github.com/a/b/tag/v1)x{{a}} <i>"),
                         "https://github.com/a/b/tag/v1%29x%7B%7Ba%7D%7D%20%3Ci%3E")
        for bad in ("http://github.com/a", "https://github.com.evil/a", "javascript:x", None):
            self.assertIsNone(render.safe_url(bad))

    def test_hostile_release_url(self):
        scans = render.load_scans(FIXTURES)
        current = dict(scans)[END]
        rel = next(r for repo in current["repos"] for r in repo.get("releases") or []
                   if r.get("tag") == "v2.0.0")
        rel["url"] = "https://github.com/beta/release/releases/tag/v1)x{{a}}"
        text = render.render_edition(current, scans, 2, END)
        self.assertIn("[Version 2](https://github.com/beta/release/releases/tag/v1%29x%7B%7Ba%7D%7D)", text)
        for target in re.findall(r"\]\(([^)\s]*)", text):
            for bad in (")", "{{", "<"):
                self.assertNotIn(bad, target)
        self.assertNotIn("{{", text)
        self.assertNotIn("v1)x", text)
        rel["url"] = "http://evil.example/x"
        text = render.render_edition(current, scans, 2, END)
        self.assertNotIn("evil.example", text)
        self.assertIn("released Version 2 on", text)


class TestDueAndNumbering(unittest.TestCase):
    def test_is_due(self):
        last = dt.date(2026, 11, 25)
        self.assertFalse(render.is_due(dt.date(2026, 12, 1), last))
        self.assertTrue(render.is_due(dt.date(2026, 12, 2), last))
        self.assertTrue(render.is_due(dt.date(2026, 12, 2), None))

    def test_last_edition(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(render.last_edition(d), (None, 0))
            for name in ("2026-11-25-edition-1.md", "2026-12-02-edition-2.md", "notes.md"):
                open(os.path.join(d, name), "w").close()
            self.assertEqual(render.last_edition(d), (dt.date(2026, 12, 2), 2))


class TestMain(unittest.TestCase):
    def setUp(self):
        self.out = tempfile.mkdtemp()
        open(os.path.join(self.out, "2026-11-25-edition-1.md"), "w").close()

    def tearDown(self):
        shutil.rmtree(self.out)

    def test_writes_next_edition_once(self):
        code, msg = run_main("--data-dir", FIXTURES, "--out-dir", self.out, "--if-due")
        self.assertEqual(code, 0)
        path = os.path.join(self.out, "2026-12-02-edition-2.md")
        self.assertTrue(os.path.exists(path), msg)
        with open(path, encoding="utf-8") as f:
            first = f.read()
        code, msg = run_main("--data-dir", FIXTURES, "--out-dir", self.out, "--force")
        self.assertIn("already exists", msg)
        self.assertEqual(sorted(os.listdir(self.out)), ["2026-11-25-edition-1.md", "2026-12-02-edition-2.md"])
        with open(path, encoding="utf-8") as f:
            self.assertEqual(f.read(), first)

    def test_not_due(self):
        code, msg = run_main("--data-dir", FIXTURES, "--out-dir", self.out, "--if-due", "--date", "2026-11-29")
        self.assertIn("Not due", msg)
        self.assertEqual(os.listdir(self.out), ["2026-11-25-edition-1.md"])
        run_main("--data-dir", FIXTURES, "--out-dir", self.out, "--if-due", "--force", "--date", "2026-11-29")
        self.assertIn("2026-11-29-edition-2.md", os.listdir(self.out))

    def test_skips_when_scan_mostly_failed(self):
        data = tempfile.mkdtemp()
        try:
            with open(os.path.join(FIXTURES, "2026-12-02.json"), encoding="utf-8") as f:
                scan = json.load(f)
            for r in scan["repos"][:2]:
                r["status"] = "rate_limited"
            with open(os.path.join(data, "2026-12-02.json"), "w", encoding="utf-8") as f:
                json.dump(scan, f)
            code, msg = run_main("--data-dir", data, "--out-dir", self.out, "--force")
            self.assertEqual(code, 0)
            self.assertIn("Skipping", msg)
            self.assertEqual(os.listdir(self.out), ["2026-11-25-edition-1.md"])
        finally:
            shutil.rmtree(data)


if __name__ == "__main__":
    unittest.main()
