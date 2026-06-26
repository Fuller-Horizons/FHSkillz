# Changelog — jail-prompt

All notable changes to this skill. Versions track `metadata.version` in SKILL.md.

## 1.9.0
- Epistemic truth-tagging (`✓Known`/`~Infer`/`?Unknown`) as schema fields with evidence IDs (`references/truth-tagging.md`); `scripts/truth-lint.py` rejects an unevidenced `✓Known` and is grounding-conditional (`--require-evidence` only when SOURCES declares retrieval, so it never invites fabricated source ids).
- External / second-model verification for citations and the contrary case — same-model self-grading is the fallback, not the default.
- New `VERIFICATION PLAN` skeleton line: `[AUTO]`/`[HUMAN]` steps, lead with the most-falsifying check, mark results provisional when `[AUTO]` checks disagree.
- Per-mode generation-settings reference (`references/generation-settings.md`) and the "parameter beats prompt" principle.
- High-stakes escalation now routes the adversarial pass to a different model, require