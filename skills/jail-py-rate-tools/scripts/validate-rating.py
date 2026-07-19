#!/usr/bin/env python3
"""Validate a rate-skill JSON rating record.

Checks: all 10 canonical categories present; every score / post_reco is within
0.0-10.0 at 0.1 increments; post_reco >= score; overall == rounded mean of the
10 scores. Exits non-zero on any failure so it can gate CI / a pre-commit hook.

Usage: python3 validate-rating.py rating.json
"""
import json
import sys

CANON = [
    "Utility & Value",
    "Clarity of Instructions",
    "Execution Reliability",
    "Safety & Guardrails",
    "Maintainability",
    "Context & Token Efficiency",
    "Idempotency & Determinism",
    "Handoff & Collaboration",
    "Machine-Verifiable Exit Criteria",
    "Client Portability",
]


def _is_valid_score(v):
    return (
        isinstance(v, (int, float))
        and 0.0 <= v <= 10.0
        and round(v * 10) == v * 10  # 0.1 increments
    )


def validate(record):
    errors = []

    cats = record.get("categories")
    if not isinstance(cats, dict):
        return ["'categories' is missing or not an object."]

    present = set(cats)
    expected = set(CANON)
    for missing in sorted(expected - present):
        errors.append(f"Missing category: {missing}")
    for extra in sorted(present - expected):
        errors.append(f"Unknown category: {extra}")

    scores = []
    for name in CANON:
        entry = cats.get(name)
        if not isinstance(entry, dict):
            continue  # already reported as missing
        score = entry.get("score")
        if not _is_valid_score(score):
            errors.append(f"{name}: 'score' must be 0.0-10.0 in 0.1 steps (got {score!r}).")
        else:
            scores.append(score)
        if "post_reco" in entry:
            pr = entry["post_reco"]
            if not _is_valid_score(pr):
                errors.append(f"{name}: 'post_reco' must be 0.0-10.0 in 0.1 steps (got {pr!r}).")
            elif _is_valid_score(score) and pr < score:
                errors.append(f"{name}: 'post_reco' ({pr}) is below 'score' ({score}).")

    overall = record.get("overall")
    if not _is_valid_score(overall):
        errors.append(f"'overall' must be 0.0-10.0 in 0.1 steps (got {overall!r}).")
    elif len(scores) == 10:
        expected_overall = round(sum(scores) / 10, 1)
        if abs(overall - expected_overall) > 1e-9:
            errors.append(
                f"'overall' ({overall}) != rounded mean of scores ({expected_overall})."
            )

    return errors


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 validate-rating.py rating.json", file=sys.stderr)
        sys.exit(2)
    try:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            record = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"[!] Could not read/parse {sys.argv[1]}: {e}", file=sys.stderr)
        sys.exit(2)

    errors = validate(record)
    if errors:
        print("[!] Rating validation FAILED:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print(f"[+] Rating valid: {record.get('skill', '?')} (overall {record.get('overall')}).")
    sys.exit(0)


if __name__ == "__main__":
    main()
