# Quantified lane — expected-value worksheet

Use only when money or time is load-bearing AND real numbers exist. If the
inputs are gut feel, stay in comparative prose (SKILL.md, Step 2). Do the
arithmetic by hand or with a calculator; if `jail-py-toolkit` is available it
can double-check, but nothing here requires it.

## Worksheet (one block per option)

1. **Benefit if it works (B)** — a yearly dollar figure. Label and source it.
2. **Probability range** — `p_low` and `p_high`. These are always an
   **Estimate**: say how you chose them (vendor claim discounted, past
   project, peer data).
3. **Cost (C)** — setup + running cost over the same period. Label and source.
4. **EV range** — `EV_low = p_low × B − C` and `EV_high = p_high × B − C`.
   If the range crosses zero, say so. If two options' ranges overlap, they
   are a tie on money: break it on a named non-money criterion.
5. **Cost of delay (per month)** — what one more month of not deciding
   forfeits: `(p × monthly benefit − monthly running cost)`, low and high.
   For do-nothing, also state the status-quo cost that keeps running.
6. **Payback** — `setup cost ÷ monthly net`, low and high (months).
7. **Break-even** — the smallest `p` where EV = 0: `p_be = C ÷ B`. Compare it
   to your `p_low`/`p_high`: if `p_be` sits inside the range, confidence is
   not high.

Every input line ends with its label (Fact, User-provided, Estimate) and
source. Results are Estimates.

## Worked example (synthetic, arithmetic checked)

A 12-person HVAC company: dispatch software vs a second dispatcher vs
do-nothing. Horizon: first 12 months.

| Input | Value | Label and source |
|---|---|---|
| Overtime today | $1,800/mo = $21,600/yr (B for both options) | User-provided: owner, current payroll |
| Software cost | $3,000 setup + $400/mo × 12 = $7,800 (C) | User-provided: vendor quote |
| Software p | 0.40 to 0.70 | Estimate: vendor claim discounted, no pilot yet |
| Hire cost | $52,000/yr loaded (C) | User-provided: owner's loaded figure |
| Hire p | 0.70 to 0.90 | Estimate: a second person likely removes most overtime |

Software: EV_low = 0.40 × 21,600 − 7,800 = 8,640 − 7,800 = **$840**;
EV_high = 0.70 × 21,600 − 7,800 = 15,120 − 7,800 = **$7,320**.
Monthly net = p × 1,800 − 400 = **$320 (low) to $860 (high)**, so cost of
delay is $320 to $860 per month. Payback = 3,000 ÷ 320 = **9.4 months** (low)
to 3,000 ÷ 860 = **3.5 months** (high). Break-even p = 7,800 ÷ 21,600 =
**0.36**, just below the low estimate of 0.40, so the pick is positive but
thin at the bottom.

Hire: EV_low = 0.70 × 21,600 − 52,000 = **−$36,880**; EV_high =
0.90 × 21,600 − 52,000 = **−$32,560**. Break-even p = 52,000 ÷ 21,600 =
2.41, which is impossible (p cannot exceed 1), so overtime savings alone can
never repay a hire. Any case for hiring must rest on other benefits (extra
jobs booked, call coverage). Those are **Unknown** here and must not be
invented.

Do-nothing: EV = $0 by definition; the status-quo cost is $1,800/mo
(User-provided) and it keeps running while the decision waits.

Reading: software wins on money; its range stays positive; hire is negative
in every case on the numbers given. Change-conditions come from the
worksheet: a pilot showing p below 0.36, or a booked-jobs estimate that
changes the hire's B.
