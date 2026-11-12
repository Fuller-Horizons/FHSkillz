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

Warnings (exit 0 unless --strict):
  - a step has no machine-verifiable `success_test`
  - no chain-level `success_test`
  - a produced key is never consumed (and isn't the final step's output)
  - a step declares `on_fail: retry` while a later step depends on it
    (retry-forever risk; cap at one then stop)

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
