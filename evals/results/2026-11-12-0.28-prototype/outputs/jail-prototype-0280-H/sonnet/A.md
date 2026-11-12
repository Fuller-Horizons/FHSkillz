**SPIKE VERDICT**
```
QUESTION:     Does a 4-stage lead pipeline (new, contacted, quoted, won/lost) handle a customer who asks for a second quote after saying no?
SHAPE:        logic
TIMEBOX:      one session, one feedback round → in progress · rounds: 0
LEDGER-CHECK: reuses 2026-11-12 lead-pipeline entry (inconclusive, never run); a run that answers it supersedes it
EVIDENCE:     none yet. The run needs approval and wasn't granted.
VERDICT:      inconclusive
ANSWER:       Not confirmed. The earlier hand-trace suggests the literal model can't track it (see below).
ARCHIVE:      /tmp/claude-0/-tmp-fhlive-sil10pyk/3d79d59b-2279-440e-be08-641d0487eabb/scratchpad/proto-lead-pipeline.py
CONSUMER:     none (jail-decide once answered)
```

**What happened**
- The ledger already had this question as `inconclusive`. The earlier harness was written but never run, and its path is outside this session, so I rebuilt it.
- The new harness is at the archive path above. It's stdlib Python, in memory, and uses sample data only (Pat Sample).
- It runs two models through the same story: new → contacted → quoted (Q1) → lost → asks for a second quote (Q2).
  - **A. Literal 4 stages, forward-only.**
  - **B. The same 4 stages plus a `lost → quoted` reopen rule.**
- My `python3` run command was not approved, so I have no surfaced-state evidence. By the ship gate, the verdict stays `inconclusive`. My hand-trace isn't evidence.

**Hand-trace, unconfirmed:**
- In A, `won/lost` is terminal. The second quote is rejected, or the lead has to be re-entered as a new lead, which splits the customer's history.
- B keeps both quotes on one record, but only if your CRM allows a reopen transition.

**To finish**
- Approve this command and I'll run it, report the printed state changes verbatim, and add a ledger line that supersedes the inconclusive one:
  `python3 -I /tmp/claude-0/-tmp-fhlive-sil10pyk/3d79d59b-2279-440e-be08-641d0487eabb/scratchpad/proto-lead-pipeline.py`
- I haven't written a duplicate inconclusive line to the project ledger. Nothing has left the machine.

```
JAIL-HANDOFF:
  skill: jail-prototype
  status: partial
  assumptions: [lost is terminal in the literal model; sample data only]
  unknowns: [whether the harness output matches the hand-trace; whether the target CRM supports reopen]
  outputs: [SPIKE VERDICT (inconclusive), harness]
  evidence: []
  next: jail-decide
  approval_required: [run the harness; ledger write after the run]
  tested: untested - run command not approved
```