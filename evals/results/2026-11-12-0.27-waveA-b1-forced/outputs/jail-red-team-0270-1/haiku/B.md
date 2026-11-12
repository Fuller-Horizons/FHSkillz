**Lane: FULL SWEEP.** The plan is consequential (firm-wide revenue and 140 client relationships) and contested (the no-churn premise). I had no revenue, margin, churn, or contract data, so findings that need it are marked HANDOFF.

**Steelman:** Your clients are underpriced for the value they get, and loyalty is strong enough that a one-time 25% increase lands without losing accounts. The existing book then grows about 25%, and new-client growth closes the gap to 2×.

**RED-TEAM FINDINGS** (ranked by severity × likelihood)

1. **Price alone cannot double revenue. The plan needs roughly 84–112 new clients and never names them.** Severity: critical. Basis: with churn *c* and current revenue *R*, next year's revenue from existing clients is 1.25 × (1 − c) × R. Doubling therefore requires new-client revenue of (0.75 + 1.25c) × R, which is 140 × (0.6 + c) new clients at the new price: 84 at 0% churn, 98 at 10%, 112 at 20%. Even with zero churn, the price lever tops out at 1.25×.
   → Fix: restate the target as a bridge (price + retention + new logos) and commit to a new-logo number. Question to answer: how many net-new clients per year can sales close and delivery serve today?
   → Falsifier: the plan has a pipeline covering 84+ new clients at the new price.
     · falsifier-status: RUN-NOW → result: **confirmed** on the plan as written (the arithmetic holds and no new-logo figure appears). The pipeline check is HANDOFF to sales lead with the CRM pipeline export.

2. **The "churn won't change" premise is untested. Satisfaction is not willingness to pay at +25%.** Severity: critical. Basis: revenue breaks even at 20% churn, and above that the increase shrinks the existing book. Each point of churn costs about 1.25% of revenue. "Customers love us" usually comes from referenceable, engaged clients, so the accounts most likely to leave are the ones not heard from (survivorship and selection bias).
   → Fix: before committing, check whether past price changes moved churn. Segment the 140 clients by revenue, tenure, and margin. Interview 15–20 at-risk accounts, including recent churners. Pilot the increase on a subset before going firm-wide.
   → Falsifier: churn in the 180 days after prior price changes, or among the lowest-satisfaction quartile, rose above baseline.
     · falsifier-status: HANDOFF → owner: finance/ops with CRM churn history and exit-interview notes. Lab spec: apply the increase to a randomized ~20% of renewals, compare churn to a control group over one full renewal cycle.

3. **No capacity plan. A price rise adds revenue, not delivery hours.** Severity: major. Basis: a services firm's revenue is capped by billable hours and sales capacity. The 84–112 new clients in finding 1 need both, and the plan funds neither.
   → Fix: model required billable hours, delivery headcount, and sales headcount for the target, then state the utilization ceiling you will not exceed.
   → Falsifier: current team utilization is well below capacity and could absorb roughly 60% more client volume.
     · falsifier-status: HANDOFF → owner: operations lead with time-tracking data for the last 12 months.

4. **Uniform 25% ignores contract timing and segmentation. Year-one uplift will likely be well below 25%.** Severity: major. Basis: if renewals are spread evenly through the year and the increase applies at renewal, the average in-year effect is about half, roughly 12.5% realized in year one (RUN-NOW under that assumption: confirmed). Fixed-fee SOWs, multi-year terms, and rate-protection clauses can block mid-term repricing.
   → Fix: pull contract terms and renewal dates, model realized uplift month by month, and set increases by segment.
   → Falsifier: at least half of revenue is on contracts that renew within six months and allow repricing. If so, year-one uplift is closer to 25%.
     · falsifier-status: HANDOFF → owner: contracts or operations lead with the contract register.

5. **A visible, unexplained increase invites re-shopping.** Severity: major. Basis: clients buy against alternatives. A 25% rise with unchanged scope prompts "what changed?" and gives competitors a pitch: same quality, lower price. Clients will read it as opportunism.
   → Fix: pair the increase with a visible change in scope, outcomes, or service tier, and pre-brief the top 20 accounts before the notice goes out.
   → Falsifier: win/loss records in the last 12 months cite price, or renewal conversations report competitor quotes.
     · falsifier-status: HANDOFF → owner: sales lead with CRM win/loss fields.

6. **The plan has no invalidation conditions, so it cannot be proven wrong.** Severity: major. Basis: nothing observable is defined that would trigger a rollback, so the plan rests on faith rather than strategy.
   → Fix: set tripwires before launch. Examples: first-cohort churn above baseline + 3 points; price-concession requests in more than 15% of renewals; new-logo win rate below target for two consecutive quarters. Each tripwire triggers a predefined response (phase-in, rollback, or segment change).
   → Falsifier: the plan contains no such thresholds.
     · falsifier-status: RUN-NOW → result: **confirmed** (none present).

7. **The option set is missing: do-nothing, segmented increases, new-client-only pricing, value-tier packaging.** Severity: major. Basis: a uniform increase treats every client alike. Some accounts are probably underpriced and some probably unprofitable. Losing unprofitable clients could improve margin, and the plan doesn't count that.
   → Fix: compare at least three options on margin and risk, not only revenue. Include the do-nothing baseline.
   → Falsifier: if more than about 20% of clients sit below target margin, a targeted approach dominates a uniform one.
     · falsifier-status: HANDOFF → owner: finance with client-level margin data.

**Survives the attack:** Repricing is a sound instinct. A 25% increase is within the range firms take when underpriced, and pricing is often the highest-leverage margin lever. If the relationships are as strong as believed, the existing-book uplift is real. Losing the unprofitable tail might also help margin.

**Verdict: RETHINK.** Price can deliver at most a quarter of the doubling, and the churn premise has never been tested; keep the pricing move, but rebuild the plan around an explicit revenue bridge, a pilot, and tripwires.

**JAIL-HANDOFF**
```
next: producer (fixes) → then jail-decide (re-choose among pricing options with these findings)
open HANDOFF items: CRM churn history by cohort · contract register with renewal dates · utilization/capacity data · win/loss · client-level margin
required before decision: a named new-logo target and a pilot design
```