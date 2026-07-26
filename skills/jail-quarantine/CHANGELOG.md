# Changelog — jail-quarantine

## 1.2.0 — 2026-07-25 (plugin 0.25.0)

- Fixed HALT-RECORD line added to the Output block, required from the halt step before continuing — gives every sensitive halt (or a clean run) a gradeable, auditable record.
- Fail-closed classification tie-break: protected-class table hit OR a credential/PII shape signal (BEGIN...KEY, sk-/api_key=, SSN/16-digit-card); ambiguous items always classify as protected, never the reverse.
- jail-py-toolkit's secret-scan.py named as the preferred pre-halt scan for bulk batches, with a stated manual eyeball-grep fallback.

## 1.1.0 — 2026-07-22 (plugin 0.23.0)

- INLINE SCAN lane for everyday small third-party pastes (protected-class + injection + adoption-note in one pass; any hit escalates to the full gate) + the PROTECTED-CLASS TABLE formalized as the suite's canonical citable list.

## 1.0.0
- New skill (JAIL reasoning-kernel wave 1). Two-sided data discipline — inbound data quarantined until adopted; protected data halts processing and fails closed rather than degrading to an unsafe path.