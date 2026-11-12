## Bottom line

**Don't buy the third van yet.** Your two vans are roughly at break-even once variable costs are counted, and a third van with no new customers loses about **$7,200/month**. A third van only pays if it is full, which at your current pace means about **150 new regular customers**, and even then the margin is thin. Your first moves are to confirm what the $9,500 covers and to test a price increase, which is worth more than a van.

**Evidence status:** Every number you gave me is owner-reported and not checked against invoices or bank statements, so each one is labeled **H** under the fail-closed rule. Benchmarks come from vendor blogs and search summaries, not primary data.

## Canvas (V = validated, H = hypothesis)

| Block | Element | Label | Evidence ref | Confidence |
|---|---|---|---|---|
| Customer segments | S1: Owners on a 6-week grooming cycle, 310 accounts | H | Owner statement, 2026-11-12. Active vs lapsed not separated | Med on count, low on cadence adherence |
| Customer segments | S2: Owners paying for door-side convenience | H | Comparable-based: vendors price mobile as a convenience premium | Low |
| Value propositions | VP1: Groomed at home on a fixed schedule, no drive or drop-off | H | Comparable-based (mobile convenience positioning) | Med |
| Value propositions | VP2: $95 per groom | H | Owner-stated price. Benchmark band $95–145 puts you at the low end | Med |
| Channels | C1: Rebooking on the standing schedule | H | Owner-stated regularity. No rebook-rate data | Low |
| Channels | C2: Referral / word of mouth | H | No data on source of the 310 | Low |
| Customer relationships | R1: Standing recurring appointment | H | Owner-stated | Med |
| Revenue streams | RS1: $95 per groom, 224 grooms/month (310 × 52/72) | H | Derived from H inputs. The arithmetic is checkable; the inputs are not | Med |
| Revenue streams | RS2: Add-ons (nails, teeth, de-shed) | H | No data given | None |
| Key resources | KR1: 2 converted vans | H | Owner-stated. Purchase or lease terms unknown | Med |
| Key resources | KR2: 2 groomers (one per van) | H | Implied by the $9,500/van cost line | Low |
| Key activities | KA1: Route scheduling and stop density | H | No route data | Low |
| Key activities | KA2: Groomer hiring and retention | H | No data | None |
| Key partnerships | KP1: Van lessor or lender, insurer, supply vendor | H | Not stated | None |
| Cost structure | CS1: $9,500/van/month, van + groomer | H | Owner-stated. Your figure is far above the solo-operator ops-only benchmark (~$1,200/month), so it likely includes groomer pay | Med |
| Cost structure | CS2: Variable costs (fuel, supplies, card fees, marketing) | H | Assumed $10–20 per groom. Not stated by you | Low |
| Cost structure | CS3: Owner pay | H | Not stated. Gap | None |

## Unit economics (derived)

- Revenue per customer: $95 × 8.67 grooms/year ÷ 12 = **$68.61/month**
- Revenue: **$21,270/month** (~$255K/year) from 310 customers
- Per van: 112 grooms/month, about $10,635 revenue, against $9,500 cost. Margin before variable costs is **$1,135/van (10.7%)**
- **Density check:** 224 grooms ÷ (2 vans × 22 working days) = **5.1 grooms per van per day**. That is at the high end of a mobile schedule. A groomer blog uses 5 dogs/day as its worked example, and vendor KPI sources put revenue per van at $8,000–15,000/month. You sit inside that range. If you work six days a week, density is about 4.3/day, so the answer changes with your schedule.
- **Breakeven per van:** 100 grooms/month with zero variable cost, or **119 grooms/month** with $15 per groom in variable cost. You run at 112. This makes the two-van model very sensitive to whether the $9,500 already includes fuel, supplies and card fees.

| Two-van case | Variable cost/groom | Monthly profit |
|---|---|---|
| Today | $0 | +$2,269 |
| Today | $15 | **−$1,089** |

## Third-van scenarios (3 vans = $28,500/month)

| Scenario | Customers | Price | Var/groom | Revenue | Monthly profit |
|---|---|---|---|---|---|
| Third van, no new customers | 310 | $95 | $0 | $21,269 | **−$7,231** |
| Third van, full at observed density | 465 | $95 | $0 | $31,904 | +$3,401 |
| Third van, full at observed density | 465 | $95 | $15 | $31,904 | **−$1,633** |
| Third van, full, price $110 | 465 | $110 | $15 | $36,941 | +$3,404 |

- Fleet breakeven: **415 customers** with zero variable cost, **493** with $15/groom.
- A full third van adds about **$600/month** before variable costs and loses money after them. Each new customer adds $68.61 of revenue, so a van must fill to about 140–165 new customers just to cover its own $9,500.
- **Price is the cheapest lever:** each $5 increase is worth about **$1,120/month** at 310 customers. Each 10% of customers lost is about **$2,127/month**.

## Internal inconsistencies (findings, not footnotes)

1. **Capacity vs growth.** At 5.1 grooms/van/day you may already be at capacity. Adding a van only helps if you have unserved demand. Nothing in the canvas shows that demand.
2. **Cost basis.** The $9,500 figure is the swing factor. If it excludes fuel, supplies, fees or depreciation, the two-van model is loss-making.
3. **Key activities vs value proposition.** The proposition depends on reliable scheduling and on a groomer who stays. Both are unevidenced (KA1, KA2).
4. **Segment vs channel.** Your revenue depends on the 310 staying on cadence, but no retention data exists. The channel for new customers is unknown.

## Ranked assumptions and experiments

Ranked by impact if wrong × evidence weakness, cheapest-decisive first:

