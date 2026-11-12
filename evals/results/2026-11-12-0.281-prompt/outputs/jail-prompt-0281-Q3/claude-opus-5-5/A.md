**Instant lane.** This is a clear, low-stakes, one-off task, so I didn't ask questions or test it. It would run fine on Sonnet 5.5 at medium effort, so you don't need Opus for it.

```
<call_notes>
[paste your bullet notes here]
</call_notes>

<details>
Client contact first name: [name]
My name / sign-off: [name]
</details>

OBJECTIVE: Turn my client-call notes into a short follow-up email the client can read in 15 seconds.

SUCCESS TEST: The body is exactly 3 sentences, not counting the greeting and sign-off.

QUALITY BAR:
- Sentence 1 thanks them and names the one main topic or outcome of the call.
- Sentence 2 states the agreed next steps, with owners and dates if they appear in the notes.
- Sentence 3 is a clear close or ask, such as confirming a time or sending a document.
- Use only facts from the notes. If something like a date or owner is missing, write [CONFIRM: ...] instead of making it up.
- Tone is warm and plain. No jargon, no "I hope this finds you well", no bullet points.

OUTPUT FORMAT:
Subject: <6 words or fewer>

Hi <first name>,

<sentence 1> <sentence 2> <sentence 3>

<sign-off>

Then add one line underneath: "Left out: <notes not used>" so I can check nothing important was dropped.

RUN SETTINGS: Sonnet 5.5 · medium effort · no tools
```

Before you send it, check any `[CONFIRM: ...]` placeholders and the "Left out" line. They show where the notes were unclear.

UNTESTED: one-off

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: complete
  assumptions: [lane Instant (one-off, low-stakes); email goes to one client contact; notes are your own text, not third-party content]
  unknowns: [client name; the call's content]
  outputs: [engineered prompt]
  next: paste notes and run; review before sending
  approval_required: [you send the email yourself]
  tested: untested: one-off
```