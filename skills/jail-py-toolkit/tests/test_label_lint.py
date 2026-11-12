import unittest
from _helper import run, fixture


class TestLabelLint(unittest.TestCase):
    def test_pass(self):
        rc, _, err = run("label-lint.py", fixture("label_pass.md"))
        self.assertEqual(rc, 0, err)

    def test_fail_legacy_labels(self):
        rc, _, err = run("label-lint.py", fixture("label_fail_legacy.md"))
        self.assertEqual(rc, 1)
        for lab in ("Known", "Analyst Judgment", "Missing Evidence"):
            self.assertIn(lab, err)

    def test_require_evidence_fails(self):
        rc, _, err = run("label-lint.py", "--require-evidence", fixture("label_fail_nocite.md"))
        self.assertEqual(rc, 1)
        self.assertIn(":1:", err)
        self.assertNotIn(":2:", err)

    def test_without_flag_nocite_ok(self):
        self.assertEqual(run("label-lint.py", fixture("label_fail_nocite.md"))[0], 0)

    def test_pass_with_evidence_flag(self):
        # label_pass has one Fact with [1]
        self.assertEqual(run("label-lint.py", "--require-evidence", fixture("label_pass.md"))[0], 0)


if __name__ == "__main__":
    unittest.main()
