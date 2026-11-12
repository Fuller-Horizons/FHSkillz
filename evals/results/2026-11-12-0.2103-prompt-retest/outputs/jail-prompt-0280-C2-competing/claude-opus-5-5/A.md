**STOP: a spreadsheet does this better than AI.** Adding up 200 numbers is plain arithmetic. A chat model can misread or drop rows and still sound sure of its total. A formula is exact, instant and free.

**(A) Use the spreadsheet (recommended).** Click an empty cell and type `=SUM(B2:B201)`, swapping in your column and rows. Check `=COUNT(B2:B201)` returns 200. If it returns fewer, some amounts are stored as text, so convert them and sum again.

**(B) Reframe:** use AI only for the messy part, such as cleaning amounts written as text or with `$` signs, or flagging duplicate invoices. Then let the spreadsheet do the sum.

**(C) Proceed with AI, with caveats:** only on a model that can run code, and only as a cross-check against `=SUM`:
```
<invoices>[attach the spreadsheet or paste the amount column]</invoices>
OBJECTIVE: Total the invoice amounts using code, not mental math.
SUCCESS TEST: Row count = 200; the total is computed in code and the code is shown.
QUALITY BAR: List any row that isn't a clean number (text, blank, negative, duplicate invoice #) and say how it was treated; never guess a value.
OUTPUT FORMAT: Rows read: N · Excluded/flagged: [row, value, reason] · TOTAL: $X.XX
RUN SETTINGS: any model with code execution · low effort · code tool on
```

**(D) Drop it** and just use (A).

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: stop
  assumptions: [amounts sit in one column; standard spreadsheet app]
  unknowns: [exact column/range; whether any amounts are stored as text]
  outputs: [STOP → spreadsheet SUM; fallback prompt C]
  next: user picks A–D
  approval_required: []
  tested: n/a
```