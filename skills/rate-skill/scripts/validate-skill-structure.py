#!/usr/bin/env python3
"""validate-skill-structure.py — structural lint for a skill directory.

Enforces the repo invariants a rating depends on, independent of score:
  * SKILL.md exists
  * YAML frontmatter present with non-empty `name` and `description`
  * folder name == frontmatter `name`
  * name is lowercase-hyphenated [a-z0-9-] (no spaces/uppercase/underscores)

Exits non-zero on any failure so it can gate a pre-commit hook or CI.

Usage:
    python3 validate-skill-structure.py <skill-dir> [<skill-dir> ...]
    python3 validate-skill-structure.py skills/*/
"""
import os
import re
import sys

NAME_RE = re.compile(r"^[a-z0-9-]+$")


def frontmatter(text):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end]
    fm = {}
    for line in block.splitlines():
        if ":" in line and not line.startswith((" ", "\t", "#")):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip("\"'")
    return fm


def check(skill_dir):
    errs = []
    skill_dir = skill_dir.rstrip("/\\")
    folder = os.path.basename(skill_dir)
    sp = os.path.join(skill_dir, "SKILL.md")
    if not os.path.isfile(sp):
        return [f"{folder}: missing SKILL.md"]
    with open(sp, encoding="utf-8") as fh:
        fm = frontmatter(fh.read())
    if fm is None:
        return [f"{folder}: no valid YAML frontmatter block"]
    name = fm.get("name", "")
    desc = fm.get("description", "")
    if not name:
        errs.append(f"{folder}: frontmatter missing 'name'")
    if not desc:
        errs.append(f"{folder}: frontmatter missing 'description'")
    if name and not NAME_RE.match(name):
        errs.append(f"{folder}: name '{name}' must be lowercase-hyphenated [a-z0-9-]")
    if name and name != folder:
        errs.append(f"{folder}: folder name != frontmatter name ('{name}')")
    return errs


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate-skill-structure.py <skill-dir> [...]", file=sys.stderr)
        return 2
    all_errs = []
    for d in sys.argv[1:]:
        if not os.path.isdir(d):
            continue
        all_errs += check(d)
    if all_errs:
        print("[!] Skill structure FAILED:")
        for e in all_errs:
            print(f"  - {e}")
        return 1
    print(f"[+] Skill structure valid ({len(sys.argv) - 1} checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
