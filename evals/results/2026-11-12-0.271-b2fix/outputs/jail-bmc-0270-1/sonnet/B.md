# Business Model Canvas: Monthly Pool-Equipment Subscription, Long Island

**Wrong-lane check:** this is a canvas request, so it stays in jail-bmc.
**Contract:** a pre-revenue idea with no customers. The decision it serves is whether to spend on a pilot. The inputs in hand are the $89/mo price, monthly visits, residential pools and Long Island, all **User-provided**. Nothing else is known.

**No element below is VALIDATED.** There are no transactions, signed customers or measured data, so everything defaults to HYPOTHESIS. Where outside comparables exist they are national and weak, and they are tagged that way.

## Timing finding
Today is Nov 12, 2026, which is off-season. One guide puts the Long Island season at about May to October, with pools closing in mid to late October [S4]. Two consequences:
- You can't measure real cost to serve on live pools until spring 2027.
- You can pre-sell now for a May start. Demand and channel tests run in winter; cost tests run in spring.

## 1. Canvas

| Block | Element | Label (V/H) | Evidence ref | Confidence |
| :-- | :-- | :-: | :-: | :-: |
| Customer segments | Owners of in-ground pools in Nassau/Suffolk single-family homes who already pay for an opener/closer | H | none | L |
| Customer segments | Owners of above-ground pools (may not need equipment checks) | H | none | L |
| Value propositions | Pump, filter, heater and salt cell checked monthly, so failures are caught before they cost a season | H | none | L |
| Value propositions | One flat price, no surprise quotes for covered checks | H | none | L |
| Channels | Google Local Services ads | H | none | L |
| Channels | Referrals from openers/closers and pool-supply stores | H | none | L |
| Customer relationships | Text reminder before each visit, photo report after | H | none | M |
| Revenue streams | $89/mo subscription, card billing | H | weak: national comparables [S1][S2] | L |
| Revenue streams | Repair and parts upsell, billed per job | H | none | L |
| Key resources | Seasonal technicians, one van, parts stock | H | none | M |
| Key activities | Route scheduling, monthly equipment inspection, repair follow-up | H | none | M |
| Key partnerships | Pool-supply wholesaler for trade-price parts | H | none | L |
| Cost structure | Technician labor, supplies, vehicle, insurance, ad spend | H | none | L |

## 2. Internal inconsistencies

1. **Price versus the comparables (Fact from [S1][S2], national).**
   - Weekly cleaning averages about $86/mo nationally [S1].
   - Monthly-visit plans run $30–$90/mo on annual contracts [S2].
   - $89 sits at the top of the monthly-visit band and matches a weekly cleaning price.
   - Unless the owner sees the equipment check as a different product from cleaning, they will compare the two.
   - Long Island prices are likely at or above national, but I found no source that confirms this (Unknown).
2. **"$89/mo" versus a six-month season.**
   - The model doesn't say whether you bill 12 months or only in season.
   - This one choice swings the economics from healthy to broken (see section 3).
3. **Labor is listed as a variable cost, but the work is seasonal.**
   - Technicians would be idle November to April unless you add opener/closer or winter work.
   - Route density is Unknown with zero customers.
4. **Segment mismatch.** Above-ground owners likely have simpler equipment, so the proposition may not fit them. Judgment, low confidence.
5. **Licensing is Unknown.** I did not verify NY and county licensing for equipment work, such as electrical or gas heater service. Check before you sell repairs.

## 3. Unit economics (every input is HYPOTHESIS; results are Estimates)

| Input | Value | Label / strength |
| :-- | --: | :-- |
| Price | $89/mo | H (User-provided) |
| Service visits per year | 6 (May–Oct) | H, weak [S4] |
| Cost per visit: labor and drive 1.5 h × $38 loaded | $57 | H, none |
| Cost per visit: supplies | $8 | H, none |
| Cost per visit: vehicle | $6 | H, none |
| **Cost per visit** | **$71** | H |
| Annual churn | 30% | H, none |
| CAC | $300 | H, none |
| Annual discount rate | 10% | H, chosen |

Annual cost to serve is 6 × $71 = **$426**. Lifetime is 1 ÷ 0.30 = **3.3 years**.

| | A: bill 12 months | B: bill in season only (6 months) |
| :-- | --: | --: |
| Revenue per year | 89 × 12 = $1,068 | 89 × 6 = $534 |
| Margin per year | 1,068 − 426 = **$642** (60%) | 534 − 426 = **$108** (20%) |
| LTV, undiscounted | 642 × 3.33 = $2,140 | 108 × 3.33 = $360 |
| LTV, discounted (margin ÷ (0.10 + 0.30)) | $1,605 | $270 |
| LTV:CAC, undiscounted / discounted | 7.1 / 5.4 | 1.2 / 0.9 |
| CAC payback | 300 ÷ 642 = 0.47 yr (about 5.6 months) | 300 ÷ 108 = 2.8 yr |

The discounted figure uses an annual-period approximation of the worksheet formula.

**Judgment:** the model only works if owners accept 12 monthly payments for about six months of service (A).
- On in-season-only billing (B), you would need about **$116/mo** to reach LTV:CAC of 3. That is (426 + 270) ÷ 6.
- On 12-month billing, a price near **$58/mo** reaches the same ratio, so $89 has room to spare there.
- Billing structure is therefore the riskiest assumption, not price.
- Fixed costs (insurance, software, van payment) are not included, so I can't state a break-even customer count yet. That is Unknown.

