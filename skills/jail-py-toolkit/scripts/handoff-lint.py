#!/usr/bin/env python3
"""handoff-lint.py — validate JAIL-HANDOFF blocks against the handoff schema.

Finds every fenced ```yaml block whose first line is `JAIL-HANDOFF:` and checks
(docs/schemas/jail-handoff.schema.json rules, enforced with a small stdlib
parser — no PyYAML): required keys (skill, status, unknowns, approval_required),
allowed top-level keys only, canonical key order (x-key-order), status in
{complete, partial, blocked, stop}, confidence in {high, medium, low}, skill
matching ^jail-[a-z0-9-]+$, list-typed keys are lists, `next` is a scalar,
`checks` maps to {pass, fail, error, n/a}; optional `tested` starts with
tested | untested | n/a.

Parser supports `key: value`, `key: [a, b]`, `key:` + `- item` lines, and one
nested `checks:` mapping. Trailing ` # comments` are stripped.

Usage:  handoff-lint.py FILE [FILE ...]
Exit codes: 0 = all blocks valid, 1 = invalid or no block found, 2 = usage/IO.
"""
import re
import sys
import argparse

ORDER = ["skill", "status", "facts", "assumptions", "unknowns", "outputs",
         "evidence", "risks", "confidence", "next", "approval_required", "checks", "tested"]
REQUIRED = ["skill", "status", "unknowns", "approval_required"]
LISTS = {"facts", "assumptions", "unknowns", "outputs", "evidence", "risks",
         "approval_required"}
STATUS = {"complete", "partial", "blocked", "stop"}
CONF = {"high", "medium", "low"}
CHECK_VALUES = {"pass", "fail", "error", "n/a"}
FENCE = re.compile(r"^\s*```")


def strip_comment(s):
    out, quote = [], None
    for i, ch in enumerate(s):
        if quote:
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch == "#" and (i == 0 or s[i - 1] in " \t"):
            break
        out.append(ch)
    return "".join(out).rstrip()


def unquote(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v


def split_flow(inner):
    items, cur, quote = [], [], None
    for ch in inner:
        if quote:
            cur.append(ch)
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
            cur.append(ch)
        elif ch == ",":
            items.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
    items.append("".join(cur))
    return [unquote(i) for i in items if i.strip()]


def extract_blocks(text):
    """Return [(start_line, [body lines after JAIL-HANDOFF:])]."""
    blocks, lines, i = [], text.splitlines(), 0
    while i < len(lines):
        m = re.match(r"^\s*```\s*ya?ml\s*$", lines[i], re.I)
        if m:
            j = i + 1
            body = []
            while j < len(lines) and not FENCE.match(lines[j]):
                body.append(lines[j])
                j += 1
            first = next((b for b in body if b.strip()), "")
            if first.strip().startswith("JAIL-HANDOFF:"):
                idx = body.index(first)
                blocks.append((i + 1 + idx + 1, body[idx + 1:]))
            i = j
        i += 1
    return blocks


def parse(body):
    """Parse block body -> (ordered [(key, value)], errors). value: str|list|dict."""
    errors, pairs = [], []
    body = [(n, strip_comment(l)) for n, l in enumerate(body)]
    body = [(n, l) for n, l in body if l.strip()]
    if not body:
        return pairs, ["empty JAIL-HANDOFF block"]
    base = len(body[0][1]) - len(body[0][1].lstrip())
    idx = 0
    while idx < len(body):
        n, line = body[idx]
        indent = len(line) - len(line.lstrip())
        m = re.match(r"^(\w[\w-]*):\s*(.*)$", line.strip())
        if indent != base or not m:
            errors.append(f"cannot parse line: unexpected indentation or syntax (block line {n + 1})")
            idx += 1
            continue
        key, rest = m.group(1), m.group(2).strip()
        idx += 1
        child = []
        while idx < len(body) and (len(body[idx][1]) - len(body[idx][1].lstrip())) > base:
            child.append(body[idx][1].strip())
            idx += 1
        # a "- item" list may also sit at the same indent as its key
        while not rest and not child and idx < len(body) and \
                body[idx][1].strip().startswith("- ") and \
                (len(body[idx][1]) - len(body[idx][1].lstrip())) == base:
            child.append(body[idx][1].strip())
            idx += 1
        if rest.startswith("[") and rest.endswith("]"):
            pairs.append((key, split_flow(rest[1:-1])))
        elif rest:
            pairs.append((key, unquote(rest)))
        elif child and all(c.startswith("- ") or c == "-" for c in child):
            pairs.append((key, [unquote(c[2:]) for c in child if c != "-"]))
        elif child:
            d = {}
            for c in child:
                mm = re.match(r"^([^:]+):\s*(.*)$", c)
                if mm:
                    d[mm.group(1).strip()] = unquote(mm.group(2))
                else:
                    errors.append(f"{key}: cannot parse nested line")
            pairs.append((key, d))
        else:
            pairs.append((key, []))
    return pairs, errors


def validate(pairs):
    errs = []
    keys = [k for k, _ in pairs]
    vals = dict(pairs)
    for k in REQUIRED:
        if k not in vals:
            errs.append(f"missing required key: {k}")
    for k in keys:
        if k not in ORDER:
            errs.append(f"unknown top-level key: {k}")
    if len(set(keys)) != len(keys):
        errs.append("duplicate top-level key")
    known = [k for k in keys if k in ORDER]
    pos = [ORDER.index(k) for k in known]
    if pos != sorted(pos):
        errs.append("keys out of canonical order (expected: " +
                    ", ".join(k for k in ORDER if k in known) + ")")
    if "skill" in vals and not (isinstance(vals["skill"], str)
                                and re.match(r"^jail-[a-z0-9-]+$", vals["skill"])):
        errs.append("skill must match ^jail-[a-z0-9-]+$")
    if "status" in vals and vals["status"] not in STATUS:
        errs.append("status must be one of: complete, partial, blocked, stop")
    if "confidence" in vals and vals["confidence"] not in CONF:
        errs.append("confidence must be one of: high, medium, low")
    for k in LISTS & set(vals):
        if not isinstance(vals[k], list):
            errs.append(f"{k} must be a list")
    if "next" in vals and not isinstance(vals["next"], str):
        errs.append("next must be a scalar string")
    if "tested" in vals and not re.match(r"^(tested|untested|n/a)\b", str(vals["tested"]).strip().strip('"\'')):
        errs.append("tested must start with 'tested', 'untested' or 'n/a'")
    if "checks" in vals:
        c = vals["checks"]
        if not isinstance(c, dict):
            errs.append("checks must be a mapping of script: pass|fail|error|n/a")
        else:
            for s, r in c.items():
                if r not in CHECK_VALUES:
                    errs.append(f"checks.{s} must be one of: pass, fail, error, n/a")
    return errs


def lint_text(text):
    blocks = extract_blocks(text)
    if not blocks:
        return ["no JAIL-HANDOFF block found"]
    errors = []
    for start, body in blocks:
        pairs, perrs = parse(body)
        for e in perrs + validate(pairs):
            errors.append(f"block at line {start}: {e}")
    return errors


def main():
    ap = argparse.ArgumentParser(description="Validate JAIL-HANDOFF blocks.")
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
        for e in errs:
            print(f"{f}: {e}", file=sys.stderr)
        if errs:
            bad = True
        else:
            print(f"handoff-lint: {f}: OK")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
