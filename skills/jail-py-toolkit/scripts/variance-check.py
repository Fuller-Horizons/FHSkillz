#!/usr/bin/env python3
"""variance-check.py — empirically verify rating determinism.

Takes 2+ jail-rate-skill JSON records of the SAME skill (produced across repeated
runs) and reports per-category mean and standard deviation. Fails (non-zero
exit) if any category's stddev exceeds the determinism threshold, so a claim of
"temperature 0.0, identical scores" is measured rather than assumed.

Borrows skill-creator's empirical mean +/- stddev pattern and applies it to the
static rating, grounding the "Idempotency & Determinism" category.

Usage:
    python3 variance-check.py run1.json run2.json [run3.json ...]
    python3 variance-check.py --threshold 0.2 run*.json
"""
import argparse
import json
import statistics
import sys

DEFAULT_THRESHOLD = 0.2


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def main():
    ap = argparse.ArgumentParser(description="Check score variance across repeated jail-rate-skill runs.")
    ap.add_argument("records", nargs="+", help="2+ rating JSON files of the same skill")
    ap.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD,
                    help=f"max allowed per-category stddev (default {DEFAULT_THRESHOLD})")
    args = ap.parse_args()

    if len(args.records) < 2:
        print("error: need at least 2 rating records to measure variance", file=sys.stderr)
        return 2

    records = [load(p) for p in args.records]

    skills = {r.get("skill") for r in records}
    if len(skills) > 1:
        print(f"error: records are for different skills: {sorted(skills)}", file=sys.stderr)
        return 2
    skill = skills.pop()

    # Collect category -> [scores...] in input order
    categories = list(records[0].get("categories", {}).keys())
    series = {c: [] for c in categories}
    for r in records:
        cats = r.get("categories", {})
        for c in categories:
            if c not in cats:
                print(f"error: category '{c}' missing in one of the records", file=sys.stderr)
                return 2
            series[c].append(float(cats[c]["score"]))

    overalls = [float(r["overall"]) for r in records]

    print(f"Skill: {skill}   runs: {len(records)}   threshold: +/-{args.threshold}\n")
    header = f"{'Category':36} {'mean':>6} {'stddev':>7} {'min':>5} {'max':>5}  flag"
    print(header)
    print("-" * len(header))

    failed = []
    for c in categories:
        vals = series[c]
        mean = statistics.fmean(vals)
        sd = statistics.pstdev(vals)
        flag = "DRIFT" if sd > args.threshold else "ok"
        if sd > args.threshold:
            failed.append(c)
        print(f"{c:36} {mean:6.2f} {sd:7.3f} {min(vals):5.1f} {max(vals):5.1f}  {flag}")

    o_mean = statistics.fmean(overalls)
    o_sd = statistics.pstdev(overalls)
    print("-" * len(header))
    print(f"{'Overall':36} {o_mean:6.2f} {o_sd:7.3f} {min(overalls):5.1f} {max(overalls):5.1f}")

    if failed:
        print(f"\nFAIL: {len(failed)} category(ies) drift > +/-{args.threshold}: {', '.join(failed)}",
              file=sys.stderr)
        return 1
    print(f"\nPASS: all categories within +/-{args.threshold} across {len(records)} runs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
