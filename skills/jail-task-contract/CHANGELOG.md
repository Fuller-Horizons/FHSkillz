# Changelog — jail-task-contract

## 1.4.0 — 2026-11-12

- Field 13 now uses a structured acceptance-criterion format (AC-NNN: scenario, trigger/action, expected result, must-not, verification method, priority); Quick Capture 3-7 ACs, Full adds a risk row per security/data/migration/external dependency; "the check must be able to FAIL" kept. Pattern adapted from ECC (MIT).
- New ENGAGEMENT preset (consulting scope): ACs, in-scope list, 5+ out-of-scope items with why, change-order triggers, decision rights, client inputs with due dates.
- Preset detail moved out of the core into `references/presets.md`.
- Business-rule boundary: business rules, compliance duties, SLAs, pricing, retention policy are never inferred from files; User-provided or Unknown until an authoritative artifact states them.
- Proportion rule: trivial single-step asks get no contract; vague goals are recorded as an assumption or blocking question; `[revised]` handling for ACs blocked by a discovered constraint.
- New Delivery section (client-facing copy: clean document, 9th-grade English, no YAML).
- Worked example `references/example-engagement-contract.md`.
- Canonical claim labels; description shortened to under 450 characters.

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