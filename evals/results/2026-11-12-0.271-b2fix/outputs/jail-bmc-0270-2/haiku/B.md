**Wrong-lane check:** This is a business model canvas, so jail-bmc is the right skill. I ran the unit economics and coherence checks myself and did not pull outside pricing or cost benchmarks.

## What the numbers say

On your stated figures, each subscriber contributes **$48/month** after cost to serve (54% margin). At 3% monthly churn, the average customer stays about 33 months, so **LTV is about $1,600** against a **$240 CAC: about 6.7x, with a 5-month payback.** That is a strong subscription unit on paper.

Three things could change that picture, and an investor will test all three first:

1. **Your $240 blended CAC may hide a paid-channel CAC near $480.** About half your customers come from referrals and yard signs. If those cost little, the other half costs about $480 each. That gives LTV:CAC of about 3.3x and a 10-month payback for paid channels.
2. **It is unclear whether the $41 cost to serve includes your own time.** Your 15 hours a week is about 65 hours a month. At a $30/hour value, that is about $2,000 a month, or roughly $9.25 per customer. If it is excluded, your real margin is lower.
3. **One price and one cost are applied to three different customer types.** HOA shared pools and motels probably differ from single-family pools in visit frequency, billing unit, and seasonality.

Everything above is contribution per customer, not profit. Office, insurance, vehicles, software, and overhead are not in your figures, so you cannot yet show net margin.

## Derived figures
- Revenue run rate: 212 × $89 = **$18,868/month** (about $226k/year)
- Cost to serve: 212 × $41 = $8,692/month
- Contribution: 212 × $48 = **$10,176/month**
- Implied new customers: about **14/month** (to grow 40 → 212 with 3% churn), so acquisition spend is about **$3,400/month**
- Implied customers lost to churn so far: about **65**

## Sensitivity (LTV:CAC; payback in months)

| Scenario | LTV | LTV:CAC at $240 | LTV:CAC at $480 | Payback at $240 / $480 |
|---|---|---|---|---|
| Base: 3% churn, $41 cost | $1,600 | 6.7x | 3.3x | 5.0 / 10.0 |
| Churn 5% | $960 | 4.0x | 2.0x | 5.0 / 10.0 |
| Churn 2% | $2,400 | 10.0x | 5.0x | 5.0 / 10.0 |
| Cost to serve $50 (3% churn) | $1,300 | 5.4x | 2.7x | 6.2 / 12.3 |

## The canvas

**Labels:** V = validated, backed by a checkable evidence ref. H = hypothesis. **Evidence ref O1** = your 18-month figures as you reported them. Nothing has been checked against billing or the ledger yet, so every V item below rests on your word and should be confirmed by your accountant.

| Block | Element | Label | Evidence ref | Confidence |
|---|---|---|---|---|
| Customer segments | Single-family homeowners with in-ground pools (~68%, ≈144) | V | O1 mix | Medium |
| Customer segments | HOA/condo shared-pool communities (~22%, ≈47) | H | O1; billing unit (per community or per unit) unknown | Low |
| Customer segments | Small motels and B&Bs (~10%, ≈21) | H | O1; seasonality unknown | Low |
| Value propositions | Recurring pool service for one fixed fee ($89/month) | V | O1 price; O1 retention | Medium |
| Value propositions | Homeowners: a clean pool without managing it | H | None; inferred from retention | Low |
| Value propositions | HOAs and motels: one vendor, scheduled and documented care | H | None; not tested | Low |
| Channels | Neighbor referrals and yard signs (~50%) | V | O1 source mix ("roughly") | Medium |
| Channels | Google Maps and local search (~33%) | V | O1 source mix | Medium |
| Channels | Pool-supply store partnership (~17%) | V | O1 source mix | Medium |
| Channels | Cost per customer by channel | H | None; only blended $240 given | Low |
| Customer relationships | Monthly subscription with route-based visits | V | O1 price and churn | Medium |
| Customer relationships | Service quality driving retention | H | None; no churn reasons | Low |
| Revenue streams | Subscription fees: 212 × $89 = $18,868/month | V | O1 count and price; D1 | Medium (high once billing matches) |
| Revenue streams | Add-on repairs and parts billed to customers | H | None; parts are in cost but no parts revenue given | None |
| Key resources | Two technicians plus you | V | O1 headcount | High |
| Key resources | Trucks, chemicals, parts | V | O1 cost lines | Medium |
| Key resources | Your ~15 hours/week of route work (key-person dependency) | V | O1 | High |
| Key activities | Scheduled route service | V | O1 (212 active) | Medium |
| Key activities | Lead generation: referrals, signs, local search, partner program | V | O1 channel mix | Medium |
| Key activities | Churn prevention | H | None | None |
| Key partnerships | Pool-supply store referrals (~17% of customers) | V | O1 source mix | Medium |
| Key partnerships | Store terms: fees, exclusivity, continuity | H | None | None |
| Key partnerships | Chemical and parts suppliers | H | None named | None |
| Cost structure | Cost to serve $41 × 212 = $8,692/month | H | O1 stated; composition unknown | Low |
| Cost structure | Blended CAC $240 (≈14 new/month ≈ $3,400/month) | H | O1 stated; D1 implied adds | Low |
| Cost structure | Fixed overhead (office, insurance, software, your pay) | H | Not provided | None |

