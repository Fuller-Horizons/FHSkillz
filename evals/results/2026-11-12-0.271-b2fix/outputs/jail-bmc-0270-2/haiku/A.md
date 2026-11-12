# Business Model Canvas: Long Island Pool-Service Subscription

**Bottom line:** On your numbers, each customer contributes **$48/month** after cost to serve, about a **$1,600 lifetime contribution** at 3% churn, and pays back acquisition in about **5 months**. The model is strong on paper. Three things will break it before a skeptical investor or accountant accepts it: the $41 cost-to-serve doesn't reconcile with two technicians on payroll, churn comes from only 18 months of data, and the owner's 15 hours a week of route work isn't costed anywhere.

## Evidence references

Nothing external was researched in this pass. Every number below comes from your figures or from arithmetic on them.

| Ref | Source | Status |
|---|---|---|
| E1 | Customer count (40 → 212) and $89 price | Checkable in billing system. Not yet checked. |
| E2 | Cost to serve, $41/customer-month | Owner estimate. No ledger breakdown. |
| E3 | Churn, 3%/month | Owner-stated average. No cohort data. |
| E4 | CAC, $240 blended | Owner-stated. Not tied to spend ÷ sign-ups. |
| E5 | Segment mix (68/22/10) and channel mix (50/33/17) | Owner says "about" and "roughly." |
| E6 | Staffing: two technicians plus owner | Checkable in payroll. Not yet checked. |

## 1. The canvas

Labels: **V** = validated (checkable ref), **H** = hypothesis.

| Block | Element | Label | Evidence ref | Confidence |
|---|---|---|---|---|
| Customer segments | Single-family homeowners with in-ground pools (~68%, ~144 accounts) | H | E5 | Medium |
| | HOA/condo shared pools (~22%, ~47 accounts). Unit of "customer" undefined. | H | E5 | Low |
| | Small motels and B&Bs (~10%, ~21 accounts) | H | E5 | Low |
| Value propositions | Single-family: weekly service, flat monthly fee, one bill, chemistry handled | H | E2, E5 | Medium |
| | HOA/condo: one vendor, scheduled service, board-ready documentation | H | None | Low |
| | Motels/B&Bs: guest-ready pool, reliable service, chemistry records | H | None | Low |
| Channels | Neighbor referrals and yard signs (~50%) | H | E5 | Medium |
| | Google Maps / local search (~33%). Cost of this channel unknown. | H | E5 | Medium |
| | Pool-supply store partnership (~17%). Terms unknown. | H | E5 | Low |
| Customer relationships | Recurring monthly subscription. Billing method (auto-pay or invoice) unknown. | H | None | Low |
| | Route-based personal service. Owner is the main relationship holder. | H | E6 | Medium |
| | Retention: 3% monthly churn | H | E3 | Low |
| Revenue streams | Monthly subscription at $89 per customer; MRR $18,868 | V | E1 | Medium (pending check) |
| | Add-on or repair revenue | H | None | Gap: unknown whether it exists |
| | Price increases | H | None | Untested |
| Key resources | Two technicians | V | E6 | Medium (pending check) |
| | Owner's route time (~15 hr/week) | H | Owner statement | Medium |
| | Trucks, chemical and parts inventory | H | E2 | Low |
| | Route density: 212 accounts | V | E1 | Medium (pending check) |
| | Local referral trust and reviews | H | None | Low |
| Key activities | Route servicing: chemistry, cleaning, equipment checks | H | E2 | Medium |
| | Scheduling and routing | H | None | Medium |
| | Billing and collections | H | None | Low |
| | Acquisition: referral prompts, yard signs, Google profile | H | E4 | Low |
| Key partnerships | Pool-supply store as lead source (~17%) | H | E5 | Low. Dependency risk. |
| | Chemical and parts suppliers | H | None | Low |
| Cost structure | Cost to serve, $41/customer-month (labor, truck, chemicals, parts) | H | E2 | Low. Fails the closure check in §4. |
| | CAC, $240 per new customer (blended) | H | E4 | Low–medium |
| | Owner's route time (~65 hr/month) | H | None | Gap: not costed |
| | Fixed overhead: insurance, software, phone, vehicle, accountant, marketing | H | None | Gap: not provided |
| | Partner fees to the supply store, if any | H | None | Gap: unknown |

## 2. What the numbers say

| Metric | Value | Method |
|---|---|---|
| Contribution per customer-month | $48 (54% of price) | $89 − $41 |
| Average customer life | 33 months | 1 ÷ 3% |
| LTV, undiscounted | ~$1,600 | $48 × 33.3 |
| LTV, 1%/month discount | ~$1,200 | $48 ÷ (3% + 1%) |
| LTV : CAC | 6.7x undiscounted, 5.0x discounted | $1,600 ÷ $240 |
| CAC payback | 5.0 months | $240 ÷ $48 |
| MRR | $18,868 | 212 × $89 |
| ARR run-rate | ~$226k | MRR × 12 |
| Monthly contribution, before overhead | ~$10,176 | 212 × $48 |
| Customers churned per month | ~6.4 | 3% × 212 |
| Monthly acquisition spend to hold flat | ~$1,530 | 6.4 × $240 |
| Implied gross adds | ~14/month, ~240 over 18 months | Solves to 212 at 3% churn from a start of 40 |
| Implied churned over 18 months | ~65 | 240 gross adds − 172 net adds |
| Acquisition spend, 18 months | ~$57k | 240 × $240 |
| Revenue collected, 18 months | ~$213k (estimate) | Sum of monthly customers × $89 |
| Contribution after CAC, 18 months | ~$57k (estimate) | ~$115k contribution − ~$57k CAC. Before overhead and owner pay. |

