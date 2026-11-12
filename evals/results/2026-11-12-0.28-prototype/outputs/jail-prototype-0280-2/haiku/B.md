The onboarding checklist question is answered: layout C is the pick. The verdict passed the ship gate, and I recorded it in the project's spike ledger as superseding the earlier inconclusive entry.

```
SPIKE VERDICT
QUESTION:     Which of three onboarding-checklist layouts makes it easiest for a new client to finish?
SHAPE:        look
TIMEBOX:      1 round → 1 round (r1)
LEDGER-CHECK: supersedes 2026-11-12 onboarding checklist entry (inconclusive, awaiting review)
EVIDENCE:     "PROTOTYPE FEEDBACK r1 · PICK: C · READ FIRST: the progress bar · NOTES: #4 remove the video step · #6 label 'Docs' is unclear. Wrap it up."
VERDICT:      answered
ARCHIVE:      /tmp/claude-0/-tmp-fhlive-36paqhru/9d28cbab-9c01-47ac-b5e0-7bc1095d1d96/scratchpad/proto-onboarding-layouts.html
CONSUMER:     none
```

**What to carry into the real build:**
- Use layout C, with the progress bar as the first thing a customer sees.
- Remove the video step (note #4).
- Rename the "Docs" label, which reviewers found unclear (note #6). I haven't picked a replacement wording; that's yours to choose.

**Ship gate, 5 of 5:**
1. Ledger checked before building: yes. This question was already in the ledger as inconclusive, so I recorded the new result rather than rebuilding.
2. Throwaway name: `proto-onboarding-layouts.html`.
3. No production files: nothing in production paths was touched.
4. Surfaced-state evidence: the only evidence is the reviewer's round-1 report. I didn't re-capture the page state myself, so this rests on their observation. It matches how the scorecard entry was recorded.
5. Archive resolves: the file exists and I read it.

The prototype's sample data is fictional (Harbor Point Heating & Air), so nothing in the archive is client data.