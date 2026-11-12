import unittest
from _helper import run, fixture


class TestGateRecordLint(unittest.TestCase):
    def test_pass(self):
        rc, _, err = run("gate-record-lint.py", fixture("gate_pass.md"))
        self.assertEqual(rc, 0, err)

    def test_fail_bad_tier(self):
        rc, _, err = run("gate-record-lint.py", fixture("gate_fail_tier.md"))
        self.assertEqual(rc, 1)
        self.assertIn("tier must be", err)

    def test_fail_missing_ts_result(self):
        rc, _, err = run("gate-record-lint.py", fixture("gate_fail_missing.md"))
        self.assertEqual(rc, 1)
        self.assertIn("missing field: approver", err)
        self.assertIn("valid ISO-8601", err)
        self.assertIn("result must be", err)


if __name__ == "__main__":
    unittest.main()
