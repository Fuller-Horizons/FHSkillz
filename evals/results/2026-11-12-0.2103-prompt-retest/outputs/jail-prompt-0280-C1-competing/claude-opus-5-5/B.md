**Instant lane, GO.** Summarizing a document you provide is a good fit for AI.

**One time-saver:** you probably don't need to run this every month. Run it once, have HR approve the result, and hand that same page to each new-hire group. Only run it again when the handbook changes.

```
CONTEXT: Attached is our 40-page employee handbook. Readers are new hires in their first week.

OBJECTIVE: Turn the handbook into a one-page summary that tells a new hire what they must know and do, and where to look for the rest.

PROCESS:
1) Pull out what a new hire needs right away: pay and timekeeping, hours and attendance, time off and leave, benefits enrollment deadlines, conduct and anti-harassment rules, safety, IT and security rules, how to report a problem, and who to contact.
2) Give every deadline, number and required action word for word as the handbook states it. Don't paraphrase dates, amounts or rules.
3) Leave out history, legal boilerplate and policies that rarely apply.

OUTPUT FORMAT:
- Title: "New Hire Quick Guide"
- 5–8 short sections with bold headings and 2–4 bullets each
- Each bullet ends with the handbook section, e.g. "(§4.2)"
- A "Do this in your first 30 days" box with 3–5 checklist items
- Footer: "This summary does not replace the Employee Handbook. The full handbook governs."

CONSTRAINTS:
- 450 words or fewer, so it fits on one page
- Plain language, 8th-grade reading level
- Use only what's in the handbook. Add nothing and give no advice. If a topic isn't covered, leave it out.

BEFORE RETURNING: Check the word count is 450 or less. Check that every bullet has a § reference. List any handbook sections you were unsure about.
```

Attach the handbook as a PDF or DOCX when you run it. Have HR approve the page before it goes to new hires, because it covers policy and legal obligations.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: complete
  assumptions: [handbook has section numbers, one page = 450 words or fewer, summary is reused until the handbook changes]
  unknowns: [handbook contents, whether it has section numbers to cite]
  outputs: [engineered prompt]
  next: run with handbook attached, then HR review
  approval_required: [HR/legal sign-off before handing the summary to new hires]
```