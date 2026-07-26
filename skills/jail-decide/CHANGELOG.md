# Changelog — jail-decide

## 1.2.1 — 2026-07-26 (plugin 0.25.0)

- Ship-check fix (behavioral gate defect): when the input is an existing
  draft/package, run the ship-check FIRST against it as received and keep
  the real FAILs as the audit record — then fix and emit a SECOND line.
  Producers were silently repairing violating drafts and emitting only a
  clean line, destroying the evidence that a gate was ever breached.
- Unclosable gates (no owner nameable, no source obtainable) no longer strand
  the run on an open FAIL: emit the FAIL, name the question/evidence that
  would close it, and withhold the package instead of inventing a value.

## 1.2.0 — 2026-07-25 (plugin 0.25.0)

- Ship-check: 7 binary gates emitted as one line before release (criteria-first, do-nothing priced, door type, ≥2 change-conditions, sourced numbers, owner named, council check), fail-closed — packages no longer ship with a silently missing gate.
- Sensitive-input rule in Step 1: personnel/comp/health/privileged facts and NDA figures enter as roles, bands, and ranges; no raw evidence dump; stop and ask the owner rather than restate regulated data.
- Package budget + fixed ordering above the template (≤450 words, ≤5 option rows, cite the research packet by reference; do-nothing first then by rank; ties declared and broken by a named criterion) — cuts length drift and silent picks.
- Seeded `evals/behavioral-0.25/jail-decide.json` (4 cases) asserting the ship-check line fires and that a missing do-nothing or an unsourced number trips FAIL.

## 1.1.0 — 2026-07-22 (plugin 0.23.0)

- Quantified lane (expected value as ranges, cost of delay pricing do-nothing, payback; earned by evidence, never gut-feel decimals) + explicit council-escalation check recorded in the package (Tier-D mini-council for everyday contested calls).

## 1.0.0
- New skill (JAIL reasoning-kernel wave 1). Defensible decision packages — criteria before options, do-nothing always priced, reversibility named, change-conditions written down.