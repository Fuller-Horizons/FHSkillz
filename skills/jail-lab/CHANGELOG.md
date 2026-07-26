# Changelog — jail-lab

## 1.1.0 — 2026-07-25 (plugin 0.25.0)

- Added a Blast radius rule to Step 0: runs default to sandboxed/non-production data; production, real-user, or irreversible-state experiments need jail-approval-gate sign-off before running, flagged in the Budget line (manual fallback: state the tier and get an explicit human "approved" inline). [Rule 5]
- Step 6 now closes with the Constitution's JAIL-HANDOFF block (facts/outputs/risks/approval_required mapped to lab semantics) instead of a prose-only report, so downstream skills get structured handoff.
- Added a one-line self-check before closing: ledger row count = experiments run (baseline + every discard); best-so-far = the ledger's max KEEP row — a machine-checkable exit gate for "done."

## 1.0.0
- New skill (JAIL reasoning-kernel wave 1). Metric-driven experiment loops on anything improvable — one variable, bounded runs, keep/discard against best, append-only audit ledger. Adapted from karpathy/autoresearch (MIT).
