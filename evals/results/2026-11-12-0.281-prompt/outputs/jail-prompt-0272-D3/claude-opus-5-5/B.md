**Lane: Lite** (a short one-off client note). **GO, but not with subagents.** This is a single-pass writing task. Subagents would only add hand-off cost; there are no independent streams to split and nothing a separate checker would catch that a word count can't. Below is one prompt that does the job. Lite work runs fine on Sonnet 5.5, so this session's Opus is more than you need here.

**Assumptions:** the email comes from you at Signal Results Group. The client's details aren't given, so they're placeholders and the model is told to leave gaps bracketed rather than invent them. "150 words" means the body only, ±10.

```
<client_details>
Contact name and title: [FIRST NAME, TITLE]
Company: [COMPANY]
What the retainer covers, in 1-2 lines: [SCOPE]
First meeting or milestone, with date: [NEXT STEP + DATE]
One specific moment or goal from the sales conversations (optional): [DETAIL]
</client_details>

<sender>
Jonathan [LAST NAME], [TITLE], Signal Results Group
</sender>

OBJECTIVE: Write a warm, professional thank-you email to the client in client_details, who just signed a 12-month consulting retainer with Signal Results Group. It should leave them confident in the decision and clear on what happens next.

SUCCESS TEST: Body is 140-160 words (not counting subject or signature); exactly one subject line; the 12-month retainer is mentioned once; exactly one concrete next step, with its date taken from client_details.

QUALITY BAR:
- Every name, scope item, and date comes from client_details. If one is missing, write it as a [BRACKETED PLACEHOLDER] and never invent it, because this goes to a real client.
- The first sentence thanks them. The work is described in terms of their goals, not our services.
- No promised results, figures, or ROI. A retainer email that over-promises sets expectations the engagement then has to fight.
- No hype words ("thrilled," "game-changer," "synergy," "excited to partner"). The reader is a busy owner, and plain warmth reads as more credible.
- Someone should be able to read it in 30 seconds and know exactly what happens next.

OUTPUT FORMAT:
Subject: <under 8 words>

<body: 2-3 short paragraphs, 140-160 words>

<signature from sender>

Word count: <n>
```

**RUN SETTINGS:** Sonnet 5.5 · low effort · no tools. Check the word count with a counter rather than trusting the model's own figure.

**QUICK version:** *"Using the client details below, write a 140-160 word thank-you email for a newly signed 12-month Signal Results Group retainer. Thank them first, give one dated next step, promise no results, use no hype, and bracket any missing facts. [details]"*

If you still want it delegated, I can send a two-step set (a writer brief plus an independent checker brief). The only reason to do that is if this becomes a template you'll reuse for every new retainer client, which would move it to the Full lane.

UNTESTED: I didn't run it because the real client details aren't supplied. Fill in the placeholders and run it once.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: complete
  assumptions: [sender is Jonathan at Signal Results Group, "150 words" = body ±10, subagents not warranted for a one-pass task, project prompt library not checked]
  unknowns: [client name/company, retainer scope, first milestone date, any personal detail from sales]
  outputs: [engineered prompt + QUICK version]
  next: fill client_details and run on Sonnet 5.5; offer the writer+checker delegation set if this becomes a reusable template
  approval_required: [human review before sending to the client]
  tested: untested: client details not supplied
```