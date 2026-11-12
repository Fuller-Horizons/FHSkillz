#!/usr/bin/env python3
"""dry-run.py — verify a prompt's OUTPUT FORMAT actually holds against a mock output.

The Phase 3 "Dry Run Sandbox Verification" guardrail: before presenting a
high-stakes prompt, confirm the declared OUTPUT FORMAT parses and that a mock
output conforms to it — so a broken schema or mismatched table is caught here,
not in production.

Usage:
  dry-run.py PROMPT_FILE [--mock MOCK_FILE]
  dry-run.py PROMPT_FILE                 # auto-checks the format declaration itself

Supported OUTPUT FORMAT kinds (auto-detected):
  * JSON Schema  (a ```json block whose top level has "type"/"properties") -> validate mock against it
  * JSON example (any other ```json block)                                  -> mock must be valid JSON
  * Markdown table (a header row with | pipes)                              -> mock rows must match column count

Exit codes: 0 = format valid + mock conforms, 1 = format invalid / mock mismatch, 2 = usage/IO.
Stdlib only — includes a tiny JSON-Schema subset validator (type, required, properties).
"""
import sys, re, json, argparse

SECTIONS = ["METADATA","ROLE","CONTEXT","OBJECTIVE","SUCCESS TEST","PROCESS",
            "SOURCES","OUTPUT FORMAT","CONSTRAINTS","BEFORE RETURNING"]


def section_body(text, name):
    pat = re.compile(r"(?m)^\s*(" + "|".join(re.escape(s) for s in SECTIONS) + r")\s*:")
    marks = [(m.group(1).strip(), m.start(), m.end()) for m in pat.finditer(text)]
    for i, (nm, _s, e) in enumerate(marks):
        if nm == name:
            end = marks[i + 1][1] if i + 1 < len(marks) else len(text)
            return text[e:end].strip()
    return ""


def first_json_block(text):
    m = re.search(r"```json\s*(.*?)```", text, flags=re.S | re.I)
    return m.group(1).strip() if m else None


def first_table(text):
    rows = [ln for ln in text.splitlines() if ln.strip().startswith("|") or " | " in ln]
    return rows or None


JTYPES = {"object": dict, "array": list, "string": str, "number": (int, float),
          "integer": int, "boolean": bool, "null": type(None)}


def validate_schema(schema, data, path="$"):
    """Minimal JSON-Schema check: type, required, properties, array items."""
    errs = []
    t = schema.get("type")
    if t:
        py = JTYPES.get(t)
        if py and not isinstance(data, py):
            errs.append(f"{path}: expected {t}, got {type(data).__name__}")
            return errs
    if t == "object" or "properties" in schema:
        for req in schema.get("required", []):
            if not isinstance(data, dict) or req not in data:
                errs.append(f"{path}: missing required property '{req}'")
        for k, sub in schema.get("properties", {}).items():
            if isinstance(data, dict) and k in data:
                errs += validate_schema(sub, data[k], f"{path}.{k}")
    if t == "array" and "items" in schema and isinstance(data, list):
        for idx, item in enumerate(data):
            errs += validate_schema(schema["items"], item, f"{path}[{idx}]")
    return errs


def main():
    ap = argparse.ArgumentParser(description="Dry-run a prompt's OUTPUT FORMAT against a mock.")
    ap.add_argument("prompt", help="file containing the engineered prompt block")
    ap.add_argument("--mock", help="file with a mock output to validate against the format")
    args = ap.parse_args()

    try:
        text = open(args.prompt, encoding="utf-8").read()
    except OSError as e:
        print(f"error: cannot read {args.prompt}: {e}", file=sys.stderr)
        return 2

    of = section_body(text, "OUTPUT FORMAT") or text
    jb = first_json_block(of) or first_json_block(text)
    table = first_table(of)

    mock = None
    if args.mock:
        try:
            mock = open(args.mock, encoding="utf-8").read()
        except OSError as e:
            print(f"error: cannot read mock {args.mock}: {e}", file=sys.stderr)
            return 2

    # --- JSON kinds ---
    if jb is not None:
        try:
            spec = json.loads(jb)
        except json.JSONDecodeError as e:
            print(f"dry-run: FAIL — OUTPUT FORMAT JSON does not parse: {e}", file=sys.stderr)
            return 1
        is_schema = isinstance(spec, dict) and ("properties" in spec or spec.get("type") in JTYPES)
        if mock is None:
            print(f"dry-run: OUTPUT FORMAT JSON parses ({'schema' if is_schema else 'example'}). "
                  "Provide --mock to validate a sample output.")
            return 0
        try:
            mock_obj = json.loads(mock)
        except json.JSONDecodeError as e:
            print(f"dry-run: FAIL — mock output is not valid JSON: {e}", file=sys.stderr)
            return 1
        if is_schema:
            errs = validate_schema(spec, mock_obj)
            if errs:
                print("dry-run: FAIL — mock does not conform to schema:", file=sys.stderr)
                for e in errs:
                    print(f"  {e}", file=sys.stderr)
                return 1
        print("dry-run: PASS — mock output conforms to the declared JSON OUTPUT FORMAT.")
        return 0

    # --- Markdown table kind ---
    if table:
        cols = table[0].count("|")
        if mock is None:
            print(f"dry-run: OUTPUT FORMAT is a {cols-1 if cols>1 else cols}-column table. "
                  "Provide --mock rows to check column alignment.")
            return 0
        bad = [i for i, ln in enumerate(mock.splitlines(), 1)
               if ln.strip() and ("|" in ln) and ln.count("|") != cols]
        if bad:
            print(f"dry-run: FAIL — mock rows {bad} don't match the {cols}-pipe header.", file=sys.stderr)
            return 1
        print("dry-run: PASS — mock rows match the table format.")
        return 0

    print("dry-run: WARN — no machine-checkable OUTPUT FORMAT (JSON/table) found; "
          "nothing to verify automatically.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
