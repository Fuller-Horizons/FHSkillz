I couldn't run the prototype, so the question is still unanswered. The run command needs your approval, and I won't get around that. The Ship Gate fails closed on this: no surfaced-state evidence means the verdict is `inconclusive`.

```
SPIKE VERDICT
QUESTION:     Does a 4-stage lead pipeline (new, contacted, quoted, won/lost) handle a customer who asks for a second quote after saying no?
SHAPE:        logic
TIMEBOX:      one session → run blocked, no extension used
LEDGER-CHECK: none (the existing 2026-11-12 entry is inconclusive and was never run; a run that answers this question will supersede it)
EVIDENCE:     none. The harness has not been executed, so there is no surfaced state to quote (Rule 5).
VERDICT:      inconclusive
ARCHIVE:      /tmp/claude-0/-tmp-fhlive-umfuthoh/a3315acb-9ec1-4039-850f-78c555da2577/scratchpad/proto-lead-pipeline-r2.py
CONSUMER:     none
```

**What the harness tests.** It replays Pat R., a fictional Harbor Point lead, through contacted, quote $9,200, "no" (lost), then "can I get a second quote?". It does this under two models, printing the full state after every step:
- **Model A** is the literal 4-stage pipeline, where won and lost are final.
- **Model B** is the same four stages, but lost can reopen to contacted.

**What I expect, from reading the code and not from a run.** In Model A, lost → quoted and lost → contacted are both rejected. The second quote has nowhere to go, so the CRM would have to hold it as a new duplicate lead or you would have to override the stage by hand. Model B accepts the second quote, but the lead's history now shows a loss followed by a win. Treat this as a hypothesis until it runs.

**How to proceed.** Approve the run command, `python3 -I` on that script, and I'll capture the output as evidence. I'll then ship an `answered` verdict that supersedes the existing ledger line. I haven't added a duplicate `inconclusive` line to the spike ledger, since it would say the same thing as the entry already there.