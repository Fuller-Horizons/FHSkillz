Subagents are the wrong method here. A 150-word email is one writing pass, so splitting it across agents would cost more and make it read like it was written by committee. Below is one prompt that does the job instead.

**Lane:** Lite, because it's a short one-off client note. **Gate: GO.** The task doesn't need delegation. Sonnet 5.5 is enough to run it, so this Opus session is more than the task needs.

**Assumptions** (change any of these if they're wrong):
- It goes out from Signal Results Group.
- The sender is the engagement lead.
- The tone is warm and professional, not salesy.
- The email names one concrete next step, which is the kickoff.

**Missing inputs:** fill in the `<...>` fields below. I left them blank so nothing gets made up.

```
<client_details>
Client company: <company name>
Contact first name: <first name>
Engagement focus: <e.g., "operations and margin improvement across the HVAC service division">
Retainer start date: <date>
Kickoff meeting: <date, time, format — or "to be scheduled">
One specific detail from the sales process: <e.g., "your point about technician retention being the real growth constraint">
</client_details>

<sender>
Name: <name>
Title: <title>
Firm: Signal Results Group
</sender>

OBJECTIVE: Write a thank-you email to the contact above, who just signed a 12-month consulting retainer. It should leave them confident they made the right call and clear on what happens next.

SUCCESS TEST:
- The body is 140–160 words. The subject line and signature block don't count.
- The contact's first name, the company name, and "12-month" (or "twelve-month") each appear at least once.
- Exactly one next step, with the kickoff date from <client_details>, or "to be scheduled" if no date was given.
- No brackets, placeholders, or made-up facts. Use only details from <client_details> and <sender>.

QUALITY BAR:
- It mentions the specific detail from the sales process, so it reads as written for this client and not as a template.
- It thanks them once, early, and moves on. No repeated gratitude, no flattery.
- It refers to the engagement focus in plain language and promises no results, numbers, or timelines beyond what's given. This is a client-facing commitment.
- It sounds like a senior consultant writing to a peer: short sentences, no buzzwords ("synergy," "leverage," "excited to partner").
- It ends on the next step, not on a vague offer like "let me know if you have questions."

OUTPUT FORMAT:
Subject: <under 8 words>

<body, 140–160 words, 3 short paragraphs>

<sender name>
<title>
Signal Results Group

Word count (body): <n>

RUN SETTINGS: Sonnet 5.5 · low effort · no tools
```

If you want an independent check before sending, `jail-verify` can review the draft against the SUCCESS TEST above. That replaces a checker subagent.

UNTESTED: the client details above aren't filled in yet. I didn't run the prompt, because doing it on placeholders would only show the format, not whether it meets the quality bar. Send me the details and I'll do one test run.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: partial
  assumptions: [sender is the engagement lead at Signal Results Group, warm-professional tone, single next step is the kickoff, subagents dropped because the task is one writing pass]
  unknowns: [client company, contact name, engagement focus, start and kickoff dates, specific detail from the sales process, sender name and title]
  outputs: [engineered prompt]
  next: fill client_details and run on Sonnet 5.5; optionally use jail-verify before sending
  approval_required: [human review before the email is sent to the client]
  tested: untested: client details not supplied
```