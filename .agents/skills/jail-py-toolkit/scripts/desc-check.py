#!/usr/bin/env python3
"""desc-check.py — skill description / size hygiene over a skills directory.

For every SKILL.md under <skills-dir> (or a single skill dir containing one):
  - frontmatter `description` is <= 450 characters (folded scalars joined)
  - description contains the negative trigger `Do NOT use`
  - core (SKILL.md body, excluding frontmatter) is <= 160 lines
  - frontmatter has `metadata:` with a `version:` key

Usage:  desc-check.py SKILLS_DIR
Exit codes: 0 = pass, 1 = violations, 2 = usage/IO error.
"""
import os
import re
import sys
import argparse

MAX_DESC, MAX_LINES = 450, 160


def split_frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, lines
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[1:i], lines[i + 1:]
    return None, lines


def get_description(fm):
    for i, line in enumerate(fm):
        m = re.match(r"^description:\s*(.*)$", line)
        if not m:
            continue
        val = m.group(1).strip()
        if re.fullmatch(r"[>|][+-]?", val):
            parts = []
            for l in fm[i + 1:]:
                if l.strip() and not l.startswith((" ", "\t")):
                    break
                parts.append(l.strip())
            return " ".join(p for p in parts if p)
        if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
            val = val[1:-1]
        return val
    return None


def has_metadata_version(fm):
    in_meta = False
    for line in fm:
        if re.match(r"^metadata:\s*$", line):
            in_meta = True
        elif in_meta and re.match(r"^\s+version:\s*\S", line):
            return True
        elif in_meta and line.strip() and not line.startswith((" ", "\t")):
            in_meta = False
    return False


def check_skill(path):
    errs = []
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    fm, body = split_frontmatter(text)
    if fm is None:
        return ["no YAML frontmatter"]
    desc = get_description(fm)
    if desc is None:
        errs.append("missing description")
    else:
        if len(desc) > MAX_DESC:
            errs.append(f"description is {len(desc)} chars (max {MAX_DESC})")
        if "Do NOT use" not in desc:
            errs.append("description lacks negative trigger 'Do NOT use'")
    if len(body) > MAX_LINES:
        errs.append(f"core is {len(body)} lines (max {MAX_LINES})")
    if not has_metadata_version(fm):
        errs.append("frontmatter missing metadata.version")
    return errs


def main():
    ap = argparse.ArgumentParser(description="Check SKILL.md descriptions and size.")
    ap.add_argument("skills_dir")
    args = ap.parse_args()
    root = args.skills_dir
    if not os.path.isdir(root):
        print(f"error: not a directory: {root}", file=sys.stderr)
        return 2
    if os.path.isfile(os.path.join(root, "SKILL.md")):
        targets = [root]
    else:
        targets = [os.path.join(root, d) for d in sorted(os.listdir(root))
                   if os.path.isfile(os.path.join(root, d, "SKILL.md"))]
    bad = 0
    for t in targets:
        try:
            errs = check_skill(os.path.join(t, "SKILL.md"))
        except OSError as e:
            print(f"error: cannot read {t}: {e}", file=sys.stderr)
            return 2
        for e in errs:
            print(f"{os.path.join(t, 'SKILL.md')}: {e}", file=sys.stderr)
        bad += bool(errs)
    if bad:
        print(f"desc-check: {bad} of {len(targets)} skill(s) with violations", file=sys.stderr)
        return 1
    print(f"desc-check: {len(targets)} skill(s) OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
