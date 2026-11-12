import unittest
from _helper import run, fixture


class TestScoreCheck(unittest.TestCase):
    def test_pass_rate(self):
        rc, _, err = run("score-check.py", fixture("score_pass.md"))
        self.assertEqual(rc, 0, err)

    def test_pass_prospect(self):
        rc, _, err = run("score-check.py", fixture("score_prospect_pass.md"))
        self.assertEqual(rc, 0, err)

    def test_fail_weights(self):
        rc, _, err = run("score-check.py", fixture("score_fail_sum.md"))
        self.assertEqual(rc, 1)
        self.assertIn("weights sum to 90", err)

    def test_fail_overall_and_range(self):
        rc, _, err = run("score-check.py", fixture("score_fail_overall.md"))
        self.assertEqual(rc, 1)
        self.assertIn("outside 0.0-10.0", err)
        self.assertIn("overall mismatch", err)

    def test_no_table(self):
        self.assertEqual(run("score-check.py", fixture("label_pass.md"))[0], 1)


if __name__ == "__main__":
    unittest.main()
