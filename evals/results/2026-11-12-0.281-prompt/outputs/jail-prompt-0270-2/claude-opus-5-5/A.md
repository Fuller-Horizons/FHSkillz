**STOP: an AI prompt is the wrong tool for this.** Adding up 40 numbers is a calculation. A spreadsheet or a one-line script gets it exactly right every time, while a language model doing arithmetic can make a mistake you won't notice. No prompt needed.

I tried to run the sum as a script, but the command needed approval and didn't run. So I added the totals by hand, twice, using two different methods:

| Row | Invoices | Subtotal |
|---|---|---|
| 1 | 1250.00 … 2999.99 | 11,566.99 |
| 2 | 415.50 … 1399.00 | 9,900.47 |
| 3 | 275.00 … 2390.00 | 9,324.43 |
| 4 | 147.20 … 999.00 | 9,403.10 |
| **Total** | **40 invoices** | **40,194.99** |

The first method added each row in order. The second added the whole dollars and the cents separately, then combined them. Both gave the same subtotal for every row. Still, this was done by hand, so treat **$40,194.99** as provisional until a tool confirms it.

**How to confirm it in 10 seconds:**
- **(A) Spreadsheet (best):** paste the numbers into column A and use `=SUM(A1:A40)`. Add `=COUNT(A1:A40)` to make sure it shows 40, so none were dropped.
- **(B) Script:** approve the command I tried, or run it yourself:
  `python3 -c "from decimal import Decimal as D; print(sum(D(x) for x in open('totals.txt').read().replace(',',' ').split()))"`
- **(C) If you have to use AI:** paste the numbers into a Claude chat that has code execution turned on and ask it to "sum these using code, and report the count."

**Model:** this is a light task. Sonnet 5.5 at medium effort is enough; Opus is more than it needs.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: stop
  assumptions: [the 40 values are all the invoices; USD; no tax, credits or duplicates to adjust]
  unknowns: [total not yet confirmed by a tool, because the script needed approval]
  outputs: [STOP → spreadsheet SUM or script; provisional hand total 40,194.99]
  next: run =SUM in a spreadsheet, or approve the script, to confirm
  approval_required: [running the Python sum command]
  tested: n/a
```