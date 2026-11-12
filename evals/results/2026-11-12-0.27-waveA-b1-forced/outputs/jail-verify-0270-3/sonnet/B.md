**VERIFICATION: FAIL**
Checks: 8 run · 4 pass · 3 fail · 1 unverified (checks 6 and 10 don't apply)

**Failures (ranked)**
1. **Grounding (check 4) and completion criteria (check 2): the "more orders, not higher prices" claim isn't supported by the source.**
   - The summary says AOV is "basically the same as it was in Q2." The source gives Q3 AOV ($7,103) but no Q2 order count or Q2 AOV.
   - Q2 AOV can't be derived from Q2 revenue alone. That is the figure the whole growth-driver conclusion rests on.
   - **Fix:** pull Q2 order count and AOV from the export. If you can't, drop the causal sentence.
2. **Unsupported confidence (check 8): "a good sign for the pipeline."**
   - Closed orders are not pipeline data. The source has no pipeline, lead or forecast figures, so this is opinion presented as a finding.
   - **Fix:** remove it, or label it as your read ("I read this as...").

**Passed**
- **Growth rate:** $412,000 vs $396,000 is +$16,000, which is +4.04%, so "about 4%" is correct.
- **Order math:** 58 × $7,103 = $411,974, which is consistent with $412,000 (412,000 ÷ 58 = $7,103.45). "Roughly $7,100" is fine.
- **Internal consistency:** no statement contradicts another.

**Flags**
- There is a typo: "the the pipeline."
- **Unverified (check 7):** the Q2 order count is missing. If Q2 had meaningfully fewer or more orders, the conclusion could flip.

**Evidence examined:** only the figures you pasted. I did not open the Q3 sales export itself. This is same-producer verification, so weight it accordingly.

**Suggested safe version (all claims supported):**
> Q3 revenue was $412,000, up about 4% from Q2's $396,000. We closed 58 orders in the quarter, at an average order value of roughly $7,100.

Add the growth-driver sentence back only once you have Q2 orders and AOV.

JAIL-HANDOFF
- status: FAIL
- next: producing author. Apply fixes 1–2, or pull the Q2 order count and AOV, then re-run jail-verify. If it passes, post it.