**Reconciliation check:** The implied ~240 gross adds and ~65 churned should match your sign-up and cancellation records. If they don't, one of your inputs is off.

**Sensitivity:**

| Scenario | Churn | CAC | Cost/customer | LTV | LTV:CAC | Payback |
|---|---|---|---|---|---|---|
| Base | 3% | $240 | $41 | $1,600 | 6.7x | 5.0 mo |
| Churn at 5% | 5% | $240 | $41 | $960 | 4.0x | 5.0 mo |
| CAC at $400 | 3% | $400 | $41 | $1,600 | 4.0x | 8.3 mo |
| Cost at $50 | 3% | $240 | $50 | $1,300 | 5.4x | 6.2 mo |
| Owner time costed at $50/hr (~$15/customer) | 3% | $240 | $56 | $1,100 | 4.6x | 7.3 mo |
| Combined: churn 5%, CAC $400, cost $50 | 5% | $400 | $50 | $780 | 1.95x | 10.3 mo |

A 3x LTV:CAC is a common investor rule of thumb. The model holds above it on base assumptions and stays above it if any one assumption moves. Two bad assumptions together break it.

## 3. Internal inconsistencies

1. **One price and one service for three different buyers.** Single-family owners, HOA boards and motel operators buy different things. The model prices and costs them as one customer. The HOA "customer" may be one association paying for a shared pool, or one account per unit. That changes revenue per pool and cost per pool. Define the unit before anything else.
2. **Cost-to-serve doesn't close against payroll.** At an assumed $22/hour, two full-time technicians cost about $7,600/month in wages before payroll taxes and insurance. Total cost-to-serve at 212 customers is $8,692/month. That leaves about $1,100/month for trucks, fuel, chemicals, parts, insurance and payroll taxes. Either the $41 excludes items, the technicians are part-time or paid less than assumed, or visits are less frequent than weekly. Your accountant can settle this quickly.
3. **Blended CAC hides the marginal cost of growth.** About half of new customers come from referrals, which are cheap, and a third from search. The $240 average probably understates what the next 100 customers cost. Referrals don't scale linearly.
4. **Owner time is outside the model.** The owner's 15 hours a week of route work is capacity. Either it's in the $41 (in which case the owner is paid through the cost line) or it's free labor the business depends on. Both are fine, but the canvas must say which.
5. **The partnership is an uncosted dependency.** It supplies 17% of customers. If it charges a fee or margin, that cost is missing. If it ends, 17% of acquisition goes with it.
6. **Churn is extrapolated from a young base.** A 3% monthly rate implies about 33 months of life, but the business is 18 months old. Most of the lifetime hasn't been observed yet. Also check for seasonality: a Long Island pool business may see cancellations and pauses around fall closings.
7. **Capacity has no ceiling in the model.** If visits are weekly, 212 stops is about 21 per technician per day, across five days, before the owner's share. The model implies growth without stating where the route capacity runs out.

## 4. Unit-economic dependencies

- **LTV depends on churn.** It scales with 1 ÷ churn. Cutting churn from 3% to 5% drops LTV by 40%.
- **Contribution depends on a complete cost-to-serve.** Each $1 of cost is about $212/month across the base. Adding owner time at $50/hour removes about a third of contribution.
- **LTV:CAC depends on CAC holding as referrals saturate.** Each +$100 in CAC cuts LTV:CAC from 6.7x to 4.7x.
- **Everything depends on route capacity.** Scaling past current density needs a third technician or fewer stops per technician. Neither is in the cost structure.

## 5. Riskiest assumptions and experiments

Ranked by impact if wrong × evidence weakness. Experiments are sequenced cheapest-decisive-first.

**A1. Churn holds at 3%, across segments, over full customer lives.** Impact high. Evidence weak.
- **Experiment 1: cohort retention export.** Metric: 6-month logo retention by start month and segment (direction: up). One variable: none, this is measurement. Run: export billing history, about one day, $0. Pass: blended trailing-6-month churn ≤ 3.5%, and no segment above 2x the blend. Fail: churn above 4%. Then rebuild LTV at observed churn and re-run the canvas.

**A2. The $41 is complete and holds as routes grow.** Impact high. Evidence weak. Fails closure check.
- **Experiment 2: fully loaded cost capture.** Metric: fully loaded cost per customer-month (direction: down). One variable: none, this is measurement. Run: eight weeks logging technician hours by route, truck miles, chemical and parts receipts, and payroll taxes and insurance. Pass: fully loaded cost ≤ $45 at current density. Fail: above $48, which takes contribution to $41 or less. Then re-price or change service frequency.

