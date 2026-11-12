One thing first: if the handbook doesn't change every month, run this once, have HR approve the result, and hand out that same page. Running it again each month will give slightly different wording each time and could misstate a policy. Only re-run it when the handbook is updated.

```
<handbook>
[Paste the full employee handbook here, or attach the file]
</handbook>

<company_details>
Company name: [ ]
HR contact (name / email / phone): [ ]
Handbook version or date: [ ]
</company_details>

OBJECTIVE: Turn the handbook above into a one-page summary that a new hire can read in 5 minutes. It should cover what they need in their first 90 days: how to get paid, when to show up, how to take time off, how to behave, and who to ask.

SUCCESS TEST:
- 450 words or fewer in total.
- Every bullet ends with a handbook reference in brackets, like [§4.2] or [p. 12].
- The last line is exactly: "This summary does not replace the Employee Handbook. If they differ, the Handbook governs."

QUALITY BAR:
- Each statement comes from the handbook. Do not add policies, numbers, or benefits from general knowledge, because new hires will treat this page as official.
- Copy numbers, deadlines, and eligibility rules exactly as written (PTO accrual, pay dates, probation length, notice periods).
- Write in plain language at about an 8th-grade reading level. No legal phrasing.
- Include anything that could get a new hire in trouble if they missed it (attendance, conduct, harassment reporting, safety, confidentiality).
- If a standard topic is not in the handbook, list it under "Not covered — ask HR" instead of guessing.

OUTPUT FORMAT (Markdown, sections in this order, each with 2-5 bullets):
# Welcome to [Company] — Your First-Week Guide
## Pay & Hours
## Time Off & Leave
## Benefits (eligibility & when they start)
## How We Work (conduct, dress, attendance, devices)
## Safety & Reporting Concerns
## Your First 90 Days (probation, reviews, required training)
## Who to Ask — [HR contact]
**Not covered — ask HR:** [list, or "None"]
[Disclaimer line]

RUN SETTINGS: Claude Sonnet 5.5 · medium effort · no web tools · attach the handbook as a file if pasting is too long
```

**Quick version** (if you only want something short to paste):
```
Summarize the attached employee handbook into one page (450 words or fewer) for new hires. Use these sections: Pay & Hours, Time Off, Benefits, Conduct, Safety & Reporting, First 90 Days, Who to Ask. Use only what the handbook says, copy all numbers exactly, and end every bullet with a [section/page] reference. List topics the handbook doesn't cover under "Not covered — ask HR". End with: "This summary does not replace the Employee Handbook. If they differ, the Handbook governs."
```

**Before you use it each time:** HR checks 5 numbers against the handbook: PTO accrual, pay schedule, probation length, benefits start date, and the harassment reporting contact.

UNTESTED: you asked to skip testing, and I don't have the handbook to run it on. If you want it tested later, try it on the current handbook, on an older or shortened version, and on a version where a section such as benefits has been removed. That last one checks that the prompt flags the gap under "Not covered" instead of making something up.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: complete
  assumptions: [handbook supplied as file or paste; US employer; audience is new hires in their first 90 days; one page = 450 words or fewer; HR reviews before distribution]
  unknowns: [whether the handbook changes monthly; company name and HR contact; handbook format]
  outputs: [engineered prompt + QUICK version]
  next: run once on the current handbook → HR checks it → reuse that page until the handbook changes
  approval_required: [HR/legal sign-off before handing the summary to employees]
  tested: untested: user waived testing; no handbook provided
```