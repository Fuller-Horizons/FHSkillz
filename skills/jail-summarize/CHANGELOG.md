# Changelog — jail-exec-brief

## 1.3.1 — 2026-07-26 (plugin 0.25.0)

- Fixed defect found by the behavioral gate: a refusal rationale restated a confidential specific verbatim (raw SSN count) that the shipped brief correctly withheld. Pre-ship check item 7 now explicitly binds every emitted artifact — refusal, hold notice, gap list — not only the shipped brief; name the class of sensitive detail, never the specific, in the rationale.

## 1.3.0 — 2026-07-25 (plugin 0.25.0)

- Added "Pre-ship check": a 7-item fail-closed gate (answer-first, fact/analysis labels, risk consequences, single priced recommendation, owned+dated next actions, named audience row, no classification silently dropped) run before any brief ships.

## 1.2.0 — 2026-07-22 (plugin 0.24.0)

- **Renamed jail-exec-brief → jail-summarize.** Same decision-forcing executive-communication skill (lead with the answer, translate tech→business, end on the forced decision); broader name. Cross-references updated; history preserves the jail-exec-brief lineage.

## 1.1.0 — 2026-07-22 (plugin 0.23.0)

- Decision-forcing mandate (every brief ends with the named decision, priced options, one recommendation, deadline + cost of delay; FYI is a declared justified exception) + audience-calibration table (board-CEO / operating exec / line manager).

## 1.0.0
- New skill (JAIL workflow layer, wave 1). Executive communication that leads with the answer and translates technical findings into business consequences — seven-part structure, facts labeled.
