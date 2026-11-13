I used the Full lane because you'll reuse this prompt and the summaries go to clients. I checked whether an existing skill already does this job. `jail-summarize` could handle one call at a time, but a fixed prompt gives every owner the same format and runs cheaply on Sonnet. **GO.**

Your request already covered the reader, the reading level, the length, the ending and the input size, so I used those as given.

## v1 prompt (copy this)

```
<call_notes>
[Paste your discovery-call notes here, bullets as-is, typos and all.]
</call_notes>

<call_details>
Company: [name]
Owner: [first name]
Call date: [date]
</call_details>

OBJECTIVE: Turn the call notes above into a one-page summary I can send to the owner of an HVAC company, written so they can read it on a phone in about two minutes and come away knowing what we heard, what it is costing them, and the one thing to do next.

CONTEXT: I'm a business consultant with Signal Results Group. The reader is the owner of a small or mid-size HVAC contractor (typically 10-80 employees, residential and/or light commercial service, install and maintenance agreements). They know their trade cold but have little patience for consulting language. They read on a phone between jobs, so short paragraphs and short bullets beat anything wide or dense. The summary goes out under my name, so anything wrong or invented costs me trust with the owner.

CONSTRAINTS:
- Use only what is in the notes. If a number, name or claim isn't in the notes, leave it out; the owner will notice a figure they never gave. When you connect two facts into a conclusion the notes don't state outright, open it with "It looks like" so it reads as our read, not their words.
- Plain English at about an 8th-grade reading level. Say "cash coming in" rather than "cash flow velocity". If an industry term the owner used helps (call-backs, maintenance agreements, techs, tickets, shoulder season), keep it; drop consulting terms (EBITDA, synergies, leverage, KPI, optimize) or replace them with plain words.
- No tables, no columns, no nested bullets: they break on a phone screen.
- Stay at or under 350 words for the summary, so it fits one page and a two-minute read.
- End with exactly one recommended next step. One action, who does it, and by when, plus one sentence on why it matters to them. If the notes point to several possible steps, choose the one that most directly addresses the owner's biggest stated problem and mention no others.
- If something important was left open on the call (a number they'll get back to us on, a decision partner not yet involved), put it under "Still to confirm" rather than guessing.

QUALITY BAR (each line is pass/fail):
1. Every number, name and quote in the summary can be found in the notes.
2. The owner's top problem, in their terms, is in the first two sentences.
3. A busy owner could act on the next step without asking a question: it names an action, a person, and a date or timeframe.
4. No sentence is longer than 25 words, and no consulting jargon is left unexplained.
5. Nothing in the notes that the owner said matters most is missing.

OUTPUT FORMAT: Return the summary in exactly this shape (plain text with light markdown, bold headings only), then the check block after the line of dashes.

**[Company]: what we heard on [call date]**

**The short version**
[2-3 sentences: their biggest problem in their words, why it matters in dollars or time if the notes give a figure, and the direction we'd take.]

**What's working**
- [2-3 bullets, one line each]

**What's holding you back**
- [2-4 bullets, one line each, most costly first, with the owner's figures where given]

**Still to confirm**
- [0-3 bullets; omit this whole section if nothing is open]

**Recommended next step**
[One action. Who does it. By when.] [One sentence on why it matters to them.]

[My name], Signal Results Group

----------
CHECK (for me, not the owner):
- Word count of the summary: [n]
- Each figure used, with the note bullet it came from: [figure → "quoted note text"]
- Inferences (the "It looks like" lines): [list, or "none"]
- Notes I left out and why: [list, or "none"]

SUCCESS TEST: The summary above the dashes is 350 words or fewer, contains all five bold headings in that order ("Still to confirm" may be omitted), contains no table or nested bullet, and has exactly one action under "Recommended next step"; every figure in the CHECK list maps to quoted text from the notes.

RUN SETTINGS: Claude Sonnet 5.5 · medium effort · no tools · API max_tokens 3000 (room for thinking plus a ~500-word reply).
```

**QUICK version** (for quick use in chat):
```
<call_notes>[paste notes]</call_notes>
Turn these discovery-call notes into a one-page summary (350 words max) for the owner of an HVAC company who will read it on a phone. Plain English, short bullets, no tables, no consulting jargon. Use only facts and figures from the notes; flag anything open under "Still to confirm". Headings: The short version / What's working / What's holding you back / Still to confirm / Recommended next step. End with exactly one next step: action, who, by when, and why it matters. After a line of dashes, list each figure you used with the note it came from.
```

**Why the extra pieces are there:**
- **CONTEXT** says who the reader is, so the model writes in an owner's terms instead of a consultant's.
- **CONSTRAINTS** give the reasons behind each rule, so the model follows the intent and not just the wording.
- **The CHECK block** lets you see in 10 seconds whether a figure was invented before you send. That matters most here, because an owner who spots a number they never gave stops trusting the rest.

## Three questions (unanswered ones keep the first option)

1. **Voice:** (A) Signal Results Group as "we", writing to the owner as "you" *(current draft)* · (B) first person "I" · (C) something else, in your words
2. **How it's sent:** (A) pasted into an email or text body *(current draft, light markdown)* · (B) a PDF/DOCX attachment, so I'd add a layout spec · (C) something else
3. **The next step:** (A) the action that best fixes the owner's biggest problem, whoever does it *(current draft)* · (B) always a step with you (a follow-up call, a data request, a proposal review) · (C) something else

**One flag:** discovery notes often hold the owner's financials. Run this inside your Project or another private workspace, not a free public chatbot.

I saved the prompt at `/tmp/claude-0/-tmp-fhlive-mr0oh1dd/5bb19790-b204-46b4-9c25-5ef9e3ec137d/scratchpad/discovery-summary-prompt.md`. I couldn't run the automated prompt check (`prompt-lint.py --strict`) because it needed your approval. Instead I checked by hand that every required section is there and that the success test can actually fail.

UNTESTED: I don't have any real notes, and test results on made-up notes would overstate how well it works. The test set I'd use is 5 sets of your past notes, 3 to tune on and 2 held back. They should cover: (1) a clean call with figures, (2) a messy call with no figures, (3) an owner listing several problems, (4) notes with an open item ("will send P&L"), (5) a call where the owner is lukewarm. Each would run 3 times against the QUICK version as the baseline, graded on the success test plus the quality-bar items. Send 3-5 old sets of notes, with names removed if you like, and I'll run it.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: partial
  assumptions: [voice "we"/"you" from Signal Results Group, delivered in an email or text body, next step chosen for owner's benefit, Sonnet 5.5 is enough, 350-word cap = one phone page]
  unknowns: [answers to Q1-Q3, real-note performance, whether the CHECK block should be kept or dropped]
  outputs: [engineered prompt, QUICK version]
  next: user answers Q1-Q3 and supplies 3-5 past note sets → run Full-lane test → save to prompt library
  approval_required: [supplying client notes for testing, sending any summary to an owner]
  tested: untested: no real call notes yet; 5-input test set defined
```