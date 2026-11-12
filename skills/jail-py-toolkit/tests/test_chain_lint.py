import copy
import json
import unittest
from _helper import run, fixture

BASE = json.load(open(fixture("delegation_pass.json"), encoding="utf-8"))
LINEAR = {
    "chain": "two-step", "inputs": ["notes"],
    "success_test": "summary.json parses; 3 bullets",
    "steps": [
        {"id": "extract", "requires": ["notes"], "produces": ["facts"],
         "success_test": "facts.json parses", "on_fail": "stop"},
        {"id": "write", "requires": ["facts"], "produces": ["summary"],
         "success_test": "summary.json parses; 3 bullets", "on_fail": "stop"}]}


def lint(manifest, *flags):
    return run("chain-lint.py", *flags, stdin=json.dumps(manifest))


def mutate(fn):
    m = copy.deepcopy(BASE)
    fn(m)
    return m


def step(m, sid):
    return next(s for s in m["steps"] if s["id"] == sid)


class TestChainLintLinear(unittest.TestCase):
    def test_linear_pass(self):
        rc, out, err = lint(LINEAR, "--strict")
        self.assertEqual(rc, 0, err)

    def test_broken_handoff(self):
        m = copy.deepcopy(LINEAR)
        m["steps"][1]["requires"] = ["missing-key"]
        rc, _, err = lint(m)
        self.assertEqual(rc, 1)
        self.assertIn("no earlier step or input produces it", err)


class TestChainLintDelegation(unittest.TestCase):
    def test_example_passes_strict(self):
        rc, _, err = run("chain-lint.py", "--strict", fixture("delegation_pass.json"))
        self.assertEqual(rc, 0, err)

    def test_bad_model(self):
        rc, _, err = lint(mutate(lambda m: step(m, "scan-a")["agent"].update(model="gpt")))
        self.assertEqual(rc, 1)
        self.assertIn("agent.model", err)

    def test_bad_effort(self):
        rc, _, err = lint(mutate(lambda m: step(m, "compare")["agent"].update(effort="max")))
        self.assertEqual(rc, 1)
        self.assertIn("agent.effort", err)

    def test_max_agents_too_small(self):
        rc, _, err = lint(mutate(lambda m: m["orchestration"].update(max_agents=3)))
        self.assertEqual(rc, 1)
        self.assertIn("below the 5 agent steps", err)

    def test_depth_out_of_range(self):
        rc, _, err = lint(mutate(lambda m: m["orchestration"].update(max_depth=5)))
        self.assertEqual(rc, 1)
        self.assertIn("max_depth", err)

    def test_depth_two_warns(self):
        m = mutate(lambda m: m["orchestration"].update(max_depth=2))
        self.assertEqual(lint(m)[0], 0)
        rc, _, err = lint(m, "--strict")
        self.assertEqual(rc, 1)
        self.assertIn("start their own agents", err)

    def test_missing_scope_and_context(self):
        def f(m):
            del step(m, "scan-b")["agent"]["scope"]
            step(m, "scan-c")["agent"]["context"] = ["the conversation"]
        rc, _, err = lint(mutate(f))
        self.assertEqual(rc, 1)
        self.assertIn("agent.scope missing", err)
        self.assertIn("not the whole conversation", err)

    def test_verifier_missing_or_unknown(self):
        rc, _, err = lint(mutate(lambda m: m["orchestration"].pop("verifier")))
        self.assertEqual(rc, 1)
        self.assertIn("verifier missing", err)
        rc, _, err = lint(mutate(lambda m: m["orchestration"].update(verifier="nope")))
        self.assertEqual(rc, 1)
        self.assertIn("is not a step id", err)

    def test_verifier_checks_nothing(self):
        def f(m):
            m["orchestration"]["verifier"] = "scan-a"
        rc, _, err = lint(mutate(f))
        self.assertEqual(rc, 1)
        self.assertIn("checks nothing", err)

    def test_same_model_verifier_warns(self):
        def f(m):
            for s in m["steps"]:
                if "agent" in s:
                    s["agent"]["model"] = "sonnet"
        rc, _, err = lint(mutate(f), "--strict")
        self.assertEqual(rc, 1)
        self.assertIn("same model", err)

    def test_parallel_dependency(self):
        def f(m):
            step(m, "scan-b")["requires"] = ["competitor-list", "prices-a"]
        rc, _, err = lint(mutate(f))
        self.assertEqual(rc, 1)
        self.assertIn("sequential, not parallel", err)

    def test_haiku_needs_checkable_test(self):
        m = mutate(lambda m: step(m, "scan-a").update(success_test="looks right"))
        rc, _, err = lint(m, "--strict")
        self.assertEqual(rc, 1)
        self.assertIn("haiku step needs", err)

    def test_no_budget_warns(self):
        rc, _, err = lint(mutate(lambda m: m["orchestration"].pop("budget")), "--strict")
        self.assertEqual(rc, 1)
        self.assertIn("budget missing", err)


if __name__ == "__main__":
    unittest.main()