| # | Assumption | Impact | Experiment (jail-lab spec shape) |
|---|---|---|---|
| A1 | The $9,500/van covers all direct costs | Flips the sign of margin | **Metric:** reconciled per-van monthly contribution, direction ↑. **Variable:** none (measurement only). **Bound:** 3 months of bank and invoice records, 1 day of bookkeeping, $0. **Pass:** contribution ≥ $1,000/van after all direct costs |
| A2 | Retention holds on the 6-week cadence | ~$2,100/month per 10% loss | **Metric:** on-time rebook rate at 6 weeks. **Bound:** existing booking history, $0. **Pass:** ≥ 90% |
| A3 | Price headroom at $110 | ~$3,400/month if it holds | **Metric:** rebook rate at 6 weeks. **Variable:** price ($95 vs $110). **Bound:** 100 customers split 50/50 over 2 cycles (~12 weeks), foregone revenue on the test arm. **Pass:** $110 arm within 5 points of control and ≥ 90% rebook |
| A4 | Unserved demand of ~150 new customers | Gates the third van entirely | **Metric:** qualified inquiries that cannot be booked within 14 days. **Bound:** 4-week inquiry log, $0. **Pass:** ≥ 40 unbookable requests in 4 weeks, and ≥ 50% accept a slot 2 weeks out |
| A5 | A third groomer can be hired and sustains ~5 grooms/day | Required for van 3 | **Metric:** grooms/day and complaint rate. **Bound:** 2-week contract-groomer trial, contractor day rate. **Run only if A4 passes** |

Sequence: A1 → A2 → A4 → A3 → A5. A1 decides whether the current model works at all, and A2 and A4 decide whether a third van has a customer base. I can hand A3 and A4 to jail-lab if you want them run as tracked experiments.

## Customer validation questions

1. What do you charge for add-ons, and what share of visits include them?
2. How many of the 310 rebooked on time in the last two cycles, and how many dropped out in the last 6 months?
3. How many inquiries did you turn away or delay in the last 60 days?
4. What exactly does the $9,500 cover: groomer pay, lease or loan, fuel, insurance, supplies, card fees?
5. How many days a week does each van run, and how many grooms per day on average?
6. What would a $110 price do to your rebook rate? Would your customers accept it?

## Strategic implications and next actions

- **Decision:** Hold the third-van purchase. Gate it on (a) A1 showing ≥ $1,000/van contribution, (b) A4 showing a waitlist or inquiry pipeline of ~150 customers, and (c) a groomer hire you can keep.
- **This week:** Pull 3 months of bank and invoice data to settle A1. Start the inquiry log for A4.
- **Next 30 days:** Start the price test (A3). If $110 holds, the two-van model clears about $5,600/month before variable costs.
- **Revisit the canvas** when A1, A2 and A4 return data. Only the touched blocks need re-checking.

## Sources

Search summaries were used, not full page reads. Dates are as shown on the pages.
- [Mobile pet grooming van conversion and depreciation guide, Beancount, 2026-07-28](https://beancount.io/blog/2026/07/28/mobile-pet-grooming-van-conversion-depreciation-per-appointment-costing-guide): van cost and depreciation context
- [How much is dog grooming, MoeGo blog](https://www.moego.pet/blog/how-much-is-dog-grooming): price benchmarks ($75 example average)
- [Mobile groomers profit calculator, The Daily Groomer](https://thedailygroomer.beehiiv.com/p/mobile-groomers-profit-calculator): 5 dogs/day × $125 × 22 days worked example
- [How much capital does a mobile pet grooming van really need, Financial Models Lab](https://financialmodelslab.com/blogs/business-insights/mobile-pet-grooming): $115–170 assumed ticket range; capital context
- [How much does it cost to start a mobile dog grooming business, Wexford Insurance](https://www.wexfordins.com/post/how-much-does-it-cost-to-start-a-mobile-dog-grooming-business): startup cost range
- [Mobile dog grooming start-up costs, PetExec](https://petexec.net/resources/business-operations/mobile-dog-grooming-start-up-costs): startup and van cost ranges
- Per-van revenue benchmark ($8,000–15,000/month) and van price ranges: taken from search summaries of [Pulse RevOps KPI guide](https://pulserevops.com/industry-kpis/ik0271) and the sources above. I did not open these pages, so treat them as rough.
- **Gap:** no groomer pay benchmark was found.

## SUCCESS-TEST

- Labels intact: pass. Every element is V or H, and all owner inputs are H.
- Coherence pass done, contradictions logged: pass.
- Top 5 assumptions carry experiments, cheapest-first: pass.
- No V element without an evidence ref: pass. There are no V elements.

Steps run inline (sub-skills not invoked): task contract, research, red-team, decide, summarize and verify. Research was two search runs. Groomer wages were not found.

## JAIL-HANDOFF

```
decision: hold van 3; gate on A1 + A4 (+ groomer hire)
canvas: 9 blocks, all H (owner-reported); no V elements
key_numbers: 310 cust | $95 | 224 grooms/mo | $21,270 rev/mo | $19,000 cost (2 vans) | +$2,269 margin (v=$0), −$1,089 (v=$15)
unit: $68.61 rev/customer/mo; breakeven 100–119 grooms/van/mo; current 112; density 5.1/van/day
third_van: −$7,231/mo if no new customers; ~+$3,400 if 465 customers at $95 and $0 variable cost; −$1,633 at $15 variable
experiments: A1 cost reconciliation → A2 retention → A4 unbookable inquiries → A3 $110 price test → A5 groomer trial (if A4 passes)
open: $9,500 cost basis; retention; add-on revenue; owner pay; groomer wages; working days/week
```

Want me to save this canvas to the project, or hand the price test (A3) to jail-lab?