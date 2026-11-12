**GO, with one change:** don't rerun this every month. If the handbook hasn't changed, each run will still word things differently. New hires could get versions that disagree, and every new version needs HR to check it again. Run it once, have HR approve the result, and send that same page to every new hire. Rerun only when the handbook changes.

```
<handbook>
{{PASTE FULL HANDBOOK TEXT}}
</handbook>

OBJECTIVE: Turn the handbook above into a one-page summary a new hire can read in 5 minutes on day one.

CONTEXT: The reader is a new employee. The handbook is the only source. The page is an orientation aid, not policy, so it must never contradict or add to the handbook. A wrong date, number, or rule can cause pay, leave, or legal problems.

SUCCESS TEST: no more than 450 words; every bullet ends with a handbook section or page reference, e.g. (§4.2) or (p. 12); every number, date, or deadline appears word for word in the handbook; the last line is exactly: "This is a summary. The Employee Handbook governs; ask HR with questions."

QUALITY BAR:
- Covers what a new hire needs in the first 90 days: pay and timekeeping, hours and attendance, time off and leave, benefits enrollment deadlines, conduct and safety, technology and confidentiality, who to contact.
- Puts deadlines and required actions first, in a "Do this first" box.
- Plain language, no legalese, under 20 words per bullet.
- Leaves out anything the handbook doesn't say. Puts any gaps under "Ask HR" rather than guessing.

OUTPUT FORMAT:
# Welcome to [Company]: Your Handbook at a Glance
**Do this first** (3-5 bullets: action, deadline, ref)
**Pay & Hours** · **Time Off** · **Benefits** · **Conduct & Safety** · **Tech & Confidentiality** (2-4 bullets each, each with a ref)
**Who to contact** (role: how to reach them, only if the handbook gives it)
**Ask HR** (topics the handbook leaves unclear, or "none")
[required last line]

RUN SETTINGS: Claude Opus 5.5 · medium effort · no tools; attach the handbook as a file or paste the full text.
```

**QUICK version:** "Summarize the attached handbook into a one-page new-hire guide (≤450 words). Use only what the handbook says, cite a section for every bullet, put deadlines first, and end with 'The Employee Handbook governs.'"

UNTESTED: I don't have your handbook, so I couldn't run it. Before you use it the first time, run it on your handbook and check every number and deadline against the source.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: complete
  assumptions: [handbook is text-extractable, US employer, reader is a general new hire, one page means about 450 words]
  unknowns: [state-specific policies, whether the handbook has numbered sections]
  outputs: [engineered prompt + QUICK version]
  next: run once on the real handbook, HR approves, save it to the prompt library
  approval_required: [HR/legal sign-off before handing the page to new hires]
  tested: untested: no handbook supplied
```