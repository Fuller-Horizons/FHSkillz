**Wrong-lane check:** this is a business model canvas, so jail-bmc applies. I ran the chain inline (task contract, research, red-team, decision, and verify steps) using each step's fallback, since no sub-skills were invoked.

## Task contract (inline)
- **Venture:** monthly on-site pool-equipment check subscription, Long Island (Nassau and Suffolk).
- **Stage:** idea. No customers, no revenue.
- **Decision served:** whether to fund a 20-customer pilot.
- **In hand:** the $89/mo price and the region (User-provided).
- **Missing:** customer data, cost data, channel data, and any evidence that owners will pay.

## Market comparables (what the research found)
These are contractor marketing pages and vendor blogs. They support a price range. They do not validate this offer.

| Comparable | Price | Source | Reliability |
| :-- | :-- | :-- | :-: |
| Monthly check-up, DIY-chemistry owners, Long Island | from $150/mo | [S1] | Low |
| Weekly maintenance, chemicals included, Nassau/Suffolk | $120–180/mo | [S2], [S3] | Low |
| Weekly maintenance, same firm's other page | $175–350/mo | [S3] | Low |
| NY monthly pool service, aggregator range | $275–550/mo | [S4] | Low–medium |
| DIY chemicals and supplies | $70–130/mo | [S4] | Low–medium |
| Cost per residential visit | $25–44 vs. $80–150 (about 3x apart) | [S5] | Low |

No 2026 Long Island price survey for monthly equipment-only checks turned up. The closest comparable is the $150 DIY check-up.

## The nine-block canvas

V = VALIDATED (needs an evidence ref). H = HYPOTHESIS. No element is VALIDATED, because there are no transactions, commitments, or measured results.

| Block | Element | Label(V/H) | Evidence ref | Confidence |
| :-- | :-- | :-: | :-: | :-: |
| Customer segments | Owners of in-ground pools, single-family homes, Nassau/Suffolk, who handle their own chemistry | H (comparable-based) | [S1], [S4] | L |
| Customer segments | Owners who pay weekly service but want an equipment-only check | H | none | L |
| Value propositions | Monthly on-site check of pump, filter, heater, and salt cell, with a photo report | H (comparable-based) | [S1] | L |
| Value propositions | One flat monthly price; repairs quoted separately | H | none | L |
| Channels | Google local search ads | H | none | L |
| Channels | Referrals from pool openers and closers | H | none | L |
| Customer relationships | Reminder text before each visit, photo report after, one-tap repair approval | H | none | M |
| Revenue streams | $89/mo subscription, card billing | H (User-provided price; comparable range only) | [S1]–[S3] | L |
| Revenue streams | Repair and parts billed per job | H | none | L |
| Key resources | Trained technicians (count TBD), one van, parts stock | H | none | M |
| Key resources | Licensing and insurance for heater (gas/electric) work | H | Unknown | L |
| Key activities | Route scheduling, monthly inspection, photo reporting, repair follow-up | H | none | M |
| Key partnerships | Referral agreements with pool openers and closers | H | none | L |
| Key partnerships | Parts wholesaler at trade price | H | none | L |
| Cost structure | Cost to serve about $61/visit (1.25 h at $40/h loaded, $8 mileage, $3 supplies) | H | none; wage not sourced | L |
| Cost structure | Fixed overhead about $1,500/mo (van, insurance, software, phone, bookkeeping) | H | none | L |
| Cost structure | CAC about $250 | H | none | L |

## Coherence pass: findings (not smoothed over)
1. **Price sits below the one direct comparable.** $89 is 40% under the $150 DIY monthly check-up [S1]. Either it is a deliberate entry price or it leaves thin margin. The pricing decision was made before cost to serve was measured.
2. **Overlap with bundled service.** Weekly-service firms already include equipment checks inside $120–180/mo [S2], [S3]. The offer only holds up if it is sold as equipment-only, with no chemicals. That makes the segment owners who already handle chemistry themselves, which is a narrower group than "pool owners."
3. **Unit economics depend on an unstated labor model.** If technicians are paid per visit, the $28 margin covers about 54 subscribers of fixed overhead. If a technician is salaried (about $5,800/mo loaded, Estimate, wage not sourced), the break-even rises to about 94 subscribers. That needs about 70% of one technician's capacity at 6 stops per day. The model has to name which one it uses.
4. **Seasonality.** Launching in November means the pool is closed and there is little to find. The pilot should start in spring (Judgment).
5. **Licensing is Unknown.** Heater work can require licensed or insured trades in New York. If it does, cost to serve rises and the labor model changes.
6. **Cost-per-visit benchmarks conflict about 3x** [S5], so cost to serve cannot be benchmarked yet.

