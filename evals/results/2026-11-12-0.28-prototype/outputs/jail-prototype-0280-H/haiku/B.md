**Answer: not verified. The prototype didn't run, so this is inconclusive.** The Bash call that would execute the script was refused with "This command requires approval," and I retried once with the same result.

**What I can say from reading the code (a hand-trace, not evidence):** under the literal four-stage model, `lost` is terminal. A second quote therefore can't be tracked as stage progression: `lost → quoted` and `lost → contacted` are both rejected. The workaround I scripted, reopening to `contacted`, is also rejected, because the code allows no transitions out of `lost`. So a real CRM would need an explicit reopen transition, or the re-quote would have to live as a sub-state or a separate quote record rather than a stage change. That is what the run would need to confirm.

```
SPIKE VERDICT
QUESTION:     Does a 4-stage lead pipeline (new, contacted, quoted, won/lost) handle a customer who asks for a second quote after saying no?
SHAPE:        logic
TIMEBOX:      one session → one session (run blocked, no extension used)
LEDGER-CHECK: none (checked claude/spike-ledger.md before building; no prior entry)
EVIDENCE:     none surfaced (run blocked by approval)
VERDICT:      inconclusive
ARCHIVE:      /tmp/claude-0/-tmp-fhlive-i5v5o7l8/943e0034-0378-4ff7-8345-b5e2b4f26d57/scratchpad/proto-lead-pipeline.py
CONSUMER:     none
```

**Files:**
- Harness: `/tmp/claude-0/-tmp-fhlive-i5v5o7l8/943e0034-0378-4ff7-8345-b5e2b4f26d57/scratchpad/proto-lead-pipeline.py` (stdlib only, in-memory, marked "PROTOTYPE — wipe me"). Run it with `python3 -I` once approved.
- I added an inconclusive line to `claude/spike-ledger.md` in the project so the question isn't re-asked from scratch. A run that answers it should supersede that line.

**To finish:** approve the run command, or run `python3 -I` on the harness yourself and paste the output. The verdict will then be `answered` if the output shows the rejections above, and the answer will be settled before you change the CRM.