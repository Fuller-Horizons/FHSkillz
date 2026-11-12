import json
import os
import tempfile
import unittest
from _helper import run, fixture

SRC = fixture("quote/src")


def qc(claims, *extra):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(claims, f)
    try:
        return run("quote-check.py", "--claims", f.name, "--sources", SRC, *extra)
    finally:
        os.unlink(f.name)


class TestQuoteCheck(unittest.TestCase):
    def test_found_with_html_and_dashes(self):
        rc, out, err = qc([
            {"id": "c1", "claim": "Plan costs $189/yr", "quote": "annual tune-up plan is $189 per year", "source": "s1"},
            {"id": "c2", "claim": "Two visits", "quote": "includes two visits - spring and fall", "source": "s1"},
            {"id": "c3", "claim": "Re-explaining", "quote": "explain the alarm code and the dog every single time", "source": "s2"}])
        self.assertEqual(rc, 0, out + err)  # entity &#8209; (non-breaking hyphen), <b>, em dash all normalize
        self.assertIn("3 Fact claim(s) verified", out)

    def test_invented_quote_fails(self):
        rc, _, err = qc([{"id": "c1", "claim": "x", "quote": "plan is $149 per year and includes three visits", "source": "s1"}])
        self.assertEqual(rc, 1)
        self.assertIn("NOT FOUND", err)

    def test_fact_without_quote_or_source(self):
        rc, _, err = qc([{"id": "a", "claim": "x"}, {"id": "b", "claim": "y", "quote": "Comfort Club annual tune", "source": "s9"}])
        self.assertEqual(rc, 1)
        self.assertIn("a: Fact with no quote", err)
        self.assertIn("b: source 's9' not provided", err)

    def test_inference_needs_no_quote(self):
        rc, out, err = qc([{"id": "i", "claim": "cheaper than client", "label": "Inference"}])
        self.assertEqual(rc, 0, err)
        self.assertIn("0 Fact claim(s)", out)

    def test_short_and_long_quotes(self):
        rc, _, err = qc([{"id": "s", "claim": "x", "quote": "$189 per year", "source": "s1"}])
        self.assertEqual(rc, 1)
        self.assertIn("too short", err)
        long_q = "I have to explain the alarm code and the dog every single time."
        rc, _, err = qc([{"id": "l", "claim": "x", "quote": long_q, "source": "s2"}], "--strict")
        self.assertEqual(rc, 0, err)

    def test_usage(self):
        self.assertEqual(run("quote-check.py", "--claims", "nope.json", "--sources", SRC)[0], 2)


if __name__ == "__main__":
    unittest.main()
