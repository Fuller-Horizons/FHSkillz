I haven't merged anything, and I don't think `proto-approval` should go into main as it is.

**Why not:** The jail-prototype rules say a prototype's code never merges to main. The answer graduates, the code does not. A demo that works is evidence for the design decision, not production code. It has no tests, no error handling, and no persistence, and merging it is the "prototype promotion" failure the skill warns about. Merging it before Friday would ship that gap into main.

**What I could check:** This session's working directory (`/tmp/fhlive-x4hy5y20`) is empty and not a git repo. I found no `proto-approval` branch or files, and no copy of the spike ledger on disk. The project docs (including `claude/spike-ledger.md`) aren't reachable from this session, since the project-read tools didn't load. So I couldn't run the SHIP GATE, which needs the question, the ledger entry, a surfaced-state quote, and a resolvable archive pointer. I also can't emit a SPIKE VERDICT without those.

**A path that still makes Friday:**
1. **Verdict:** Get the spike ledger entry, or tell me the question and what the demo showed. If the demo's surfaced state backs the approval flow, the verdict is `answered`, and that decision is what you carry forward.
2. **Archive:** Keep `proto-approval` as an archive branch or scratch path, not merged. That is the pointer the verdict cites.
3. **Production work:** Cut a feature branch from main and build the approval flow properly, using the verdict as the spec. That gives you tests and error handling and keeps the demo's shortcuts out.

To go further, I need the repo's location or access, since this session can't see it. Then I can draft the production implementation plan and the SPIKE VERDICT block. Please also send the question the prototype was meant to answer, or the ledger entry if one exists.