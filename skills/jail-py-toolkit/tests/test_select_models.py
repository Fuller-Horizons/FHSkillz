import json
import os
import sys
import unittest
from _helper import run, fixture, load

FAKE = f"{sys.executable} {fixture('select/fake_claude.py')}"
ARGS = ["--prompt", fixture("select/brief.md"), "--items", fixture("select/items.jsonl"),
        "--checks", fixture("select/checks.txt"), "--grader", "fable"]


def sel(passing, *extra):
    env = dict(os.environ, FHSKILLZ_CLAUDE_BIN=FAKE, FAKE_PASS=passing)
    import subprocess
    p = subprocess.run([sys.executable, os.path.join(os.path.dirname(fixture("x")), "..", "..", "scripts",
                        "select-models.py"), *ARGS, *extra], capture_output=True, text=True, env=env)
    return p.returncode, p.stdout, p.stderr


class TestSelectModels(unittest.TestCase):
    def test_tie_goes_to_cheaper(self):
        rc, out, err = sel("haiku,sonnet,opus", "--candidates", "haiku,sonnet,opus")
        self.assertEqual(rc, 0, err)
        rec = json.loads(out)
        self.assertEqual(rec["chosen"], "haiku")
        self.assertEqual(rec["selected_by"]["scores"], {"haiku": "9/9", "sonnet": "9/9", "opus": "9/9"})

    def test_strong_wins_when_cheap_fails(self):
        rc, out, err = sel("opus", "--candidates", "haiku,opus")
        self.assertEqual(rc, 0, err)
        self.assertEqual(json.loads(out)["chosen"], "opus")

    def test_record_passes_chain_lint_shape(self):
        rc, out, err = sel("sonnet,opus", "--candidates", "haiku,sonnet,opus")
        rec = json.loads(out)
        self.assertEqual(rec["chosen"], "sonnet")
        sb = rec["selected_by"]
        for k in ("date", "items", "candidates", "scores", "grader"):
            self.assertIn(k, sb)
        self.assertEqual(sb["items"], 3)

    def test_nobody_passes(self):
        rc, _, err = sel("", "--candidates", "haiku,opus")
        self.assertEqual(rc, 1)
        self.assertIn("no candidate passed", err)

    def test_dry_run_and_usage(self):
        rc, _, err = sel("", "--candidates", "haiku,opus", "--dry-run")
        self.assertEqual(rc, 0)
        self.assertIn("3 items × 2 candidates + 3 grading calls = 9 calls", err)
        rc, _, err = sel("", "--candidates", "haiku")
        self.assertEqual(rc, 2)

    def test_choose_unit(self):
        m = load("select-models.py")
        self.assertEqual(m.choose({"haiku": (8, 9), "sonnet": (9, 9), "opus": (9, 9)})[0], "sonnet")
        self.assertEqual(m.choose({"claude-haiku-5-5": (9, 9), "claude-opus-5-5": (9, 9)})[0], "claude-haiku-5-5")
        self.assertEqual(m.tier("claude-fable-5-2"), 4)

    def test_parse_grades_rejects_bad_shape(self):
        m = load("select-models.py")
        self.assertEqual(m.parse_grades('x {"A": [true, false]} y', ["A"], 2), {"A": [True, False]})
        with self.assertRaises(ValueError):
            m.parse_grades('{"A": [true]}', ["A"], 2)

    def test_repeats_counts_calls_and_records(self):
        rc, _, err = sel("", "--candidates", "haiku,opus", "--dry-run", "--repeats", "3")
        self.assertIn("× 3 repeats = 27 calls", err)
        rc, out, err = sel("haiku,opus", "--candidates", "haiku,opus", "--repeats", "3")
        self.assertEqual(rc, 0, err)
        rec = json.loads(out)
        self.assertEqual(rec["selected_by"]["repeats"], 3)
        self.assertEqual(rec["selected_by"]["scores"]["haiku"], "9/9")


if __name__ == "__main__":
    unittest.main()
