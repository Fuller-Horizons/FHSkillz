I won't merge `proto-approval` into main. The jail-prototype rules say a prototype is never merged: the answer graduates into the real plan and the build stays archived. Cleaning up a demo for Friday is the polish creep the skill guards against, and the demo was never tested as production code.

The question this prototype answered is already in the project's spike ledger, so nothing needs rerunning:

- **Question:** weekly scorecard layout for business owners (see what needs attention in 30 seconds)
- **Verdict:** answered. Layout B, a headline plus 3 tiles, with the "This week…" insight placed under the tiles so the large numbers are read first.
- **Evidence:** the reviewer wrote "PICK: B · READ FIRST: the Large text in the boxes · NOTES: I would like the insights 'This week...' under the boxes."
- **Archive:** `proto-weekly-scorecard` r1 (`FHSkillz skills/jail-prototype/references/example-scorecard-layouts.html`) and r2 (`proto-weekly-scorecard-r2.html`, a chat file). I haven't confirmed that either path resolves.

I also couldn't find `proto-approval` in this session. The working directory isn't a git repo, so there's no branch I can inspect or merge.

For Friday, the path that works is:

1. Build the scorecard for real on a new branch off main: layout B, headline and 3 tiles, insight under the tiles, with real tests and real data handling.
2. Keep the prototype archived as the source of the decision. Don't carry its code over.

If you tell me which repo the production scorecard lives in, and whether it should be built from the r2 archive's layout or from the verdict text, I can start on the branch. If `proto-approval` holds something other than the scorecard, tell me what question it answered and I'll check it against the ledger.