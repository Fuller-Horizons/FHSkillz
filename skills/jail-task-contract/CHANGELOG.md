# Changelog — jail-task-contract

## 1.3.0 — 2026-07-25 (plugin 0.25.0)

- SHIP-GATE before emitting: 14 fields valued-or-"none", field 13 restated as the failing check, field 14 non-empty-or-none, any unfillable field ships as `UNKNOWN — <question>` and blocks the contract (fail-closed — no partial contract leaves the skill).
- Operational safety in Step 3: field-14 actions wait on a recorded human "approved"; an unlisted irreversible/external/durable/spend action found mid-run means STOP + amend 14 + re-approve; secrets/PII named by class in field 5, never pasted raw.
- Budget & settings in Step 1: temperature 0 / fixed 1–14 field order so identical inputs yield an identical contract; default lane ≤2 rounds × ≤5 questions and ≤1200 words of transcript, ≤1 line per field except 9/11/13, grill transcript compressed to decisions-only.
- New behavioral suite `evals/behavioral-0.25/jail-task-contract.json` (4 cases): UNKNOWN-not-ship, unlisted irreversible action, determinism, default-lane round cap.

## 1.2.0 — 2026-07-22 (plugin 0.23.0)

- Type presets: RESEARCH / BUILD / ANALYSIS pre-shaped contract starts (cut fill time; never skip fields).

## 1.1.0
- Delta adapted from Matt Pocock's skills repo (github.com/mattpocock/skills, MIT): grill mode (one-question-at-a-time exhaustive branch-walk for high stakes) + look-up-facts/ask-only-decisions rule; gotcha aligned.

## 1.0.0
- New skill (JAIL reasoning-kernel wave 1). Executable task contracts before work begins, and scope guarding after — 14 fields, testable completion, approval-required actions.