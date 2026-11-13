# 0.29 blind test: jail-prompt 2.14.0 vs 2.13.0 (2026-11-13)

7 cases on Opus 5.5 medium; two blind Sonnet graders, no disagreements.

| | 2.13.0 | 2.14.0 |
|---|---|---|
| Cases fully passing | 6/7 | 5/7 |
| Assertions | 94% | 94% |

- Won Q4 (dependent questions): 2.13 asked a client-tone question while the audience was still open; 2.14 asked only the frontier.
- Lost Q5: asked "who reads it?" although the request named HVAC owners.
- Lost C1-supportive: no TEST RESULTS/UNTESTED line (only the handoff `tested:` field).

VERDICT: REVERT 2.14.0 as is → 2.14.1 fixes both losses (stated facts never asked again; the test line is required in every reply with a prompt). Retest: `2026-11-13-0.29r2-prompt`.