## 4. Red-team attacks
- **The segment that won't pay:** owners who pay an opener/closer may see equipment checks as part of that service, and refuse to pay twice.
- **The channel that doesn't reach them:** Long Island local-services ad costs are Unknown, and the ad-cost hypothesis is the weakest input. Referrals from openers/closers are a dependency risk, because those firms can add the same service themselves.
- **Second-order response:** incumbents can bundle a monthly check into an existing contract at near-zero marginal cost.
- **Winter billing:** charging for months with no visits invites churn and card disputes. A written plan for what the customer gets in winter would help.

## 5. Top risky assumptions and experiments

Ranked by impact if wrong × evidence weakness. Sequenced cheapest and most decisive first.

| # | Assumption | Experiment (metric · variable · bound · pass) |
| :-- | :-- | :-- |
| 1 | Owners accept 12-month billing for a seasonal service at $89 | **Metric:** signed or deposit-backed May-start commitments, higher is better. **Variable:** the offer page (12 payments of $89). **Bound:** 40 in-ground owners reached via openers/closers and local groups, 30 days, $0 ad spend. **Pass:** 6 or more commitments. |
| 2 | In-ground owners buy an equipment check, separate from the opener/closer | **Metric:** share of 15 owner interviews who say they'd pay and name a current spend. **Variable:** the interview script. **Bound:** 2 weeks, $0. **Pass:** 5 or more of 15 say yes, and at least 3 of those yes answers come with a current-spend figure, as the lowest-effort proof of intent. Run it alongside #1. |
| 3 | CAC is $300 or less | **Metric:** ad spend ÷ commitments, lower is better. **Variable:** one Google Local Services campaign. **Bound:** 45 days, $1,000. **Pass:** CAC at or below $300. |
| 4 | Cost to serve is $71 or less per visit | **Metric:** measured labor + supplies + vehicle per visit, lower is better. **Variable:** a real visit routine. **Bound:** 10 friendly pools, May 2027, about $500 of owner time. **Pass:** average at or below $71. Can't run before spring. |
| 5 | Annual retention is 70% or higher | **Metric:** customers retained after the first full season. **Pass:** 70% or more. Needs customers, so it runs last. |

## 6. Customer validation questions
- Who services your pool equipment today, and what do you pay per year?
- What failure cost you the most in the last two seasons?
- Would you pay $89 a month for 12 months, or a seasonal price? Why?
- Would you expect an equipment check to come with your opener/closer?

## 7. Implications and next actions
1. Don't spend on a pilot until experiments 1 and 2 pass. They cost close to nothing and fit the winter window.
2. Decide the billing structure before anything else. 12-month billing makes $89 work, while in-season billing makes it fail on these inputs.
3. Get 2–3 local Long Island quotes for monthly and weekly service to replace the national comparables.
4. Confirm licensing and insurance requirements before offering repairs.
5. Re-run this canvas in delta mode after the experiments, using real data.

## SUCCESS-TEST
- Labels intact: 13 of 13 elements labeled. Pass.
- Coherence pass done, 5 contradictions logged. Pass.
- Top assumptions carry experiments, cheapest first. Pass.
- No VALIDATED element lacks a ref: none are VALIDATED. Pass.

## Sources
Accessed 2026-11-12. Search snippets only; I did not open the pages, and publication dates were not shown. All figures are national estimates, not Long Island data.
- [S1] [Thumbtack pool maintenance cost](https://www.thumbtack.com/p/pool-maintenance-cost): weekly cleaning about $86/mo, range $80–$200.
- [S2] [Fixr pool maintenance cost](https://www.fixr.com/costs/swimming-pool-maintenance): $30–$90/mo on annual contracts with monthly visits.
- [S3] [Swimply 2026 pool service cost guide](https://swimply.com/hostblog/post/swimming-pool-service-cost-in-2026-full-price-guide): weekly $150–$350+/mo, biweekly $100–$250+/mo.
- [S4] [Swimply 2026 New York pool owner's guide](https://swimply.com/hostblog/post/2026-new-york-pool-owners-guide-costs-care-more): Memorial Day to Labor Day season, closing mid to late October (vendor blog, rough guidance).
- I excluded a "Local Test Long Island" site that looked like a placeholder with no prices.
- I found no count of Long Island residential pools. The market size is Unknown.

```yaml
JAIL-HANDOFF:
  skill: jail-bmc
  status: complete
  facts: ["Price $89/mo, monthly visits, residential pools, Long Island, no customers (all user-provided)", "National comparables: weekly cleaning about $86/mo [S1]; monthly-visit plans $30-$90/mo [S2]"]
  assumptions: ["Owners accept 12-month billing for a seasonal service", "Cost to serve is $71 per visit", "CAC is $300", "Annual churn is 30%", "In-ground owners buy equipment checks separately from opener/closer"]
  unknowns: ["Long Island pool count", "Local pricing", "Route density", "NY and county licensing", "Fixed costs and break-even customer count", "Local ad costs"]
  outputs: ["Nine-block canvas, all HYPOTHESIS", "Estimate: LTV:CAC 7.1 undiscounted / 5.4 discounted on 12-month billing; 1.2 / 0.9 on in-season-only billing", "Five ranked experiments"]
  risks: ["Economics depend on 12-month billing for about 6 months of service", "Price matches weekly cleaning, so the value proposition must differ clearly", "Cost-to-serve test can't run until spring 2027"]
  confidence: low
  next: jail-lab
  approval_required: ["Contacting owners for experiments 1 and 2", "Spending ad budget on experiment 3"]
```

I can also render this as a one-page visual canvas, or save it to your Business Consulting Tools project as a doc. I haven't done either.