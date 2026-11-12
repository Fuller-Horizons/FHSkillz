```
VERIFICATION: FAIL
Checks: 10 run · 4 pass · 6 fail · 0 unverified
Failures (ranked):
1. Completion criteria (check 2): the memo's numbers must reconcile and its claims must match its sources. Both fail. Revenue in §1 is $25,250, but $12,400 + $8,750 + $3,100 = $24,250. The memo is off by $1,000.
2. Grounding (check 4): §2 says Long Island demand "is expected to grow 12% per year through 2028," citing SBA 2024 NY Small Business Profile. Footnote 4 says that source "contains no forecasts or growth projections." The memo contradicts its own citation. Fix: remove the 12% claim, or replace it with a source that actually forecasts growth and cite that source.
3. Internal consistency (check 3): the same contradiction, between §2 and footnote 4. Fixed by the change above.
4. Calculations (check 5): the $25,250 total does not recompute. Fix: change the total to $24,250, or correct a line item if one is wrong.
5. Unsupported confidence (check 8): "is expected to grow 12%" is stated as fact, though the cited source has no forecast. Fix: delete the claim or downgrade it to a labeled assumption.
6. Implementation readiness (check 10): the third action, "Build a one-page seasonal-planting offer," has no owner. Fix: assign one, for example Jon Fuller or Maria Santos, and confirm the Jan 10 date with that person.
Flags:
- No task contract was supplied. I verified against your request verbatim: the memo is complete, with all four sections present.
- I did not open the SBA source. The verdict does not depend on it, because the memo's own footnote contradicts the claim.
- Footnote 4 is in the memo, but the §2 body text does not reflect it. A client reading only the body will be misled.
- The memo names individuals (Maria Santos, Jon Fuller) and client-facing dates. These are fine for a client memo, but confirm both are meant to be named.
Evidence examined: the memo text as pasted (§1–§4, footnote 4). Arithmetic recomputed by hand: 12,400 + 8,750 + 3,100 = 24,250.

JAIL-HANDOFF
next: producing skill / author, to fix the 6 items above and re-run jail-verify before sending.
ranked fixes: (1) correct total to $24,250; (2) remove or source the 12% growth claim; (3) assign an owner to the spring-mailer action; (4) re-verify.
```

Do not send this version. The revenue total is wrong, and the market-growth claim is contradicted by the memo's own footnote. Once the fixes are in, send me the revised text and I'll re-run the check.