# Worked example: pre-revenue canvas (pool-equipment subscription)

**Input (user):** "Build a business model canvas for my idea: a subscription service that sends a technician to service residential pool equipment monthly, $89/mo, Long Island. No customers yet."

All data below is synthetic. No sources are cited because nothing is checked yet; that is the point of this run.

## Task contract (short)
**Venture:** monthly pool-equipment service subscription, Long Island NY. **Stage:** idea, no customers, no revenue. **Decision served:** whether to spend on a 20-customer pilot. **Inputs in hand:** the price ($89/mo) and the region, both User-provided. **Inputs missing:** any customer, cost, or channel data.

## Canvas

| Block | Element | Label(V/H) | Evidence ref | Confidence |
| :--- | :--- | :---: | :---: | :---: |
| Customer segments | Owners of in-ground pools, single-family homes, Suffolk County, who already pay a seasonal opener/closer | H | none | L |
| Customer segments | Owners of above-ground pools | H | none | L |
| Value propositions | Equipment (pump, filter, heater, salt cell) checked monthly so failures are caught before the season | H | none | L |
| Value propositions | One flat monthly price, no surprise repair quotes for covered checks | H | none | L |
| Channels | Local search ads (Google local services) | H | none | L |
| Channels | Referrals from pool openers/closers and pool-supply stores | H | none | L |
| Customer relationships | Text reminder before each visit, photo report after | H | none | M |
| Revenue streams | $89/mo subscription, billed by card | H | none | L |
| Revenue streams | Repair and parts upsell, billed per job | H | none | L |
| Key resources | Two trained technicians, one van, parts inventory | H | none | M |
| Key activities | Route scheduling, monthly equipment inspection, repair follow-up | H | none | M |
| Key partnerships | Pool-supply wholesaler for parts at trade price | H | none | L |
| Cost structure | Technician labor, supplies, vehicle, ad spend | H | none | L |

No element is VALIDATED. Nothing here has a transaction, signed commitment, or measured result behind it, so each defaults to HYPOTHESIS. The price and region are User-provided; a price the owner chose is not a price a customer has paid.

## Coherence pass
- Segment to value proposition: the in-ground segment maps to the equipment-check proposition. The above-ground segment may not need it (simpler equipment). Judgment, Low confidence.
- Revenue to segments: the payer and the user are the same person (the homeowner). Holds.
- **Finding:** the $89 price was chosen before cost to serve was measured. See unit economics.
- Key activities to value proposition: "monthly" visits need route density. With no customers, density is Unknown.

## Unit economics (inputs are all HYPOTHESIS)

| Input | Value | Label | Strength |
| :-- | --: | :-: | :-- |
| Price per month | $89 | H (User-provided) | none |
| Technician labor per visit | $48 (1.5 hours at $32 loaded) | H | weak |
| Supplies per visit | $8 | H | none |
| Vehicle per visit | $5 | H | none |
| Monthly churn | 4% | H | none |
| CAC | $260 | H | none |
| Annual discount rate | 10% | H | chosen |

Estimate (method: worksheet formulas, inputs above):

| Step | Calculation | Result |
| :-- | :-- | --: |
| Cost to serve | 48 + 8 + 5 | $61 |
| Margin per month | 89 − 61 | $28 |
| Margin % | 28 ÷ 89 | 31.5% |
| Expected lifetime | 1 ÷ 0.04 | 25 months |
| LTV, undiscounted | 28 × 25 | $700 |
| LTV, discounted | 28 ÷ (0.00797 + 0.04) | $584 |
| LTV:CAC, undiscounted | 700 ÷ 260 | 2.7 |
| LTV:CAC, discounted | 584 ÷ 260 | 2.2 |
| CAC payback | 260 ÷ 28 | 9.3 months |

Judgment: below the common 3:1 rule of thumb. What would close the gap, one lever at a time: price of $92.20 (at the other inputs), or CAC of $233 (about), or churn of 3.6% (about). Labor per visit is the biggest cost line, so route density and visit time matter most.

## Top risky assumptions and experiments (jail-lab spec shape)

1. **Cost to serve is $61 or less per visit** (impact high, evidence none). Metric: measured labor + supplies + vehicle per visit, lower is better. Variable: a real visit routine on 10 friendly pools. Bound: 3 weeks, 10 visits, about $500 of owner time. Pass: average cost at or below $61.
2. **Owners will pay $89 a month for checks, not just repairs** (impact high, evidence none). Metric: signed 3-month commitments, higher is better. Variable: the offer page with the $89 price. Bound: 30 days, 40 owners contacted through pool openers, $0 ad spend. Pass: 6 or more signed.
3. **CAC is $260 or less via local search ads** (impact high, evidence none). Metric: ad spend ÷ signed customers, lower is better. Variable: one Google local services campaign. Bound: 45 days, $1,000. Pass: CAC at or below $260.
4. **Churn stays at or below 4% a month** (impact medium, evidence none). Metric: monthly cancellations. Variable: the pilot cohort. Bound: 3 months of the pilot. Pass: 4% or lower. This one needs customers, so it runs last.

Order, cheapest and most decisive first: 1, 2, 3, 4.

## Customer validation questions
- Who services your pool equipment today, and what do you pay per year?
- What failure cost you the most in the last two seasons?
- Would you prefer one flat price or pay per visit? Why?

## Strategic implications and next actions
- Do not spend on a pilot until experiments 1 and 2 pass. They cost almost nothing.
- If experiment 1 shows cost above $70 per visit, the $89 price cannot work at current churn and CAC; re-price or cut visit time.
- Re-run this canvas in delta mode after the experiments.

## SUCCESS-TEST
- Labels intact: 13 of 13 elements labeled. Pass.
- Coherence pass done, finding logged. Pass.
- Top assumptions carry experiments, cheapest first. Pass.
- No VALIDATED element lacks a ref: none are VALIDATED. Pass.

## Delivery note
For a client copy, keep the canvas table and the unit-economics table, drop the YAML below, and use plain short sentences.

```yaml
JAIL-HANDOFF:
  skill: jail-bmc
  status: complete
  facts: ["Price of $89/mo and Long Island location, user-provided by the founder"]
  assumptions: ["Cost to serve is $61 per visit", "Churn is 4% a month", "CAC is $260 via local search ads", "In-ground pool owners pay $89 for monthly checks"]
  unknowns: ["Real cost to serve per visit", "Willingness to pay for checks", "Channel CAC", "Route density needed"]
  outputs: ["Nine-block canvas (all HYPOTHESIS)", "Unit-economics estimate: LTV:CAC 2.7 undiscounted, 2.2 discounted, payback 9.3 months", "Four ranked experiments"]
  risks: ["Estimated LTV:CAC is below 3 on unvalidated inputs", "Labor per visit is the largest cost line"]
  confidence: low
  next: jail-lab
  approval_required: ["Spending ad budget on experiment 3", "Contacting owners for experiment 2"]
```
