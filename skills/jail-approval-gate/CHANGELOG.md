# Changelog — jail-approval-gate

## 1.2.0 — 2026-07-25 (plugin 0.25.0)

- Step 4 audit trail now emits a fixed one-line `GATE-RECORD` schema (action/tier/approver/ts/result) instead of free prose, so a disputed action is settled by a parseable ledger; added an unconditional restatement of each action's effects, targets, and reversibility ahead of the approval request, and a manual eyeball check for the five GATE-RECORD fields (no validator script exists).
- Step 2 tier assignment rewritten as an ordered, first-match-wins decision procedure over the skill's existing NEVER/PER-ACTION/BATCHABLE/AUTO criteria, so tiering is a lookup instead of judgment call; the old separate tie-break sentence folds into the ordering itself.

## 1.1.0 — 2026-07-22 (plugin 0.23.0)

- Standing APPROVAL PROFILE (Step 2b): ADR-shaped jail-memory entry persisting the tier map per project; later runs load + diff (uncovered action types default PER-ACTION); profile writes are themselves PER-ACTION; manual paste-block fallback without platform memory.

## 1.0.0
- New skill (JAIL reasoning-kernel wave 1). Action authorization tiers (never / per-action / batchable / auto) designed before the run, failing closed, with proper approval requests and an audit trail.