#!/usr/bin/env python3
"""secret-scan.py — flag hardcoded secrets / high-entropy keys in supplied text.

Used by the JAIL-PROMPT Phase 2 "Secure?" check: run it on user-supplied inputs
or files BEFORE generating a prompt, so credentials get replaced with env vars
instead of being baked into the prompt.

Usage:
  secret-scan.py FILE [FILE ...]      # scan files
  secret-scan.py -                    # scan stdin
  echo "..." | secret-scan.py         # (no args) scan stdin

Exit codes: 0 = clean, 1 = secrets found, 2 = usage/IO error.
Detection patterns live in fh_patterns.py (shared with pii-scan.py and hooks).
Output is file:line: kind only — no part of a secret value is ever printed.
Stdlib only — no third-party deps, so it runs anywhere Python 3.8+ does.
"""
import sys, os, argparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fh_patterns  # noqa: E402


def scan_text(text, label):
    return [(label, f["line"], f["kind"])
            for f in fh_patterns.scan(text, classes=("secret",))]


def main():
    ap = argparse.ArgumentParser(description="Flag hardcoded secrets / high-entropy keys.")
    ap.add_argument("files", nargs="*", help="files to scan; omit or use - for stdin")
    args = ap.parse_args()

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

    all_findings = []
    for label, text in sources:
        all_findings += scan_text(text, label)

    if not all_findings:
        print("secret-scan: clean — no secrets detected.")
        return 0

    print(f"secret-scan: {len(all_findings)} potential secret(s) found:\n", file=sys.stderr)
    for label, line, name in all_findings:
        print(f"  {label}:{line}: {name}", file=sys.stderr)
    print("\nReplace these with environment variables (e.g. os.environ['API_KEY']) "
          "and use a restricted, read-only credential before generating the prompt.",
          file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
