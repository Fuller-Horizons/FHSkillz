# Changelog — jail-prompt

All notable changes to this skill. Versions track `metadata.version` in SKILL.md.

## 1.9.1
- Hardened `validate-skills.py` to skip link checks inside code spans / fenced blocks, so illustrative absolute-path examples in docs no longer false-positive; generalized the "Reference link rot" gotcha example to a non-machine-specific path. The repo's own validator now passes on this skill.

## 1.9.0
- Epistemic truth-tagging (`✓Known`/`~Infer`/`?Unknown`) as schema fields with evidence IDs (`references/truth-tagging.md`); `scripts/truth-lint.py` rejects an unevidenced `✓Known` and is grounding-conditional (`--require-evidence` only when SOURCES declares retrieval, so it never invites fabricated source ids).
- External / second-model verification for citations and the contrary case — same-model self-grading is the fallback, not the default.
- New `VERIFICATION PLAN` skeleton line: `[AUTO]`/`[HUMAN]` steps, lead with the most-falsifying check, mark results provisional when `[AUTO]` checks disagree.
- Per-mode generation-settings reference (`references/generation-settings.md`) and the "parameter beats prompt" principle.
- High-stakes escalation now routes the adversarial pass to a different model, requires different sources, and uses an impact × likelihood × reversibility rating; Phase 1 gains an epistemic mode declaration.
- Adapted from the AI Control Surface framework; deliberately excludes its cross-model platform matrix and monitoring/golden-dataset layer (out of scope — belongs in a separate eval skill).

## 1.8.0
- Added explicit **chain assembly & verification** (`references/chaining.md`): a chain manifest making every handoff explicit (`produces`→`requires`), checkpoint gates between steps (`retry`/`stop`/`rollback`/`human`), fan-out/fan-in patterns, and a chain-level SUCCESS TEST.
- Added `scripts/chain-lint.py` — fails on a broken handoff (a step requiring a key no earlier step produces) and warns on missing/weak per-step or chain-level success tests before the chain runs.
- Added a **model-driven self-critique pass** in Phase 3: argue the strongest case against the prompt, apply the one highest-impact fix (one round), complementing the structural script lints.
- Added a portable, install-free **meta-prompt** (`references/meta-prompt.md`) that reproduces the workflow in any model with no skill/scripts.
- New Gotchas: broken chain handoff, and chaining a task one good prompt could handle.

## 1.7.0
- Standardized the METADATA handoff block to a fixed key set (`inputs`/`outputs`/`params`/`requires`/`produces`) so downstream agents can parse it reliably.
- Added a mandatory output-sanitization requirement with a malicious-sample SUCCESS TEST assertion for prompts whose output is rendered or executed downstream.
- Added a determinism self-test in the dry-run step (run twice, diff structure) to verify the idempotency the METADATA promises.
- Tightened the build-vs-buy gate paragraph to reduce token footprint without losing meaning.

## 1.6.0
- Stakes-triage lanes (Instant / Lite / Full) with a silent comprehension gate.
- Bundled scripts: `secret-scan.py`, `prompt-lint.py`, `dry-run.py`, `validate-skills.py`, `pre-commit-hook.sh`.
- Reference set: `examples.md`, `sources.md`, `antipatterns.md`, `templates.md`.
