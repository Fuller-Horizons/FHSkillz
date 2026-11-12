**Lane: FULL SWEEP.** This is a company-wide pricing change with a revenue target, which makes it consequential and contested. I ran one pass with no independent reviewer, so there is no fix-and-re-attack round yet.

**Steelman:** A 25% price increase is the cheapest revenue lever a services firm has. It needs no new hires, no sales cycle, and little delivery effort, and most of the gain drops to margin. If clients value the work as much as the plan says, the firm can absorb the increase and grow revenue on the same delivery team.

**Inputs:** The project has no client, churn, or financial data for Signal Results Group. Everything below rests on your stated premises (140 clients, 25% across the board, churn unchanged, revenue doubling next year). Those premises are treated as User-provided.

---

RED-TEAM FINDINGS (ranked by severity × likelihood)

1. **A price increase cannot double revenue on its own.** Even at zero churn, 25% is the most it can add. Doubling needs about 84 new clients at the new price, which is 60% more logos than today, and the plan does not mention them. At 10% revenue churn it needs about 98; at 20% it needs about 112. — severity: critical · basis: Inference: 1.25 × (1 − churn) must be combined with new-client revenue to reach 2.0× current revenue; arithmetic on User-provided premises.
   → Restate the target as the components: price effect, churn loss, and new-logo revenue, each with its own number and owner.
   → falsifier: recompute revenue with the three components set separately (arithmetic check)
     · falsifier-status: RUN-NOW → result: confirmed (the price lever alone tops out at +25%)

2. **The "churn won't change" assumption carries the whole plan, and the break-even is low.** Revenue-weighted churn above about 20% erases the entire price gain. Churn of 10% leaves the existing book at +12.5%. — severity: major (capped: Judgment alone) · basis: Judgment, resting on User-provided premise.
   → Model churn explicitly as a range, and set a go/no-go trigger on renewal-rate data.
   → falsifier: review three years of client churn and any past price changes. Cancellation at a 25% increase, if it occurs, would disprove the premise.
     · falsifier-status: HANDOFF → owner: finance or operations lead (holds billing and CRM data). Lab spec: pull churn by year and by any prior price change; then run a price test on 10–15 renewing clients, measuring acceptance and cancellations before a full rollout.

3. **"Customers love us" is not evidence about price tolerance.** Clients who stayed are the ones who accepted past terms, so this sample excludes the price-sensitive clients who already left. Satisfaction does not mean willingness to pay 25% more. — severity: major · basis: Judgment.
   → Ask for the reasons behind recent cancellations and NPS by client. Hold 10 willingness-to-pay conversations before committing.
   → falsifier: if recent exits cite price or value, or the 10 conversations show resistance above 15%, the premise is disproved.
     · falsifier-status: HANDOFF → owner: client success lead. Lab spec: exit-reason coding of the last 24 months of churn, plus a 10-client structured interview.

4. **The plan assumes the increase takes effect immediately.** Many services contracts reprice only at renewal or on notice. If the book renews through the year, year-one realization is well below 25%, and the "next year" target slips. — severity: major · basis: Judgment. The contract terms are Unknown to me.
   → Build a repricing calendar by renewal date and notice period, then forecast revenue by quarter.
   → falsifier: if fewer than about 60% of revenue reprices within 12 months under current terms, the year-one target is unreachable on price alone.
     · falsifier-status: HANDOFF → owner: whoever holds the contract register. Lab spec: list term, renewal date, notice clause, and escalator clause for all 140 clients.

5. **The new-client requirement has no cost, capacity, or pipeline behind it.** Roughly 84–112 new clients in a year means more sales effort, more onboarding, and more delivery capacity. Price does not add capacity. Revenue also is not profit, and the plan does not say what margin the added volume carries. — severity: major · basis: Inference from finding 1.
   → Add a pipeline model: opportunities needed, historical win rate, sales cost, and delivery headcount.
   → falsifier: if historical win rates and team capacity imply fewer than about 30 new clients in a year, the revenue target fails regardless of price.
     · falsifier-status: HANDOFF → owner: sales lead. Lab spec: three years of win rate, average deal size, and sales cycle length.

6. **A uniform 25% hits clients unevenly and invites discounting.** The smallest and most price-sensitive clients are the most likely to leave, and any account that negotiates back erodes the average. Competitors may also use the increase to pitch the same clients. Losing a few anchor accounts moves the total a lot at 140 clients. — severity: minor · basis: Judgment.
   → Segment the increase (for example, by account size, tenure, or margin) and set a discount policy before the announcement.
   → falsifier: revenue and churn by segment. If one segment carries most of the churn risk, the uniform rule is the wrong design.
     · falsifier-status: HANDOFF → owner: finance lead. Lab spec: revenue and margin per client, with tenure and segment tags.

**Open questions (Unknown, not findings):** current total revenue and margin; whether the 140-client count is the full revenue base; whether any past price changes exist; and what the increase costs in delivery and sales time.

**Scenario spread (illustrative, index: current revenue = 100):**
- **Best:** zero churn, full repricing on day one, and about 84 new clients at the new price → 200. Driver: all three hold at once.
- **Expected:** about 10% churn and partial renewal timing → existing book near 100–110. Price alone adds roughly 0–10%.
- **Worst:** churn above 20% plus discounting on renewal → existing book below 100. Revenue falls even with the price increase.

A plan that only reaches its target in the best case fails this test.

**Invalidation conditions (observable):**
- Revenue-weighted churn above 20% in the first renewal cycle after the increase.
- Fewer than 60% of clients reprice within 12 months under current contract terms.
- Pipeline and win rates imply fewer than 30 new clients a year.
- Exit reasons from the last 24 months cite price or value.

Survives the attack: The lever itself is sound. A 25% increase adds revenue without capacity, and the break-even churn of about 20% leaves real room if the premise holds. The attack targets the target and the single-lever causal claim, not the idea of repricing.

**Verdict: RETHINK.** The plan's core claim, that price alone doubles revenue, is arithmetically impossible at a maximum of 1.25×, so the plan needs a rebuilt target with explicit churn, repricing timing, and new-client components. Repricing itself can remain part of the plan.

---

JAIL-HANDOFF
- next: producer (rebuild the revenue model with the three components from finding 1, then fix findings 2–5 with the named HANDOFF owners).
- After the producer revises, send the revised model to **jail-verify** for a post-fix check, or run another **jail-red-team** pass with a fresh reviewer to close round 1 properly.
- If the revised plan still depends on one lever, it goes to **jail-decide** with these findings as inputs.

I can save this as a project doc (for example, `claude/redteam-2027-price-increase.md`) so the team can find it alongside the other decision packages. I have not written it yet.