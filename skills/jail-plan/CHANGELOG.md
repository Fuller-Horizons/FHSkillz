# Changelog — jail-plan

## 1.0.0 — 2026-07-22 (plugin 0.24.0)

Initial release as the merger of **jail-operationalize 1.0.0** (→ OPERATE
lane) and **jail-wayfind 1.1.0** (→ MAP lane); both retired this release
(lineage in git history).

- **OPERATE lane:** the full 13-field operating-workflow spec, carried over
  intact (trigger…completion standard), with field 6 referencing
  jail-approval-gate rather than containing it.
- **MAP lane:** the decision-ticket map for foggy multi-session work —
  name-the-destination, index-not-store, tickets-are-decisions, blocking
  edges, resolve-one-at-a-time, declare-the-way-clear — carried over intact.
  Map persistence now references **jail-handoff** (renamed from jail-baton).
- New in the merge: an explicit lane pick, and the "map the fog → then
  operationalize each cleared path" sequence for big efforts.
- Not merged (deliberate): jail-task-contract (up-front task scoping stays
  the universal front door) and jail-approval-gate (a fail-closed safety
  gate that must fire for any run, planned or not) — jail-plan references
  both.
