**Lane: Full.** You'll reuse this, and every summary goes to a client. Opus 5.5 is the right model for this lane. I'm sending the v1 prompt now, built on default answers. Three questions follow it, and your answers update the draft.

## Gate
1. **Right tool?** GO. `jail-summarize` can write owner briefs one at a time. A saved prompt is worth having because you'll run it on every call and can use it anywhere. You may already have something similar in the Project's `prompt-library.md`, but I can't open Project docs from here. If one is there, paste it and I'll merge the two.
2. **Groundable?** GO. Everything comes from your notes. The prompt needs no outside facts.
3. **Worth it?** GO. Writing the prompt takes about one run's worth of effort, and you'll use it many times.
4. **Secure?** GO. You wrote the notes, so they don't need a pasted-content wrapper. One risk is that your private impressions of the owner could end up in the summary. The prompt removes them and lists what it removed.

**Readiness: GO.** I'm 99% confident on structure, length and grounding. The weakest part is how specific the next step will be. Question 2 below settles that.

## The prompt (v1)

```
<discovery_notes>
{{PASTE YOUR 1-2 PAGES OF BULLETS HERE}}
</discovery_notes>

<call_details>
Company: {{company name}}
Owner first name: {{name}}
Call date: {{date}}
From: {{your name}}, Signal Results Group
</call_details>

OBJECTIVE: Turn my discovery-call notes into a one-page summary I'll send to the owner of this HVAC company. Don't just restate the bullets. Connect what they told me into the two or three things that matter most to their business, and end with one recommended next step.

CONTEXT: The reader owns and runs an HVAC company. They'll read this on their phone, often between jobs. They're practical, short on time, and wary of consultant-speak. This is the first thing they get from us in writing, so it should show we listened and understood their business in their own terms. It isn't a sales pitch.

SUCCESS TEST:
- Summary is 350 words or fewer (excluding the NOTES FOR ME block).
- It uses exactly the six headings in OUTPUT FORMAT, in order.
- The last section has exactly one next step.
- Every number, dollar figure, percentage, name, and date in the summary appears in the notes.
- No section has more than 3 bullets, and the summary has no tables.

QUALITY BAR:
- After one read on a phone, an owner could say back their main problem and the next step.
- Where the notes quote the owner, the summary uses the owner's words.
- Plain English at about an 8th-grade reading level. Use the HVAC terms owners use (service agreements, callbacks, shoulder season, techs). Avoid business-school words (leverage, optimize, synergy, KPI, value proposition, stakeholders).
- Nothing is invented. Anything not in the notes is either left out or phrased as a question under "What we still need to confirm."
- The next step says who does what, by when, and why it's worth the owner's time.

CONSTRAINTS:
- Keep paragraphs to 1-2 sentences and sentences under about 20 words, because long blocks are hard to read on a phone.
- Leave out my private observations about the owner, family, or staff (for example "seemed overwhelmed" or "son not ready to take over"). They're for me, not the owner, and could damage trust if sent.
- If the notes don't give a cost or dollar figure, describe the impact in plain terms ("jobs slipping to next week") instead of estimating one.
- If the notes suggest more than one next step, pick the one that is smallest, most concrete, and most likely to get a yes. List the others in NOTES FOR ME.

OUTPUT FORMAT:
Subject: {{Company}}: what we heard on {{date}}

**The short version**
Two sentences: their main problem and why it matters now.

**What you told us**
Up to 3 bullets, in their words where possible.

**What it's likely costing you**
Up to 3 bullets. Figures only from the notes. Otherwise describe the impact plainly.

**What we're hearing underneath**
1-2 sentences connecting the points above. Present it as our read, not as fact ("It sounds like...").

**What we still need to confirm**
Up to 3 short questions.

**Recommended next step**
1-2 sentences covering action, who, when, and why.

{{your name}}, Signal Results Group

---
NOTES FOR ME (don't send):
- Word count:
- Left out as private observations:
- Other possible next steps:
- Numbers to double-check against my memory of the call:

RUN SETTINGS: Claude Sonnet 5.5 · medium effort · no tools · max_tokens 2500. Use Opus 5.5 if the notes are unusually messy or contradictory.
```

**QUICK version** (for when you're in a hurry):
```
<notes>{{paste notes}}</notes>
Turn these discovery-call notes into a phone-friendly summary of 350 words or fewer for the HVAC owner. Use plain English with no consultant jargon, and use their own words where I quoted them. Sections: The short version (2 sentences) · What you told us · What it's likely costing you · What we still need to confirm · Recommended next step (exactly one: who, what, when, why). No more than 3 bullets per section and no tables. Use only facts and numbers from the notes, and turn anything uncertain into a question. Leave out my private observations about people. Below a line, list for me only: what you left out, other possible next steps, and the word count.
```

## Questions (unanswered ones keep option A)
1. **Voice**
   - A) "We" from Signal Results Group to the owner *(recommended)*
   - B) "I" from you personally
   - C) Neutral third person
   - D) Other, in your own words
2. **What the next step usually is**
   - A) A short follow-up meeting or site visit with a proposed date *(recommended)*
   - B) A request for specific documents or data
   - C) A paid diagnostic or engagement offer
   - D) Other, in your own words
3. **Where it gets sent**
   - A) Email body *(recommended; matches the current format)*
   - B) Text message, which means cutting to about 150 words
   - C) An attached PDF or Word one-pager
   - D) Other, in your own words

UNTESTED: I have no real notes to run it on yet. The test set I'd use is 5 anonymized notes, each run 3 times and compared with a plain "summarize this for the owner" request:
1. Clean notes with dollar figures
2. Notes full of private impressions
3. Notes with no numbers at all
4. *(held out)* Notes that point to two competing next steps
5. *(held out)* Two pages of rough shorthand

You can send 3–5 real notes with names removed, or I can write realistic samples and run the test.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: partial
  assumptions: [voice "we" from Signal Results Group, next step = follow-up meeting/visit, delivered as email body, ≤350 words ≈ one phone page, notes are user-authored (no injection wrapper needed)]
  unknowns: [answers to Q1-3, whether a similar prompt already exists in Project prompt-library.md, real note samples for testing]
  outputs: [engineered prompt v1 + QUICK version]
  next: answer Q1-3 and supply 3-5 anonymized notes → run test set (or jail-lab for longer tuning); then save to prompt library
  approval_required: [sending any summary to a client, saving to the Project prompt library]
  tested: untested - no input samples yet; test set defined (5 inputs, 2 held out, 3 runs each vs plain request)
```