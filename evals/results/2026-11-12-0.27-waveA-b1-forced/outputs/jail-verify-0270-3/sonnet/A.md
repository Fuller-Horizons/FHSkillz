```
VERIFICATION: FAIL
Checks: 10 run · 6 pass · 3 fail · 1 unverified
Failures (ranked):
 1. Check 4 (grounding) · The claim "growth came from more orders rather than higher prices" and "AOV is basically the same as Q2" has no support. Your source gives Q2 revenue only. It has no Q2 order count or Q2 AOV, so the Q2 comparison can't be made. · Fix: pull Q2 orders and AOV from the export, or cut the claim.
 2. Check 2 (completion criteria) · The done-check is that every figure and claim traces to the source. The Q2 AOV claim doesn't. · Fix: same as above.
 3. Check 8 (unsupported confidence) · The causal wording ("came from", "rather than") is stated as fact. Without Q2 volume it is at most a guess. "A good sign for the pipeline" is a judgment, and closed orders aren't pipeline. · Fix: label it as a judgment or remove it.
Flags:
 - Typo: "the the pipeline".
 - Check 6 UNVERIFIED: I did not open the Q3 export. I used the figures you typed in.
Verified OK:
 - Growth: (412,000 − 396,000) / 396,000 = 4.04%, so "about 4%" holds.
 - AOV: 412,000 / 58 = $7,103.45, so "roughly $7,100" holds. 58 × 7,103 = 411,974, which is rounding.
Evidence examined: your pasted figures and summary only (no export file, no contract; checked against your request verbatim).
Checklist used: report/memo. This is a same-producer verification, and DUAL was unavailable.
```
VERDICT-JSON: {"verdict":"FAIL","run":10,"pass":6,"fail":3,"unverified":1,"lane":"single"}

**Do not post as written.** The numbers are right, but the "more orders, not higher prices" conclusion isn't backed by what you gave me.

**Safe version, using only what's verified:**
> Q3 revenue was $412,000, up about 4% from Q2's $396,000. We closed 58 orders in Q3, at an average order value of roughly $7,100.

If you add Q2's order count and AOV, I can re-check the "more orders vs. higher prices" line. If Q2 AOV was within a few percent of $7,100, the claim holds, but only then.

JAIL-HANDOFF
- status: blocked on one open item
- next: producing author fixes the claim (get Q2 orders and AOV, or cut the line), then re-run jail-verify. Once the verdict is PASS, ship or run jail-summarize.