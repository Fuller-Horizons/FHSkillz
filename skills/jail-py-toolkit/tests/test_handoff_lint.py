import unittest
from _helper import run, fixture, load


class TestHandoffLint(unittest.TestCase):
    def test_pass(self):
        rc, out, err = run("handoff-lint.py", fixture("handoff_pass.md"))
        self.assertEqual(rc, 0, err)

    def test_fail_missing_required(self):
        rc, _, err = run("handoff-lint.py", fixture("handoff_fail_missing.md"))
        self.assertEqual(rc, 1)
        self.assertIn("missing required key: approval_required", err)

    def test_fail_enums_unknown_key_order(self):
        rc, _, err = run("handoff-lint.py", fixture("handoff_fail_order.md"))
        self.assertEqual(rc, 1)
        for frag in ("status must be", "confidence must be", "unknown top-level key: extra"):
            self.assertIn(frag, err)

    def test_order_violation(self):
        text = "```yaml\nJAIL-HANDOFF:\n  skill: jail-x\n  unknowns: []\n  status: stop\n  approval_required: []\n```\n"
        m = load("handoff-lint.py")
        errs = m.lint_text(text)
        self.assertTrue(any("canonical order" in e for e in errs))

    def test_no_block(self):
        m = load("handoff-lint.py")
        self.assertEqual(m.lint_text("nothing here"), ["no JAIL-HANDOFF block found"])


if __name__ == "__main__":
    unittest.main()
