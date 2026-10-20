import datetime as dt
import tempfile
import unittest
from pathlib import Path

from scripts import check_pages as cp

GOOD = '---\ntitle: "X"\nowner: "Build committee"\nlast_reviewed: 2026-10-20\n---\n\n# X\n\nSee [other](other.md).\n'


class Pages(unittest.TestCase):
    def run_check(self, text, extra=()):
        d = Path(tempfile.mkdtemp())
        for name in extra:
            (d / name).write_text(GOOD)
        p = d / "page.md"
        p.write_text(text)
        root, cp.ROOT = cp.ROOT, d
        try:
            return cp.check(p, dt.date(2026, 10, 21))
        finally:
            cp.ROOT = root

    def test_good_page(self):
        self.assertEqual(self.run_check(GOOD, ["other.md"]), ([], []))

    def test_broken_link(self):
        errors, _ = self.run_check(GOOD)
        self.assertTrue(any("broken link" in e for e in errors))

    def test_missing_owner(self):
        errors, _ = self.run_check(GOOD.replace('owner: "Build committee"\n', ""), ["other.md"])
        self.assertTrue(any("owner" in e for e in errors))

    def test_old_page_warns(self):
        _, warnings = self.run_check(GOOD.replace("2026-10-20", "2024-01-01"), ["other.md"])
        self.assertTrue(warnings)

    def test_real_pages_pass(self):
        today = dt.date.today()
        errors = [e for p in sorted(cp.PAGES.rglob("*.md")) for e in cp.check(p, today)[0]]
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
