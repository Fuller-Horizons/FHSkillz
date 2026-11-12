#!/usr/bin/env python3
"""chain-lint.py — verify the handoffs in a JAIL-PROMPT chain manifest.

A chain manifest is JSON describing ordered steps, each with `requires` and
`produces` key lists (see references/chaining.md). This linker check proves the
chain is wired correctly *before* it runs: every key a step requires must be
produced by an earlier step or declared in the chain `inputs`. A broken handoff
fails the chain at runtime no matter how good each prompt is — catch it here.

Errors (exit 1):
  - a step `requires` a key produced by no earlier step and not in `inputs`
  - duplicate step ids
  - a step has no `produces` (it can't hand anything off)
  - manifest is not the expected shape
  - delegation manifests (an `orchestration` block, see jail-prompt
    references/delegation.md): bad model/effort value, missing or too-small
    caps, an agent step with no scope or context, a missing or non-checking
    verifier, parallel steps that need each other's output

Warnings (exit 0 unless --strict):
  - a step has no machine-verifiable `success_test`
  - no chain-level `success_test`
  - a produced key is never consumed (and isn't the final step's output)
  - a step declares `on_fail: retry` while a later step depends on it
    (retry-forever risk; cap at one then stop)
  - delegation: no budget, max_depth > 1, a haiku step without a
    machine-verifiable success_test, a verifier on the same model as the
    only producer it checks

Usage:
  chain-lint.py FILE        # lint manifest in FILE
  chain-lint.py -           # lint stdin
  ... | chain-lint.py       # (no args) lint stdin
  add --strict to fail on warnings too.

Exit codes: 0 = pass, 1 = errors, 2 = usage/IO/parse error. Stdlib only.
"""
import sys, os, json, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# Same notion of "machine-verifiable" as prompt-lint.py — imported, not copied,
# so the two linters can't drift (filename has a hyphen, so load it by path,
# same pattern save-rating.py uses for validate-rating.py).
import importlib.util

try:
    _spec = importlib.util.spec_from_file_location(
        "prompt_lint", os.path.join(HERE, "prompt-lint.py")
    )
    _pl = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_pl)
    VERIFIABLE = _pl.VERIFIABLE
except (OSError, ImportError, AttributeError) as e:
    print(
        f"error: cannot load sibling prompt-lint.py (must sit next to chain-lint.py "
        f"in scripts/ for the shared VERIFIABLE regex): {e}",
        file=sys.stderr,
    )
    sys.exit(2)

VALID_ON_FAIL = {"retry", "stop", "rollback", "human"}
VALID_MODELS = {"haiku", "sonnet", "opus", "inherit"}
VALID_EFFORT = {"low", "medium", "high"}


def as_keys(v):
    """Normalize a requires/produces field to a list of non-empty strings."""
    if v is None:
        return []
    if isinstance(v, str):
        v = [v]
    if not isinstance(v, list):
        return None  # signal a shape error
    return [str(x).strip() for x in v if str(x).strip()]


