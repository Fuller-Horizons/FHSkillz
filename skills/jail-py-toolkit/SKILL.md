---
name: jail-py-toolkit
metadata:
  version: 1.0.0
description: >-
  JAIL-PY machine checks for prompts AND ratings — the runnable companion to
  jail-prompt and jail-rate-skill in one toolkit. Use when either skill calls
  for a machine check, or when the user asks to scan pasted input or files
  for secrets/API keys, lint an engineered prompt block, validate a chain
  manifest's handoffs, check truth-tagged claims, dry-run an output format,
  validate or save a skill-rating record with history deltas, measure rating
  variance/drift, or structurally lint a skill directory. Triggers: "scan for
  secrets", "lint this prompt", "validate the chain manifest", "dry-run the
  output format", "validate this rating", "save the rating", "check rating
  variance", "lint the skill structure". Requires code execution (Python
  3.8+, stdlib only). Not for authoring prompts (jail-prompt) or producing
  ratings (jail-rate-skill).
---

# JAIL-PY-TOOLKIT

Successor to jail-py-prompt-tools + jail-py-rate-tools (merged 0.23.0 — one
install, two check families). The cores stay instruction-only per the
code-free rule; this companion holds all the code. Every script is
stdlib-only Python 3.8+, takes files (or stdin) as arguments, and exits
non-zero on failure so it drops into CI, a pre-commit hook, or the repo's
release validator (`scripts/validate-skills.py` runs the self-checks each
release).

## Prompt checks (back jail-prompt)

| Script | Backs | What it does | Exit |
|---|---|---|---|
| `scripts/secret-scan.py` | Phase 2 — Secure? | Flags hardcoded secrets / high-entropy keys (AWS, OpenAI, GitHub, Google, Slack, Stripe, JWT, PEM, secret-assignments, entropy). | 0 clean · 1 found · 2 IO |
| `scripts/prompt-lint.py` | Phase 3 — sanity check | Required skeleton sections, machine-verifiable SUCCESS TEST, concrete OUTPUT FORMAT, embedded ```json parses. | 0 pass · 1 errors · 2 IO |
| `scripts/chain-lint.py` | Chaining | Chain manifest handoffs: every stage's `requires` produced upstream; no cycles. | 0 pass · 1 errors · 2 IO |
| `scripts/truth-lint.py` | Truth-tagging | Known/Infer/Unknown claims each carry evidence ids that resolve. | 0 pass · 1 errors · 2 IO |
| `scripts/dry-run.py` | Output contract | Declared OUTPUT FORMAT vs a mock output — structural match before spending a real run. | 0 pass · 1 mismatch · 2 IO |

## Rating checks (back jail-rate-skill)

| Script | Backs | What it does | Exit |
|---|---|---|---|
| `scripts/validate-rating.py` | Rule 7 — self-verify | Rating record structure: 10 categories, scores 0.0–10.0, `overall` = rounded mean. | 0 pass · non-zero fail |
| `scripts/save-rating.py` | Rule 7 — persist | Validates, appends to `${CLAUDE_PLUGIN_DATA}/rating-history.jsonl` (fallback `~/.rate-skill/`), prints Overall delta vs previous. | 0 pass · non-zero fail |
| `scripts/variance-check.py` | Rule 3 — determinism | 2+ records of the same skill; per-category mean ± stddev; fails on drift > ±0.2. | 0 pass · non-zero drift |
| `scripts/validate-skill-structure.py` | Structure | Skill dir lint: SKILL.md present, frontmatter name+description, folder==name. | 0 pass · non-zero fail |

## Manual fallback
No code execution available → each backing skill's SKILL.md states the
manual version of every check; run those inline and label the result
"manually checked, not machine-verified".
