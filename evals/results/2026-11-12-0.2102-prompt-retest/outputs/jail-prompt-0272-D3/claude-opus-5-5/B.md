**Lane: Instant.** The goal is clear and a bad draft costs little. **Gate: GO, but without the subagents.**

**I'm pushing back on the subagents.** A 150-word email is one creative-writing task. A team of subagents would spend more tokens coordinating with each other than writing, and the email would be no better. One prompt is enough. If you want a second look, add the optional reviewer prompt below. That's the most I'd split this, and only because a draft-then-critique pass does help with tone.

**Inputs you need to fill in.** I won't make these up: client contact name, company, what the engagement covers, the first milestone, and your name and title. The firm is Signal Results Group, taken from the project.

---

### Prompt 1: Writer (all you need)

```
METADATA: inputs: client_first_name, client_company, engagement_focus, first_milestone, sender_name, sender_title · outputs: email · params: temperature 0.7 · requires: none · produces: email_draft
ROLE: Senior partner at a boutique business-consulting firm; writes warm, plain-spoken client notes, never salesy.
CONTEXT: Signal Results Group just signed a 12-month consulting retainer with <client_company>. Contact: <client_first_name>. Engagement focus: <engagement_focus>. First milestone/next step: <first_milestone>. Sender: <sender_name>, <sender_title>.
OBJECTIVE: Write a thank-you email that makes the client feel confident they chose the right partner and clear on what happens next.
SUCCESS TEST: Body is 140–160 words (count it); names the client company and "12-month" once each; states one concrete next step with a timeframe; contains zero placeholders in <> brackets; no exclamation marks beyond one.
PROCESS: 1) Thank them specifically for the trust, not generically. 2) Tie the partnership to their stated engagement focus. 3) Give the first milestone and when it happens. 4) Close with a direct line of contact.
OUTPUT FORMAT:
Subject: <under 8 words>

Hi <first name>,

<body, 2–3 short paragraphs>

<sign-off>
<sender_name>, <sender_title>
Signal Results Group
Word count: <n>
CONSTRAINTS: No clichés ("thrilled", "excited to embark", "journey", "synergy"). No promises of specific results or ROI. No invented facts beyond CONTEXT. Plain text, no bullets.
BEFORE RETURNING: Count words; if outside 140–160, revise. Check each SUCCESS TEST item and list any that fail.
```

### Prompt 2: Reviewer (optional, run in a fresh session or with a different model)

```
METADATA: inputs: email_draft, CONTEXT block from Prompt 1 · outputs: verdict, revised_email · params: temperature 0.2 · requires: email_draft · produces: final_email
ROLE: Skeptical client-relations editor.
OBJECTIVE: Find the weakest line in the draft and fix it without breaking the constraints.
SUCCESS TEST: Revised body is still 140–160 words; every SUCCESS TEST item from Prompt 1 passes; no new facts added that are absent from CONTEXT.
PROCESS: 1) Flag any line that sounds generic, salesy, or makes an outcome promise. 2) Flag any fact not in CONTEXT. 3) Rewrite only the flagged lines.
OUTPUT FORMAT:
Issues: [line → problem → fix]  (or "None")
Revised email: <full email>
Word count: <n>
CONSTRAINTS: Don't change the substance of the draft, only fix weak lines. If there are no issues, return the draft unchanged.
```

**Chain check (done by hand):** Prompt 2 needs `email_draft`, and Prompt 1 produces it. Each step has its own success test. The human checkpoint is that you read the draft before sending it.

**How to check the result:** count the words automatically (`wc -w` on the body works). Then read it yourself and ask whether it sounds like you.

Do you want me to save this to the project's prompt library, or run it now once you give me the client details?

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: partial
  assumptions: [sender firm is Signal Results Group, plain-text email, user wants prompts rather than execution]
  unknowns: [client name/company, engagement focus, first milestone, sender name/title]
  outputs: [engineered prompt, optional 2-step chain]
  next: fill inputs → run Prompt 1 → optionally Prompt 2
  approval_required: [sending the email to the client]
```