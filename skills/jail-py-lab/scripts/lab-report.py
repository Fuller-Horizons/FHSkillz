#!/usr/bin/env python3
"""lab-report.py — summarize a jail-lab JSONL ledger.

Prints: baseline → best trajectory, keep rate, kept changes in order, the
last entries, and stop-condition status (consecutive discards).

Exit codes: 0 = ok · 2 = error.

Usage: lab-report.py --ledger lab-ledger.jsonl [--tail N] [--max-discards N]
"""
import argparse
import json
import os
import sys


def die(msg: str) -> None:
    print(f"[lab-report] ERROR: {msg}", file=sys.stderr)
    sys.exit(2)


def main() -> None:
    ap = argparse.ArgumentParser(description="Summarize a jail-lab ledger.")
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--tail", type=int, default=5, help="how many recent entries to show")
    ap.add_argument(
        "--max-discards", type=int, default=5,
        help="consecutive-discard stop threshold to report against",
    )
    args = ap.parse_args()

    if not os.path.exists(args.ledger):
        die(f"ledger not found: {args.ledger}")
    entries = []
    with open(args.ledger, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                die(f"ledger line {i} is not valid JSON")
    if not entries:
        die("ledger is empty — record a baseline with lab-run.py --baseline")

    base = entries[0]
    direction = base.get("direction", "?")
    kept = [e for e in entries if e.get("verdict") == "KEEP"]
    experiments = [e for e in entries if e.get("verdict") != "BASELINE"]
    best = entries[-1].get("best_after")

    streak = 0
    for e in reversed(entries):
        if e.get("verdict") == "DISCARD":
            streak += 1
        else:
            break

    print(f"JAIL-LAB REPORT — {args.ledger}")
    print(f"  direction: {direction}  ·  experiments: {len(experiments)}  ·  entries: {len(entries)}")
    print(f"  baseline:  {base.get('metric')}  ({base.get('change', '')})")
    print(f"  best:      {best}")
    if experiments:
        rate = len(kept) / len(experiments)
        print(f"  keep rate: {len(kept)}/{len(experiments)} ({rate:.0%})")
    if kept:
        print("  kept changes, in order:")
        for e in kept:
            print(f"    #{e['id']}: {e.get('change')}  ->  {e.get('metric')}")
    else:
        print("  kept changes: none yet — baseline still stands")
    print(f"  last {min(args.tail, len(entries))} entries:")
    for e in entries[-args.tail:]:
        print(
            f"    #{e['id']} [{e.get('verdict')}] {e.get('metric')}  "
            f"{e.get('change')!r}"
        )
    print(f"  consecutive discards: {streak} (stop threshold: {args.max_discards})")
    if streak >= args.max_discards:
        print("  STOP CONDITION MET — ideas have gone dry; ship the best and close the lab.")
    sys.exit(0)


if __name__ == "__main__":
    main()
