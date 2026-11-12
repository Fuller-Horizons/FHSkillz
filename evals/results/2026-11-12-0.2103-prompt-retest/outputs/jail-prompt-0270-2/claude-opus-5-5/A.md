**STOP: adding numbers is a job for a calculator, not an AI prompt.** A language model can slip a digit when it does arithmetic, and invoice totals are money. A spreadsheet `SUM` is exact, free, and you can check it.

I tried to run an exact sum in the sandbox, but the command needed your approval and didn't run. So no tool has confirmed the figure below yet.

**Check figure: $40,194.99**, done by hand two ways that agree:

| Row (10 invoices each) | Subtotal |
|---|---|
| 1 | 11,566.99 |
| 2 | 9,900.47 |
| 3 | 9,324.43 |
| 4 | 9,403.10 |
| **Total (40 invoices)** | **40,194.99** |

To confirm it, paste the 40 values into column A of a spreadsheet and use `=SUM(A1:A40)` and `=COUNT(A1:A40)`. The count should be 40 and the sum should be 40194.99. If it isn't, use the row subtotals above to find where it differs.

How do you want to go?
- **(A)** Approve the sandbox command and I'll run an exact sum (the recommended way).
- **(B)** Reframe: if this is a regular task, I can write a small script or spreadsheet template that adds up an invoice export and flags duplicates or outliers.
- **(C)** Go ahead with an AI prompt anyway, with the risk that the arithmetic is wrong.
- **(D)** Drop it, since you now have the figure to check against.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: stop
  assumptions: [the 40 values are complete and correctly transcribed, amounts in USD]
  unknowns: [whether the sandbox sum confirms 40,194.99]
  outputs: [STOP, plus a hand-computed check figure]
  next: approve the sandbox sum (A), or check with =SUM in a spreadsheet
  approval_required: [sandbox command to compute the exact sum]
  tested: n/a
```