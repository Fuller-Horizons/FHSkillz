#!/usr/bin/env python3
"""_ledger_io.py — shared JSONL ledger reader for jail-py-lab.

One read routine, reused by lab-run.py, lab-report.py, and lab-compare.py,
so the line-numbered corrupt-line error can't drift out of sync across the
three tools. Not a CLI entry point on its own.
"""
import json
import os
import sys


def read_ledger(path, prog, missing_ok=False, missing_msg=None):
    """Read a JSONL ledger into a list of dicts.

    On any error, prints "[{prog}] ERROR: ..." to stderr and exits 2 — every
    caller in this toolkit already treats 2 as its error exit code, so this
    preserves each script's existing contract.

    missing_ok=True   -> a missing file returns [] (lab-run: the ledger is
                          created on first write, so absence isn't an error).
    missing_ok=False  -> a missing file exits 2 with missing_msg (default:
                          "ledger not found: {path}").
    A malformed line reports its 1-based line number and exits 2; blank
    lines are skipped.
    """
    if not os.path.exists(path):
        if missing_ok:
            return []
        print(
            f"[{prog}] ERROR: {missing_msg or f'ledger not found: {path}'}",
            file=sys.stderr,
        )
        sys.exit(2)

    entries = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError:
                    print(
                        f"[{prog}] ERROR: ledger line {i} is not valid JSON — ledger corrupt",
                        file=sys.stderr,
                    )
                    sys.exit(2)
    except OSError as e:
        print(f"[{prog}] ERROR: could not read {path}: {e}", file=sys.stderr)
        sys.exit(2)
    return entries
