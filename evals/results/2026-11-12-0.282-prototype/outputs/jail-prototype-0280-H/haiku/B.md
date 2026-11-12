I couldn't run the script. Running it needs approval and the approval was not granted, so the walkthrough below is a hand trace of the transition table, not observed output.

**Question:** Does a 4-stage lead pipeline (new, contacted, quoted, won/lost) handle a customer who asks for a second quote after saying no?

**Short answer: No, not as a naive design.** Won and lost are terminal, so the re-quote request has nowhere to go. A fix that keeps four stages works, with a caveat about reporting.

**Hand trace of the naive table** (`won` and `lost` have no outgoing transitions):

| Step | Action | Result | Stage |
|---|---|---|---|
| 1 | add L1 | OK | new |
| 2 | move to contacted | OK | contacted |
| 3 | move to quoted | OK | quoted |
| 4 | move to lost (customer says no) | OK | lost |
| 5 | move to quoted (asks for second quote) | **REJECTED**, lost → quoted not allowed | lost |

The lead is stuck at `lost` with the wrong stage. The team would have to either create a duplicate lead, which splits history and double-counts pipeline, or edit the stage by hand, which breaks the audit trail.

**Candidate fix:** allow `lost → quoted`. Trace: new → contacted → quoted → lost → quoted, all OK, with full history retained. The cost is that `lost` is no longer terminal, so win/loss reporting has to use the latest stage and count a reopened lead once, not as a loss plus a new quote.

**Verdict status: inconclusive, and not archived.** I could not read `claude/spike-ledger.md`. This session has no project read or write tool, so the ledger-first gate could not be checked, and the prototype is not registered as a spike entry. The script is at `/tmp/claude-0/-tmp-fhlive-ajbbx6fy/19cf9c03-eab4-4c81-a1d1-92fcbd614c4e/scratchpad/proto-pipeline-requote.py`, marked "wipe me". To finish the gate, run it with `python3 -I` on that path, then tell me whether the project ledger already has a verdict on this question so I can check it or register the result.