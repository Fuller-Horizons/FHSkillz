#!/usr/bin/env python3
"""prompt-lint.py — lint a JAIL-PROMPT engineered-prompt block.

Enforces the Phase 3 skeleton and catches the two antipatterns the skill cares
about most: a SUCCESS TEST that can't fail (no machine-verifiable check) and an
OUTPUT FORMAT that only names a shape instead of showing one. Also confirms any
embedded ```json block actually parses.

Usage:
  prompt-lint.py FILE        # lint the prompt block in FILE
  prompt-lint.py -           # lint stdin
  ... | prompt-lint.py       # (no args) lint stdin
  add --strict to fail on warnings too.

Exit codes: 0 = pass (no errors), 1 = errors, 2 = usage/IO error.
Stdlib only.
"""
import sys, re, json, argparse

REQUIRED = ["OBJECTIVE", "SUCCESS TEST", "PROCESS", "OUTPUT FORMAT", "CONSTRAINTS"]
OPTIONAL = ["METADATA", "ROLE", "CONTEXT", "SOURCES", "BEFORE RETURNING"]
ALL_SECTIONS = REQUIRED + OPTIONAL

# A SUCCESS TEST is machine-verifiable if it names a runnable/automatable check.
VERIFIABLE = re.compile(
    r"(?i)\b(test|tests|assert|assertion|unit test|test suite|script|run|execute|"
    r"schema|json schema|regex|exit code|parse[sd]?|compile[sd]?|lint|diff|"
    r"count|matches|==|equals|returns|validate[sd]?|pytest|build passes)\b"
)
# OUTPUT FORMAT shows a concrete shape if it has a fence, table, JSON, or example.
CONCRETE = re.compile(r"(```|\||\{|\[|e\.g\.|example|schema|<[A-Za-z])")


def extract_sections(text):
    """Return {SECTION: body}. A section starts at 'NAME:' at a line start."""
    pat = re.compile(r"(?m)^\s*(" + "|".join(re.escape(s) for s in ALL_SECTIONS) + r")\s*:")
    marks = [(m.group(1).strip(), m.start(), m.end()) for m in pat.finditer(text)]
    out = {}
    for i, (name, _s, e) in enumerate(marks):
        end = marks[i + 1][1] if i + 1 < len(marks) else len(text)
        out[name] = text[e:end].strip()
    return out


def find_json_blocks(text):
    return re.findall(r"```json\s*(.*?)```", text, flags=re.S | re.I)


def lint(text):
    errors, warnings = [], []
    sec = extract_sections(text)

    for r in REQUIRED:
        if r not in sec:
            errors.append(f"missing required section: {r}:")
        elif not sec[r]:
            errors.append(f"section {r}: is empty")

    if "SUCCESS TEST" in sec and sec["SUCCESS TEST"]:
        if not VERIFIABLE.search(sec["SUCCESS TEST"]):
            errors.append("SUCCESS TEST has no machine-verifiable check "
                          "(name a test/script/schema/assertion/exit-code check, not subjective review)")

    if "OUTPUT FORMAT" in sec and sec["OUTPUT FORMAT"]:
        if not CONCRETE.search(sec["OUTPUT FORMAT"]):
            warnings.append("OUTPUT FORMAT names a shape but doesn't show one "
                            "(add a fenced example, header row, or schema)")

    for i, block in enumerate(find_json_blocks(text), 1):
        try:
            json.loads(block)
        except json.JSONDecodeError as e:
            errors.append(f"embedded ```json block #{i} does not parse: {e}")

    if "BEFORE RETURNING" not in sec:
        warnings.append("no BEFORE RETURNING: self-check section (recommended)")

    return errors, warnings


def main():
    ap = argparse.ArgumentParser(description="Lint a JAIL-PROMPT engineered-prompt block.")
    ap.add_argument("file", nargs="?", default="-", help="file to lint; - or omit for stdin")
    ap.add_argument("--strict", action="store_true", help="treat warnings as failures")
    args = ap.parse_args()

    try:
        text = sys.stdin.read() if args.file == "-" else open(args.file, encoding="utf-8").read()
    except OSError as e:
        print(f"error: cannot read {args.file}: {e}", file=sys.stderr)
        return 2

    errors, warnings = lint(text)
    for w in warnings:
        print(f"warning: {w}", file=sys.stderr)
    for e in errors:
        print(f"error: {e}", file=sys.stderr)

    if errors or (args.strict and warnings):
        print(f"\nprompt-lint: FAIL ({len(errors)} error(s), {len(warnings)} warning(s)).", file=sys.stderr)
        return 1
    print(f"prompt-lint: PASS ({len(warnings)} warning(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
