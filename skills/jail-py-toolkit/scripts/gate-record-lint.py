#!/usr/bin/env python3
"""gate-record-lint.py — validate GATE-RECORD audit lines.

Format (jail-approval-gate):
  GATE-RECORD | action=<> | tier=<NEVER|PER-ACTION|BATCHABLE|AUTO> | approver=<> | ts=<ISO8601> | result=<approved|denied|pending>

Every GATE-RECORD line must carry all five fields, non-empty and not an
unfilled `<...>` placeholder; tier and result must be in their enums; ts must
be a valid ISO-8601 timestamp. `result` also accepts the documented
`approved-modified-<detail>` form. Fails if a file has no GATE-RECORD line.

Usage:  gate-record-lint.py FILE [FILE ...]
Exit codes: 0 = pass, 1 = invalid record(s), 2 = usage/IO error.
"""
import re
import sys
import argparse
from datetime import datetime

TIERS = {"NEVER", "PER-ACTION", "BATCHABLE", "AUTO"}
RESULT = re.compile(r"^(approved(-modified-\S+)?|denied|pending)$")
FIELDS = ["action", "tier", "approver", "ts", "result"]
LINE = re.compile(r"^\s*(?:[-*>]\s*)?GATE-RECORD\b")
TS = re.compile(r"^(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?)(Z|[+-]\d{2}:?\d{2})?$")


def valid_ts(v):
    m = TS.match(v)
    if not m:
        return False
    try:
        datetime.strptime(m.group(1), "%Y-%m-%d")
        t = m.group(2).split(".")[0]
        datetime.strptime(t, "%H:%M:%S" if t.count(":") == 2 else "%H:%M")
    except ValueError:
        return False
    return True


def lint_text(text):
    errs, found = [], 0
    for n, line in enumerate(text.splitlines(), 1):
        if not LINE.match(line):
            continue
        found += 1
        parts = [p.strip() for p in line.split("|")]
        kv = {}
        for p in parts[1:]:
            if "=" in p:
                k, v = p.split("=", 1)
                kv[k.strip()] = v.strip()
        for f in FIELDS:
            v = kv.get(f)
            if v is None or v == "":
                errs.append((n, f"missing field: {f}"))
            elif re.fullmatch(r"<[^>]*>", v):
                errs.append((n, f"unfilled placeholder in {f}"))
        if kv.get("tier") and kv["tier"] not in TIERS and not re.fullmatch(r"<[^>]*>", kv["tier"]):
            errs.append((n, "tier must be one of NEVER, PER-ACTION, BATCHABLE, AUTO"))
        if kv.get("result") and not RESULT.match(kv["result"]) and not re.fullmatch(r"<[^>]*>", kv["result"]):
            errs.append((n, "result must be approved, denied, or pending"))
        ts = kv.get("ts")
        if ts and not re.fullmatch(r"<[^>]*>", ts) and not valid_ts(ts):
            errs.append((n, "ts is not a valid ISO-8601 timestamp"))
    if not found:
        errs.append((0, "no GATE-RECORD lines found"))
    return errs


def main():
    ap = argparse.ArgumentParser(description="Validate GATE-RECORD lines.")
    ap.add_argument("files", nargs="+")
    args = ap.parse_args()
    bad = False
    for f in args.files:
        try:
            with open(f, "r", encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except OSError as e:
            print(f"error: cannot read {f}: {e}", file=sys.stderr)
            return 2
        errs = lint_text(text)
        for n, e in errs:
            print(f"{f}:{n}: {e}" if n else f"{f}: {e}", file=sys.stderr)
        if errs:
            bad = True
        else:
            print(f"gate-record-lint: {f}: OK")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
