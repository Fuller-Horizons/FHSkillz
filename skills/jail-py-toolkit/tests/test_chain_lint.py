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

    def test_full_model_ids_accepted(self):
        def f(m):
            step(m, "compare")["agent"]["model"] = "claude-opus-5-5"
            step(m, "verify")["agent"]["model"] = "claude-fable-5-2"
        rc, _, err = lint(mutate(f), "--strict")
        self.assertEqual(rc, 0, err)

    def test_fable_alias_warns_to_pin(self):
        m = mutate(lambda m: step(m, "verify")["agent"].update(model="fable"))
        self.assertEqual(lint(m)[0], 0)
        rc, _, err = lint(m, "--strict")
        self.assertEqual(rc, 1)
        self.assertIn("claude-fable-5-2", err)

    def test_bad_model_id_rejected(self):
        rc, _, err = lint(mutate(lambda m: step(m, "verify")["agent"].update(model="claude-fable")))
        self.assertEqual(rc, 1)
        self.assertIn("full model ID", err)

    def test_haiku_full_id_still_needs_checkable_test(self):
        def f(m):
            step(m, "scan-a")["agent"]["model"] = "claude-haiku-5-5"
            step(m, "scan-a")["success_test"] = "looks right"
        rc, _, err = lint(mutate(f), "--strict")
        self.assertEqual(rc, 1)
        self.assertIn("haiku step needs", err)

    def test_escalate_must_be_stronger(self):
        rc, _, err = lint(mutate(lambda m: step(m, "compare")["agent"].update(escalate_to="haiku")))
        self.assertEqual(rc, 1)
        self.assertIn("not stronger", err)

    def test_escalate_must_be_valid(self):
        rc, _, err = lint(mutate(lambda m: step(m, "scan-a")["agent"].update(escalate_to="gpt-9")))
        self.assertEqual(rc, 1)
        self.assertIn("escalate_to", err)

    def test_missing_max_output_warns(self):
        m = mutate(lambda m: step(m, "compare")["agent"].pop("max_output"))
        rc, _, err = lint(m, "--strict")
        self.assertEqual(rc, 1)
        self.assertIn("max_output", err)

    def test_cheap_step_without_escalation_warns(self):
        m = mutate(lambda m: step(m, "scan-b")["agent"].pop("escalate_to"))
        rc, _, err = lint(m, "--strict")
        self.assertEqual(rc, 1)
        self.assertIn("no agent.escalate_to", err)

    def test_bad_check_policy_and_batch(self):
        def f(m):
            m["orchestration"]["check_policy"] = "some"
            step(m, "scan-a")["agent"]["batch"] = 0
        rc, _, err = lint(mutate(f))
        self.assertEqual(rc, 1)
        self.assertIn("check_policy", err)
        self.assertIn("agent.batch", err)

    def test_too_many_agents_warns(self):
        def f(m):
            base = step(m, "scan-a")
            for i in range(8):
                s = copy.deepcopy(base)
                s["id"] = f"scan-x{i}"
                s["produces"] = [f"prices-x{i}"]
                m["steps"].insert(0, s)
                step(m, "compare")["requires"].append(f"prices-x{i}")
            m["orchestration"]["max_agents"] = 20
        rc, _, err = lint(mutate(f), "--strict")
        self.assertEqual(rc, 1)
        self.assertIn("batch items into fewer agents", err)

    # ---- quality-first mode and measured model selection
    def test_mode_missing_warns_and_bad_mode_errors(self):
        m = mutate(lambda m: m["orchestration"].pop("mode"))
        rc, _, err = lint(m, "--strict")
        self.assertEqual(rc, 1)
        self.assertIn("treated as quality-first", err)
        rc, _, err = lint(mutate(lambda m: m["orchestration"].update(mode="fast")))
        self.assertEqual(rc, 1)
        self.assertIn("orchestration.mode", err)

    def test_quality_first_weak_merge_errors(self):
        rc, _, err = lint(mutate(lambda m: step(m, "compare")["agent"].update(model="sonnet")))
        self.assertEqual(rc, 1)
        self.assertIn("merge step 'compare'", err)

    def test_quality_first_weak_verifier_errors(self):
        rc, _, err = lint(mutate(lambda m: step(m, "verify")["agent"].update(model="sonnet")))
        self.assertEqual(rc, 1)
        self.assertIn("verifier 'verify' must run on a strong model", err)

    def test_quality_first_verifier_same_as_merge_warns(self):
        m = mutate(lambda m: step(m, "verify")["agent"].update(model="opus"))
        rc, _, err = lint(m, "--strict")
        self.assertEqual(rc, 1)
        self.assertIn("use a different strong model", err)

    def test_quality_first_unmeasured_cheap_step_warns(self):
        m = mutate(lambda m: step(m, "scan-a")["agent"].pop("selected_by"))
        self.assertEqual(lint(m)[0], 0)
        rc, _, err = lint(m, "--strict")
        self.assertEqual(rc, 1)
        self.assertIn("no agent.selected_by proof", err)

    def test_cost_first_allows_cheap_merge_unmeasured(self):
        def f(m):
            m["orchestration"]["mode"] = "cost-first"
            step(m, "compare")["agent"]["model"] = "sonnet"
            step(m, "scan-a")["agent"].pop("selected_by")
        rc, _, err = lint(mutate(f), "--strict")
        self.assertEqual(rc, 0, err)

    def test_selection_chosen_below_top_errors(self):
        def f(m):
            step(m, "scan-a")["agent"]["selected_by"]["scores"] = {"haiku": "9/12", "sonnet": "12/12", "opus": "12/12"}
        rc, _, err = lint(mutate(f))
        self.assertEqual(rc, 1)
        self.assertIn("below the top score", err)

    def test_selection_tie_should_pick_cheaper(self):
        def f(m):
            ag = step(m, "scan-a")["agent"]
            ag["model"] = "sonnet"
            ag["escalate_to"] = "opus"
        rc, _, err = lint(mutate(f), "--strict")
        self.assertEqual(rc, 1)
        self.assertIn("tie goes to the cheaper model", err)

    def test_selection_needs_strong_candidate_in_quality_first(self):
        def f(m):
            step(m, "scan-a")["agent"]["selected_by"]["candidates"] = ["haiku", "sonnet"]
            step(m, "scan-a")["agent"]["selected_by"]["scores"] = {"haiku": "12/12", "sonnet": "12/12"}
        rc, _, err = lint(mutate(f))
        self.assertEqual(rc, 1)
        self.assertIn("must include a strong candidate", err)

    def test_selection_shape_errors(self):
        rc, _, err = lint(mutate(lambda m: step(m, "scan-a")["agent"]["selected_by"].update(scores={"haiku": "x"})))
        self.assertEqual(rc, 1)
        self.assertIn("scores missing or unreadable", err)
        rc, _, err = lint(mutate(lambda m: step(m, "scan-a")["agent"]["selected_by"].update(candidates=["haiku"])))
        self.assertEqual(rc, 1)
        self.assertIn("2+ valid models", err)


if __name__ == "__main__":
    unittest.main()
