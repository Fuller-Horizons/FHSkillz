**VERIFICATION: FAIL**
**Checks:** 10 run · 7 pass · 2 fail · 1 unverified

**Failures (ranked)**
1. **Check 4, grounding:** "The growth came from more orders rather than from higher prices." The figures you gave include Q3 order count and average order value but not Q2's order count, so nothing supports the volume-vs-price split. **Fix:** Pull Q2's order count from the export and compute Q2 AOV. Keep the claim only if the numbers support it. For reference, $396,000 at $7,103 implies about 56 Q2 orders, but that is arithmetic, not evidence.
2. **Check 4, grounding:** "which is a good sign for the pipeline." Nothing in the sales export covers pipeline. **Fix:** Delete the clause, or cite a pipeline source and label it as an inference.
3. **Check 8, unsupported confidence:** "basically the same as it was in Q2" is stated as fact, but Q2 AOV isn't in the source. **Fix:** Replace it with the Q2 AOV figure, or remove the comparison.

**Flags (don't block shipping)**
- Typo: "for the the pipeline."
- The headline numbers are correct but the summary omits the Q2 order count, which any reader will ask for.

**Passing checks, with the arithmetic**
- Q3 revenue $412,000 vs. Q2 $396,000: +$16,000, or +4.04%. "About 4%" is accurate.
- 58 orders × $7,103 = $411,974. $412,000 ÷ 58 = $7,103.45, so the AOV rounds correctly. "Roughly $7,100" is accurate.
- No secrets or customer-identifying data in the summary.

**Evidence examined:** The four figures and the summary text you pasted. I did not open the Q3 sales export itself, so the source figures are verified only against what you quoted. Checks 1, 2, 3, 5, 6, 9 and 10 pass on those figures. Check 5 is unverified because Q2 AOV can't be recomputed without Q2 order count.

**Corrected draft you can post now, with the open item marked:**
> Q3 revenue was $412,000, up about 4% from Q2's $396,000. We closed 58 orders at an average order value of about $7,100. [Add once confirmed from the export: Q2 order count and AOV, and whether growth came from volume or price.]

JAIL-HANDOFF
- next: Fix failures 1–3 (or post the corrected draft above), then re-run jail-verify on the revised text. Ship only after the Q2 numbers are in the summary or the causal claim is removed.