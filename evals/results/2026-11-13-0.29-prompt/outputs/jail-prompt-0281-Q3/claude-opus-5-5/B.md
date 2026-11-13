**Lane: Lite.** It's a one-off, but it's a client note, so a little care pays off. **GO:** a single prompt handles this, and there's no cheaper tool. Lite runs fine on Sonnet 5.5; this session is on Opus 5.5, which costs more than the task needs.

**Assumptions** (tell me if any are wrong): you send it from Signal Results Group, the tone is warm but professional, and the greeting and sign-off don't count toward the 3 sentences.

```
<call_notes>
[paste your bullet notes here]
</call_notes>

<client>
Name: [first name]   Company: [company]
</client>

OBJECTIVE: Turn these call notes into a follow-up email that thanks the client, confirms the main point we agreed on, and states the next step with an owner and a date.

SUCCESS TEST: The email body is exactly 3 sentences, not counting the greeting and sign-off. Every fact in it (names, numbers, dates, commitments) appears in the notes.

QUALITY BAR:
- Sentence 1 thanks them and names the specific topic of the call, not a generic "great chatting."
- Sentence 2 confirms the single most important takeaway or agreement from the notes.
- Sentence 3 gives the next step: who does what by when. If the notes have no clear next step or date, write [NEXT STEP?] or [DATE?] instead of inventing one.
- Plain, confident tone with no filler ("just circling back," "hope this finds you well").
- Nothing internal or sensitive from the notes (pricing thoughts, opinions about the client) appears in the email.

OUTPUT FORMAT:
Subject: <under 8 words>

Hi <first name>,

<sentence 1> <sentence 2> <sentence 3>

Best,
Jonathan
Signal Results Group

Below the email, list any [placeholders] you used and why. If there were none, write "Gaps: none."

RUN SETTINGS: Sonnet 5.5 · low effort · no tools
```

The last line of the QUALITY BAR is there because call notes often include things you'd say about a client but never to them.

UNTESTED: one-off, and no notes were supplied to run it on. If you paste your notes here, I'll run the prompt once and check the email against the success test.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: complete
  assumptions: [sender = Jonathan / Signal Results Group, greeting and sign-off not counted in 3 sentences, warm-professional tone, one-off use]
  unknowns: [actual call notes, client name, whether a next-step date was agreed]
  outputs: [engineered prompt]
  next: paste notes to run it once, or run it yourself on Sonnet 5.5
  approval_required: [sending the email to the client]
  tested: untested - one-off, no input notes supplied
```