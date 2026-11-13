**Lane: Lite.** It's a one-off, but the email goes to a client, so I stated my assumptions instead of asking questions. This session runs on Opus 5.5; Sonnet 5.5 is enough for this lane and costs about a tenth as much.

**GO.** A single prompt fits this task, and I don't have a better tool to point you to.

**Assumptions:** the email is from you to the client's main contact. The tone is warm and professional. Commitments only appear in the email if they're in your notes. There's no signature block, because your email client adds one.

```
<call_notes>
[paste your bullet notes here]
</call_notes>

<context>
Client name: [name]
My name: [your name]
</context>

OBJECTIVE: Turn my call notes into a 3-sentence follow-up email to the client that I can send today with light or no edits.

SUCCESS TEST: The email body is exactly 3 sentences, and every fact, date, number and commitment in it appears in <call_notes>.

QUALITY BAR:
- Sentence 1 thanks them and names the main topic or result of the call.
- Sentence 2 gives the most important agreed point or decision.
- Sentence 3 states the next step, with owner and date if the notes have them.
- Nothing is invented. If the notes don't give a next step, write [NEXT STEP?] so I fill it in rather than you guessing.
- The tone is plain, warm and professional, with no filler like "I hope this finds you well."

OUTPUT FORMAT:
Subject: <under 8 words>

Hi <client first name>,

<sentence 1> <sentence 2> <sentence 3>

<my first name>

Then, on a separate line, list any [BRACKETED] gaps I need to fill. If there are none, write "Gaps: none".

RUN SETTINGS: Sonnet 5.5 · low effort · no tools
```

UNTESTED: no notes were supplied. Paste your bullets here and I'll run the prompt once on them.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: complete
  assumptions: [sent from user to client's main contact, warm-professional tone, no signature block, commitments only from notes]
  unknowns: [actual call notes, client name]
  outputs: [engineered prompt]
  next: run the prompt on today's notes
  approval_required: [user reviews email before sending]
  tested: untested: no call notes supplied
```