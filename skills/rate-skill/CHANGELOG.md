# Changelog — rate-skill

All notable changes to this skill. Versions track `metadata.version` in SKILL.md.

## 2.0.0
- **Instruction-only core (code-free policy).** `validate-rating.py`, `save-rating.py`, `variance-check.py`, and `validate-skill-structure.py` moved to the companion **jail-py-rate-tools** skill; the skill-level pre-commit hook retired in favor of the repo-level `scripts/pre-commit-hook.sh`. Every validation step now names the companion-skill run *and* a manual fallback (recompute the mean, diff repeat records, eyeball structure).
- Fixed the duplicated History-location paragraph; added a README.

## 1.4.0
- Added `references/summarizer-guide.md` and a 300-line summarizer rule to stay within the token budget on large targets.
- Added `scripts/validate-skill-structure.py` (structural lint) and `scripts/pre-commit-hook.sh` (gates commits with both validators).
- New rule: scan the target's scripts/code for dangerous operations before scoring (never execute), recorded under Safety & Guardrails.
- Documented the `${CLAUDE_PLUGIN_DATA}` → `~/.rate-skill/` history fallback path.

## 1.3.0
- Added `scripts/variance-check.py` — empirical per-category mean ± stddev across repeated runs; grounds the Idempotency & Determinism category.
- Added a "static audit vs empirical eval" handoff to Anthropic's `skill-creator`.

## 1.2.0
- 10-category rating matrix, IDE/CLI compatibility matrices, deterministic (temp 0.0) scoring.
- `config.json` for IDE/CLI targets; `validate-rating.py` and `save-rating.py` (history + deltas).
