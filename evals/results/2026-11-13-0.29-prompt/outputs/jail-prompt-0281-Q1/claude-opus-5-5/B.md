The prompt is ready below, but I haven't tested it. You use it every month and clients make decisions from it, so it needs a real test before you rely on it. I also couldn't run the lint check because the command needs your approval.

**Gate: GO, with one condition.** Claude is good at writing the story behind the numbers. It's not reliable at doing the math in its head. So the prompt has it calculate every change and variance with code execution, and every number has to trace back to your data. If a client's data already sits in a spreadsheet, you could do the math there and let Claude write only the narrative. The prompt still works that way.

**My assumptions (I'll change these if you say so):** one client per run, client-facing Markdown that pastes into Word, and you supply the numbers each month. I couldn't read your project docs from here, including the prompt library, so I wrote this one from scratch.

### Full version
```
<client_profile>
[Client name, industry, size, what they hired Signal Results Group for, the 3-5 goals this engagement is measured against, who reads this report (owner / CEO / leadership team) and their numeracy level.]
</client_profile>

<kpi_data>
[This month's numbers, pasted or attached as CSV/spreadsheet. One row per metric. Columns, if you have them: metric, unit, this month, last month, same month last year, YTD, target/budget. Leave a cell blank rather than guessing.]
</kpi_data>

<consultant_notes>
[Your notes: what you know happened this month (lost a customer, price increase, new hire, storm, promo), what you're working on with them, anything sensitive to avoid or frame carefully. Write "none" if none.]
</consultant_notes>

<last_report>
[Last month's report, pasted in full, so actions and commitments carry forward. Write "first report" if none.]
</last_report>

<report_month>[Month YYYY]</report_month>

OBJECTIVE: Turn this client's numbers into a monthly report they can read in five minutes and act on: what changed, why it matters to their goals, and what to do next. I want the judgment of a senior operator-consultant, not a restatement of the table.

SUCCESS TEST:
- The scorecard has exactly one row per metric in <kpi_data>, and every value matches the input.
- Every change and variance (absolute and %) is computed with code execution, not mentally; the QA appendix shows the calculation table.
- Every number in the narrative appears in <kpi_data> or in the QA calculation table.
- Every "why" claim is tagged in the QA appendix as Fact (from consultant notes or data), Inference (your reasoning), or Unknown.
- Each item marked "Open" or "In progress" in <last_report> has a status line under "Last month's actions."

QUALITY BAR:
- Leads with the answer: the headline says whether the month was good or bad against their goals, in one sentence, with the single number that proves it.
- Explains causes only from the data or my notes; where the cause isn't known, it says so and gives the question to ask the client, rather than inventing a reason.
- Separates signal from noise: a move under about 5%, or one that matches the usual seasonal pattern, is not called a trend unless the data shows a sustained run.
- Recommendations are specific, owned, and dated (who does what by when), at most 3, each tied to a metric on the scorecard.
- Plain business language at the reader's level; no jargon, no hedging filler, no praise the numbers don't earn.

OUTPUT FORMAT (Markdown, ready to paste into Word):

# [Client] — Monthly Performance Report, [Month YYYY]

**Headline:** [one sentence: verdict + proof number]

## Scorecard
| Metric | This month | vs last month | vs last year | vs target | Status |
|---|---|---|---|---|---|
| Revenue | $412,000 | +6.2% | +11.0% | −2.1% | 🟡 Watch |
(Status: 🟢 On track / 🟡 Watch / 🔴 Act. Show "n/a" where the input has no comparison value.)

## What moved and why
[2-4 short paragraphs, biggest impact first. Each: what happened, the number, the likely cause, and what it means for their goals.]

## Last month's actions
- [Action from last report] — [Done / In progress / Not started / Dropped]: [one line]

## Recommended actions for next month
1. [Action] — Owner: [name/role] — By: [date] — Moves: [metric]

## Questions for you
- [Only where a missing fact would change the advice; skip the section if none]

---
## QA APPENDIX — internal, delete before sending
- **Calculation table:** metric, inputs used, formula, result
- **Claim log:** each causal claim → Fact / Inference / Unknown, with its source
- **Data issues:** blanks, outliers, possible entry errors, units that don't reconcile
- **Not included and why:** anything you left out on purpose

BEFORE RETURNING: Re-check the scorecard row count against <kpi_data> and confirm every narrative number appears in the inputs or the calculation table. If any metric looks like a data-entry error (for example a 10x jump), flag it in Data issues and in "Questions for you" instead of building a story on it.

RUN SETTINGS: Claude Opus 5.5 (Sonnet 5.5 is fine for simple clients) · medium effort · code execution on (for the math) · no web search · one client per run.
```

**Why some lines are there:**
- **`<last_report>`:** without it, each month starts from zero and nobody follows up on the actions you recommended.
- **QA appendix:** it lets you check every number and claim in two minutes before you send. Delete it before the report goes to the client.
- **The "10x" check:** a typo in the client's data is the most likely way this report goes wrong in front of them.

### Quick version (for an informal month)
```
<kpi_data>[paste numbers: metric, this month, last month, last year, target]</kpi_data>
<consultant_notes>[what happened / "none"]</consultant_notes>
Write a one-page monthly report for [client], whose goals are [goals]. Use code execution for all % changes. Give: a one-sentence headline verdict, a scorecard table (one row per metric, 🟢/🟡/🔴), what moved and why (only causes supported by the data or my notes; otherwise say "cause unknown" and give the question to ask), and up to 3 dated actions with owners. Then, under a line, list any numbers that look like data errors.
```

### Three questions (unanswered ones keep the first option)
1. **Report format:** **A) Markdown to paste into Word** · B) email body · C) a 5-slide outline · D) something else (tell me)
2. **What your numbers look like:** **A) a KPI sheet with prior months and targets** · B) raw P&L or financial statements (then I'd add a step to pull the KPIs out first) · C) it varies by client · D) something else (tell me)
3. **Where it runs:** **A) one Claude Project per client, with the profile saved in the Project** (so you only paste the data and notes each month) · B) one Project for all clients · C) automated through the API · D) something else (tell me)

UNTESTED: not run yet. To test it, I'd make 5 fictional client months (made up so no real client data is used), run each 3 times, and compare against a plain "write a monthly report from these numbers" request:
1. A normal month with all columns filled
2. A first report, with no last report and no targets
3. A month with a planted 10x data-entry error
4. A down month where the notes give no explanation
5. A last report with 4 open actions

Months 1–3 would be used to fix the prompt and months 4–5 to check that the fixes hold. With your go-ahead I'll run that, plus the lint check. If you'd rather, send me one real month with the names removed and I'll run it on that.

The prompt is saved at `/tmp/claude-0/-tmp-fhlive-bgrm934v/2f5ab3e1-e3c2-4d45-a15e-417a73986ba9/scratchpad/monthly-client-report-prompt.md`.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: partial
  assumptions: [one client per run, client-facing Markdown pasted into Word, user supplies KPI table monthly, code execution available, no project prompt library reachable]
  unknowns: [actual data format per client, delivery format, where it runs, client confidentiality rules for the data]
  outputs: [engineered prompt + QUICK version]
  next: answer the 3 questions → run Full-lane test (5 fictional inputs × 3 runs vs plain request) + prompt-lint --strict
  approval_required: [running the lint script, test runs (token spend), any use of real client data]
  tested: untested: test set defined, awaiting go-ahead and lint approval
```