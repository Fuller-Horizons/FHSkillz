# 0.29 round 2: jail-prompt 2.14.1 vs 2.13.0 (2026-11-13)

3 cases (the two 2.14.0 lost plus the dependent-questions case it won), Opus 5.5 medium, two blind Sonnet graders (agreed on every case).

| Case | 2.13.0 | 2.14.1 |
|---|---|---|
| Q4 dependent questions | pass | fail (asked tone and framing while the audience was still open) |
| Q5 facts already given | fail (asked who reads it) | pass |
| C1 supportive | pass | pass |
| Cases | 2/3 | 2/3 |

VERDICT: REVERT. A tie after the 2-round limit; jail-prompt stays at 2.13.0. The frontier rule didn't hold reliably on Opus.