def lint(manifest):
    errors, warnings = [], []

    if not isinstance(manifest, dict):
        return ["manifest must be a JSON object"], []
    steps = manifest.get("steps")
    if not isinstance(steps, list) or not steps:
        return ["manifest.steps must be a non-empty array"], []

    inputs = as_keys(manifest.get("inputs"))
    if inputs is None:
        errors.append("manifest.inputs must be a list of strings")
        inputs = []

    if not (manifest.get("success_test") or "").strip():
        warnings.append("no chain-level success_test (the contract for the whole chain)")
    elif not VERIFIABLE.search(str(manifest.get("success_test"))):
        warnings.append("chain-level success_test has no machine-verifiable check")

    available = set(inputs)            # keys producible so far
    produced_by = {k: "inputs" for k in inputs}
    consumed = set()
    seen_ids = set()
    step_index = {}                    # id -> position
    requires_map = {}                  # id -> [keys]

    for i, step in enumerate(steps, 1):
        if not isinstance(step, dict):
            errors.append(f"step #{i} must be a JSON object")
            continue
        sid = str(step.get("id") or f"#{i}").strip()
        if sid in seen_ids:
            errors.append(f"duplicate step id: {sid!r}")
        seen_ids.add(sid)
        step_index[sid] = i

        reqs = as_keys(step.get("requires"))
        prods = as_keys(step.get("produces"))
        if reqs is None:
            errors.append(f"step {sid!r}: requires must be a list of strings")
            reqs = []
        if prods is None:
            errors.append(f"step {sid!r}: produces must be a list of strings")
            prods = []
        requires_map[sid] = reqs

        for r in reqs:
            consumed.add(r)
            if r not in available:
                errors.append(
                    f"step {sid!r} requires {r!r} but no earlier step or input produces it"
                )

        if not prods:
            errors.append(f"step {sid!r} produces nothing — it can't hand off to a later step")
        for p in prods:
            if p in produced_by:
                warnings.append(
                    f"key {p!r} produced by both {produced_by[p]!r} and {sid!r} (later overwrites earlier)"
                )
            produced_by[p] = sid
            available.add(p)

        on_fail = step.get("on_fail")
        if on_fail is not None and on_fail not in VALID_ON_FAIL:
            errors.append(f"step {sid!r}: on_fail {on_fail!r} not one of {sorted(VALID_ON_FAIL)}")

        st = (step.get("success_test") or "").strip()
        if not st:
            warnings.append(f"step {sid!r} has no success_test")
        elif not VERIFIABLE.search(st):
            warnings.append(f"step {sid!r} success_test has no machine-verifiable check")

    # retry-forever risk: a retry step that a later step depends on
    for sid, i in step_index.items():
        step = steps[i - 1]
        if isinstance(step, dict) and step.get("on_fail") == "retry":
            prods = set(as_keys(step.get("produces")) or [])
            downstream = any(
                step_index.get(other_id, 0) > i and (prods & set(reqs))
                for other_id, reqs in requires_map.items()
            )
            if downstream:
                warnings.append(
                    f"step {sid!r} is on_fail=retry but a later step depends on it "
                    "(cap retries at one, then stop)"
                )

    # produced-but-never-consumed (ignore the final step's output = the deliverable)
    final_prods = set(as_keys(steps[-1].get("produces")) if isinstance(steps[-1], dict) else [])
    for k, src in produced_by.items():
        if src not in ("inputs",) and k not in consumed and k not in final_prods:
            warnings.append(f"key {k!r} produced by {src!r} is never consumed")

    if "orchestration" in manifest:
        e2, w2 = lint_orchestration(manifest, steps)
        errors += e2
        warnings += w2

    return errors, warnings


