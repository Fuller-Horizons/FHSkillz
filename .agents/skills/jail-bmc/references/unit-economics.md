# Unit-economics worksheet (step 4 dependency)

Use this to test whether one customer is worth more than it costs to win and
serve. Every input gets a label: **VALIDATED** (with an evidence ref: billing
export, ad invoices, signed contracts) or **HYPOTHESIS** (with strength:
none / weak / comparable-based). A result is only as strong as its weakest
input; if any input is HYPOTHESIS, the result is an Estimate, not a Fact.

## Inputs

| # | Input | How to get it | Label | Evidence ref |
| :-- | :-- | :-- | :-: | :-: |
| 1 | Price per customer per month | Billing data or quote | V/H | |
| 2 | Cost to serve per customer per month | Labor + supplies + delivery for one customer | V/H | |
| 3 | Monthly churn | Customers lost in a month ÷ customers at start of month | V/H | |
| 4 | Ad / sales spend by channel | Invoices, payroll share | V/H | |
| 5 | New customers by channel | Count from the same period as the spend | V/H | |
| 6 | Annual discount rate (only if lifetime > 12 months) | Your cost of capital; say the rate you chose | H | |

## Formulas

1. **CAC (by channel)** = channel spend ÷ new customers from that channel.
   **Blended CAC** = total spend ÷ total new customers. Judge channels
   one by one; a good blend can hide a bad channel.
2. **Gross margin per customer per month** = price − cost to serve.
   **Margin %** = margin ÷ price.
3. **Expected lifetime (months)** = 1 ÷ monthly churn.
4. **LTV (undiscounted)** = margin × lifetime.
5. **LTV (discounted)**, use when lifetime is over 12 months:
   LTV = margin ÷ (monthly discount rate + monthly churn). Monthly discount
   rate = (1 + annual rate)^(1/12) − 1.
6. **LTV:CAC** = LTV ÷ CAC. Common rule of thumb: 3 or higher is healthy.
   Treat that as a Judgment, not a Fact.
7. **CAC payback (months)** = CAC ÷ margin per month. Shorter is safer.
8. **Contribution margin** = price − variable cost per customer. Fixed
   costs (office, software, salaried staff) are not in it; show them in
   the cost-structure block and state the break-even customer count.

## Worked example (operating business, synthetic numbers)

A pool-service business with 18 months of data. All inputs are VALIDATED
from billing and ad invoices (refs [B1] billing export, [A1] ad invoices),
except the discount rate (HYPOTHESIS, chosen at 10% a year).

Inputs: price $89 · cost to serve $41 · churn 3% a month · Google local
ads $3,000 for 15 new customers · Meta ads $2,520 for 8 new customers.

| Step | Calculation | Result |
| :-- | :-- | --: |
| CAC, Google local ads | 3,000 ÷ 15 | $200 |
| CAC, Meta ads | 2,520 ÷ 8 | $315 |
| Blended CAC | (3,000 + 2,520) ÷ (15 + 8) = 5,520 ÷ 23 | $240 |
| Margin per month | 89 − 41 | $48 |
| Margin % / contribution margin | 48 ÷ 89 | 53.9% |
| Expected lifetime | 1 ÷ 0.03 | 33.3 months |
| LTV, undiscounted | 48 × 33.33 | $1,600 |
| Monthly discount rate | 1.10^(1/12) − 1 | 0.797% |
| LTV, discounted | 48 ÷ (0.00797 + 0.03) | $1,264 |
| LTV:CAC, undiscounted | 1,600 ÷ 240 | 6.7 |
| LTV:CAC, discounted | 1,264 ÷ 240 | 5.3 |
| CAC payback | 240 ÷ 48 | 5.0 months |

Reading it: the blend looks healthy, but Meta at $315 pays back in
315 ÷ 48 = 6.6 months against 4.2 months for Google local ads (200 ÷ 48).
The finding is to test whether Meta is worth its spend. Lifetime of 33
months leans on 3% churn holding, so churn is the input to watch. In this
example churn is VALIDATED, but only over 18 months.

## Rules

- Never average churn across different customer types; compute per segment.
- If an input is missing, write HYPOTHESIS with its strength and run the
  numbers anyway; then show what price, CAC, or churn would make LTV:CAC
  reach 3. That is the target for the first experiment.
- Show the arithmetic so a reader can check it by hand.
- Manual fallback: no calculator tool is needed; every formula above is
  one or two operations. If `jail-py-toolkit` is available, it may be used
  to double-check; the table above is the manual path.
