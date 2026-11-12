**STOP: a spreadsheet does this better.** Language models can drop, duplicate or misadd numbers across 200 rows. A spreadsheet formula gets the exact total every time, for free.

```
=SUM(B2:B201)
```

Change `B` to your amount column. If some amounts are stored as text (with `$` signs or commas), use this instead:

```
=SUMPRODUCT(VALUE(SUBSTITUTE(SUBSTITUTE(B2:B201,"$",""),",","")))
```

**If you still want AI to do it,** use this prompt. It only works if the AI can run code, like ChatGPT's data analysis or Claude with file analysis turned on. It also makes the AI show a row count so you can check its work.

```
<spreadsheet>
[attach the file]
</spreadsheet>

OBJECTIVE: Total the invoice amount column in the attached spreadsheet using code, not mental arithmetic.

SUCCESS TEST: The row count you report matches the number of invoice rows in the file (about 200), and the total is calculated by code you ran.

QUALITY BAR:
- Run code to load the file and sum the column; don't add the numbers by reading them.
- Clean "$", commas, and spaces first; count negative amounts (credits) as negative.
- List any cell you couldn't read as a number, with its row number. Don't guess its value.
- Leave out header, subtotal, and total rows, and say which ones you left out.

OUTPUT FORMAT:
Column used: <name/letter>
Rows summed: <n>
Rows skipped: <row #: reason> (or "none")
TOTAL: $<amount, 2 decimals>

RUN SETTINGS: any model that can run code · low effort · code execution ON
```

To check the result, compare "Rows summed" with your sheet's row count. If they don't match, don't trust the total.

UNTESTED: one-off, and I don't have your file.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: stop
  assumptions: [amounts are in one column, about 200 rows, headers in row 1]
  unknowns: [exact column, whether amounts are stored as text, whether there are subtotal rows]
  outputs: [STOP pointing to =SUM, plus a fallback prompt that uses code]
  next: use =SUM in the spreadsheet
  approval_required: []
  tested: untested: one-off, no file provided
```