# JAIL-BMC: Mobile Dog-Grooming, 2 Vans → Third Van?

**Bottom line: not yet.** The third van only pays if you can add about 139 new regular customers, a 45% jump in your base. Your current numbers don't show whether that demand exists. Run the cheap tests below first.

*Caveats: no external benchmarks were researched, so none are cited. Figures marked V are your own numbers, taken as given. I haven't seen the records, so check them against your booking system or bank before relying on them.*

## Unit economics (derived from your figures)

| Metric | Value |
|---|---|
| Revenue per customer | $95 × 52/6 ÷ 12 = **$68.61/month** ($823/yr) |
| Total revenue | 310 × $68.61 = **$21,269/month** |
| Van + groomer cost | 2 × $9,500 = **$19,000/month** |
| **Contribution** | **$2,269/month (10.7%)**, before owner pay, marketing, insurance or admin, unless your $9,500 already includes them |
| Per van | 155 customers, about 26 grooms/week (about 5.2/day over 5 days), $10,634 revenue, $1,134 margin |
| **Break-even per van** | $9,500 ÷ $68.61 = **139 customers** (about 4.6 grooms/day) |
| Third van at today's 310 customers | $21,269 − $28,500 = **−$7,231/month**. A van splits existing customers; it doesn't create revenue. |
| Third van matching today's per-van margin | **155 new customers** |

**Ramp loss if van 3 launches empty** (cash burned until break-even, ignoring churn):

| Net new customers/month | Months to break-even | Cumulative loss |
|---|---|---|
| 8 | 17 | about $82k |
| 12 | 11.5 | about $55k |
| 20 | 7 | about $33k |

## The canvas

| Block | Element | Label | Evidence ref | Confidence |
|---|---|---|---|---|
| Segments | 310 regular recurring clients | V | Owner-reported; check the booking export | High |
| Segments | Who they are (home type, dog size, multi-dog, age of owner) and service radius | H (none) | Not provided | Low |
| Value prop | Convenience: groomer comes to you | H (weak: 310 repeat clients suggest it, but there's no direct evidence) | Retention proxy only | Medium |
| Value prop | Calmer dog, one-on-one care | H (none) | None | Low |
| Channels | How new clients arrive (referral, Google, Nextdoor, vets) | H (none) | Not provided | Low |
| Channels | Recurring booking, rebooked at about 6-week intervals | V | Owner-reported cadence | Medium |
| Relationships | Personal bond with the groomer drives retention | H (none) | None | Low |
| Revenue | $95 average per groom | V | Owner-reported | High |
| Revenue | $21.3k/month total | V (derived) | Arithmetic from the above | High |
| Revenue | Tips and add-ons not included | H | Not stated | Low |
| Resources | 2 equipped vans | V | Owner-reported | High |
| Resources | Groomers who stay and can be replaced; a third hire is available | H (none) | None | Low |
| Activities | Grooming, route and schedule density | H (no utilization or drive-time data) | None | Low |
| Activities | Customer acquisition at a pace of 10+ net new/month | H (none) | None | Low |
| Partnerships | None stated (vets, rescues, upfitter, groomer pipeline) | H | None | Low |
| Cost | $9,500/van/month | V | Owner-reported | High |
| Cost | What's inside the $9,500 (owner pay, insurance, marketing, software, supplies) | H | Unknown | Low |
| Cost | Fixed vs variable split (groomer on commission or salary) | H | Unknown | Low |

## Contradictions and findings

1. **Thin margin vs growth plan.** A 10.7% contribution before owner pay and overhead leaves little room to absorb a $55–82k ramp loss.
2. **Capacity claim is unsupported.** Expanding implies the vans are full or you're turning people away. About 5.2 grooms/day per van is plausible but unverified.
3. **Segment is unnamed.** You can't pick a channel for van 3 until you know who your 310 are and where they live.
4. **Value prop depends on groomer quality, and that's a hypothesis.** A third van needs a third strong groomer, and nothing shows you can hire one.
5. **Pricing may be the cheaper lever.** A +$10 increase (to $105) adds about $2,240/month at 310 customers, the same as about 33 new customers, with no van.

## Red-team points

- **Referral saturation:** word of mouth from the first 310 clients may run out, so acquisition cost jumps once you grow past your network.
- **Route density:** a third van in a thin territory adds drive time, which cuts grooms per day and raises cost per groom.
- **Customer shuffling:** moving existing clients across three vans changes nothing in revenue.
- **Groomer risk:** one groomer leaving leaves a van with fixed costs and no revenue, and nothing here says how you'd cover it.
- **Seasonality:** shedding seasons and holidays may be skewing your 6-week average.
- **Competitor response:** salons or a mobile competitor could cut prices when you enter new territory.

## Top assumptions, ranked, with experiments (cheapest first)

| # | Assumption | Experiment (metric · one variable · bound · pass/fail) |
|---|---|---|
| 0 | Your base figures are correct (free) | Pull 12 months of bookings, then compute net new customers/month, churn and the real rebook interval. **Pass:** ≥10 net new/month and ≥85% 6-month retention. |
| 1 | The vans are capacity-constrained | For 4 weeks, log next-available appointment lead time and every inquiry you turned away. Cost: $0. **Pass:** lead time >3 weeks, or ≥25 turned-away inquiries. |
| 2 | Price headroom ($95 → $105) | Quote $105 to new customers only for 4 weeks. **Pass:** booking conversion drops <10% vs the $95 baseline. |
| 3 | Unserved demand of 139+ customers in the target area | 60-day waitlist or deposit campaign in the proposed van-3 zip codes, with ad spend capped at about $1,500. **Pass:** ≥60 deposits or signed commitments. |
| 4 | You can hire and keep a third groomer | Post a role and talk to candidates. **Pass:** one qualified candidate at or below budgeted pay. Run this only if #1 and #3 pass. |

The thresholds are my proposals; adjust them to your risk tolerance. These specs are written for **jail-lab**, but the lab skill wasn't run here.

## Decision

| Option | Result |
|---|---|
| Do nothing | Stays at about $2.3k/month contribution, with no ramp risk |
| Third van now | Loses $33–82k before break-even if demand is unproven, and is hard to reverse |
| **Fix pricing and utilization first (recommended)** | Run experiments #0–#2 (about 6 weeks, near-zero cost). Raising price may bring more than a van would. |
| Staged expansion | If #1 and #3 pass, add a part-time groomer or extra days before buying a van. Buy van 3 once the waitlist is ≥100 customers. |

**Confidence:** high on the arithmetic, medium on the recommendation, because demand and capacity are unknown. **What would change it:** lead times over 3 weeks, a waitlist of 100+ and 12+ net new customers/month sustained would move this to "go."

## Questions to ask your customers

- How long did you wait for your first appointment?
- Would you pay $105? At what price would you switch to a salon?
- Who have you referred, and who would you refer?
- Would you stay if your groomer changed?

## Next actions

1. This week: export 12 months of bookings (experiment #0) and confirm what's inside the $9,500.
2. Start the lead-time and turned-away log, and quote $105 to new clients.
3. In 6 weeks, review the results and decide whether to run the zip-code demand test.

**SUCCESS-TEST:** labels are intact, the coherence pass is done, the top 5 assumptions have experiments, and every V row cites an owner-reported ref that you can check. The one caveat is that these are not external records.

**JAIL-HANDOFF:** the next step is **jail-lab** for experiments #0–#3 (or a canvas-delta pass once results land). Open items are the unknown contents of the $9,500, the segment definition, and the acquisition channel mix.

If you'd like, I can save this to the Business Consulting Tools project. I didn't, because it looks like your own business rather than a client deliverable.