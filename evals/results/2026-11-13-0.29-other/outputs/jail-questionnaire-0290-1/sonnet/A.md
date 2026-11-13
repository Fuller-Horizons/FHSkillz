I've written the questionnaire as a Markdown draft. It is not yet a .docx. It runs about 20 minutes and has 14 questions plus a closing "Anything else?" prompt.

**File:** `/tmp/claude-0/-tmp-fhlive-mf2itcpw/8b8c660e-fd41-42b9-ad5f-23abe73d2c6d/scratchpad/discovery-intake-hvac.md`

**Coverage of what must come back:**
- **Goals:** Q1–3 cover the one change they want, the sales target, and their own role in 3 years.
- **Where money leaks:** Q4–10 cover:
  - maintenance-agreement share
  - job-level profit visibility
  - estimate close rate
  - free return visits
  - billable technician time
  - days to get paid
  - the owner's own view of the biggest leak
- **Readiness for change:** Q11–14 cover the last change they tried, who else would help lead, hours available per week, and past blockers.

**Format:** Client copies are meant to be a Docs artifact or .docx. No Docs connector is attached here, and I couldn't run Python to build a .docx in this session. Tell me which you'd prefer: I can publish it as a clean private page, or you can allow python-docx and I'll generate the .docx.

**Assumptions:**
- The client answers on their own. The wording is plain English with tick boxes and ranges, so the owner can estimate instead of looking things up.
- Nothing about this client was in the project files, so there are no "confirm" items. If you already know their headcount, services or revenue range, I can add them as confirm questions.
- The questionnaire asks for no account numbers, passwords or ID numbers.

**You need to fill in:** your name, the client's name and company, and the reply-by date. Sending it is your call.

```
JAIL-HANDOFF:
  skill: jail-questionnaire
  status: partial
  assumptions: [async, owner-completed; ~20 min; no known client facts on file; 14 questions + "Anything else"]
  unknowns: [client name, reply-by date, final format (.docx vs page)]
  outputs: [discovery-intake-hvac.md, coverage map above]
  next: jail-task-contract
  approval_required: [sending to the recipient]
  tested: n/a
```