**Triage: Instant lane. Verdict: STOP. AI is the wrong tool for this.**

Adding up numbers is exact arithmetic. A spreadsheet or calculator gets it right every time, and a language model can quietly drop a digit or skip a line. Writing a better prompt doesn't fix that, because the task itself is the issue. This also matters more if the total goes into billing, a report or a client document.

I tried to run the sum as a script with exact decimal math, but the command needed your approval and didn't run. So the figure below is not machine-checked.

**My hand-added total (not verified): $40,194.99**

| Row | Subtotal |
|---|---|
| Row 1 (1250.00 … 2999.99) | 11,566.99 |
| Row 2 (415.50 … 1399.00) | 9,900.47 |
| Row 3 (275.00 … 2390.00) | 9,324.43 |
| Row 4 (147.20 … 999.00) | 9,403.10 |
| **Total (40 items)** | **40,194.99** |

I checked Row 1 a second way (dollars and cents added separately) and got the same number. Don't rely on this figure until a real tool confirms it.

**Pick a next step:**
- **A (recommended):** Paste the 40 values into column A of Excel or Google Sheets and use `=SUM(A1:A40)`. Add `=COUNT(A1:A40)` and check it returns **40**, so you know no values were dropped. This takes about 30 seconds and the result is exact.
- **B:** Approve the Python run and I'll sum the values exactly and check the count.
- **C:** If you add up invoices like this regularly, pull the total straight from your accounting system (for example, a QuickBooks report filtered to these invoices) rather than copying values by hand.
- **D:** Use the figure above with the caveat that it hasn't been verified.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: stop
  assumptions: [values are USD invoice totals; all 40 belong in one sum]
  unknowns: [deterministic confirmation of 40,194.99 — script run not approved]
  outputs: [STOP]
  next: spreadsheet =SUM/=COUNT, or approved Python run
  approval_required: [running the Python summation command]
```