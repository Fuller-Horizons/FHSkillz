**Lane: Full.** You'll reuse this, and the summary goes to clients. Opus 5.5 fits this lane. The prompt itself runs fine on Sonnet 5.5.

**Gate: GO.** `jail-summarize` could write these one at a time, but a saved prompt gives you the same structure every time and works in any chat. That's the reason to build it. No inputs were supplied yet, so there was nothing to scan for secrets.

**One risk I designed for:** your notes are private, and this summary goes to the owner. Comments like "owner seems burned out, might sell" must not reach them. The prompt removes that kind of material and lists what it removed in a section only you see.

**Objective:** turn your call notes into a phone-friendly summary the owner can read in about 90 seconds, ending on one next step.
**Success test:** 350 words or fewer, four fixed headings, exactly one next step, no tables, and every number traceable to your notes.

### The prompt (v1, built on the defaults below)

```
<discovery_notes>
[Paste your discovery-call notes here, 1-2 pages of bullets.]
</discovery_notes>

<call_details>
Company: [name]
Owner first name: [name]
Call date: [date]
Sender: Jonathan, Signal Results Group
</call_details>

OBJECTIVE: Turn the discovery-call notes above into a one-page summary I will send to the owner of this HVAC company. The owner will read it on a phone between jobs, so it should read like a short, plain-English note from someone who listened. Show them we understood their business, name what the problems are costing them, and end with exactly one recommended next step.

SUCCESS TEST:
- The summary (everything above the divider line) is 350 words or fewer.
- It uses exactly these four section headings, in this order: "What we heard", "What it's costing you", "Where we'd start", "Recommended next step".
- "Recommended next step" holds one action only: one sentence or two, no list.
- There are no tables, and no section has more than 5 bullets.
- Every number, dollar figure, percentage, and date in the summary also appears in the notes or call details.

QUALITY BAR:
- Plain English: no consulting or finance jargon (no "leverage", "synergies", "EBITDA", "KPIs", "optimize"). Where the notes use a term the owner wouldn't use, say it the way an HVAC owner would ("profit per job", not "gross margin by job"). HVAC trade terms the owner uses (service agreements, callbacks, techs, dispatch) are fine.
- Grounded: every point traces to the notes. If the notes don't support a cost or impact, write "We'd want to put a number on this together" instead of estimating one. Never invent figures, names, or commitments.
- Client-safe: the notes are my private notes. Leave out anything the owner shouldn't read: my opinions of them or their staff, sale or exit speculation, pricing strategy, comments about competitors or other clients, and anything marked "internal", "note to self", or "NTS". List what you left out below the divider.
- Their words: "What we heard" should sound like the owner's own concerns, using phrasing from the notes where it fits, so they recognize their own business.
- The next step is specific and low-friction: what happens, who does it, and a rough when (for example "a 45-minute walk-through of your last 3 months of service tickets, next week"). If the notes record a next step we agreed on the call, use that one.

OUTPUT FORMAT (use this exact shape; short paragraphs and bullets for a phone screen):

**[Company] – Call Summary**
[Call date]

Hi [Owner first name], thanks for the time on [day]. Here's what I took away.

**What we heard**
- [3-5 bullets, one line each where possible]

**What it's costing you**
- [2-4 bullets, using numbers only from the notes]

**Where we'd start**
- [2-3 bullets]

**Recommended next step**
[One action: what, who, rough when.]

[Sign-off: Jonathan, Signal Results Group]

---
FOR JONATHAN ONLY (not for the owner):
- Left out (internal): [items removed from the notes, or "none"]
- Inferred, not stated: [anything in the summary you inferred rather than read directly, or "none"]
- Unknown / confirm before sending: [gaps, unclear notes, missing call details, or "none"]

RUN SETTINGS: Claude Sonnet 5.5 · low-to-medium effort · no tools · API: max_tokens 2000
```

**QUICK version** (for a fast paste into a chat):
```
<discovery_notes>[paste notes]</discovery_notes>
Write a 350-word-max, phone-friendly summary of these discovery-call notes for the HVAC company owner. Use plain English and no jargon. Use four headings: What we heard / What it's costing you / Where we'd start / Recommended next step (exactly one action, with who and when). Use only numbers that appear in the notes. Leave out my private opinions and anything about a sale or exit. Below a --- line, list for me only what you left out, what you inferred, and what I should confirm.
```

**Saved at:** `/tmp/claude-0/-tmp-fhlive-vtlgm4hj/bb361841-03a6-4243-be5a-813d4c330029/scratchpad/discovery-summary-prompt.md`

**Check:** I couldn't run the automatic prompt checker (`prompt-lint.py --strict`) because the command wasn't approved, so I checked the prompt by hand instead. All the core sections are there, the success test can fail and can be checked by code (word count, headings, number matching), the output format is fixed, and run settings are included.

### Questions (unanswered ones keep the default already built into v1)

1. **Who reads it?**
   - **A) Sent straight to the owner, from you (default)**
   - B) Only for you, as call prep, so the private-notes filter isn't needed
   - C) Your team, before a proposal
   - D) Something else (tell me)
2. **What should the next step usually be?**
   - **A) Whatever was agreed on the call; if nothing was, the prompt picks the smallest sensible step (default)**
   - B) Always a paid assessment or proposal meeting
   - C) Always a free follow-up working session
   - D) Something else (tell me)
3. **How long?**
   - **A) 350 words or fewer, about one phone scroll (default)**
   - B) 200 words or fewer, a text-length note
   - C) Up to 500 words, with more detail on causes
   - D) Something else (tell me)

UNTESTED: I have no real discovery notes, and made-up notes wouldn't show how your actual note style behaves (shorthand, "NTS" asides, missing numbers). **Test set ready to run:** 5 of your real call notes, with names changed if you want. Three are used to fix problems and two are held back to check the fixes. Each runs 3 times and is compared against a plain "summarize this for the owner" request. Each test checks the word count, the headings, a single next step, that every number appears in the notes, and that no private remarks leaked. Send the notes and I'll run it. Before that, I'd like to save the prompt to your prompt library as v1.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: partial
  assumptions: [summary goes directly to the owner; notes may contain private remarks that must be filtered; 350-word cap; next step = the one agreed on the call, else the smallest sensible step; sign-off "Jonathan, Signal Results Group"; runs on Sonnet 5.5]
  unknowns: [how you usually format your notes and mark private asides; whether pricing ever belongs in the summary; preferred next-step offer]
  outputs: [engineered prompt + QUICK version, saved to scratchpad]
  next: run the 5-input test on your real notes, then save to claude/prompt-library.md
  approval_required: [sending any generated summary to a client; adding the prompt to the project prompt library]
  tested: untested: no sample notes supplied; test set defined above
```