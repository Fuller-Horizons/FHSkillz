**GO, but without subagents.** A 150-word email is one short writing task. Subagents would add cost and a merge step without improving the email, so this is a single prompt. If you still want to delegate, the only split worth having is a writer plus an independent checker, and I can write that pair.

**Lane:** Lite (a short one-off client note). This lane runs fine on Sonnet 5.5, so you don't need Opus for it.

**Assumptions:** the email comes from Signal Results Group; the tone is warm and professional; "150 words" means the body only, within ±10 words.

```
<client_details>
Contact name:
Company:
Engagement focus (one line, in their words):
Next step + date (e.g., kickoff call Tue Nov 18):
Sender name and title:
</client_details>

OBJECTIVE: Write a thank-you email from Signal Results Group to a client who just signed a 12-month consulting retainer. It should confirm they made a good decision and tell them exactly what happens next.

SUCCESS TEST: The body (excluding subject line and signature) is 140–160 words; there is exactly one subject line; the body names the contact and states the next step with its date.

QUALITY BAR:
- The thanks is specific to their decision and their engagement focus, not a generic "thanks for your business."
- There is one concrete next step, with a date and the person who owns it.
- It makes no promises of specific results or ROI, because this is a client-facing document and an overpromise becomes a liability.
- It reads as one person writing to another: no hype words and no more than one exclamation mark.
- Every fact comes from client_details. If a field is blank, write a [bracketed placeholder] in its place, because an invented detail in a client email is worse than a visible gap.

OUTPUT FORMAT:
Subject: <under 8 words>

<body, 140–160 words, 2–3 short paragraphs>

<signature: sender name, title, Signal Results Group>

Word count (body): <N>

RUN SETTINGS: Sonnet 5.5 · medium effort · no tools
```

**Before you run it, fill in:** the contact name, company, engagement focus, next step and date, and sender. I don't have any of these, so I didn't make any up.

**Check the result:** paste the body into a word counter. Models often get their own word counts wrong.

UNTESTED: the client details aren't supplied yet, and testing on made-up details would prove nothing. Send me the five fields and I'll run it once and check it against the success test.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: complete
  assumptions: [sender is Signal Results Group, warm-professional tone, 150 words = body ±10, subagents dropped (one-pass task)]
  unknowns: [contact name, company, engagement focus, next-step date, sender name/title]
  outputs: [engineered prompt]
  next: fill client_details and run on Sonnet 5.5; optionally I run it once and check the word count
  approval_required: [human review before sending the email to the client]
  tested: untested: client details not supplied
```