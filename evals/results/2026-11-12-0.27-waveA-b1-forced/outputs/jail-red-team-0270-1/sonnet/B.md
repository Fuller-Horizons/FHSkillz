# RED-TEAM FINDINGS

**Lane:** THREE LENSES. The stakes are real (a year of revenue), but the artifact is two sentences, so a full sweep would be padding.

**Steelman:** You have 140 clients with strong relationships and good retention. Your prices likely lag the value you deliver and your own cost inflation. A 25% increase on a sticky base lifts revenue and margin with little added work. Strong goodwill means few clients leave, and any who do leave are probably the least profitable. That's a legitimate play. The problem is that it doesn't get you to 2x.

1. **The arithmetic doesn't reach the goal.** Severity: critical. Basis: a 25% price increase with zero churn and zero new clients gives 1.25x revenue, not 2x. To reach 2.0x you need 1.6x the volume (2.0 ÷ 1.25), which means about 60% more billable work. For a services firm, that means more clients or more scope, and more delivery capacity. The plan names no source for that volume.
   → Fix: Restate the goal honestly (~+25% at best), or add a separate, costed growth plan (new logos, upsell, capacity) for the other 60%.
   → Falsifier: compute required volume from your current revenue and the plan. · falsifier-status: RUN-NOW → result: **confirmed.** 1.25 × 1.0 = 1.25, so the plan is 0.75x short of its own target, and the volume gap is 60%.

2. **"Churn won't change" is an assumption, not evidence.** Severity: critical. Basis: affection is not price insensitivity. The break-even is steep: if you lose more than about 20% of revenue (1 − 1/1.25), the increase leaves you worse off. A 25% hike is far above typical B2B renewal uplifts, so it turns a relationship into a procurement event. Clients who've never benchmarked you will start.
   → Fix: Replace the assumption with a measured range. Model revenue at 0%, 5%, 10%, 20% churn, and set a pre-agreed stop-loss.
   → Falsifier: pilot the increase on a small slice (e.g., 10–15 clients) before rolling out, and track acceptance and renegotiation. · falsifier-status: HANDOFF → owner: managing partner or account lead; jail-lab spec: metric = % revenue retained at 90 days, budget = 1 renewal cycle, control = unchanged-price cohort.

3. **"Across the board" ignores who your 140 clients are.** Severity: major. Basis: client revenue is almost certainly concentrated, and elasticity differs by segment. Losing one or two top accounts could erase the gain from the other 130. Flat treatment overcharges price-sensitive, low-margin clients and undercharges your most embedded ones.
   → Fix: Segment by revenue share, margin, switching cost and contract status. Raise prices by tier, with higher increases where you're embedded and lower ones (or none) where you're not.
   → Falsifier: rank clients by revenue and compute how many top accounts it takes to lose 20% of revenue. · falsifier-status: HANDOFF → owner: finance or ops, needs the client revenue list. I don't have it.

4. **Contracts and timing aren't addressed.** Severity: major. Basis: multi-year or fixed-fee agreements may block mid-term increases. Others have notice periods. If the increase lands only at renewal, only a fraction of the year's revenue is affected, which shrinks the in-year lift further.
   → Fix: Map renewal dates and notice clauses, and compute the actual in-year uplift.
   → Falsifier: pull the contract renewal calendar. · falsifier-status: HANDOFF → owner: whoever holds client contracts.

5. **Nothing in the plan says what would prove it wrong.** Severity: major. Basis: there are no leading indicators, no trigger to roll back, and no do-nothing or alternative option (modest increase plus upsell, value-based tiers, packaging changes). A plan with no invalidation condition is a bet.
   → Fix: Set tripwires, e.g., "if more than X% of repriced clients push back or leave in the first 60 days, pause and revert for the remaining cohort."
   → Falsifier: check whether the plan lists any observable that would change your mind. · falsifier-status: RUN-NOW → result: **confirmed.** The stated plan contains none.

6. **Costs go up while revenue is at risk.** Severity: minor. Basis: a 25% increase usually brings more scrutiny, scope pushback and support load, and you have no stated capacity plan to deliver the extra volume that item 1 requires.
   → Fix: Include delivery capacity and hiring lead time in the model.
   → Falsifier: compare current utilization to the capacity needed for 1.6x volume. · falsifier-status: HANDOFF → owner: delivery lead.

**Survives the attack:** The instinct that you're underpriced and have pricing headroom is plausible, and a targeted increase is a reasonable lever. The price increase can be part of the plan. It can't be the whole plan.

**Verdict:** RETHINK. The plan misses its own target by arithmetic (about 1.25x versus 2x), and its main risk assumption, flat churn, is unmeasured and has a roughly 20% break-even.

```
JAIL-HANDOFF
next: producer (fixes) → then jail-decide to choose between (a) tiered increase + growth plan, (b) flat increase, (c) do nothing
open items: client revenue concentration, contract renewal calendar, capacity data
```