def lint_orchestration(manifest, steps):
    """Checks for a delegation (multi-agent) manifest."""
    errors, warnings = [], []
    orch = manifest.get("orchestration")
    if not isinstance(orch, dict):
        return ["orchestration must be a JSON object"], []
    by_id = {}
    for i, st in enumerate(steps, 1):
        if isinstance(st, dict):
            by_id[str(st.get("id") or f"#{i}").strip()] = st
    agent_steps = [sid for sid, st in by_id.items() if "agent" in st]
    if not agent_steps:
        errors.append("orchestration present but no step has an agent block")

    ma = orch.get("max_agents")
    if not isinstance(ma, int) or isinstance(ma, bool) or ma < 1:
        errors.append("orchestration.max_agents must be a positive whole number")
    elif ma < len(agent_steps):
        errors.append(f"orchestration.max_agents={ma} is below the {len(agent_steps)} agent steps")
    md = orch.get("max_depth")
    if not isinstance(md, int) or isinstance(md, bool) or not 0 <= md <= 2:
        errors.append("orchestration.max_depth must be a whole number 0-2 (default 1)")
    elif md > 1:
        warnings.append("orchestration.max_depth > 1 lets subagents start their own agents")
    if not str(orch.get("budget") or "").strip():
        warnings.append("orchestration.budget missing (time/tokens/dollars and what happens when it runs out)")

    produced = {}
    for sid, st in by_id.items():
        for k in as_keys(st.get("produces")) or []:
            produced.setdefault(k, set()).add(sid)

    for sid in agent_steps:
        ag = by_id[sid]["agent"]
        if not isinstance(ag, dict):
            errors.append(f"step {sid!r}: agent must be a JSON object")
            continue
        if ag.get("model") not in VALID_MODELS:
            errors.append(f"step {sid!r}: agent.model {ag.get('model')!r} not one of {sorted(VALID_MODELS)}")
        if "effort" in ag and ag.get("effort") not in VALID_EFFORT:
            errors.append(f"step {sid!r}: agent.effort {ag.get('effort')!r} not one of {sorted(VALID_EFFORT)}")
        if not str(ag.get("scope") or "").strip():
            errors.append(f"step {sid!r}: agent.scope missing (what it owns and must not touch)")
        ctx = as_keys(ag.get("context"))
        if not ctx:
            errors.append(f"step {sid!r}: agent.context missing (list the exact inputs it receives)")
        elif any(c.lower() in ("conversation", "the conversation", "all", "everything") for c in ctx):
            errors.append(f"step {sid!r}: agent.context must list specific inputs, not the whole conversation")
        if ag.get("model") == "haiku" and not VERIFIABLE.search(str(by_id[sid].get("success_test") or "")):
            warnings.append(f"step {sid!r}: haiku step needs a machine-verifiable success_test to catch cheap misses")

    vid = str(orch.get("verifier") or "").strip()
    if not vid:
        errors.append("orchestration.verifier missing (id of the independent check step)")
    elif vid not in by_id:
        errors.append(f"orchestration.verifier {vid!r} is not a step id")
    else:
        vreqs = as_keys(by_id[vid].get("requires")) or []
        checked = {p for k in vreqs for p in produced.get(k, set()) if p != vid}
        if not checked:
            errors.append(f"verifier {vid!r} requires no output of another step, so it checks nothing")
        vm = (by_id[vid].get("agent") or {}).get("model") if isinstance(by_id[vid].get("agent"), dict) else None
        pm = {(by_id[c].get("agent") or {}).get("model") for c in checked if isinstance(by_id[c].get("agent"), dict)}
        if vm and pm == {vm} and vm != "inherit":
            warnings.append(f"verifier {vid!r} uses the same model as everything it checks; prefer a different model")

    groups = {}
    for sid, st in by_id.items():
        g = st.get("parallel_group")
        if g:
            groups.setdefault(str(g), []).append(sid)
    for g, members in groups.items():
        outs = {k: sid for sid in members for k in as_keys(by_id[sid].get("produces")) or []}
        for sid in members:
            for r in as_keys(by_id[sid].get("requires")) or []:
                if r in outs and outs[r] != sid:
                    errors.append(f"parallel_group {g!r}: {sid!r} needs {r!r} from {outs[r]!r}; that is sequential, not parallel")
    return errors, warnings


def main():
    ap = argparse.ArgumentParser(description="Verify handoffs in a JAIL-PROMPT chain manifest.")
    ap.add_argument("file", nargs="?", default="-", help="manifest to lint; - or omit for stdin")
    ap.add_argument("--strict", action="store_true", help="treat warnings as failures")
    args = ap.parse_args()

    try:
        raw = sys.stdin.read() if args.file == "-" else open(args.file, encoding="utf-8").read()
    except OSError as e:
        print(f"error: cannot read {args.file}: {e}", file=sys.stderr)
        return 2
    try:
        manifest = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"error: manifest is not valid JSON: {e}", file=sys.stderr)
        return 2

    errors, warnings = lint(manifest)
    for w in warnings:
        print(f"warning: {w}", file=sys.stderr)
    for e in errors:
        print(f"error: {e}", file=sys.stderr)

    if errors or (args.strict and warnings):
        print(f"\nchain-lint: FAIL ({len(errors)} error(s), {len(warnings)} warning(s)).", file=sys.stderr)
        return 1
    print(f"chain-lint: PASS ({len(warnings)} warning(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
