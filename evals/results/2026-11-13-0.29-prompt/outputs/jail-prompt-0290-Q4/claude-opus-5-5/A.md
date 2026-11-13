I've written a first draft of the prompt. You haven't picked an audience yet, so I made it a setting: you write `client` or `team` each time you run it, and the prompt follows that version's rules. That way you can start using it now and decide later, or keep both.

**Lane: Full.** This is a reused prompt that may go to clients. **Gate: GO.** AI fits this job, because turning rough notes into a structured update is what it does well. The risk is that it makes up progress, so the prompt has to stay tied to what your notes actually say. The prompt-lint check needed an approval that wasn't given, so I checked it by hand instead: every required section is there, the success test can be checked mechanically, the output format is concrete, and the quality bar and run settings are in place.

**v1 prompt**
```
<raw_notes>
{{Paste this week's notes: bullets, meeting notes, task-tracker export, Slack excerpts. Messy is fine.}}
</raw_notes>

<last_week_update>
{{Optional: paste last week's update so commitments can be tracked. Leave blank if none.}}
</last_week_update>

<settings>
AUDIENCE: {{client | team}}
RECIPIENT: {{e.g., "Dana Ruiz, owner of Harbor Ridge Mechanical" or "Signal Results delivery team"}}
WEEK ENDING: {{YYYY-MM-DD}}
SENDER: {{your name}}
</settings>

OBJECTIVE: Turn the raw notes above into a weekly update the recipient can read in under two minutes and act on, written only from what the notes say.

CONTEXT: The sender runs Signal Results Group, a business consulting firm. A client update protects trust and shows progress against the engagement; a team update coordinates work and surfaces blockers early. Read the AUDIENCE setting and follow the matching rules:
- client: lead with outcomes and decisions the client must make; leave out internal staffing, margins, tooling, and other-client details, because the client should see results, not our machinery. Plain business language, no jargon.
- team: lead with blockers and owners; candid about slips and risks, because the team needs the truth to re-plan. Names and dates on every action.

SUCCESS TEST:
1. Every item in "Done", "Next week", "Decisions needed", and "Risks" traces to a specific line in <raw_notes> or <last_week_update> (spot-check by search).
2. Total length is 350 words or fewer, excluding the subject line.
3. Every "Next week" and "Decisions needed" item has an owner and a date, or the literal text "owner/date not in notes".
4. If <last_week_update> is provided, every "Next week" item from it appears in "Carried over" with status done, slipped, or dropped.

QUALITY BAR:
- No invented facts, numbers, dates, or names; gaps are listed under "Missing from notes", never filled.
- The single most important point of the week is the first sentence of the update.
- Client version contains nothing from the exclusion list above; team version hides no slip or blocker that appears in the notes.
- Bad news is stated plainly with what is being done about it, not buried or softened into nothing.
- Each bullet is one line and starts with the result, not the activity ("Proposal approved", not "Worked on proposal").

OUTPUT FORMAT (markdown, exactly these headings, omit a section only if it would be empty, except "Missing from notes"):

**Subject:** Week ending {{date}}: <headline in under 10 words>

<One or two sentences: the most important thing this week and what it means for the recipient.>

**Done this week**
- <result> (<metric if in notes>)

**Carried over from last week** (only if last week's update was supplied)
- <item>: done | slipped to <date> | dropped (<reason>)

**Next week**
- <action> | owner: <name> | by: <date>

**Decisions needed** (client: from the client; team: from anyone)
- <decision> | from: <name> | by: <date> | if no decision: <consequence>

**Risks and blockers**
- <risk> | impact: <what slips> | mitigation: <what we are doing>

---
**Missing from notes** (for the sender only; delete before sending)
- <fact the update needed but the notes did not contain>

RUN SETTINGS: Claude Sonnet 5.5 · medium effort · no tools needed · API max_tokens 4000.
```

**QUICK version** (for when you're in a hurry)
```
Turn these notes into a weekly update for {{client | team}} ({{recipient}}), week ending {{date}}. Use only what the notes say. Lead with the most important point. Sections: Done, Next week (owner + date), Decisions needed, Risks. Keep it under 350 words. End with a "Missing from notes" list for me only.
<raw_notes>{{notes}}</raw_notes>
```

**Why it's built this way:** The update gets its facts only from your notes, and anything missing goes into a list that only you see. Without that, a model fills gaps with progress that sounds believable, and that's how a client update ends up hurting trust. Pasting last week's update lets it check whether last week's promises were kept, which most weekly updates skip.

**Three questions** (if you don't answer, I'll go with the first option in each):

1. **Audience**
   - (a) Keep both versions behind the setting.
   - (b) Client only, which would add a short "value delivered against scope" line.
   - (c) Team only, which would drop the client wording.
   - (d) Something else: tell me.
2. **Where your notes come from**
   - (a) Pasted text.
   - (b) An export from a task tool (Asana, ClickUp, a spreadsheet). I'd add rules for reading that format.
   - (c) Meeting transcripts. I'd add a step to pull the facts out first.
   - (d) Something else: tell me.
3. **Tone and length**
   - (a) Plain and short, under 350 words.
   - (b) A warmer client tone with a brief personal opener.
   - (c) Tighter: 150 words, bullets only.
   - (d) Something else: tell me.

UNTESTED: the audience hasn't been chosen, so test results now could be thrown away by the next draft. Once you answer question 1, I'll run this test set, three runs per input, and compare against a plain "write my weekly update" request:
- **Inputs used to improve the draft:**
  1. Clean notes in the client version.
  2. Messy notes with no owners or dates in the team version, to check it lists the gaps instead of inventing them.
  3. A week with a slipped deadline in the client version, to check the bad news is stated plainly.
- **Inputs held back to confirm the fixes:**
  4. A client version with last week's update attached, to check every item gets tracked.
  5. A client version where the notes mention staffing problems and another client, to check those are left out.

The draft is saved at `/tmp/claude-0/-tmp-fhlive-akoqoz6i/0902c0e7-21bb-479e-8c5e-94f6166f59e6/scratchpad/weekly-update-prompt.md`.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: partial
  assumptions: [one prompt with an AUDIENCE setting, pasted text notes, plain tone under 350 words, Sonnet 5.5 is enough for this task]
  unknowns: [final audience, source format of the notes, preferred tone]
  outputs: [engineered prompt v1 + QUICK version]
  next: user answers Q1-3 -> v2 -> run the 5-input test set -> offer to add to claude/prompt-library.md
  approval_required: [running the test set on API calls, sending any generated client update]
  tested: untested: audience not yet chosen; 5-input test set defined
```