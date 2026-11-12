**Gate: GO on the prompt. Skip the subagents.** A 150-word note is a single pass with nothing to split up, so subagents would add cost without improving quality. I've written one prompt on stated defaults instead. A checker is the only subagent role that makes sense here, so I've added it as an optional step below. This is Lite-lane work, so Sonnet 5.5 is enough to run it.

### Main prompt (copy this)

```
<client_details>
Contact first name: [ ]
Company: [ ]
Retainer start date: [ ]
Engagement focus (one line): [ ]
Next step (what, when, who): [ ]
Sender name and title: [ ] of Signal Results Group
</client_details>

OBJECTIVE: Write a warm, professional thank-you email from Signal Results Group to a client who just signed a 12-month consulting retainer, and confirm the next step.

SUCCESS TEST: The body (excluding subject and signature) is 140-160 words; there is exactly one subject line; the body contains "12-month" and the next step from client_details.

QUALITY BAR:
- Thanks them for this specific decision, not in generic terms.
- Names their engagement focus in one concrete phrase.
- States one clear next step with its date and owner.
- Promises no results, figures, or deliverables that are not in client_details, because a thank-you note that overpromises reads as a commitment.
- Plain, confident tone: no stock phrases such as "embark on this journey", and at most one exclamation point.

CONSTRAINTS: If a detail is blank, leave a [bracketed placeholder] instead of inventing it. Made-up names or dates in a client email cost trust.

OUTPUT FORMAT:
Subject: <one line>

<body, 140-160 words>

<signature>
Word count: <N>

RUN SETTINGS: Sonnet 5.5 · low effort · no tools
```

### Optional checker (use this if you still want a subagent)

Run it in a fresh session so it doesn't see how the draft was written.

```
<client_details>…same block as above…</client_details>
<draft_email>…paste the output…</draft_email>

OBJECTIVE: Check the draft against the client details. Do not rewrite it.

SUCCESS TEST: Return exactly 5 lines, each PASS or FAIL.

OUTPUT FORMAT:
1. Body word count is 140-160 (state the count): PASS/FAIL
2. Contains "12-month" and the stated next step: PASS/FAIL
3. No names, dates, results, or deliverables that are missing from client_details (quote any): PASS/FAIL
4. One subject line, at most one exclamation point: PASS/FAIL
5. Names the engagement focus specifically: PASS/FAIL

RUN SETTINGS: Sonnet 5.5 · low effort · no tools
```

**Defaults I assumed:** the email comes from Signal Results Group and is addressed to one contact. "150 words" means the body only, with a tolerance of ±10.

**Checking:** The linter script wouldn't run (it gave a parser error), so I checked the prompt by hand. It has every required section, the success test can be checked by machine, and the output format is concrete.

UNTESTED: you haven't supplied client details yet, so there was nothing to run it on. Fill in the block and I'll run it once.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: complete
  assumptions: [sender = Signal Results Group, single named contact, 150 words = body ±10, subagents replaced by one prompt plus an optional checker]
  unknowns: [client name, company, start date, engagement focus, next step/kickoff date, sender name]
  outputs: [engineered prompt, optional checker prompt]
  next: fill client_details, then run the main prompt on Sonnet 5.5, then optionally the checker
  approval_required: [sending the email to the client]
  tested: untested: client details not supplied; linter errored, manual structure check passed
```