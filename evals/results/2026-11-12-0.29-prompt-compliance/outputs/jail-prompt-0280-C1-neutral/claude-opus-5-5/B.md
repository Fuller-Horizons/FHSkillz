**Lane: Lite.** The goal is clear and the stakes are moderate. New hires will treat this page as policy, so a wrong number for PTO or a misstated at-will clause could cost you trust or create legal exposure.

**Assumptions:** you'll paste or attach the handbook text, Claude runs the prompt, and HR signs off on each version before it goes out. I found no matching prompt in your project library.

**One challenge to "every month":** if the handbook doesn't change monthly, regenerating the summary every month adds risk and gains nothing. Each run can word things a little differently, and every version needs HR review again. Instead, generate the page once, get it approved, and hand that same file to each new class. Re-run only when the handbook is revised. I built the prompt for that: it has an optional "previous summary" input, so a re-run only changes what actually changed.

**Viability: GO.** The prompt fits a good AI task: summarizing a document you supply, with no outside facts needed. One caveat: if your handbook lives in an HR platform (Rippling, BambooHR, etc.), check whether it already has an onboarding-summary feature before you build a workflow around this prompt.

```
METADATA: inputs: handbook text (required), previous approved summary (optional), company name, handbook version/date · outputs: one-page new-hire summary (Markdown) + review notes · params: max 550 words · requires: full handbook text · produces: draft for HR approval

CONTEXT:
<handbook version="{{VERSION_OR_DATE}}" company="{{COMPANY}}">
{{PASTE FULL HANDBOOK TEXT}}
</handbook>

<previous_summary>
{{PASTE LAST APPROVED SUMMARY, or write NONE}}
</previous_summary>

The handbook above is the only source of truth. New employees will read the summary in their first week and may act on it (request time off, report an issue, ask about pay timing). A misstated policy can mislead them or create legal exposure, so accuracy matters more than polish. HR reviews every version before release.

OBJECTIVE: Produce a one-page summary of the handbook that tells a new hire what they need to know and do in their first 90 days, with every statement traceable to a handbook section.

SUCCESS TEST:
- The summary body is 550 words or fewer (machine-checkable word count).
- Every bullet ends with a section reference in the form [§x.x] or [p. N] that exists in the handbook.
- The summary ends with the exact disclaimer line given in OUTPUT FORMAT.
- If a previous summary was supplied, the Review Notes list every change from it, or state "No substantive changes."

QUALITY BAR:
- No policy, number, deadline, or benefit appears that is not in the handbook. Paraphrases keep the original meaning, including qualifiers like "eligible after 90 days" or "at manager discretion."
- The material is ordered by what a new hire needs first (pay, hours, time off, who to contact), not by the handbook's chapter order.
- Obligations and deadlines (forms due, reporting duties, probation terms) are stated as concrete actions.
- The tone is plain and welcoming, at about an 8th-grade reading level, with no legalese.
- Anything with legal weight (at-will status, harassment reporting, confidentiality, discipline) is stated neutrally and points to the full section rather than condensing it into a looser promise.

PROCESS:
1) Read the whole handbook. Extract every policy a new hire must act on or will ask about in their first 90 days, with its section reference.
2) Rank the extracted items by first-week relevance and keep what fits in 550 words. Cut detail before you cut a whole topic.
3) For each standard topic below that the handbook doesn't cover, write "Not specified in handbook" in the Review Notes. Don't fill the gap from general knowledge. Standard topics: pay schedule, work hours/attendance, PTO/sick leave, holidays, benefits eligibility, code of conduct, harassment reporting, safety, technology/confidentiality, who to contact.
4) If a previous summary was supplied, keep its approved wording wherever the underlying policy is unchanged, and edit only what the handbook changed.
5) Draft, then check every bullet against its cited section.

OUTPUT FORMAT (Markdown):
# Welcome to {{COMPANY}}: Your Handbook at a Glance
*Based on Employee Handbook {{VERSION_OR_DATE}}*

## Your first week
- … [§x.x]
## Pay and hours
- … [§x.x]
## Time off and benefits
- … [§x.x]
## How we work together
- … [§x.x]
## If something goes wrong
- … [§x.x]
## Who to ask
- … [§x.x]

*This summary is for convenience only. The full Employee Handbook governs; if anything here differs, the handbook controls.*

---
## Review Notes for HR (not for distribution)
- Word count of summary body: N
- Items needing HR/legal attention (ambiguous, contradictory, or legally sensitive wording): …
- Topics not specified in handbook: …
- Changes from previous summary: … (or "No previous summary" / "No substantive changes")
- Confidence that every bullet matches its source: N%

CONSTRAINTS: Use only the handbook text. If two sections contradict each other, don't resolve it; flag it in the Review Notes. Don't include individual names, salaries, or other personal data even if they appear in the handbook; use role titles instead (e.g. "HR Manager").

VERIFICATION PLAN:
[AUTO] Count the words in the summary body (must be 550 or fewer); confirm every bullet has a reference; confirm the disclaimer line is present.
[HUMAN] HR spot-checks the 5 bullets with numbers or deadlines against their cited sections first, since those are the most likely to be wrong.
[HUMAN] HR or legal approves the at-will, harassment, and discipline wording before release.

RUN SETTINGS: Claude Opus 5.5 (Sonnet 5.5 is fine for re-runs with a previous summary) · effort medium · tools: none (file upload only) · thinking on

BEFORE RETURNING: Check the draft against the SUCCESS TEST and QUALITY BAR, report the confidence score in the Review Notes, and name 1-2 knobs HR might want to adjust (e.g. word limit, which section to expand).
```

UNTESTED: I don't have your handbook, so I couldn't run it. The test set should be your current handbook, an older version passed in as "previous summary" input to check that only the changes get edited, and one deliberately trimmed copy with the PTO section removed, to confirm the prompt flags the gap instead of inventing a policy. I also couldn't run the automatic prompt linter here, so I checked the prompt's sections by hand.

Should I save this to the project's prompt library, or run it now if you share the handbook?

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: complete
  assumptions: [handbook text supplied by user, Claude runs it, HR approves each version, handbook not revised monthly]
  unknowns: [handbook format and length in words, whether the HR platform has a built-in summary feature, how often the handbook actually changes]
  outputs: [engineered prompt]
  next: run the 3-case test set, then save to the prompt library
  approval_required: [HR/legal sign-off before distributing any summary]
```