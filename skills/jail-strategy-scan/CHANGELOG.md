# Changelog — jail-strategy-scan

## 1.0.0 — 2026-07-22 (plugin 0.23.0)

Initial release as the merger of **jail-swot 1.1.0** and **jail-pestle
1.1.0** (both retired this release; full lineage in their histories in git).

- Three lanes: INTERNAL (SWOT+TOWS) · MACRO (PESTLE+tripwires) · FULL SWEEP
  (both + interaction pass).
- Carried forward intact: SWOT sorting rules (internal+evidenced+controlled
  vs external+specific-mechanism, symptom-vs-root-cause, one-point-one-
  quadrant, materiality+confidence per entry), mandatory TOWS; PESTLE
  factor fields (trend/likelihood/magnitude/time-to-impact/O-T/confidence),
  materiality cut line, honest empty cells, mandatory tripwires.
- New in the merge: single shared evidence sweep (kills duplicate research
  cost), the cross-lane interaction pass (macro factor flips internal
  entry), tripwires handed to jail-memory as monitored entries.
