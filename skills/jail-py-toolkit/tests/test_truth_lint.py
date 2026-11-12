import json
import unittest
from _helper import run


def block(*claims):
    return json.dumps({"claims": list(claims)})


def claim(cid, status, ids=(), deriv="source", text="x"):
    return {"id": cid, "text": text, "status": status, "evidence_count": len(ids),
            "source_ids": list(ids), "derivation_type": deriv}


class TestTruthLint(unittest.TestCase):
    def test_canonical_labels_pass(self):
        b = block(claim("c1", "Fact", ["s1"]),
                  claim("c2", "Inference", ["s1"], "reasoned"),
                  claim("c3", "Unknown", [], "none"))
        rc, out, err = run("truth-lint.py", "-", stdin=b)
        self.assertEqual(rc, 0, err)
        self.assertIn("PASS", out)

    def test_legacy_aliases_still_pass(self):
        b = block(claim("c1", "Known", ["s1"]),
                  claim("c2", "Infer", ["s1"], "reasoned"),
                  claim("c3", "?Unknown", [], "none"),
                  claim("c4", "✓Known", ["s2"]),
                  claim("c5", "~Infer", ["s2"], "reasoned"))
        rc, _, err = run("truth-lint.py", "-", stdin=b)
        self.assertEqual(rc, 0, err)

    def test_unknown_status_fails(self):
        rc, _, err = run("truth-lint.py", "-", stdin=block(claim("c1", "Verified fact", ["s1"])))
        self.assertEqual(rc, 1)
        self.assertIn("not one of", err)

    def test_unevidenced_fact_fails(self):
        rc, _, err = run("truth-lint.py", "-", stdin=block(claim("c1", "Fact", [])))
        self.assertEqual(rc, 1)
        self.assertIn("Fact with no source_ids", err)

    def test_unevidenced_legacy_known_fails(self):
        rc, _, _ = run("truth-lint.py", "-", stdin=block(claim("c1", "Known", [])))
        self.assertEqual(rc, 1)

    def test_settled_fact_ok_without_retrieval(self):
        b = block(claim("c1", "Fact", [], "settled"))
        self.assertEqual(run("truth-lint.py", "-", stdin=b)[0], 0)

    def test_require_evidence_rejects_settled_fact(self):
        b = block(claim("c1", "Fact", [], "settled"))
        rc, _, err = run("truth-lint.py", "--require-evidence", "-", stdin=b)
        self.assertEqual(rc, 1)
        self.assertIn("require-evidence", err)

    def test_evidence_count_mismatch_fails(self):
        c = claim("c1", "Fact", ["s1"])
        c["evidence_count"] = 3
        self.assertEqual(run("truth-lint.py", "-", stdin=block(c))[0], 1)

    def test_bad_json_is_io_error(self):
        self.assertEqual(run("truth-lint.py", "-", stdin="{nope")[0], 2)


if __name__ == "__main__":
    unittest.main()
