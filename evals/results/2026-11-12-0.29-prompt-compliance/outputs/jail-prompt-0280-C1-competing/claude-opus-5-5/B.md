**Instant lane: GO.** One note on cost: if the handbook hasn't changed since last month, reuse last month's summary. Only rerun the prompt when the handbook changes.

```
METADATA: inputs: handbook (full text) · outputs: one-page new-hire summary · params: company name, effective date · requires: none · produces: summary (markdown)

CONTEXT: New hires get this one-page summary on day one, alongside the full 40-page handbook. It helps them get oriented. It does not replace the handbook, which stays the binding document. Because the summary is used every month, it must match the current handbook exactly.

<handbook>
[paste full handbook text here]
</handbook>

OBJECTIVE: Turn the handbook above into a one-page summary a new hire can read in under 3 minutes. It should cover what they need in their first 30 days and where to find the rest.

SUCCESS TEST: 450 words or fewer · every policy point includes a handbook section reference, e.g. (§4.2) · no fact appears that isn't in the handbook.

QUALITY BAR:
- Put first what affects a new hire's first weeks: pay schedule, hours and attendance, PTO and sick leave accrual, benefits enrollment deadlines, conduct and harassment reporting, and who to contact.
- Copy every deadline, number, and eligibility rule exactly. Never round or paraphrase them, because a wrong number becomes an HR problem.
- Use plain language with no legalese. Each line should tell the reader what to do or what is true.
- If the handbook is unclear or contradicts itself on a point, mark it "[CHECK WITH HR]" rather than guessing.

OUTPUT FORMAT:
# [Company] — New Hire Quick Guide (effective [date])
**Your first week:** 3–5 bullets
**Pay & hours:** bullets
**Time off:** bullets
**Benefits:** bullets (include enrollment deadline)
**How we work together:** conduct, safety, reporting concerns
**Who to ask:** names, roles, or contacts as stated in the handbook
*This is a summary. The full Employee Handbook governs. Questions: [HR contact].*

CONSTRAINTS: Leave out anything not in the handbook. Skip sections that don't apply to a new hire's first 30 days, such as retirement vesting details and termination procedures. For those, give a one-line pointer to the section number.

RUN SETTINGS: Claude Opus 5.5 · medium effort · no tools · thinking on

BEFORE RETURNING: Count the words. Confirm every bullet has a § reference. Spot-check 3 numbers against the handbook. List any [CHECK WITH HR] items below the summary.
```

**Before each handout:** have HR spend 2 minutes checking the numbers and deadlines in the summary against the handbook.

UNTESTED: you asked to skip testing · test set: run it once on the current handbook and have HR check that first output.

I can save this to the Project prompt library if you'd like, and run it once you paste the handbook.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: complete
  assumptions: [handbook is pasteable text; audience is all new hires; the full handbook stays the binding document]
  unknowns: [whether the handbook changes monthly]
  outputs: [engineered prompt]
  next: run on the current handbook → HR review
  approval_required: [HR sign-off before distribution]
```