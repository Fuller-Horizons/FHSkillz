#!/usr/bin/env python3
"""lab-run.py — append one experiment to a jail-lab JSONL ledger.

Gets the metric from --metric VALUE or by running --metric-cmd and parsing
the LAST number in its stdout. Compares against best-so-far per --direction,
records KEEP / DISCARD / BASELINE. Append-only: never rewrites past lines.

Exit codes: 0 = keep/baseline recorded · 1 = discard recorded · 2 = error.

Usage:
  lab-run.py --ledger lab-ledger.jsonl --direction max --baseline \
             --change "unmodified baseline" --metric 0.72
  lab-run.py --ledger lab-ledger.jsonl --direction max \
             --change "tightened description" --hypothesis "better routing" \
             --metric 0.78 [--evidence evals/run-14.txt]
  lab-run.py --ledger lab-ledger.jsonl --direction min \
             --change "cache prefix" --hypothesis "fewer tokens" \
             --metric-cmd "python3 bench.py --quiet"
"""
import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

NUM_RE = re.compile(r"-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?")


def die(msg: str) -> None:
    print(f"[lab-run] ERROR: {msg}", file=sys.stderr)
    sys.exit(2)


def read_ledger(path: str):
    entries = []
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError:
                    die(f"ledger line {i} is not valid JSON — ledger corrupt")
    return entries


def measure_from_cmd(cmd: str) -> float:
    try:
        proc = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, timeout=1800
        )
    except subprocess.TimeoutExpired:
        die("metric command exceeded 30-minute bound")
    out = (proc.stdout or "") + ("\n" + proc.stderr if proc.stderr else "")
    if proc.returncode != 0:
        die(f"metric command exited {proc.returncode}: {out.strip()[-300:]}")
    nums = NUM_RE.findall(proc.stdout or "")
    if not nums:
        die("no number found in metric command stdout")
    return float(nums[-1])


def main() -> None:
    ap = argparse.ArgumentParser(description="Append one jail-lab experiment.")
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--direction", required=True, choices=["min", "max"])
    ap.add_argument("--change", required=True, help="what was changed (one variable)")
    ap.add_argument("--hypothesis", default="", help="why it should move the metric")
    ap.add_argument("--metric", type=float, help="measured value (if already measured)")
    ap.add_argument("--metric-cmd", help="command whose stdout's last number is the metric")
    ap.add_argument("--evidence", default="", help="path/URL supporting the measurement")
    ap.add_argument("--baseline", action="store_true", help="record as experiment #0 baseline")
    args = ap.parse_args()

    if (args.metric is None) == (args.metric_cmd is None):
        die("provide exactly one of --metric or --metric-cmd")
    if not args.baseline and not args.hypothesis:
        die("--hypothesis is required for non-baseline experiments (why should this work?)")

    entries = read_ledger(args.ledger)

    if args.baseline and entries:
        die("ledger already has entries; baseline must be experiment #0")
    if not args.baseline and not entries:
        die("no baseline in ledger — record one first with --baseline")
    if entries and entries[0].get("direction") != args.direction:
        die(
            f"direction mismatch: ledger declared '{entries[0].get('direction')}', "
            f"got '{args.direction}' — the lab's metric direction never changes mid-run"
        )

    metric = args.metric if args.metric is not None else measure_from_cmd(args.metric_cmd)

    better = (lambda a, b: a > b) if args.direction == "max" else (lambda a, b: a < b)
    best_prev = None
    for e in entries:
        v = e.get("metric")
        if v is None:
            continue
        if best_prev is None or better(v, best_prev):
            best_prev = v

    if args.baseline:
        verdict, best_after = "BASELINE", metric
    elif better(metric, best_prev):
        verdict, best_after = "KEEP", metric
    else:
        verdict, best_after = "DISCARD", best_prev  # ties discard: complexity must pay rent

    entry = {
        "id": len(entries),
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "change": args.change,
        "hypothesis": args.hypothesis,
        "metric": metric,
        "direction": args.direction,
        "verdict": verdict,
        "best_after": best_after,
        "evidence": args.evidence,
    }
    with open(args.ledger, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

    arrow = "▲" if verdict == "KEEP" else ("•" if verdict == "BASELINE" else "▼")
    print(
        f"[lab-run] #{entry['id']} {verdict} {arrow}  metric={metric}  "
        f"best={best_after}  change={args.change!r}"
    )
    if verdict == "DISCARD":
        print("[lab-run] revert this change — a regression never stays.")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
