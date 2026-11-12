**STOP: a prompt is the wrong tool here.** Adding up numbers is a job for a calculator. An AI model can drop a digit or carry a cent wrong, and nothing would flag it. For invoice totals, use a spreadsheet:

1. Paste the 40 values into column A (A1:A40).
2. Enter `=SUM(A1:A40)` and `=COUNT(A1:A40)`. The count should be 40.

I tried to run the sum as a script, but the command needed your approval and didn't run. So I added the numbers by hand twice, using two different methods. Both gave the same answer, but this has **not** been checked by a machine:

| Rows | Subtotal |
|---|---|
| Values 1–10 | 11,566.99 |
| Values 11–20 | 9,900.47 |
| Values 21–30 | 9,324.43 |
| Values 31–40 | 9,403.10 |
| **Total (40 invoices)** | **$40,194.99** |

If your spreadsheet shows a different total, check the subtotal for each group of 10 to find where they differ. If you approve the command, I can confirm the total with an exact decimal sum.

**Other options:**
- **Reframe:** if these totals come from QuickBooks or an export, run the report there. That way you also avoid typos from copying the numbers by hand.
- **Proceed:** use the hand total above, but only after the spreadsheet check.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: stop
  assumptions: [values are USD invoice totals exactly as pasted; no duplicates or credits to exclude]
  unknowns: [whether the 40 values match the source system]
  outputs: [STOP: use a spreadsheet SUM; hand-computed total 40,194.99, not machine-checked]
  next: run =SUM in a spreadsheet, or approve the script to confirm
  approval_required: [running the script to sum the values]
  tested: n/a
```