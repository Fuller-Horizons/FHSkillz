**STOP: AI is the wrong tool for this.** A language model can drop or misread rows when it adds up 200 numbers. Your spreadsheet adds them exactly, in about one second.

**The faster way (assuming the amounts are in column B, rows 2–201):**

```
=SUM(B2:B201)      ← your total
=COUNT(B2:B201)    ← should return 200
=COUNTA(B2:B201)   ← if this is higher than COUNT, some amounts are stored as text and were left out of the SUM
```

If COUNT and COUNTA don't match, select the column and use **Data → Text to Columns → Finish** in Excel, or **Format → Number** in Google Sheets. That turns the text back into numbers.

**Next step (pick one):**
- **A.** Use the formulas above. *(Recommended)*
- **B.** You need more than a total, like totals by vendor or month, or finding duplicates. I'll write a prompt for that, because AI is useful there.
- **C.** You still want AI to do the adding. I'll write a prompt that makes it total the column with code and check the row count, not add the numbers in its head. Attach the file.
- **D.** Drop it.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: stop
  assumptions: [amounts sit in one column, B2:B201; one currency]
  unknowns: [actual column/range; whether any amounts are stored as text]
  outputs: [STOP]
  next: user picks A/B/C/D
  approval_required: []
```