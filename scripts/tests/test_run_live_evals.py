import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "..", "run-live-evals.py")
FAKE = os.path.join(HERE, "fixtures", "live", "fake_claude.py")


def mkplugin(root, name):
    d = os.path.join(root, name)
    os.makedirs(os.path.join(d, ".claude-plugin"))
    with open(os.path.join(d, ".claude-plugin", "plugin.json"), "w") as f:
        f.write('{"name":"x"}')
    return d


class LiveEvalsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        t = self.tmp.name
        self.old = mkplugin(t, "plugin_old")
        self.new = mkplugin(t, "plugin_new")
        self.out = os.path.join(t, "out")
        self.cases = os.path.join(t, "cases.json")
        self.log = os.path.join(t, "calls.log")
        json.dump({"cases": [
            {"id": "c1", "skill": "s1", "prompt": "do the thing one",
             "assertions": ["a0", "a1"]},
            {"id": "c2", "skill": "s1", "prompt": "do the thing two",
             "assertions": ["a0", "a1"]}]}, open(self.cases, "w"))
        self.env = dict(os.environ,
                        FHSKILLZ_CLAUDE_BIN=f"{sys.executable} {FAKE}",
                        FAKE_CLAUDE_LOG=self.log)

    def tearDown(self):
        self.tmp.cleanup()

    def cli(self, *a, env=None):
        return subprocess.run([sys.executable, SCRIPT] + list(a), capture_output=True,
                              text=True, env=env or self.env)

    def run_args(self, *extra):
        return ["run", "--cases", self.cases, "--old", self.old, "--new", self.new,
                "--out", self.out, "--models", "haiku", "--jobs", "2"] + list(extra)

    def ncalls(self):
        return len(open(self.log).read().splitlines()) if os.path.exists(self.log) else 0

    def test_dry_run(self):
        p = self.cli(*self.run_args("--dry-run", "--max-cases-per-skill", "1"))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("planned runs: 2", p.stdout)
        self.assertEqual(self.ncalls(), 0)
        self.assertFalse(os.path.exists(self.out))

    def test_run_and_blind(self):
        p = self.cli(*self.run_args("--max-cases-per-skill", "1", "--seed", "3"))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(self.ncalls(), 2)
        calls = [json.loads(l) for l in open(self.log)]
        for c in calls:
            a = c["argv"]
            self.assertIn("--setting-sources", a)
            self.assertIn("stream-json", a)
            self.assertNotEqual(os.path.realpath(c["cwd"]), os.path.realpath(self.tmp.name))
        self.assertEqual({os.path.basename(c["argv"][c["argv"].index("--plugin-dir") + 1])
                          for c in calls}, {"plugin_old", "plugin_new"})
        runs = [json.loads(l) for l in open(os.path.join(self.out, "runs.jsonl"))]
        self.assertEqual(len(runs), 2)
        r = runs[0]
        self.assertEqual(r["skills_invoked"], ["fh-skillz:jail-research"])
        self.assertIn("WebSearch", r["tools"])
        self.assertEqual((r["turns"], r["cost"], r["duration_ms"]), (3, 0.0123, 1234))
        self.assertFalse(r["is_error"])
        key = json.load(open(os.path.join(self.out, "private", "key.json")))
        self.assertEqual(sorted(key["c1"].values()), ["new", "old"])
        odir = os.path.join(self.out, "outputs", "c1", "haiku")
        self.assertEqual(sorted(os.listdir(odir)), ["A.md", "B.md"])
        for fn in os.listdir(odir):
            txt = open(os.path.join(odir, fn)).read()
            self.assertTrue(txt.startswith("ANSWER to:"))
            for bad in ("old", "new", "plugin_"):
                self.assertNotIn(bad, txt)
        # no version leakage anywhere outside private/ and raw/ and runs.jsonl
        for root, _, files in os.walk(os.path.join(self.out, "outputs")):
            for fn in files:
                self.assertIn(fn, ("A.md", "B.md"))

    def test_resume_skips(self):
        self.assertEqual(self.cli(*self.run_args("--max-cases-per-skill", "1")).returncode, 0)
        key1 = open(os.path.join(self.out, "private", "key.json")).read()
        self.assertEqual(self.ncalls(), 2)
        p = self.cli(*self.run_args("--max-cases-per-skill", "1", "--seed", "99"))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(self.ncalls(), 2)  # no new calls
        self.assertIn("resumed", p.stdout)
        self.assertEqual(open(os.path.join(self.out, "private", "key.json")).read(), key1)
        self.assertEqual(len(open(os.path.join(self.out, "runs.jsonl")).read().splitlines()), 2)

    def test_failed_run_not_resumed(self):
        env = dict(self.env, FAKE_CLAUDE_FAIL="1")
        self.cli(*self.run_args("--max-cases-per-skill", "1"), env=env)
        runs = [json.loads(l) for l in open(os.path.join(self.out, "runs.jsonl"))]
        self.assertTrue(all(r["is_error"] for r in runs))
        self.cli(*self.run_args("--max-cases-per-skill", "1"))
        self.assertEqual(self.ncalls(), 4)

    def test_grade_pack(self):
        self.cli(*self.run_args())
        p = self.cli("grade-pack", "--out", self.out)
        self.assertEqual(p.returncode, 0, p.stderr)
        pack = json.load(open(os.path.join(self.out, "grading", "s1.json")))
        self.assertEqual(len(pack["cases"]), 2)
        c = pack["cases"][0]
        self.assertEqual(c["assertions"], ["a0", "a1"])
        self.assertEqual(sorted(c["models"]["haiku"]), ["A", "B"])
        blob = json.dumps(pack)
        for bad in ("plugin_old", "plugin_new", '"old"', '"new"'):
            self.assertNotIn(bad, blob)

    def _grades(self, new_results, old_results):
        """new_results/old_results: {case: [bools]} -> grades file (2 graders each)."""
        key = json.load(open(os.path.join(self.out, "private", "key.json")))
        path = os.path.join(self.tmp.name, "grades.jsonl")
        with open(path, "w") as f:
            for ver, res in (("new", new_results), ("old", old_results)):
                for case, ar in res.items():
                    label = [l for l, v in key[case].items() if v == ver][0]
                    for g in ("g1", "g2"):
                        f.write(json.dumps({"case": case, "model": "haiku", "label": label,
                                            "grader": g, "assertion_results": ar}) + "\n")
        return path

    def score(self, new_results, old_results):
        self.cli(*self.run_args())
        gp = self._grades(new_results, old_results)
        p = self.cli("score", "--out", self.out, "--grades", gp)
        self.assertEqual(p.returncode, 0, p.stderr)
        return json.load(open(os.path.join(self.out, "summary.json"))), p.stdout

    def test_score_keep(self):
        s, out = self.score({"c1": [True, True], "c2": [True, True]},
                            {"c1": [True, False], "c2": [True, True]})
        v = s["verdicts"]["s1"]
        self.assertEqual(v["verdict"], "KEEP")
        self.assertEqual(v["new_case_pass_rate"], 1.0)
        self.assertEqual(v["old_case_pass_rate"], 0.5)
        self.assertIn("VERDICT s1: KEEP", out)

    def test_score_revert_regression(self):
        # new wins on case pass rate but assertion 1 regresses in 2 cases -> impossible
        # with higher case rate unless more cases pass elsewhere; so test equal rates.
        s, _ = self.score({"c1": [True, False], "c2": [True, False]},
                          {"c1": [True, True], "c2": [True, True]})
        v = s["verdicts"]["s1"]
        self.assertEqual(v["verdict"], "REVERT")
        self.assertEqual(v["blocking_assertion_indexes"], ["1"])

    def test_score_revert_no_improvement(self):
        s, _ = self.score({"c1": [True, True], "c2": [True, True]},
                          {"c1": [True, True], "c2": [True, True]})
        self.assertEqual(s["verdicts"]["s1"]["verdict"], "REVERT")

    def test_score_disagreement(self):
        self.cli(*self.run_args("--max-cases-per-skill", "1"))
        key = json.load(open(os.path.join(self.out, "private", "key.json")))
        la = [l for l, v in key["c1"].items() if v == "new"][0]
        lb = [l for l, v in key["c1"].items() if v == "old"][0]
        gp = os.path.join(self.tmp.name, "g.jsonl")
        rows = [("g1", la, [True, True]), ("g2", la, [True, False]),
                ("g1", lb, [True, False]), ("g2", lb, [True, False])]
        with open(gp, "w") as f:
            for g, l, ar in rows:
                f.write(json.dumps({"case": "c1", "model": "haiku", "label": l,
                                    "grader": g, "assertion_results": ar}) + "\n")
        self.assertEqual(self.cli("score", "--out", self.out, "--grades", gp).returncode, 0)
        s = json.load(open(os.path.join(self.out, "summary.json")))
        self.assertEqual(len(s["disagreements"]), 1)
        self.assertEqual(s["disagreements"][0]["assertion_indexes"], [1])
        self.assertEqual(s["table"]["s1"]["new"]["haiku"]["case_pass_rate"], 0.0)


if __name__ == "__main__":
    unittest.main()
