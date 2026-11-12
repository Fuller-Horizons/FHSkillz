# Batch-2 fix retest, round 1 (2026-11-12)

The 0.27 batch-2 blind test (`2026-11-12-0.27-waveA-b2-forced`) flagged jail-bmc, jail-cpr and jail-prospect as REVERT. Round-1 fixes (bmc 1.4.1, cpr 1.6.1, prospect 1.5.1) re-run against the 0.26 versions: 4 cases × Haiku/Sonnet, two blind Sonnet graders, 1 disagreement (no verdict change).

| Skill | 0.26 cases | Fixed cases | Verdict |
|---|---|---|---|
| jail-cpr 1.6.1 | 8/8 | 8/8 | Tie at ceiling; the 47-of-45-minute agenda is fixed. Keep. |
| jail-bmc 1.4.1 | 6/8 | 5/8 | REVERT: Haiku still answered a SWOT request with questions only. |
| jail-prospect 1.5.1 | 6/8 | 5/8 | REVERT: Haiku gave sub-scores with no signals; a vendor check named same-name businesses without sources. |

Both old and new fail the dog-grooming canvas case: the owner's own numbers are labeled HYPOTHESIS instead of evidence.

Round 2 (bmc 1.4.2, prospect 1.5.2): write the SWOT now (questions after); an owner's current figures are VALIDATED with a User-provided ref; a signal-and-source column sits next to every sub-score; same-name businesses only with a source. Retest: `2026-11-12-0.272-b2fix2`.
