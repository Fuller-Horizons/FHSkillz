---
name: jail-py-rate-tools
metadata:
  version: 1.0.0
description: >-
  JAIL-PY machine checks for skill ratings — runnable Python companions to the
  jail-rate-skill skill. Use when jail-rate-skill emits a JSON rating record, or when the
  user asks to validate a rating record's structure, save a rating to history
  and see the delta vs the last run, measure score variance/drift across
  repeated ratings of the same skill, or structurally lint a skill directory
  (SKILL.md present, frontmatter name+description, folder name matches).
  Triggers: "validate this rating", "save the rating", "check rating variance",
  "lint the skill structure". Requires code execution (Python 3.8+, stdlib
  only). Not for producing the rating itself — that's jail-rate-skill.
---

# JAIL-PY-RATE-TOOLS

Runnable validation, persistence, and drift-measurement for
[jail-rate-skill](../jail-rate-skill/SKILL.md)'s rating records. jail-rate-skill is
instruction-only; this companion holds all the code. Stdlib-only Python 3.8+;
every script exits non-zero on failure.

## The four tools

| Script | Backs (jail-rate-skill) | What it does | Exit |
|---|---|---|---|
| `scripts/validate-rating.py` | Rule 7 — self-verify | Structural check of a rating record: all 10 categories present, scores in 0.0–10.0, `overall` equals the rounded mean. | 0 pass · non-zero fail |
| `scripts/save-rating.py` | Rule 7 — persist | Validates, appends the record to `${CLAUDE_PLUGIN_DATA}/rating-history.jsonl` (fallback `~/.rate-skill/`), prints the Overall delta vs the previous rating of the same skill. | 0 pass · non-zero fail |
| `scripts/variance-check.py` | Rule 3 — prove determinism | Takes 2+ records of the *same* skill; per-category mean ± stddev; fails if any category drifts more than ±0.2. | 0 pass · non-zero drift |
| `scripts/validate-skill-structure.py` | Rule 1 — read before rating | Lints a target skill directory against the repo invariants (SKILL.md, frontmatter `name`+`description`, folder==name, lowercase-hyphenated). | 0 pass · non-zero fail |

## Usage

```bash
python3 scripts/validate-rating.py rating.json
python3 scripts/save-rating.py rating.json
python3 scripts/variance-check.py run1.json run2.json [run3.json]
python3 scripts/validate-skill-structure.py <skill-dir> [<skill-dir> ...]
```

## Workflow

1. jail-rate-skill emits the JSON record (schema in its `references/examples.md`).
2. Write it to `rating.json`; run `validate-rating.py`; fix any structural
   failure in the record (not by hand-editing scores to pass).
3. Run `save-rating.py` to append history and report movement vs last time.
4. High-stakes rating? Re-rate 2–3× into separate files and run
   `variance-check.py` across them; drift > ±0.2 means the rating isn't
   deterministic — re-anchor to the rubric bands before trusting it.

## Gotchas
- **History env var.** `${CLAUDE_PLUGIN_DATA}` is set by the plugin runtime;
  when unset the scripts fall back to `~/.rate-skill/` — that's expected, not
  an error.
- **Variance needs the same target.** Feeding `variance-check.py` records of
  *different* skills produces meaningless drift numbers; it compares runs of
  one skill.
- **Never "fix" a failed validation by editing scores.** A failure means the
  record (or the rating process) is wrong; recompute, don't fudge.
- **Where code can't run**, fall back to jail-rate-skill's manual checks (recompute
  the mean, diff repeat records by hand) and say so.
