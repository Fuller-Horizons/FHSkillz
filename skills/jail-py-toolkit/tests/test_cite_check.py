import unittest
from _helper import run, fixture


class TestCiteCheck(unittest.TestCase):
    def test_pass(self):
        rc, _, err = run("cite-check.py", fixture("cite_pass.md"))
        self.assertEqual(rc, 0, err)

    def test_fail_orphan_and_uncited(self):
        rc, _, err = run("cite-check.py", fixture("cite_fail_orphan.md"))
        self.assertEqual(rc, 1)
        self.assertIn("orphan marker [3]", err)

    def test_fail_source_fields_and_uncited(self):
        rc, _, err = run("cite-check.py", fixture("cite_fail_source.md"))
        self.assertEqual(rc, 1)
        self.assertIn("no URL/ref", err)
        self.assertIn("no ISO date", err)
        self.assertIn("source [2] is never cited", err)


if __name__ == "__main__":
    unittest.main()
