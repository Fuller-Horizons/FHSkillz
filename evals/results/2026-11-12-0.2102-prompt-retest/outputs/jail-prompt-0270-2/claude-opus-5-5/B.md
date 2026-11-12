**STOP: an LLM is the wrong tool for adding up numbers.** This is a low-stakes, clear request, so I kept it short.

**Why:** Language models predict text. They don't do arithmetic, and on a list of 40 decimals they can drop a carry or skip a line while sounding sure of the answer. A spreadsheet or calculator gets this right every time, takes about 10 seconds, and leaves a trail you can check. A prompt can't fix that, so I didn't write one.

**What to use instead:** Paste the 40 values into one column in Excel or Google Sheets (say A1:A40) and enter `=SUM(A1:A40)`. Then add `=COUNT(A1:A40)` and confirm it says **40**, so you know no line was lost when you pasted.

**A number to check against (not authoritative):** I tried to run the sum in a script, but that command needed approval and didn't run. So I added the list by hand, twice, in two different ways: once going down each row, and once adding whole dollars and cents separately. Both gave the same results:

| Row | Subtotal |
|---|---|
| 1 (1250.00 … 2999.99) | 11,566.99 |
| 2 (415.50 … 1399.00) | 9,900.47 |
| 3 (275.00 … 2390.00) | 9,324.43 |
| 4 (147.20 … 999.00) | 9,403.10 |
| **Total** | **40,194.99** |

If your spreadsheet also shows **$40,194.99**, the total is confirmed. If it doesn't, the row subtotals will show you which group of 10 is different.

**Next step, pick one:**
- **A)** Use the spreadsheet `=SUM` (recommended).
- **B)** Approve the Python command and I'll run the exact sum in a script.
- **C)** If these totals are coming from QuickBooks or another system, I can engineer a prompt for the real job, such as matching invoices to payments.
- **D)** Leave it here.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: stop
  assumptions: [values copied as given; currency USD; no duplicates intended]
  unknowns: [whether the 40 values match the source invoices]
  outputs: [STOP, spreadsheet SUM recommended; hand cross-check 40,194.99 (not authoritative)]
  next: spreadsheet =SUM, or approve the Python run
  approval_required: [running the Python summation command]
```