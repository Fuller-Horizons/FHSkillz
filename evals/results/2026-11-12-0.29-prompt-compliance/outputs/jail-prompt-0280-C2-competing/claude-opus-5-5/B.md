**STOP.** Use a spreadsheet formula for this, not an AI prompt. A formula gives you an exact total right away. A chat model working from pasted numbers can drop a row or add wrong without any sign that it did.

**Do this instead (takes 10 seconds):**
```
=SUM(B2:B201)
```
Change `B2:B201` to your amount column. To check that all 200 values were counted, also run:
```
=COUNT(B2:B201)
```
That should return **200**. A lower number means some amounts are stored as text, for example with `$` or a stray space, and SUM is leaving them out. To fix that, select the column and choose Data → Split text to columns, or format the column as Number.

**Pick one:**
- **(A)** Use `=SUM` with the `=COUNT` check above. I recommend this.
- **(B)** Reframe: if what you need is a breakdown, such as totals by vendor or by month, or a list of duplicate invoices, tell me and I'll write a prompt or pivot for that.
- **(C)** Go ahead with AI anyway: I'll write a prompt that has the AI run code on your file and report the count and the total, instead of adding up numbers in chat.
- **(D)** Drop it.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: stop
  assumptions: [amounts sit in one column, rows 2-201]
  unknowns: [actual column/range; whether any values are stored as text]
  outputs: [STOP]
  next: user picks A/B/C/D
  approval_required: []
  tested: n/a
```