**STOP on the subagents.** Here's the single prompt I'd use instead.

**Why not subagents:** a 150-word email is one short piece of writing. Nothing in it splits into independent parts, and it fits easily in one context. Using several agents would cost a few times the tokens and make the email worse, because one writer gives it one voice. Delegation only makes sense when the parts are truly independent, and these aren't. A quick read before you hit send does the job a checker agent would.

**What I'm doing instead:** one prompt, based on prompt #141 (Thank-You Communication) from the McKinsey playbook in your Project. Its key idea is to "go beyond courtesy." It runs on one model, and you review the draft before sending.

```
<client_details>
Client company: [CLIENT COMPANY]
Recipient name and role: [NAME, TITLE]
What the 12-month retainer covers: [e.g., monthly ops review, margin improvement, owner advisory]
The client's main goal or pain point, in their words if possible: [GOAL]
First concrete next step and date: [e.g., kickoff working session, week of Dec 1]
Sender: [YOUR NAME], Signal Results Group
</client_details>

OBJECTIVE: Write a thank-you email to the client above, who just signed a 12-month consulting retainer with Signal Results Group. It should make them feel the decision was right and show them exactly what happens next.

SUCCESS TEST: The body is 140-160 words, not counting the subject line and signature. It names the client's goal and the first next step with its date.

QUALITY BAR:
- Thanks them for trusting us, then names what the retainer will make possible for their goal, not just "we look forward to working with you."
- Says the concrete next step, with its date and who does what.
- Sounds confident and warm, written peer to peer. No groveling, no hype, no "synergy" or "excited to partner."
- Promises nothing about results or numbers that isn't in client_details.
- If a field in client_details is blank, put a [BRACKETED PLACEHOLDER] there instead of making something up.

OUTPUT FORMAT:
Subject: <under 8 words>

<email body, 140-160 words, 3 short paragraphs>

<signature>

Word count (body): <n>

RUN SETTINGS: Claude Sonnet 5.5 · low effort · no tools
```

**QUICK version** (if you'd rather not fill in the form): *"Write a 150-word thank-you email from Signal Results Group to [NAME] at [COMPANY], who just signed a 12-month retainer for [SCOPE]. Name what it makes possible for [GOAL], state the next step ([STEP, DATE]), and keep it warm and peer-to-peer with no hype or promised results."*

**What's missing:** I don't know which client this is or what the retainer covers. The Project has briefs for Harbor Ridge Mechanical, Hicks Nurseries and Zephyrine Brookhaven Millwork, but none mentions a signed retainer. If it's one of them, tell me which and I'll fill in the details.

UNTESTED: this is a one-off email and the client details aren't filled in yet. The word-count line lets you check the length yourself. Read the draft before sending.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: stop
  assumptions: [one-off email, sender reviews before sending, Sonnet is enough for a short email]
  unknowns: [client identity, retainer scope, client goal, first next-step date]
  outputs: [STOP on delegation; reframed single prompt + QUICK version]
  next: fill client_details and run, or name the client and I'll fill it from Project docs
  approval_required: [sending the email to the client]
  tested: n/a
```

I can save this to `claude/prompt-library.md`, or run it now if you name the client.