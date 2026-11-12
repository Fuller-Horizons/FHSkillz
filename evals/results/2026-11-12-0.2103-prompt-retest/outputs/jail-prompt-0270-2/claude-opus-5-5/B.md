**Lane: Instant. Verdict: STOP. An AI is the wrong tool for this.**

Adding up numbers is a job for a calculator or spreadsheet. A language model predicts text, it doesn't do arithmetic, so on a 40-number sum it can drop a cent or skip a line and still sound sure of itself. A spreadsheet gets it exactly right in seconds, so I won't write you a prompt for this.

**Fastest correct way:** paste the 40 numbers into one column of Excel or Google Sheets (say A1:A40) and type `=SUM(A1:A40)` in an empty cell. Also add `=COUNT(A1:A40)` and check it shows 40, so you know none of the numbers got lost when you pasted them.

**What to check against:** I tried to add them up with a short script, but it needed your approval and didn't run. So these totals are worked out by hand and haven't been checked by a computer. I added them two ways (running totals, and whole dollars plus cents separately) and both gave the same answers:

| Rows | Subtotal |
|---|---|
| Line 1 (1250.00 … 2999.99) | 11,566.99 |
| Line 2 (415.50 … 1399.00) | 9,900.47 |
| Line 3 (275.00 … 2390.00) | 9,324.43 |
| Line 4 (147.20 … 999.00) | 9,403.10 |
| **Total (40 invoices)** | **40,194.99** |

Only rely on 40,194.99 once your spreadsheet's `=SUM` shows the same number. If they don't match, the per-line subtotals show you which group of 10 to check.

**Next step, pick one:**
- **A)** Approve the script and I'll do the sum with exact decimal math in code. Recommended if you want me to do it.
- **B)** Use the spreadsheet formula above yourself.
- **C)** If this happens regularly (say, totals from a folder of invoice files), I can write a reusable prompt or script for that.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: stop
  assumptions: [values are exact invoice totals in one currency, no tax/discount adjustments needed]
  unknowns: [machine-verified total — script run was not approved]
  outputs: [STOP — use spreadsheet SUM or code; hand-checked figure 40,194.99 pending machine confirmation]
  next: user runs =SUM in a spreadsheet, or approves the Python sum
  approval_required: [run the Python sum script]
```