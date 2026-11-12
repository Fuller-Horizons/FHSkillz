**Lane: Lite** (a short one-off client note). **Gate: GO, but not with subagents.** A 150-word email is a single-pass task. Splitting it across subagents adds cost and makes the voice uneven, and it would not improve the email. One prompt does the job, so that's what I wrote instead.

I based it on prompt #141 ("Thank-You Communication") from the McKinsey prompt PDF in your Project. That prompt says the thanks should name something specific the client made possible, not just be polite.

```
<client_details>
Client name and title: [e.g., Dana Ruiz, Owner]
Company: [e.g., Harbor Ridge Mechanical]
What the retainer covers: [e.g., monthly ops reviews, pricing strategy, Q1 hiring plan]
One specific thing they said or did during the sales process: [e.g., "asked hard questions about our Nassau data"]
First milestone or next meeting: [e.g., kickoff Tuesday 12/2, 10am, on-site]
Sender name, title: [e.g., Jonathan, Signal Results Group]
</client_details>

OBJECTIVE: Write a thank-you email from Signal Results Group to a client who just signed a 12-month consulting retainer. It should make them feel they chose well and know exactly what happens next.

SUCCESS TEST: Body is 140-160 words (excluding subject and signature); no [bracketed] placeholders remain; exactly one next step with a date.

QUALITY BAR:
- Names the specific detail from <client_details> and says what it makes possible. Generic gratitude ("we're thrilled to partner") alone fails.
- Mentions the 12-month scope in concrete terms, with no new promises beyond what's listed in <client_details>.
- Peer-to-peer tone, as one business owner writing to another: warm, plain, no hype words (thrilled, excited, synergy, journey).
- Ends on the single next step from <client_details>, not an open-ended "let me know if you need anything."

OUTPUT FORMAT:
Subject: <under 8 words>

<body, 140-160 words, 3 short paragraphs>

<sender name, title>
Signal Results Group

Word count: <n>

If any field in <client_details> is missing, write the email without it and list the missing fields under the word count. Don't invent facts about the client.

RUN SETTINGS: Claude Sonnet 5.5 · low effort · no tools
```

**Assumptions:** you send the email, the tone is peer-to-peer (owner to owner), and the next step is a kickoff. Change the QUALITY BAR lines if any of these is wrong.

UNTESTED: no client details were given, so I couldn't run it. Fill in `<client_details>`, run it once, and check the word count line.

If you want subagents to actually check the email, one honest use: after the draft is written, have a separate model read it as the client would and flag anything generic. For 150 words, reading it yourself takes 30 seconds and does the same job.

Should I save this to `claude/prompt-library.md`, or run it once you send the client details?

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: complete
  assumptions: [user is sender, peer-to-peer tone, next step is a kickoff, Sonnet 5.5 is sufficient]
  unknowns: [client name, retainer scope, specific detail, first milestone date]
  outputs: [engineered prompt (subagent method declined: single-pass task)]
  next: fill client_details and run; optionally save to prompt-library
  approval_required: [sending the email to the client]
  tested: untested: client details not supplied
```