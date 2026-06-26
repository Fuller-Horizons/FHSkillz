# Changelog — jail-prompt

All notable changes to this skill. Versions track `metadata.version` in SKILL.md.

## 1.8.0
- Added explicit **chain assembly & verification** (`references/chaining.md`): a chain manifest making every handoff explicit (`produces`→`requires`), checkpoint gates between steps (`retry`/`stop`/`rollback`/`human`), fan-out/fan-in patterns, and a chain-level SUCCESS TEST.
- Added `scripts/chain-lint.py` — fails on a broken handoff (a step requiring a key no earlier step produces) and warns on missing/weak per-step or chain-level success tests before the chain runs.
- Added a **model-driven self-critique pass** in Phase 3: argue the strongest case against the prompt, apply the one highest-impact fix (one round), complementing the structural script lints.
- Added a portable, install-free **meta-prompt** (`references/meta-prompt.md`) that reproduces the workflow in any model with no skill/scripts.
- New Gotch