**Lane: FULL SWEEP.** This is a $65k+ hire with a payback promise, and the promise is the contested part.

## Steelman (the plan at its strongest)

Signal Results Group has 300 former customers who already bought once, so the problem fit and the relationships are proven. A dedicated seller who works only that list turns an idle asset into pipeline faster than the founder can. Commission keeps most of the cost tied to results, so the downside is bounded. Four months is a reasonable first checkpoint for her to show she's earning her keep.

**Inputs I don't have.** The project holds no SRG financials, so these are my assumptions. Replace them with your numbers and I'll rerun the math:
- Commission: 10% of collected revenue
- Gross margin on engagements: 50%
- Loaded hire cost: base × 1.25 for taxes and benefits, about $81k/yr
- One-time setup: $3k
- Historical spend and churn reasons for the 300: unknown

## Payback arithmetic (RUN-NOW)

- Cost in the 4-month window: $81k × 4/12 ≈ $27k, plus $3k setup, so about $30k.
- Each revenue dollar contributes 50% − 10% commission = 40 cents.
- Collected revenue needed in 4 months: $30k ÷ 0.40 ≈ **$75k**.

| Reactivation rate (of 300) | Accounts won | Average revenue each must produce |
|---|---|---|
| 3% | 9 | ~$8,300 |
| 5% | 15 | ~$5,000 |
| 10% | 30 | ~$2,500 |
| 20% | 60 | ~$1,250 |

Sensitivity: at 40% gross margin the target rises to ~$100k; at 60% it falls to ~$60k.

→ **result: confirmed, conditionally.** Payback in 4 months requires about 10% of the list to reactivate at roughly $2.5k or more each, inside the window, with the rep productive from day one. For a new hire with no playbook, that is the optimistic end.

## RED-TEAM FINDINGS (ranked by severity × likelihood)

1. **The 4-month payback is unreachable as written; "pay for herself" is undefined.** Revenue, gross profit, cash, or loaded cost? The table above shows the target depends on a reactivation rate nobody has measured, and ramp time isn't in it. — severity: critical · basis: the arithmetic above; a new rep doesn't produce from month one.
   → fix: define payback as gross profit covering loaded cost. Set a 9–12 month payback, with a month-4 leading-indicator gate instead of a month-4 payback.
   → falsifier: pull trailing-12-month revenue and reactivation history for the 300. If fewer than 10% ever re-bought, or average trailing spend is under ~$2.5k, the 4-month target is disproved.
   → falsifier-status: HANDOFF → owner: requester (CRM export of the 300: last purchase date, prior-year and trailing revenue, last contact owner). Cheaper first test: you personally call 30 accounts over two weeks and count closed-won within 90 days. Keep the plan only if that clears 10% at ≥$2.5k average.

2. **Relationships may not transfer from the founder to the rep.** The people who won these accounts are probably the founder or one or two others. A rep calling "on behalf of" a firm the customer knows through someone else gets voicemail, the founder gets pulled back in, and attribution becomes a fight. — severity: major · basis: failure mechanism, not yet checked against the CRM.
   → fix: founder warm intro to the top 30–50 accounts before the rep dials. Set attribution rules before she starts.
   → falsifier: count accounts whose last contact owner is the founder or one person. If more than half, transfer risk is high.
   → falsifier-status: HANDOFF → same CRM export as #1.

3. **The list is finite and may be a smaller pipeline than 300.** Dormant contacts go stale, and the plan names no new-logo prospecting. Once the list is worked, month 3–4 pipeline depends on what's left. — severity: major · basis: list hygiene is unknown; the cadence estimate is mine, not sourced.
   → fix: scrub the list first. Decide now whether the role includes new-logo prospecting from month 2, and what share of her time goes to each.
   → falsifier: audit a random 20 accounts. If fewer than 60% have a current, named decision-maker, the usable list is much smaller than 300.
   → falsifier-status: HANDOFF → owner: requester. Spec: one day, metric = % reachable with a current decision-maker. Keep the plan as written only at ≥60%.

4. **No kill criteria or leading indicators.** The plan names one outcome, payback at month 4, and nothing to read before then. A month-2 signal can't change the decision, so the plan is faith, not strategy. — severity: major · basis: the plan as written.
   → fix: write gates before signing. For example: week 6, N conversations and M meetings; week 12, Z qualified proposals. Define what happens if a gate is missed: coaching, reassignment, or exit. Set the numbers from the list audit.
   → falsifier: the gates themselves. A gate that can't fail isn't a gate.
   → falsifier-status: HANDOFF → owner: requester, set during the jail-decide pass.

5. **The cheaper test isn't in the plan.** The plan compares hiring against nothing. The unpriced option is the founder working the top 30 accounts for 2–3 weeks, or a contract caller paid per booked meeting for 90 days. Either answers the demand question before $81k/yr is committed. — severity: major · basis: the plan names no alternatives.
   → fix: run the 30-account test first. Hire only if it clears the gates.
   → falsifier: the test itself. Compare meetings per 10 calls and the meeting-to-proposal rate against the break-even table.
   → falsifier-status: HANDOFF → owner: founder, 2–3 weeks.

6. **Commission basis will shape her behavior.** Commission on booked revenue pays before cash arrives, especially with milestone billing. Commission on collected revenue delays her pay in months 1–2 and raises attrition risk. A high rate pushes her toward large accounts and discounting. — severity: major · basis: general comp mechanics; SRG's billing terms are unknown.
   → fix: pay on collected revenue. If you want her to survive the ramp, add a draw for months 1–2, which re-enters the arithmetic above. Set a discount floor.
   → falsifier: model cash timing from invoice terms and the share billed on milestones.
   → falsifier-status: HANDOFF → owner: requester (billing data).

7. **Employment terms need review.** If the rep works in New York, commission terms generally must be in writing. The W-2 versus 1099 question also matters if commission-only ideas come up. — severity: minor · basis: general knowledge, not checked against current law.
   → fix: counsel reviews the offer letter and commission plan.
   → falsifier: counsel's read.
   → falsifier-status: HANDOFF → counsel.

**Survives the attack:** the core idea holds. Warm, previously paying accounts are usually the cheapest pipeline a small firm has, and dedicated capacity on them is a defensible test. Commission-heavy pay ties the downside to results. Four months is a fine first checkpoint; it just isn't payback.

**Verdict: RETHINK.** The hire idea survives, but a 4-month payback on a list you haven't measured, with no gates and no defined payback, sets up a month-4 failure you can't read in time. Re-decide the structure before signing.

```yaml
JAIL-HANDOFF:
  skill: jail-red-team
  lane: FULL SWEEP
  verdict: RETHINK
  next: jail-decide
  decide_on:
    - hire now vs 30-account warm test first
    - payback definition and target window (9–12 months suggested)
    - commission basis, draw, discount floor
    - month-6 and month-12 gates
  inputs_needed: [CRM export of the 300, commission rate, gross margin, founder relationship map]
  approval_required: [hiring, offer terms, any outreach to the 300 customers]
```

Once you send the CRM export or your real margin and commission figures, I can rerun the break-even table with your numbers. I can also save this to the Business Consulting Tools project as a doc if you want it alongside the other briefs.