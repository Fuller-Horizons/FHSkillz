#!/usr/bin/env python3
"""truth-lint.py — validate an epistemic truth-tagged claim block.

A factual/research prompt that tags claims (see references/truth-tagging.md) emits
a JSON object with a `claims` array, each claim carrying `status` (Known / Infer /
Unknown) plus evidence fields. Prose tags are theater; this linter makes the tags
real by rejecting the ways a model fakes them:

Errors (exit 1):
  - a claim `status` is not one of Known / Infer / Unknown
  - a claim's stated `evidence_count` disagrees with len(`source_ids`)
  - a `Known` claim lists no source_ids but is not marked derivation_type
    "settled" (a certainty claim with neither evidence nor "settled" basis)
  - with --require-evidence: any `Known` claim with zero evidence ids
    (use when the prompt's SOURCES declares a retrieval capability)
  - the block isn't the expected shape

Warnings (exit 0 unless --strict):
  - a claim has no non-empty `text`
  - `Infer` with no `source_ids` and derivation_type not "reasoned"
  - duplicate claim ids

Usage:
  truth-lint.py FILE                      # validate claims in FILE
  truth-lint.py - [--require-evidence]    # validate stdin
  ... | truth-lint.py --require-evidence

Exit codes: 0 = pass, 1 = errors, 2 = usage/IO/parse error. Stdlib only.
"""
import sys, json, argparse

VALID_STATUS = {"Known", "Infer", "Unknown"}


def lint(block, require_evidence):
    errors, warnings = [], []

    if not isinstance(block, dict):
        return ["top level must be a JSON object with a 'claims' array"], []
    claims = block.get("claims")
    if not isinstance(claims, list) or not claims:
        return ["'claims' must be a non-empty array"], []

    seen = set()
    for i, c in enumerate(claims, 1):
        if not isinstance(c, dict):
            errors.append(f"claim #{i} must be a JSON object")
            continue
        cid = str(c.get("id") or f"#{i}").strip()
        if cid in seen:
            warnings.append(f"duplicate claim id: {cid!r}")
        seen.add(cid)

        status = c.get("status")
        if status not in VALID_STATUS:
            errors.append(f"claim {cid!r}: status {status!r} not one of {sorted(VALID_STATUS)}")

        sids = c.get("source_ids", [])
        if not isinstance(sids, list):
            errors.append(f"claim {cid!r}: source_ids must be a list")
            sids = []
        ecount = c.get("evidence_count", len(sids))
        if not isinstance(ecount, int):
            errors.append(f"claim {cid!r}: evidence_count must be an integer")
        elif ecount != len(sids):
            errors.append(
                f"claim {cid!r}: evidence_count {ecount} != {len(sids)} source_ids listed"
            )

        deriv = (c.get("derivation_type") or "").strip().lower()

        if status == "Known":
            if len(sids) == 0:
                if require_evidence:
                    errors.append(
                        f"claim {cid!r}: Known with no source_ids, but --require-evidence is set "
                        "(the prompt declares retrieval — ground it or drop to Infer/Unknown)"
                    )
                elif deriv != "settled":
                    errors.append(
                        f"claim {cid!r}: Known with no source_ids and not derivation_type 'settled' "
                        "(a certainty claim needs evidence or a 'settled' basis — else use Infer/Unknown)"
                    )

        if status == "Infer" and len(sids) == 0 and deriv != "reasoned":
            warnings.append(
                f"claim {cid!r}: Infer with no source_ids and not derivation_type 'reasoned'"
            )

        if not str(c.get("text") or "").strip():
            warnings.append(f"claim {cid!r}: empty text")

    return errors, warnings


def main():
    ap = argparse.ArgumentParser(description="Validate an epistemic truth-tagged claim block.")
    ap.add_argument("file", nargs="?", default="-", help="claims JSON to lint; - or omit for stdin")
    ap.add_argument("--require-evidence", action="store_true",
                    help="every Known claim must have >=1 source id (use when SOURCES declares retrieval)")
    ap.add_argument("--strict", action="store_true", help="treat warnings as failures")
    args = ap.parse_args()

    try:
        raw = sys.stdin.read() if args.file == "-" else open(args.file, encoding="utf-8").read()
    except OSError as e:
        print(f"error: cannot read {args.file}: {e}", file=sys.stderr)
        return 2
    try:
        block = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"error: claims block is not valid JSON: {e}", file=sys.stderr)
        return 2

    errors, warnings = lint(block, args.require_evidence)
    for w in warnings:
        print(f"warning: {w}", file=sys.stderr)
    for e in errors:
        print(f"error: {e}", file=sys.stderr)

    if errors or (args.strict and warnings):
        print(f"\ntruth-lint: FAIL ({len(errors)} error(s), {len(warnings)} warning(s)).", file=sys.stderr)
        return 1
    print(f"truth-lint: PASS ({len(warnings)} warning(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
