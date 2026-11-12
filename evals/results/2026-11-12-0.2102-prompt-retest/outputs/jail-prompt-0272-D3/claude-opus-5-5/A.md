**Method check:** subagents don't fit this. A 150-word email is one short writing job with no separate parts to split, and splitting it would cost more tokens and give a less consistent voice. Below is one prompt instead. If you want a second opinion on the draft, use the optional check prompt underneath it.

**GO** (Lite lane: a one-off client note). Your library has no thank-you prompt, so I modeled this on `cold-outreach-email v1` and on the book's #141 ("go beyond courtesy").

**Assumptions:** Signal Results Group is sending it to the client's main decision-maker. The goal is to thank them and set up a clear first step, not to sell. All client facts come from you.

**Inputs you need to fill in (I've left them blank rather than make them up):** client name and contact, what the retainer covers, the kickoff date or next step, one specific thing from the sales process worth mentioning, and the sender's name and title.

```
<client_facts>
Client company: {{COMPANY}}
Recipient (name, title): {{RECIPIENT}}
Retainer scope (what we'll work on): {{SCOPE}}
Start / first milestone or next step: {{NEXT_STEP}}
One specific detail from the sales conversations worth acknowledging: {{DETAIL}}
Sender (name, title): {{SENDER}}, Signal Results Group
</client_facts>

CONTEXT: The client just signed a 12-month consulting retainer with Signal Results Group. This email goes out as written to the person who signed, so any invented fact, promise, or number damages trust at the very start of the relationship.

OBJECTIVE: Write a warm, specific thank-you email that confirms the partnership and makes the first step obvious.

SUCCESS TEST: the body is 140-160 words (count it); it includes a subject line under 8 words; it uses the recipient's name and at least one detail taken word for word from <client_facts>; it contains exactly one next step, which matches {{NEXT_STEP}}; it contains no numbers, results, or commitments that aren't in <client_facts>.

QUALITY BAR:
- Thanks them for a specific reason (their trust, or the {{DETAIL}}), not a generic "thank you for your business".
- Connects the retainer scope to what the client is trying to achieve, in their terms.
- Promises nothing beyond what's in the input: no guaranteed outcomes, no new deliverables.
- Uses plain, confident language with no hype words ("synergy", "excited to revolutionize") and no flattery.
- Ends with one clear next step, followed by the signature.

OUTPUT FORMAT:
Subject: <under 8 words>

<Hi {{RECIPIENT first name}},>
<body: 3 short paragraphs (thanks, what's ahead, next step), 140-160 words total>

<{{SENDER}}>
Signal Results Group

Then one line: "Word count: N"

RUN SETTINGS: Sonnet 5.5 · effort low · tools: none
```

**Optional independent check.** Run this as a separate pass, ideally on a different model (Haiku 5.5 is enough):

```
<client_facts>{{same block as above}}</client_facts>
<draft>{{paste the email}}</draft>

OBJECTIVE: Check whether the draft can be sent as written.
SUCCESS TEST: return PASS or FAIL for each of these 5 checks: (1) body is 140-160 words; (2) every fact, name, and date in the draft appears in client_facts; (3) exactly one next step, matching the one in client_facts; (4) no promised outcomes or new deliverables; (5) no hype or flattery.
OUTPUT FORMAT: 5 lines, "N. PASS|FAIL — <quote of the offending text, or 'ok'>", then "SEND-READY: yes|no".
RUN SETTINGS: Haiku 5.5 · effort low · tools: none
```

UNTESTED: I couldn't run the prompt because the client facts weren't provided. Give me the five inputs and I'll run it once and check the result. I can also add it to `claude/prompt-library.md` as `client-thank-you-email v1` once it's tested.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: partial
  assumptions: [sender is Signal Results Group, recipient is the signer, goal is thanks plus a first step and not upsell, subagents dropped because this is a one-pass task]
  unknowns: [client name, retainer scope, next step/kickoff date, sales-process detail, sender name]
  outputs: [engineered prompt + optional checker prompt]
  next: user supplies inputs, then one test run, then optionally save to the prompt library
  approval_required: [sending the email to the client]
  tested: untested - client facts not supplied
```