I built one prompt that works for both audiences. You set `AUDIENCE: CLIENT` or `TEAM` each week and it changes what gets left out and how strict it is about owners and dates. That way you don't have to decide now.

**Lane: Full** (you'll reuse it, and it may go to clients). **Gate: GO, with notes.** A prompt is the right tool here: it turns messy notes into a consistent update. It doesn't look anything up, so nothing needs current facts. The main risk is the model making up progress, so most of the checks target that.

```
<week_notes>
{{Paste this week's raw material: bullets, task-list export, meeting notes, metrics. Messy is fine.}}
</week_notes>

<last_week_update>
{{Paste last week's sent update, or write NONE for the first week.}}
</last_week_update>

<settings>
AUDIENCE: {{CLIENT or TEAM}}
RECIPIENT: {{e.g. "Harbor Ridge Mechanical leadership" or "Signal Results delivery team"}}
WEEK ENDING: {{date}}
SENDER: {{name, role}}
</settings>

OBJECTIVE: Turn this week's raw notes into a weekly update the recipient can read in under two minutes and act on, keeping faith with what last week's update promised.

SUCCESS TEST:
- Every number, date, and name in the update appears in week_notes, last_week_update, or settings.
- Every "Next week" commitment in last_week_update appears in "Last week's commitments" with exactly one status: Done, Slipped (new date), or Dropped (reason). If week_notes don't show which, the status is [NEED: status].
- Word count of the update body: CLIENT 350 or fewer, TEAM 450 or fewer.
- Headings appear exactly as in OUTPUT FORMAT, in that order; a section with nothing to report says "None this week."

QUALITY BAR:
- The headline states the single most important thing about the week, in the reader's terms (CLIENT: outcome or risk to their business; TEAM: what changes for the team), not a list of activity.
- Nothing is invented: anything the notes imply but don't state is marked (inference); anything needed but missing is written as [NEED: what's missing] rather than filled in.
- Bad news is stated plainly in its own line with a next step; it is not buried or softened into vagueness.
- CLIENT mode leaves out internal names below the sender, internal tooling, margins, pricing, staffing problems, and blame, because the client is paying for outcomes and these erode trust. TEAM mode includes an owner and a date on every action, because unowned actions don't happen.
- Each "Decisions / asks" item names who must decide, what, and by when.

OUTPUT FORMAT (return only the update, then the check block):

Subject: Weekly update, week ending <date>: <headline in 8 words or fewer>

**Headline:** <one sentence>

**Last week's commitments**
- <commitment>: Done | Slipped to <date> | Dropped (<reason>)

**This week**
- <result, outcome first>

**Next week**
- <commitment> (TEAM: owner, due date)

**Risks and blockers**
- <risk>: <impact>; <next step>

**Decisions / asks**
- <who> to decide <what> by <date>

---
CHECK (not for sending):
- Word count: <n> / <limit>
- Inferences made: <list or "none">
- Missing info [NEED]: <list or "none">
- Left out for audience: <items omitted from notes and why, or "none">

RUN SETTINGS: Claude Sonnet 5.5 · medium effort · no tools needed (all inputs are pasted) · API: max_tokens 2000
```

**QUICK version** (for a fast week):
```
<week_notes>{{notes}}</week_notes>
<last_week_update>{{last update or NONE}}</last_week_update>
Write a weekly update for {{CLIENT/TEAM}}: {{recipient}}, week ending {{date}}, 350 words or fewer. Sections: Headline · Last week's commitments (Done / Slipped / Dropped) · This week · Next week · Risks and blockers · Decisions / asks. Use only facts from the notes; mark guesses (inference) and gaps [NEED: …]. For a client, leave out internal names, pricing and blame.
```

**Why it's built this way**
- **Carrying last week forward** is the most useful feature. If last week's update promised something, this week's has to say whether it got done. That builds trust with clients and keeps a team accountable.
- **The CHECK block** at the bottom is for you only, so you can catch guesses and gaps before you send. Delete it before sending.
- **Sonnet 5.5 is enough** for this. It's rewriting your notes, not doing analysis.

**Questions.** Any you skip, I'll go with the first option and update the draft:
1. **Audience:** (a) keep one prompt with the CLIENT/TEAM switch *(recommended)* · (b) client only, so I'd tighten the tone and drop TEAM mode · (c) team only · (d) other context in your own words
2. **Where the notes come from:** (a) you paste them in *(recommended)* · (b) pulled from a connected tool (Asana, Slack, email), which adds tool steps and injection guards · (c) other
3. **How it goes out:** (a) plain email body *(recommended)* · (b) a formatted DOCX or PDF each week · (c) other

**Checks:** the strict lint script needed a permission this session didn't have, so I checked the prompt by hand against the same rules. All required sections are there, the success test has countable checks, and the output format has a filled-in shape. One review pass found a gap: a status could be marked "Done" without proof in the notes. I fixed it with the `[NEED: status]` rule.

UNTESTED: the audience isn't decided yet, and testing both modes now would partly be wasted. I also had no access here to run the model trials the testing step needs. Test set, ready to run once you pick:
- **Fix set:** (1) a normal week, client mode; (2) a week where last week's commitments slipped, so the bad news must show; (3) team-mode notes with no owners, which must produce `[NEED]`s
- **Held out:** (4) client-mode notes that mention pricing and an internal staffing problem, which must be left out; (5) a first week with `NONE` and only 4 thin bullets, which must not be padded
- Each input gets 3 runs and is compared with the plain request "write a weekly update from these notes"

The prompt file is at `/tmp/claude-0/-tmp-fhlive-5b8ml1-d/fe4de08a-317b-4872-9af0-68a8c906eb68/scratchpad/weekly-update-prompt.md`. Once it's tested, I can save it to your prompt library and run it on this week's notes.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: partial
  assumptions: [one prompt with CLIENT/TEAM switch, notes pasted by user, plain email body output, Sonnet 5.5 sufficient]
  unknowns: [final audience, notes source, delivery format, real sample notes for testing]
  outputs: [engineered prompt v1 + QUICK version + 5-input test set]
  next: answer the questions → run the 5-input test (jail-prompt round 2), then save to prompt library
  approval_required: [sending any update to a client, connecting a notes source if option 2b]
  tested: untested - audience undecided; no model-trial access this session; test set specified
```