## Internal inconsistencies (coherence pass)
1. **Blended CAC vs. channel mix.** A $240 blend with half the customers free implies paid CAC near $480. Confirm whether referral and sign costs are in the $240.
2. **Uniform price and cost across three segments.** A single $41 cost cannot be right for both a homeowner and a shared-pool HOA until you split it.
3. **Owner time.** Either the $41 includes your route hours, or the margin is overstated by about $2,000/month at $30/hour.
4. **Parts cost with no parts revenue.** Your cost includes parts, but your revenue shows only subscriptions. Either parts are absorbed or revenue is missing.
5. **Scale.** You have not stated visits per customer per month or stops per technician per day, so growth capacity is unknown.
6. **Seasonality.** An 18-month average can hide a winter or season-close churn spike. This is untested.

## Customer-side risks (red team)
- **HOA boards** approve slowly, rebid contracts, and can lose you when the board turns over.
- **Motels** may cut pool service in slow seasons.
- **Google CAC** rises as competitors bid on the same local terms.
- **Yard-sign referrals** saturate a neighborhood, so that channel has a ceiling.
- **Pool-supply partnership** carries about 17% of new customers and can be renegotiated or ended.
- **Price or visit-frequency cuts** to lower cost could raise churn past the break-even point.

## Riskiest assumptions and experiments (cheapest and most decisive first)

| # | Assumption | Impact if wrong | Experiment: metric · one variable · bound · pass/fail |
|---|---|---|---|
| E1 | $41 is fully loaded (owner time, vehicle, insurance) | Very high | Cost per customer · cost composition · last 3 months of books, your accountant · pass if $41 holds within ±$5 with labor at market rates; fail if >$50 |
| E2 | Churn is about 3% in each segment, including winter | High | Monthly churn by segment · none (data pull) · 18 months of billing export · pass if each segment ≤4%/month and no winter spike above 2×; fail if any segment ≥5% |
| E3 | Paid-channel CAC is ~$240, not ~$480 | High | CAC by channel · source tag on every sign-up and spend booked by channel · 60 days · pass if paid CAC ≤$320; fail if ≥$480 |
| E4 | HOA and motel accounts earn the same contribution per customer | Medium (21–47 accounts) | Segment contribution margin · segment · 5 HOA and 5 motel routes, 30 days · pass if ≥40%; fail if <30% |
| E5 | Current crew can absorb growth to ~250 customers | Medium | Stops per tech per day · none · one logged week · pass if ≥20% headroom at 250; fail if below |

## Customer validation questions
- **Churned homeowners:** Why did you stop? Price, service quality, or a seasonal close?
- **HOA boards:** Who signs, how often do you rebid, and do you pay per community or per unit?
- **Motels and B&Bs:** Is your pool use seasonal? Do you prepay?
- **Referrers:** What exactly do you tell neighbors, and what does it cost you?

## Strategic implications and next actions
The subscription looks sound on your numbers, but the figures an investor will test first are the ones not yet verified: cost-to-serve composition, paid CAC, and segment margin. Before anyone else sees this canvas:
1. **Accountant:** reconcile $41 and $240 against the ledger (E1, and the spend side of E3).
2. **Billing:** export 18 months of customers by month and segment, with cancellation reasons (E2).
3. **Starting now:** tag every new customer with a source and book spend to it (E3).
4. **This month:** log one week of route time (E5).
5. **After E4:** decide whether HOA and motel pricing needs its own structure.

I also recommend a market check on Long Island pool-service pricing and competitor rates. Say the word and I'll run that through jail-research.

## Sources and labels
- **O1:** your 18-month figures as you reported them, 2026-11-12. Not audited.
- **D1:** derived figures from O1 using the formulas above: contribution = price − cost; lifetime = 1 ÷ churn; LTV = contribution × lifetime; payback = CAC ÷ contribution; implied adds from the 40 → 212 growth at 3% churn.
- **Judgment:** an LTV:CAC of 3x or more is a common rule of thumb, not a benchmark validated for your business.
- **Not included:** external benchmarks, competitor pricing, and Long Island market data.

---

**Delivery note:** This is a working copy with labels intact. For your accountant and investor, I can render it as a one-page layout with V/H badges, or as a clean document. Before the investor version goes out, the E1–E3 results should be in, so the canvas can move from hypothesis toward validated.

<details><summary>JAIL-HANDOFF</summary>

```
decision: investor/accountant-ready canvas for a monthly pool-service subscription, Long Island
stage: operating (18 months of data)
state: canvas v1 built, 9 blocks labeled V/H, coherence pass done (6 contradictions logged), 5 assumptions ranked, E1–E5 specified
evidence: O1 owner-reported, unaudited; D1 derived
assumptions_ranked:
  1. $41 cost to serve is fully loaded (very high impact)   -> E1
  2. Paid-channel CAC ≈ $240, not ≈ $480                    -> E3
  3. Churn ≈ 3% in each segment, including winter           -> E2
  4. HOA/motel economics equal single-family                -> E4
  5. 2 techs + owner absorb growth to ~250                  -> E5
unknowns: overhead, visit frequency, HOA billing unit, seasonality, channel spend, parts revenue
success_test:
  labels intact: pass
  coherence pass: pass
  experiments attached, cheapest first: pass
  V items lack checked evidence refs: CAVEAT. Revenue and churn V labels rest on O1 until billing export is pulled. Demote to H if billing does not tie to 212 × $89.
skills_next: jail-research (LI pricing comps), jail-summarize (investor one-pager), jail-verify before investor use
```

</details>