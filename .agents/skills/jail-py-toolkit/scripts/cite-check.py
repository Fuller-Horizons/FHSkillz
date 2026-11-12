#!/usr/bin/env python3
"""cite-check.py — citation integrity for answers / evidence packets.

Source lines are numbered entries:  `[n] ...` (optionally bulleted), or
`n. ...` / `n) ...` inside a section whose heading mentions Sources,
References or Citations. Checks:
  - every inline `[n]` marker in the body resolves to a numbered source line
  - every numbered source is cited at least once in the body
  - every source line has a URL/ref (https://..., or `ref:`/`file:`/`doc:`
    followed by a value, or a backticked path) and an ISO date (YYYY-MM-DD)
  - source numbers are unique
Markdown links `[text](url)` and fenced code are ignored. A file with no
markers and no sources passes.

Usage:  cite-check.py FILE [FILE ...]
Exit codes: 0 = pass, 1 = integrity failure, 2 = usage/IO error.
"""
import re
import sys
import argparse
from datetime import datetime

SRC_BRACKET = re.compile(r"^\s*(?:[-*]\s+)?\[(\d+)\][:.]?\s+(\S.*)$")
SRC_NUMBERED = re.compile(r"^\s*(\d+)[.)]\s+(\S.*)$")
MARKER = re.compile(r"\[(\d+)\](?!\()")
HEADING = re.compile(r"^\s{0,3}#{1,6}\s+(.*)$")
HAS_REF = re.compile(r"(https?://\S+|\b(?:ref|file|doc):\s*\S+|`[^`\n]+`)", re.I)
DATE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")


def valid_date(s):
    try:
        datetime.strptime(s, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def lint_text(text):
    errs, sources, cited = [], {}, set()
    in_code, in_src_section = False, False
    for n, line in enumerate(text.splitlines(), 1):
        if re.match(r"^\s*```", line):
            in_code = not in_code
            continue
        if in_code:
            continue
        h = HEADING.match(line)
        if h:
            in_src_section = bool(re.search(r"(?i)sources?|references?|citations?", h.group(1)))
            continue
        m = SRC_BRACKET.match(line) or (SRC_NUMBERED.match(line) if in_src_section else None)
        if m:
            num, rest = int(m.group(1)), m.group(2)
            if num in sources:
                errs.append((n, f"duplicate source number [{num}]"))
            sources[num] = (n, rest)
            if not HAS_REF.search(rest):
                errs.append((n, f"source [{num}] has no URL/ref"))
            d = DATE.search(rest)
            if not d or not valid_date(d.group(1)):
                errs.append((n, f"source [{num}] has no ISO date (YYYY-MM-DD)"))
            # citations inside a source line do not count as body citations
            continue
        for mk in MARKER.finditer(line):
            cited.add((int(mk.group(1)), n))
    cited_nums = {c for c, _ in cited}
    for num, n in sorted(cited):
        if num not in sources:
            errs.append((n, f"orphan marker [{num}] — no matching source line"))
    for num, (n, _) in sorted(sources.items()):
        if num not in cited_nums:
            errs.append((n, f"source [{num}] is never cited"))
    return errs


def main():
    ap = argparse.ArgumentParser(description="Check citation integrity.")
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
        for n, e in sorted(errs):
            print(f"{f}:{n}: {e}", file=sys.stderr)
        if errs:
            bad = True
        else:
            print(f"cite-check: {f}: OK")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
