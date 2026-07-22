# jail-plan

The planning skill, two lanes:

- **OPERATE** — turn a decision or recommendation into a runnable **operating
  workflow**: the 13-field spec (trigger → inputs → actions → tool → owner →
  approval → output → evidence → metric → frequency → risk → next action →
  testable completion). A named owner could run it next Monday without asking
  what was meant.
- **MAP** — navigate big, foggy, multi-session work by charting a **map of
  decision tickets** (questions whose resolution is a decision, not a build
  task) and resolving them one at a time until the path to a named
  destination is clear.

Successor to `jail-plan` 1.0.0 (OPERATE) merged with `jail-plan`
1.1.0 (MAP) at plugin 0.24.0. Rationale: both are planning at different
scales — one makes a *known* path runnable and owned, the other clears an
*unknown* path into decisions — and big efforts use them in sequence (map the
fog, then operationalize each cleared path). One skill, two declared lanes.
Legacy asks route here: "make this operational", "turn this into a process",
"who does what", "we should overhaul X", "figure out how to enter Y", "no
idea where to start".

Boundaries kept sharp: up-front scoping of a single task is still
`jail-task-contract`; action-approval tiers are still `jail-approval-gate`
(OPERATE references it for field 6, never absorbs it); multi-agent
coordination is still `jail-orchestrate`.

Fallback if chained skills are absent: each lane's rule is stated inline in
SKILL.md — the skill runs self-sufficient.
