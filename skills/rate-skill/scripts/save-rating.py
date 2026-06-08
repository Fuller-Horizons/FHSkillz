#!/usr/bin/env python3
"""Validate a rate-skill record, append it to history, and report the delta.

Runs the structural checks in validate-rating.py, then appends the record to a
history log and prints the change in Overall versus the previous rating of the
same skill. This gives the skill a memory so iterating on a target shows
measurable movement.

History location: ${CLAUDE_PLUGIN_DATA}/rating-history.jsonl
(falls back to ~/.rate-skill/rating-history.jsonl when the env var is unset).

Usage: python3 save-rating.py rating.json
"""
import json
import os
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# Reuse the validator (filename has a hyphen, so load it by path).
import importlib.util

_spec = importlib.util.spec_from_file_location(
    "validate_rating", os.path.join(HERE, "validate-rating.py")
)
_vr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_vr)


def history_path():
    base = os.environ.get("CLAUDE_PLUGIN_DATA") or os.path.join(
        os.path.expanduser("~"), ".rate-skill"
    )
    os.makedirs(base, exist_ok=True)
    return os.path.join(base, "rating-history.jsonl")


def previous_overall(path, skill):
    prev = None
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if rec.get("skill") == skill and isinstance(rec.get("overall"), (int, float)):
                prev = rec["overall"]
    return prev


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 save-rating.py rating.json", file=sys.stderr)
        sys.exit(2)

    try:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            record = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"[!] Could not read/parse {sys.argv[1]}: {e}", file=sys.stderr)
        sys.exit(2)

    errors = _vr.validate(record)
    if errors:
        print("[!] Not saved — record failed validation:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    skill = record.get("skill", "?")
    path = history_path()
    prev = previous_overall(path, skill)

    entry = {"ts": datetime.now(timezone.utc).isoformat(), **record}
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

    overall = record.get("overall")
    if prev is None:
        print(f"[+] Saved first rating for '{skill}': overall {overall}.")
    else:
        delta = round(overall - prev, 1)
        arrow = "▲" if delta > 0 else ("▼" if delta < 0 else "=")
        sign = f"+{delta}" if delta > 0 else str(delta)
        print(f"[+] Saved '{skill}': overall {overall} ({arrow} {sign} vs previous {prev}).")
    print(f"    history: {path}")
    sys.exit(0)


if __name__ == "__main__":
    main()
