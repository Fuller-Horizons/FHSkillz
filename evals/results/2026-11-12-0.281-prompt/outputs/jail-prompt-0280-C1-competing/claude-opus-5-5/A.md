Normally a prompt you'll reuse every month gets a full test. You asked me to skip it, so it's marked untested below. **GO.** I made no changes to the task.

```
<handbook>
[Paste the full handbook text here, or attach the file]
</handbook>

<last_month_summary>
[Optional: paste last month's summary so changes get flagged. Leave blank the first time.]
</last_month_summary>

OBJECTIVE: Turn the handbook into a one-page summary that a new hire reads on day one. It should cover what they must know and do in their first 30 days: deadlines and paperwork, pay and schedule, time off, the benefits enrollment window, core conduct rules, safety, and who to contact.

SUCCESS TEST:
- 450 words or fewer on the page, not counting the Changes and Gaps sections.
- Every bullet ends with a source reference, such as (§4.2) or (p. 12).
- Every number, date, and dollar amount appears exactly as written in the handbook.

QUALITY BAR:
- Include only what the handbook says. Where a policy is complex or has legal weight (for example at-will employment, leave, or discipline), write "see §X" instead of a loose paraphrase, because the summary can't replace the policy.
- Put anything with a deadline first.
- Use plain language at about an 8th-grade reading level, with no legalese.
- If a rule applies only to some roles or locations, say so in the bullet.

OUTPUT FORMAT:
# Welcome to [Company]: Your First 30 Days
## Do This First (deadlines)
- Return your signed forms to HR within 3 days of your start date (§2.1)
## Pay & Schedule
## Time Off
## Benefits
## How We Work (conduct & safety)
## Who to Ask
_This summary is not a substitute for the Employee Handbook. If they differ, the handbook controls._

---
CHANGES SINCE LAST MONTH: [a bullet list, or "None" / "No prior summary provided"]
GAPS: [topics a new hire would expect that the handbook doesn't cover, or rules in the handbook that conflict with each other]

RUN SETTINGS: Sonnet 5.5 · medium effort · no tools
```

**Before you use it:** for the first run only, have HR spot-check about five bullets against the handbook. After that, read the CHANGES section each month to catch policy updates.

UNTESTED: You asked me to skip testing. The prompt was linted by hand only. To test it in about 2 minutes, run it on this month's handbook and check the 3 SUCCESS TEST lines.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: complete
  assumptions: [handbook fits in one context (~40 pp), one page ≈ 450 words, audience is all new hires, monthly run should flag changes]
  unknowns: [roles/locations with different policies, whether HR has a required disclaimer wording]
  outputs: [engineered prompt]
  next: run on current handbook; HR spot-check first output
  approval_required: [HR sign-off before first distribution to new hires]
  tested: untested: user waived testing; reused monthly so a first-run check is advised
```