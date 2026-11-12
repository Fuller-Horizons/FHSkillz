## Verdict: GO, but the file is missing

I don't have the P&L export. Nothing is attached and there's no spreadsheet in the working folder, so I can't do the analysis yet. I won't guess at the numbers. Since a client will see this and you have a deadline, every figure has to trace back to the export.

**Lane: Lite.** The goal is clear, but a wrong number in front of a client costs trust.

### Pushback before you use AI for this
- **Use a spreadsheet for the ranking.** Sorting expense lines and adding them up is simple arithmetic. In QuickBooks, export to Excel, sort the expense rows from largest to smallest, and you have 90% of the answer in two minutes. AI is useful for two other jobs: deciding what counts as a "driver," and writing the "so what" for the client. The prompt below has the model calculate in code and show its math, not do the sums in its head.
- **Size isn't the same as a driver.** The five biggest lines (rent, payroll) are often fixed costs the client already knows about. If your export has two periods side by side (this year vs. last year, or vs. budget), the biggest *increases* in dollars usually make a better meeting topic. The prompt ranks by size and also flags the biggest movers when a comparison column exists.
- **QuickBooks adds subtotals inside the expense section.** Exports include parent-account totals like "Total Payroll Expenses" alongside their sub-accounts. If those are ranked as their own lines, costs get counted twice. This is the most likely way the output goes wrong, so the prompt handles it explicitly.
- **Confidentiality.** A client P&L is confidential. Only run it in a tool the client has agreed to, and remove account and bank numbers first.

### Assumptions (tell me if any are wrong)
- (a) The export covers one period, cash or accrual basis, exactly as QuickBooks produced it.
- (b) "Cost drivers" means expense lines at the lowest account level. Cost of Goods Sold is reported separately from operating expenses.
- (c) The output is a table. A one-page memo is the alternative.

### Engineered prompt (copy this)
```
METADATA: inputs: [pl_export.xlsx|csv] · outputs: [cost_drivers.md] · params: {temperature: 0.2} · requires: none · produces: [cost_drivers]
ROLE: Management consultant preparing a small-business client meeting brief.
CONTEXT: The attached QuickBooks Profit and Loss export is the only data source. The reader is the business owner. Figures will be discussed live, so every number must be traceable to an export row. QuickBooks exports include parent-account subtotal rows ("Total ...") that must not be ranked alongside their sub-accounts.
OBJECTIVE: Identify the five largest cost drivers in the attached P&L and explain what each means for the client.
SUCCESS TEST: [AUTO] exactly five ranked rows; [AUTO] no ranked row is a subtotal or the parent of another ranked row; [AUTO] each Amount equals the value on its cited export row; [AUTO] top five + "All other expenses" = Total Expenses (and COGS reconciles to Total COGS if present), difference = 0.00; [AUTO] Data Gaps, Assumptions, Confidence sections exist; [HUMAN] the owner can follow each "So what" without a glossary.
PROCESS:
 1) Confirm the file has Total Expenses (and Total COGS if applicable). If missing, stop and report under Data Gaps.
 2) Using a code sandbox (not mental math), parse the expense and COGS sections; drop "Total ..." subtotal rows and parent accounts that have sub-accounts; keep leaf accounts only.
 3) Rank leaf lines by amount; take the top five. Compute % of Total Expenses (COGS lines: % of Total COGS); show the formula.
 4) If the export has a comparison column (prior period or budget), also list the three largest dollar increases as "Biggest movers".
 5) Write one "So what" sentence per driver, tagged Inference.
 6) Run the reconciliation in SUCCESS TEST and print the difference.
SOURCES: The attached export only. No outside benchmarks; any industry comparison is Unknown and goes under Data Gaps.
OUTPUT FORMAT:
 | Rank | Expense line | Section (OpEx/COGS) | Amount | % of section total | Export row | Tag | So what |
 | 1 | <leaf account> | OpEx | <amount> | <pct> | <row no.> | Fact | <one sentence> (Inference) |
 Then: All other expenses | Total Expenses | Reconciliation difference | Biggest movers (if comparison exists) | Data Gaps | Assumptions | Confidence (high/medium/low + reason).
CONSTRAINTS: Under 400 words. Cite an export row for every number. Tag claims Fact / Inference / Unknown; prefer Unknown to a guess. Never invent a figure. Do not output account numbers or bank details.
VERIFICATION PLAN: [AUTO] reconciliation difference = 0.00 (most likely to falsify, catches double-counted subtotals); [AUTO] spot-check each amount against its row; [HUMAN] read "So what" for claims the export cannot support.
BEFORE RETURNING: self-check vs SUCCESS TEST; 1-5 score on grounded / verifiable / scoped / format-matched; confidence 0-100%; list gaps; offer two knobs (top three instead of five; group by category, e.g., people / occupancy / vehicles).
```
The sample row only shows the format. It contains no real data.

**Next step, pick one:**
- **(A)** Put the export in this folder or attach it, and I'll run the prompt here with code and show you the reconciliation. This is my recommendation since Thursday is close.
- **(B)** Paste just the expense section.
- **(C)** Switch the output to a one-page memo.

```yaml
JAIL-HANDOFF:
  skill: jail-prompt
  status: partial
  assumptions:
    - one period as exported
    - cost drivers = five largest leaf-level expense accounts; COGS reported separately
    - table output
  unknowns:
    - P&L export not attached; contents unknown
    - accounting basis (cash or accrual)
    - whether a comparison column (prior period/budget) exists
  outputs: [engineered prompt]
  next: attach the P&L export, then run the prompt (then jail-summarize for a client-ready one-pager if wanted)
  approval_required:
    - running the prompt on client-confidential financial data in an approved tool
```