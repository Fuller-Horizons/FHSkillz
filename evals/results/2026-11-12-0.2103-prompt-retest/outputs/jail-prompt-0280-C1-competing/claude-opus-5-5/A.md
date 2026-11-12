The handbook probably doesn't change every month, so you don't need a fresh summary every month. Run the prompt once, have HR approve the page, and hand out that approved page. Rerun it only when the handbook is revised. If you rerun it monthly anyway, the wording will drift a little each time, and policy wording shouldn't drift.

**Prompt** (paste the handbook into the tag, or attach the file):

```
<handbook>
[paste the full employee handbook here, or attach the file]
</handbook>

<previous_summary>
[optional: last approved one-page summary. Leave empty on the first run.]
</previous_summary>

OBJECTIVE: Write a one-page summary of this handbook so a new hire knows what matters in their first 90 days and where to find the full policy.

CONTEXT: New hires will read this on day one. HR will review it before it goes out. If a previous summary is provided, keep its wording wherever the handbook hasn't changed, and list what you changed at the end.

QUALITY BAR:
- Every statement comes from the handbook. Nothing is added from general HR knowledge.
- Each item cites its handbook section or page number.
- It covers, if the handbook includes them: hours and attendance, pay and timekeeping, PTO and leave, benefits eligibility, conduct and harassment reporting, safety, IT and confidentiality, and who to contact.
- Specific numbers and deadlines (accrual rates, waiting periods, notice periods) are copied exactly, not rounded.
- It is written in plain language at about an 8th-grade reading level.

CONSTRAINTS:
- Don't summarize legal statements such as at-will employment or arbitration. Quote them exactly or point to the section. Paraphrasing them creates legal risk.
- If a topic is unclear or contradicts another part of the handbook, write "See HR" instead of guessing.

OUTPUT FORMAT:
Title: "[Company] Handbook: New Hire Summary"
Then 6-9 short headed sections, each with 2-4 bullets and a (§ x.x / p. x) citation on every bullet.
"Key contacts" line.
Footer: "This summary does not replace the full handbook. If they differ, the handbook governs. Version: [handbook date]."
After the page, separately: "Flagged for HR review:" listing anything unclear or contradictory, then "Changes from previous summary:" (or "First version").

SUCCESS TEST: 450 words or fewer, not counting the review notes after the page. Every bullet has a citation. The footer is present. A spot-check of 5 citations shows each one matches the handbook.

RUN SETTINGS: Claude Sonnet 5.5 · medium effort · file upload only, no web search
```

**Short version** (if you want something smaller):

```
<handbook>[paste or attach]</handbook>
Summarize this handbook into one page (450 words or fewer) for new hires. Use only what the handbook says, cite the section or page on every bullet, copy numbers exactly, quote legal language word for word, and write "See HR" for anything unclear. End with the footer: "This summary does not replace the full handbook."
```

UNTESTED: I don't have your handbook, so I couldn't run it. Before the first use, spot-check 5 citations in the output against the handbook.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: complete
  assumptions: [audience is new hires in their first 90 days, HR reviews before it goes out, handbook is text you can paste or upload, Sonnet 5.5 is good enough for this]
  unknowns: [how often the handbook actually changes, whether legal must approve the summary]
  outputs: [engineered prompt + short version]
  next: run once → HR approves → reuse the approved page; rerun only when the handbook is revised
  approval_required: [HR/legal sign-off before the summary goes to employees]
  tested: untested - handbook not provided; check: spot-check 5 citations on the first run
```

I can save this to your project's prompt library if you'd like.