**STOP: an AI prompt is the wrong tool for this.** Adding 40 numbers is exact arithmetic. A spreadsheet or a one-line script gets it right every time. A language model adding numbers in its head can drop a cent or skip a row and still sound sure of itself. Invoice totals are money, so a small error matters.

**My figure: $40,194.99. I couldn't run it through a calculator, so check it before you rely on it.** I tried to run a script to get an exact sum, but that command needed your approval and didn't go ahead. I added the numbers by hand, twice in two different ways (row by row, then whole dollars and cents separately), and both came to the same total:

| Row (as you pasted them) | Subtotal |
|---|---|
| 1 (1250.00 … 2999.99) | 11,566.99 |
| 2 (415.50 … 1399.00) | 9,900.47 |
| 3 (275.00 … 2390.00) | 9,324.43 |
| 4 (147.20 … 999.00) | 9,403.10 |
| **Total (40 invoices)** | **40,194.99** |

**How to confirm it, quickest first:**
- **(A) Spreadsheet (recommended):** paste the numbers into column A and use `=SUM(A1:A40)`. Add `=COUNT(A1:A40)` to make sure all 40 came through.
- **(B) Let me run the calculation:** approve the Python command and I'll return the exact sum and count.
- **(C) If you have to use AI:** ask it to run code for the sum, not add the numbers itself, and have it report the count (40) and the four row subtotals so you can spot-check them.
- **(D) Drop it:** if the subtotals above match your records, you're done.

If this is a job you'll repeat, like a monthly invoice roll-up, the better long-term fix is a saved spreadsheet template rather than a prompt.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: stop
  assumptions: [one-off sum; values are USD; list as pasted is complete (40 items)]
  unknowns: [exact sum not checked by a calculator; the script was blocked pending approval]
  outputs: [STOP → spreadsheet SUM/COUNT; unverified hand total 40,194.99 with row subtotals]
  next: user confirms with =SUM/=COUNT, or approves the Python sum
  approval_required: [running the local Python sum command]
  tested: n/a
```