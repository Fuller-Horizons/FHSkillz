**Use your spreadsheet for this, not AI.** `=SUM(B2:B201)` gives an exact total, and `=COUNT(B2:B201)` should return 200. An AI adding 200 numbers in its head can get the total wrong without showing any sign of it.

If you still want AI to do it, this prompt makes it run code for the addition and show its checks:

```
<invoices>
[attach the spreadsheet, or paste the invoice-amount column here]
</invoices>

OBJECTIVE: Total the invoice amounts in the attached data.

Use a code tool (Python) to do the sum; don't add the numbers yourself, because mental arithmetic on 200 values is error-prone.

SUCCESS TEST: Rows counted = 200. If not, say how many you found and why.

QUALITY BAR:
- Every row is either summed or listed as skipped, with the reason (blank, text, duplicate header).
- Currency symbols, commas, and parentheses-negatives like (150.00) are parsed as numbers.
- Total is rounded to 2 decimals.
- Rows that look like credits/refunds (negative values) are listed, not silently dropped.

OUTPUT FORMAT:
Rows found: <n>
Rows summed: <n>
Skipped rows: <row #: reason> or "none"
Negative values: <row #: amount> or "none"
TOTAL: $<amount>

RUN SETTINGS: any model with code execution (e.g. Claude Sonnet 5.5 with analysis tool) · low effort · file upload enabled
```

Check the AI's total against your `=SUM` before you rely on it.

UNTESTED: one-off, no spreadsheet supplied

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: stop
  assumptions: [amounts are in one column, about 200 rows plus a header, USD]
  unknowns: [exact column/range, whether negatives or credits are included]
  outputs: [STOP toward =SUM, plus a fallback prompt that uses code]
  next: run =SUM in the spreadsheet; use the prompt only if needed
  approval_required: []
  tested: untested: one-off, no spreadsheet supplied
```