## Unit economics

Inputs (all HYPOTHESIS): price $89 (User-provided); cost to serve $61 (weak; wage not sourced); churn 4%/mo (none); CAC $250 (none); discount rate 10%/yr (chosen).

| Step | Calculation | Result |
| :-- | :-- | --: |
| Margin per month | 89 − 61 | $28 (31%) |
| Expected lifetime | 1 ÷ 0.04 | 25 months |
| LTV, undiscounted | 28 × 25 | $700 |
| LTV, discounted | 28 ÷ (0.00797 + 0.04) | $584 |
| LTV:CAC, undiscounted | 700 ÷ 250 | 2.8 |
| LTV:CAC, discounted | 584 ÷ 250 | 2.3 |
| CAC payback | 250 ÷ 28 | 8.9 months |

**Sensitivity to cost to serve** (price $89, churn 4%, CAC $250):

| Cost per visit | Margin/mo | LTV (undiscounted) | LTV:CAC | Payback |
| --: | --: | --: | --: | --: |
| $40 | $49 | $1,225 | 4.9 | 5.1 mo |
| $61 | $28 | $700 | 2.8 | 8.9 mo |
| $80 | $9 | $225 | 0.9 | 27.8 mo |

**What closes the gap to LTV:CAC of 3** (one lever at a time, Estimate):
- Price of about **$91** at the other base inputs.
- CAC of about **$233**.
- Churn of about **3.7%**.
- Cost to serve **below about $66** on its own.

Judgment: at $119 with the same base inputs, margin is $58 and LTV:CAC is about 5.8. That is the case for testing a higher price (A2 below).

## Attack points (inline red-team)
- **Segment that won't pay:** owners already on weekly service. They see the check as included.
- **Channel that doesn't reach them:** a seasonal service on Google local ads may cost more than $250 per customer.
- **Partnership as dependency:** openers and closers may expect a referral fee, which becomes a second cost, or may simply not refer.
- **Second-order response:** a weekly-service firm adds an $89 equipment-only tier, or bundles monthly checks at no extra charge.

## Top risky assumptions and validation experiments (jail-lab spec shape)
Ranked by impact if wrong × evidence weakness. Cheapest and most decisive first.

1. **Cost to serve is $61 or less per visit.** Impact high, evidence none.
   - Metric: fully loaded minutes and dollars per visit (lower is better).
   - Variable: a written visit routine and route.
   - Bound: 10 timed visits, 2–3 weeks, about 15 hours of owner time.
   - Pass: at or below $61 and at or below 75 minutes including drive.
2. **Owners will pay $89/mo for an equipment check.** Impact high, evidence none.
   - Metric: signed 3-month prepaid commitments ÷ owners contacted.
   - Variable: the $89 offer page. Run 10 owner interviews first.
   - Bound: 30 days, 40 owners reached through 5 openers or closers.
   - Pass: at least 6 of 40 (15%).
3. **CAC is $250 or less via local search ads.** Impact high, evidence none.
   - Metric: ad spend ÷ signed customers (lower is better).
   - Variable: one Google local campaign at $89.
   - Bound: 45 days, $1,500.
   - Pass: at most $250 (at least 6 signed). Six customers is a small sample; treat as directional.
4. **Churn is 4% a month or less.** Impact medium, evidence none. Runs last because it needs customers.
   - Metric: cancellations per subscriber-month.
   - Variable: a pilot cohort of 20.
   - Bound: 3 months, 60 subscriber-months.
   - Pass: 2 or fewer cancellations (about 3.3%).

Sequence: 1 and 2 (interviews) first, then 3, then 4. Experiments 2 and 3 involve contacting people and spending money, so they need your approval.