**A3. CAC stays near $240 beyond referrals.** Impact high. Evidence none on marginal channels.
- **Experiment 3: paid-channel CAC test.** Metric: marginal CAC on search (direction: down). One variable: monthly spend on Google local ads or a Business Profile campaign. Run: 60 days, $2,000 total, minimum 8 sign-ups, or extend. Pass: marginal CAC ≤ $300 (LTV:CAC ≥ 5x). Fail: above $400 (LTV:CAC ≤ 4x). Do not scale paid acquisition on fail.

**A4. The business runs without owner route time, at current capacity.** Impact high. Evidence none.
- **Experiment 4: owner-off-route test.** Metric: missed-visit rate, complaints and cancellations (direction: no change). One variable: owner's route hours, 15 → 0, on one route group (about 50 customers). Run: four weeks. This touches live customers, so get your approval and a plan for missed visits first. Pass: missed visits ≤ 1%, zero cancellations in the test group. Fail: hire a third technician before scaling.

**A5. $89 holds for HOA and motel segments.** Impact medium-high. Evidence none. Price is uniform, never tested.
- **Experiment 5: segment price test.** Metric: quote-to-signed conversion (direction: up). One variable: price quoted, $89 vs. about $107 (+20%). Run: six weeks, 10 quotes to HOA boards and motel managers, about 10 hours of sales time. Pass: at least 3 of 10 sign at the higher price. Fail: fewer than 2. Keep $89, or create a segment-specific service instead.

Experiments 1 and 2 cost nothing but time and should run before any investor meeting. Experiment 3 is the first with real spend. Experiment 4 is the only one that puts customers at risk. To run experiments through the jail-lab ledger, I can hand off any of them.

## 6. Customer validation questions

- **HOA boards:** Is your contract per association or per unit? Who signs, and what would make you cancel?
- **Motel and B&B operators:** How often do you need chemistry records or guest-ready checks? Would you pay more for documented service?
- **Current single-family customers:** Would you pay $107/month for weekly service plus a monthly service report? What would make you cancel?
- **Customers who left:** What was the reason: price, missed visits, a seasonal pause, a move?
- **Referrers:** What did you say when you recommended us? What would you say to a neighbor who's hesitant?
- **Add-on test:** Would you pay for opening or closing service, or for repairs handled by the same technicians?

## 7. Strategic implications and next actions

**What holds up:** 54% contribution margin, 5-month payback, and a referral engine that supplies half of new customers at low cost. These are the investor-grade parts.

**What doesn't yet:** Cost-to-serve completeness, churn beyond 18 months, marginal CAC, owner-independence, and what the partnership costs.

**Next actions:**
1. **This week (accountant):** Reconcile four numbers: customer and billing counts (E1), gross adds and acquisition spend (E4), cost-to-serve ledger (E2), and payroll (E6). Confirm the implied gross adds (~240) and churned (~65) match your records.
2. **This week (you):** Define "customer": account, pool or unit. Pull a cohort export of starts and cancellations by segment (Experiment 1).
3. **Next 30 days:** Begin cost capture by route (Experiment 2). Tag each new customer by source to split CAC by channel.
4. **Before any investor meeting:** Add overhead, owner pay and partner terms to the model. Investors will ask for a full P&L and cohort retention, and this canvas has neither yet.

**What to tell an investor now:** ARR run-rate ~$226k, contribution ~$10.2k/month before overhead, 5-month CAC payback on current data, with cost and churn validation underway.

## Sources appendix

- E1–E6 are your figures as stated in this session. No external sources were used.
- All derived figures are arithmetic on those inputs. The method is in §2.
- The $22/hour wage, the $50/hour owner-time value and the weekly visit frequency are my assumptions, not your data. Correct them and I'll re-run the closure check and sensitivity.
- Pricing comparables and local competitor cadence were not researched. Run jail-research on Long Island pool-service pricing if you want external validation for the segment table.

## JAIL-HANDOFF

```
venture: Long Island pool-equipment monthly service subscription
decision: investor and accountant review of unit economics; go/no-go on paid acquisition
canvas: 9 blocks, every element labeled V/H; V limited to E1 and E6 (pending check)
coherence: 7 findings logged, none smoothed over
unit economics (base): contribution $48/mo, LTV ~$1,600 (undiscounted), LTV:CAC 6.7x, payback 5.0 mo
top assumptions: A1 churn, A2 cost completeness, A3 marginal CAC, A4 owner dependency, A5 segment pricing
experiments: E1–E5, cheapest-first, each with metric, single variable, bound, pass/fail
open gaps: customer unit definition; cost closure vs payroll; overhead; partner terms; cohort history
SUCCESS-TEST: labels intact PASS; coherence done PASS; experiments on top 5 PASS; no V without checkable ref PASS (E1/E6 pending check, flagged)
```

If you want, I can also turn this into a shareable HTML page for your accountant and investor, with the sensitivity table and experiment plan included.