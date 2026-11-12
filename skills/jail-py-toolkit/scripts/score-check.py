#!/usr/bin/env python3
"""score-check.py — arithmetic check for jail-rate / jail-prospect scorecards.

Reads markdown tables.
RATE tables: header has `Weight`.
  - weights in a table sum to 100 (percent signs allowed)
  - if the table also has a `Now` column: each score is 0.0-10.0 and
    sum(score x weight/100), rounded half-up to 1 decimal, equals the
    headline `Overall: X.X / 10` ; a `Projected` column is checked the same way
    against the headline's `-> Y.Y / 10 projected` (or `→`) when present
PROSPECT tables: header has `Component`, `Score`, `Max` (0-100 scale)
  - each score is 0..Max; Max values sum to 100
  - a row whose first cell starts with `Total` must equal the sum of component
    scores (its Max, if given, must be 100)
Fails with exit 1 if any mismatch, or if no scorecard table is found.

Usage:  score-check.py FILE [FILE ...]
Exit codes: 0 = pass, 1 = arithmetic/range mismatch, 2 = usage/IO error.
"""
import re
import sys
import argparse
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

HEADLINE = re.compile(
    r"Overall:?\**\s*(\d+(?:\.\d+)?)\s*/\s*10(?:\s*(?:→|->)\s*(\d+(?:\.\d+)?)\s*/\s*10)?")


def num(cell):
    c = cell.replace("**", "").replace("%", "").replace(",", "").strip()
    c = re.split(r"\s*/\s*", c)[0]
    try:
        return Decimal(c)
    except InvalidOperation:
        return None


def tables(lines):
    """Yield (start_line, header_cells, [(line_no, cells)])."""
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith("|") and i + 1 < len(lines) and \
                re.match(r"^\s*\|?[\s:|-]+\|[\s:|-]*$", lines[i + 1]):
            hdr = [c.strip().replace("**", "") for c in lines[i].strip().strip("|").split("|")]
            rows, j = [], i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                rows.append((j + 1, [c.strip() for c in lines[j].strip().strip("|").split("|")]))
                j += 1
            yield i + 1, hdr, rows
            i = j
        else:
            i += 1


def col(hdr, name):
    for k, h in enumerate(hdr):
        if h.lower().startswith(name):
            return k
    return None


def r1(d):
    return d.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)


def lint_text(text):
    errs, checked = [], 0
    lines = text.splitlines()
    head = HEADLINE.search(text)
    head_now = Decimal(head.group(1)) if head else None
    head_proj = Decimal(head.group(2)) if head and head.group(2) else None
    for start, hdr, rows in tables(lines):
        w, now, proj = col(hdr, "weight"), col(hdr, "now"), col(hdr, "projected")
        comp, sc, mx = col(hdr, "component"), col(hdr, "score"), col(hdr, "max")
        if w is not None:
            checked += 1
            ws = []
            for ln, cells in rows:
                v = num(cells[w]) if w < len(cells) else None
                if v is None:
                    errs.append((ln, "weight is not a number"))
                else:
                    ws.append(v)
            if len(ws) == len(rows) and sum(ws) != 100:
                errs.append((start, f"weights sum to {sum(ws)}, expected 100"))
            for name, ci, headv in (("Now", now, head_now), ("Projected", proj, head_proj)):
                if ci is None or len(ws) != len(rows):
                    continue
                total = Decimal(0)
                for (ln, cells), wt in zip(rows, ws):
                    s = num(cells[ci]) if ci < len(cells) else None
                    if s is None:
                        errs.append((ln, f"{name} score is not a number"))
                        total = None
                        break
                    if not (Decimal(0) <= s <= Decimal(10)):
                        errs.append((ln, f"{name} score {s} outside 0.0-10.0"))
                    total += s * wt / 100
                if total is None:
                    continue
                calc = r1(total)
                if headv is None:
                    errs.append((start, f"no `Overall: X.X / 10` headline to compare {name} total {calc}"))
                elif calc != headv:
                    errs.append((start, f"{name} overall mismatch: declared {headv}, computed {calc}"))
        elif comp is not None and sc is not None and mx is not None:
            checked += 1
            parts, maxes, total_row = [], [], None
            for ln, cells in rows:
                s, m = (num(cells[sc]) if sc < len(cells) else None), (num(cells[mx]) if mx < len(cells) else None)
                if cells[comp].lower().startswith("total"):
                    total_row = (ln, s, m)
                    continue
                if s is None or m is None:
                    errs.append((ln, "component score/max is not a number"))
                    continue
                if not (0 <= s <= m):
                    errs.append((ln, f"score {s} outside 0..{m}"))
                parts.append(s)
                maxes.append(m)
            if maxes and sum(maxes) != 100:
                errs.append((start, f"component maxima sum to {sum(maxes)}, expected 100"))
            if total_row:
                ln, s, m = total_row
                if s is None or s != sum(parts):
                    errs.append((ln, f"declared total {s} != component sum {sum(parts)}"))
                if m is not None and m != 100:
                    errs.append((ln, "total max must be 100"))
            else:
                errs.append((start, "no Total row to compare against component sum"))
    if not checked:
        errs.append((0, "no scorecard table found (need Weight/Now or Component/Score/Max columns)"))
    return errs


def main():
    ap = argparse.ArgumentParser(description="Check scorecard arithmetic.")
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
            print(f"{f}:{n}: {e}" if n else f"{f}: {e}", file=sys.stderr)
        if errs:
            bad = True
        else:
            print(f"score-check: {f}: OK")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
