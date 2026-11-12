# Worked example: Lite lane, evidence-first prompt (missing input)

A complete run of jail-prompt 2.1. Data is synthetic; no real client or figures.

## Input

> **User:** "I want to use AI to pull the five biggest cost drivers out of a QuickBooks P&L export for a client meeting Thursday." (No file attached.)

## Triage

Clear goal, a client will see the numbers, a wrong figure costs trust, and a deadline exists. Not ambiguous enough for Full, so **Lite**: state assumptions, verdict, and the prompt in one reply. The comprehension gate is passed at the 97% bar on the stated objective (rank expense lines for a client discussion).

## Reply

**Verdict: GO, with one blocker.** The P&L export is not attached, so no analysis can start. I will not guess its contents or make up numbers.

**Gate (silent, summarized):**
1. Right tool: sorting and totaling expense lines is deterministic, so the prompt tells the model to compute with a code sandbox or spreadsheet formulas and show the arithmetic. The model's job is the reading: which lines are drivers, what they mean for the client.
2. Groundable: yes, every number comes from the attached file. No outside sources needed, so EXTERNAL EVIDENCE is "none".
3. Effort vs. payoff: low effort, high value before Thursday. No cheaper path.
4. Enhancement: add a one-line "so what" per driver, labeled Inference.
5. Secure: a P&L is client-confidential. Do not paste into a tool the client has not approved; remove account numbers and bank details first.

**Assumptions:** (a) one fiscal year, accrual or cash basis as exported; (b) "cost drivers" means the largest expense lines by dollar amount, with Cost of Goods Sold counted separately; (c) a table is the output (recommended default; say if you want a one-page memo instead).

**Engineered prompt (copy this):**
```
METADATA: inputs: [pl_export.csv] · outputs: [cost_drivers.md] · params: {temperature: 0.2} · requires: none · produces: [cost_drivers]
ROLE: Management consultant preparing a client meeting brief.
CONTEXT: The attached QuickBooks Profit and Loss export is the only data source. The reader is a small-business owner. Figures will be discussed live, so every number must be traceable.
OBJECTIVE: Identify the five largest cost drivers in the attached P&L and explain what each means for the client.
SUCCESS TEST: [AUTO] exactly five rows; [AUTO] each Amount equals the value on the cited export line; [AUTO] the five amounts plus "All other expenses" sum to Total Expenses in the export; [AUTO] Data Gaps, Assumptions, and Confidence sections exist; [HUMAN] the client can follow each "So what" without a glossary.
PROCESS:
 1) Confirm the file is attached and has a Total Expenses line. If not, stop and list it under Data Gaps.
 2) List every expense line with its amount; rank by amount (use a code sandbox or spreadsheet formulas for sorting and sums).
 3) Take the top five. Compute each one's share of Total Expenses; show the formula.
 4) Write one "So what" sentence per driver, labeled Inference.
SOURCES: The attached export only. No outside benchmarks; if you want to compare to an industry average, write Unknown and list it under Data Gaps.
OUTPUT FORMAT:
 | Rank | Expense line | Amount | % of total | Source (export line) | Label | So what |
 | 1 | <line name> | <amount> | <pct> | <export line no.> | Fact | <one sentence> (Inference) |
 Then: All other expenses | Total Expenses | Data Gaps | Assumptions | Confidence (high / medium / low, with reason).
CONSTRAINTS: Under 400 words. Cite a source for every number. Tag each claim Fact / Inference / Unknown. Show calculations. Never invent a figure; list it under Data Gaps. Do not output account numbers or bank details.
VERIFICATION PLAN: [AUTO] re-sum the table against Total Expenses (most likely to falsify); [AUTO] confirm each amount against its export line; [HUMAN] read the "So what" column for claims the export cannot support.
BEFORE RETURNING: self-check against SUCCESS TEST; 1-5 score on grounded / verifiable / scoped / format-matched; confidence 0-100%; list gaps; offer two knobs (top three instead of five; group by category).
```
(The sample row is a placeholder showing the shape; it contains no data.)

**Next step, pick one:** (A) attach the P&L and I will run this prompt, (B) paste only the expense section, (C) change the output to a one-page memo.

```yaml
JAIL-HANDOFF:
  skill: jail-prompt
  status: partial
  assumptions:
    - one fiscal year as exported
    - "cost drivers" means the five largest expense lines by amount
    - table output
  unknowns:
    - P&L export not attached; contents unknown
    - accounting basis (cash or accrual)
  outputs: [engineered prompt]
  confidence: medium
  next: attach the P&L export, then run the prompt
  approval_required:
    - running the prompt on client-confidential financial data
```
