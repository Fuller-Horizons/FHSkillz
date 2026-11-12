I couldn't search for the prototype or the ledger, so I haven't checked either. I'm not going to merge `proto-approval` into main, and I'd steer you away from doing it yourself.

**Why I'm not merging it**
- A prototype exists to answer one question. The answer goes into the real plan. The code and the page don't, and `proto-approval` stays archived as the primary source.
- Prototype code has no tests, no error handling, only sample data, and is wiped-on-sight by design. "Clean it up" means turning it into a production build, which this skill treats as a separate piece of work.
- The demo working well is the usual way a prototype gets promoted by accident, and a Friday deadline makes that more likely.

**What I can do before Friday**
1. **Check the ledger.** Search `claude/spike-ledger.md` in the project for the approval question. If it's already answered, I report that verdict and stop.
2. **Name the question.** Something like "Which approval flow lets a reviewer decide in under N seconds?" or "Does the approval state machine handle rejection, re-submit, and timeout?" I need your yes on one sentence.
3. **Collect evidence.** Run the demo with a reviewer and paste back their verbatim answers. My opinion of the demo doesn't count as evidence.
4. **Ship the SPIKE VERDICT and ledger line.** `proto-approval` is archived on a throwaway branch.
5. **Build the real thing from the verdict.** This is a fresh implementation in production paths with tests, and it can reuse ideas from the prototype but not its code. Given Friday, I'd scope it now, using the verdict as the requirements.

**What I need from you**
- Can you paste the contents of `claude/spike-ledger.md`, or confirm the approval question isn't in it? My search was blocked.
- What question did `proto-approval` set out to answer?
- Where does the branch live? I'll archive it, not merge it.

If the deadline means the demo itself is what ships, tell me. That's a different decision, and it needs your explicit sign-off as an exception, not a quiet merge.