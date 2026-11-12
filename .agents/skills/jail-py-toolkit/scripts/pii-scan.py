#!/usr/bin/env python3
"""pii-scan.py — flag personal data (PII) in supplied text. Never prints values.

Classes: SSN (000/666/9xx areas excluded), payment card (13-19 digits, Luhn),
US bank routing number (ABA checksum), DOB-labelled dates, email + phone on
the same line. Output is file:line: kind only. Detection lives in fh_patterns.py.

Usage:
  pii-scan.py FILE [FILE ...]     # scan files
  pii-scan.py -                   # scan stdin (also when no args)
  pii-scan.py --secrets FILE      # additionally scan for secrets (secret-scan classes)

Exit codes: 0 = clean, 1 = personal data found, 2 = usage/IO error.
Stdlib only, Python 3.8+.
"""
import sys, os, argparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fh_patterns  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description="Flag PII (class + line only, never the value).")
    ap.add_argument("files", nargs="*", help="files to scan; omit or use - for stdin")
    ap.add_argument("--secrets", action="store_true", help="also scan for secret classes")
    args = ap.parse_args()
    classes = ("pii", "secret") if args.secrets else ("pii",)

    sources = []
    if not args.files or args.files == ["-"]:
        sources.append(("<stdin>", sys.stdin.read()))
    else:
        for f in args.files:
            try:
                with open(f, "r", encoding="utf-8", errors="replace") as fh:
                    sources.append((f, fh.read()))
            except OSError as e:
                print(f"error: cannot read {f}: {e}", file=sys.stderr)
                return 2

    findings = []
    for label, text in sources:
        for hit in fh_patterns.scan(text, classes):
            findings.append((label, hit["line"], hit["cls"], hit["kind"]))

    if not findings:
        print("pii-scan: clean — no personal data detected.")
        return 0
    print(f"pii-scan: {len(findings)} hit(s) found:", file=sys.stderr)
    for label, line, cls, kind in findings:
        print(f"  {label}:{line}: {cls}/{kind}", file=sys.stderr)
    print("Values are never printed. Remove or tokenize before sharing.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