## Customer validation questions
1. Who checks your pool equipment today, and what do you pay per year?
2. Would you pay monthly for a check that does not include chemicals? Why or why not?
3. Which failure cost you the most in the last two seasons?
4. Would you pay $89 a month? Would $119 change your answer?
5. Would you put a card on file before you see the first report?

## Strategic implications and next actions
- **Do not fund a pilot yet.** Pass experiments 1 and 2 first. Both are cheap.
- **Settle the labor model** (per visit or salaried) before any price is committed.
- **Decide on the price.** If experiment 1 holds at $61, test $119 against $89 instead of assuming $89 is right.
- **Sell equipment health, not pool service.** The product has to differ from the weekly-service bundle.
- **Start the pilot in March or April,** not in winter.
- **Check licensing and insurance** for heater work before hiring.
- **Re-run this canvas in delta mode** after the experiments (jail-bmc, canvas-delta mode).

Approval needed before acting: contacting owners or openers (experiment 2 and interviews), ad spend (experiment 3), and any hiring or paid technician time for experiment 1.

## SUCCESS-TEST
- Labels intact: 16 of 16 elements labeled. **Pass.**
- Coherence pass done; six findings logged, none smoothed over. **Pass.**
- Top four assumptions each carry a cheapest-first experiment. **Pass.**
- No element is VALIDATED, so no evidence ref is needed. **Pass.**

## Sources (accessed 2026-11-12)
- [S1] Aquacade Pools, Long Island pool service: https://www.aquacadepools.com/pool-service-long-island (monthly DIY check-ups from $150; contractor marketing, Low)
- [S2] Jas Aquatics: https://jasaquatics.com/pool-service-south-jamaica-ny/ (weekly $120–180/mo; contractor marketing, Low)
- [S3] Majestic Pool: https://majesticpoolinc.com/blog/weekly-pool-maintenance-long-island-pricing/ ($120–180/mo) and https://majesticpoolinc.com/services/weekly-pool-maintenance/ ($175–350/mo; contractor marketing, Low)
- [S4] Angi, New York pool maintenance cost: https://www.angi.com/articles/how-much-does-it-cost-maintain-swimming-pool/ny/new-york ($275–550/mo; DIY chemicals $70–130/mo; aggregator, Low–medium)
- [S5] Pool industry benchmark pages (per-visit $25–44 and $80–150; 8–16 stops per day; chemicals $8–15 per visit): https://www.poolfounder.com/pool-service-average-route-size and https://poolleadnetwork.com/pool-service-pricing-benchmarks/ (vendor blogs; I did not isolate which page gave which figure; Low)

**Gaps, not checked:** New York pool-technician wages (BLS OEWS not pulled), licensing requirements for equipment work, and any price for a monthly equipment-only check beyond the $150 DIY comparable.

```yaml
JAIL-HANDOFF:
  skill: jail-bmc
  status: complete
  facts: ["Price $89/mo and Long Island location (User-provided)", "Comparable monthly pricing $120-180 weekly, $150 DIY check-up (contractor pages, dated 2026-11-12)"]
  assumptions: ["Cost to serve is $61 per visit", "Churn is 4% a month", "CAC is $250 via local search", "Owners pay $89/mo for equipment-only checks"]
  unknowns: ["Measured cost per visit", "Willingness to pay", "Channel CAC", "Technician pay model and wage", "Heater licensing requirements", "Route density"]
  outputs: ["Nine-block canvas, all HYPOTHESIS", "Unit economics: LTV:CAC 2.8 undiscounted, 2.3 discounted, payback 8.9 months", "Four ranked experiments", "Six coherence findings"]
  risks: ["Estimated LTV:CAC below 3 on unvalidated inputs", "Price below the observed monthly check-up benchmark", "Labor model changes break-even from 54 to 94 subscribers"]
  confidence: low
  next: jail-lab (experiments 1-4)
  approval_required: ["Contacting owners or pool openers (experiment 2 and interviews)", "Ad spend on experiment 3", "Paid technician time for experiment 1"]
```

I did not save this to the project, because it is a venture analysis and not Signal Results Group collateral. If you want it filed there, I can write it as a new doc.