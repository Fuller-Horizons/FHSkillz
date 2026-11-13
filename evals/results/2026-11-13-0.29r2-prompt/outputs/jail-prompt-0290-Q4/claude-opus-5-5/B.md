I'm treating this as the **Full** lane, because the prompt will be reused every week and may go to clients. Your audience question doesn't hold anything up. The draft below takes the audience as a setting you fill in each time (`client` or `team`), so one prompt works for both and you can decide later. The questions at the bottom will shape v2.

**Gate (GO, with notes)**
- **Right tool?** Yes. Turning messy notes into a clean, consistent update is a good fit for a reusable prompt, and none of your installed skills does it. `jail-cpr` covers meeting recaps and `jail-summarize` covers one-off decision briefs, not a recurring status update.
- **Groundable?** Yes. The facts come only from notes you paste in, so the prompt never needs outside data. The main risk is that it invents progress in a slow week, so the prompt rules that out.
- **Worth it?** Yes. You'd write it once and use it about 50 times a year.
- **Secure?** No inputs yet. Client notes may include confidential details. The client setting blocks internal and other-client details from the output, but you should still read each one before sending.
- **Readiness:** I'm about 97% confident the structure is right. I'm holding back from 99% only because the section list depends on your answer to Q1 below.

## v1 prompt

```
<week_notes>
{{Paste this week's raw material: your notes, task-list export, meeting recaps, email snippets, numbers. Messy is fine.}}
</week_notes>

<last_week_update>
{{Optional: paste last week's update so open items carry forward. Leave empty if none.}}
</last_week_update>

<settings>
AUDIENCE: {{client | team}}
RECIPIENT: {{client company name, or team name}}
WEEK ENDING: {{date}}
SENDER: {{your name}}, Signal Results Group
</settings>

OBJECTIVE: Turn the week notes into one weekly update the recipient can read in under two minutes and act on, written only from what the notes and last week's update actually say.

SUCCESS TEST:
- Exactly five sections, in this order, with these headings: Headline, Done this week, Next week, Needs from you, Risks and watch items.
- Headline is one sentence, 30 words or fewer.
- Body is 350 words or fewer (Headline through Risks).
- Every item in "Needs from you" names an owner and a date, or the date reads "date TBD".
- Every open item from last_week_update appears either under Done this week, Next week, or Risks; none silently disappear.

QUALITY BAR:
- Every claim, number, and date traces to week_notes or last_week_update. Nothing is invented to fill a thin week; a section with nothing real in it says "Nothing this week."
- AUDIENCE = client: written in outcome language (what changed for their business), no internal staffing, pricing, margin, or other-client details, no blame on the client, and bad news is stated plainly with the fix, not buried.
- AUDIENCE = team: direct and operational; names owners on every next-week item; internal blockers and slippage are called out by name.
- Slipped items say what slipped, by how much, and the new date. No "on track" without a reason in the notes.
- Gaps the notes leave open (a missing date, an unclear owner) go to the Unknowns list below the update, not guessed.

OUTPUT FORMAT:
Subject: Weekly update, {{RECIPIENT}}, week ending {{WEEK ENDING}}

**Headline:** <one sentence: the single most important thing this week>

**Done this week**
- <outcome, with the number or date if the notes give one>

**Next week**
- <item>, <owner>, <target date>

**Needs from you**
- <decision or input needed>, <owner>, <by date | date TBD>

**Risks and watch items**
- <risk>: <impact>, <what we're doing about it>

<SENDER>

---
Unknowns (for the sender, not the recipient; delete before sending):
- <each gap in the notes that you could not fill, or "None">
Items carried from last week: <count found> / <count placed>

RUN SETTINGS: Claude Sonnet 5.5 · medium effort · no tools needed (paste-in only). API: max_tokens 4000.
```

**Design choices:**
- **Last week's update as an input:** this is the part that matters most. Without it, open items quietly disappear from week to week. The "carried found / placed" count lets you check that in two seconds.
- **The Unknowns block:** this keeps the model from guessing. It marks gaps for you instead of inventing dates or owners.
- **Sonnet, not Opus:** this is formatting and judgment over notes you supply, and Sonnet handles it at about a tenth of the cost.

## QUICK version (for a fast week)

```
<week_notes>{{paste notes}}</week_notes>
Write a weekly update for {{client | team}} {{RECIPIENT}}, week ending {{date}}, from these notes only. Sections: Headline (1 sentence), Done this week, Next week (owner + date), Needs from you (owner + date), Risks. Under 350 words. Don't invent anything; list any gaps under "Unknowns" after the update.
```

## Questions for v2 (no answer = I keep the recommended option)

**Q1. What should the update mainly do?**
- **A. Report status and get decisions (recommended, and what v1 does)**
- B. Also show the value delivered, such as metrics moved and ROI to date (mainly useful for clients, helps renewals)
- C. Status only, no requests
- D. Something else (tell me)

**Q2. Where will the raw material usually come from?**
- **A. Notes I paste in by hand (recommended, and what v1 assumes)**
- B. A task tool or CRM export (tell me which; I'll add a parsing step)
- C. Meeting transcripts
- D. Something else (tell me)

**Q3. Tone and length?**
- **A. Plain and brief, under 350 words (recommended)**
- B. More polished and narrative, for client executives
- C. Bullets only, under 150 words
- D. Something else (tell me)

**UNTESTED:** I have no real week notes yet, and the strict lint script needed approval I didn't have, so I couldn't run it. I checked by hand instead: all the core sections are there, the success test can be checked mechanically (section count, word limits, owner and date on every request, carry-forward count), and the format is concrete. Test set ready for when you have notes:
1. A normal week for a client.
2. A thin week with almost nothing done, to check it doesn't invent progress.
3. A week with a slipped deadline and bad news for a client.
4. *(Held out)* The same notes as #3 run with the team setting, to check the tone switches and internal details show up.
5. *(Held out)* A week with last week's update included and two open items, to check nothing is dropped.

Each runs 3 times and is compared against a plain "write my weekly update" request. Send me one real week of notes, with private details removed if needed, and I'll run it.

JAIL-HANDOFF:
  skill: jail-prompt
  status: partial
  assumptions: [audience is a per-run setting rather than fixed; purpose is status plus decisions; input is pasted notes; under 350 words; Sonnet 5.5 medium is enough]
  unknowns: [final audience; source of raw material; whether clients want value/ROI framing; prompt-lint --strict not run (approval needed)]
  outputs: [engineered prompt v1 + QUICK version, /tmp/claude-0/-tmp-fhlive-9hak7zz8/580412f6-9a85-446f-80a3-d2d2b4f0db40/scratchpad/weekly-update-v1.md]
  next: user answers Q1-Q3 and supplies one real week of notes -> v2 + Full-lane test run; then save to the project prompt library
  approval_required: [running the lint script; reading each client-facing update before it is sent]
  tested: untested: no real inputs yet; 5-case test set defined above