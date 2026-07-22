#!/usr/bin/env python3
"""lab-compare.py — compare jail-lab ledgers or spans within one ledger.

Modes:
  Two ledgers:   lab-compare.py --ledger A.jsonl --against B.jsonl
                 (e.g. this wave's ledger vs last wave's)
  One ledger:    lab-compare.py --ledger A.jsonl --from-id 0 --to-id 5
                 (delta across a span; defaults: baseline -> latest)

Prints: baseline/best/latest per side, absolute + percent delta on best,
keep rates, and the kept-changes lists. Exit 0 = improved-or-equal per the
ledger's declared direction, 1 = regressed, 2 = error.
Stdlib only, Python 3.8+.
"""
import argparse
import json
import sys


def load(path):
    try:
        entries = [json.loads(l) for l in open(path, encoding="utf-8")
                   if l.strip()]
    except (OSError, json.JSONDecodeError) as e:
        print(f"[lab-compare] ERROR reading {path}: {e}", file=sys.stderr)
        sys.exit(2)
    if not entries:
        print(f"[lab-compare] ERROR: empty ledger {path}", file=sys.stderr)
        sys.exit(2)
    return entries


def summarize(entries, lo=None, hi=None):
    span = [e for e in entries
            if (lo is None or e["id"] >= lo) and (hi is None or e["id"] <= hi)]
    if not span:
        print("[lab-compare] ERROR: empty span", file=sys.stderr)
        sys.exit(2)
    direction = span[-1]["direction"]
    kept = [e for e in span if e["verdict"] in ("KEEP", "BASELINE")]
    return {
        "direction": direction,
        "n": len(span),
        "baseline": span[0]["metric"],
        "latest": span[-1]["metric"],
        "best": span[-1]["best_after"],
        "keep_rate": round(len([e for e in span if e["verdict"] == "KEEP"])
                           / max(1, len(span) - 1), 3) if len(span) > 1 else None,
        "kept_changes": [e["change"] for e in kept],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--against", help="second ledger to compare against")
    ap.add_argument("--from-id", type=int, default=None)
    ap.add_argument("--to-id", type=int, default=None)
    args = ap.parse_args()

    a = summarize(load(args.ledger), args.from_id, args.to_id)
    if args.against:
        b = summarize(load(args.against))
        left, right, ltag, rtag = b, a, args.against, args.ledger
    else:  # span mode: baseline of span vs best of span
        left = dict(a, best=a["baseline"])
        right = a
        ltag, rtag = f"{args.ledger}@start", f"{args.ledger}@end"

    delta = right["best"] - left["best"]
    pct = (delta / abs(left["best"]) * 100) if left["best"] else float("inf")
    direction = right["direction"]
    improved = delta >= 0 if direction == "max" else delta <= 0

    print(f"[lab-compare] {ltag}: best={left['best']}  →  "
          f"{rtag}: best={right['best']}")
    print(f"[lab-compare] delta={delta:+g} ({pct:+.1f}%) direction={direction}"
          f" → {'IMPROVED-OR-EQUAL' if improved else 'REGRESSED'}")
    print(f"[lab-compare] right side: n={right['n']} baseline="
          f"{right['baseline']} latest={right['latest']} "
          f"keep_rate={right['keep_rate']}")
    for c in right["kept_changes"]:
        print(f"[lab-compare]   kept: {c}")
    sys.exit(0 if improved else 1)


if __name__ == "__main__":
    main()
