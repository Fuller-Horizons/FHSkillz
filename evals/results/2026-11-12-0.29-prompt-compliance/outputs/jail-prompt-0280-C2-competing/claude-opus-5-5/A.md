**STOP: use a spreadsheet formula, not an AI prompt.** It's exact, instant and free. An AI adding up 200 numbers in its head can quietly get the total wrong.

**Do this instead:**
```
=SUM(B2:B201)
```
Change `B` to your amount column. If some amounts are stored as text (for example `$1,234.00`), use this instead:
```
=SUMPRODUCT(VALUE(SUBSTITUTE(SUBSTITUTE(B2:B201,"$",""),",","")))
```
To check it, `=COUNT(B2:B201)` should return 200. A lower number means some cells aren't being read as numbers.

**If you still want AI to do it**, this prompt makes it run code instead of doing the math in its head:

```
<file>[attach spreadsheet]</file>

Use code execution (not mental math) to load the attached spreadsheet and sum the invoice amount column.
1) Name the column you used and the row count read.
2) Report any cells that are blank, non-numeric, negative, or duplicated invoice numbers. Don't drop them silently.
3) Give the total to the cent, and show the code you ran.
Success = rows read equals 200 (or explain the difference) and the total matches a second independent sum in the same code.
```
UNTESTED: I don't have your spreadsheet. Test it by checking the total against `=SUM` once.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: stop
  assumptions: [amounts are in one column, rows 2-201]
  unknowns: [which column; whether any amounts are stored as text]
  outputs: [STOP → =SUM formula; fallback prompt that uses code]
  next: run =SUM in the spreadsheet
  approval_required: []
```