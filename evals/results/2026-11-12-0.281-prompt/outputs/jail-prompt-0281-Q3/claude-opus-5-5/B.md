**Lane: Lite.** It's a quick one-off, but the email goes to a client, so the prompt guards against invented promises or dates. **Gate: GO.** This is a good fit for AI. Sonnet 5.5 at medium effort is enough; you don't need Opus.

**Assumptions:**
- The email comes from you at Signal Results Group.
- The tone is warm and professional, not salesy.
- The email recaps the call, confirms next steps, and closes.
- It includes a subject line.

**The prompt** (paste your notes into the tags):

```
<call_notes>
[paste your bullet notes here]
</call_notes>

<client>
Name: [first name] · Company: [company]
</client>

OBJECTIVE: Turn my call notes into a 3-sentence follow-up email I can send today from Signal Results Group.

SUCCESS TEST: The body is exactly 3 sentences. Every commitment, date, number, and name in it appears in <call_notes>.

QUALITY BAR:
- Sentence 1 thanks them and names the one or two most important things we discussed.
- Sentence 2 says who does what next and when, using only what's in the notes. If the notes have no next step, write "[NEXT STEP?]" instead of making one up. A made-up promise to a client is worse than a gap.
- Sentence 3 is a short close that suggests one clear reply or action.
- The tone is plain, warm, and professional. No filler like "I hope this finds you well" and no sales pitch.
- Leave out anything in the notes that reads as internal-only, such as pricing thoughts or opinions about the client.

OUTPUT FORMAT:
Subject: <under 8 words>

Hi <first name>,

<3 sentences>

Best,
Jonathan

Then, below a line: "Left out:" and a list of any notes you didn't use, or "none".

RUN SETTINGS: Sonnet 5.5 · medium effort · no tools
```

The "Left out:" list lets you see at a glance whether anything important was dropped.

UNTESTED: no call notes were provided to test on. Before sending, count the sentences and check that every date in the email is in your notes.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: complete
  assumptions: [sent from Jonathan at Signal Results Group, warm professional tone, 3 sentences = recap / next steps / close, subject line included]
  unknowns: [the actual call notes, client name]
  outputs: [engineered prompt]
  next: paste notes and run; check the email before sending
  approval_required: [sending the email to the client]
  tested: untested: one-off, no call notes provided
```