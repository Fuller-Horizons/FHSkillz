The prototype is written but I couldn't run it. Both attempts to execute it were blocked pending approval, so I have no surfaced state to quote. Under the ship gate that makes this verdict `inconclusive`.

```
SPIKE VERDICT
QUESTION:     Does a 4-stage pipeline (new → contacted → quoted → won/lost) handle a customer who asks for a second quote after saying no?
SHAPE:        logic
TIMEBOX:      one session → not yet run
LEDGER-CHECK: unverified (project spike-ledger.md not readable from this session)
EVIDENCE:     none (the script was never executed, so nothing is quoted)
VERDICT:      inconclusive
ARCHIVE:      /tmp/claude-0/-tmp-fhlive-mskilw3k/3d792bf6-49e7-4676-a7a4-429fa9f95d64/scratchpad/proto-crm-pipeline/proto_pipeline.py
CONSUMER:     none
```

**Gate result:** 2 of 5 pass.

| Gate | Result |
|---|---|
| Ledger checked first | Fail: I couldn't read the ledger |
| Throwaway name | Pass: `proto-crm-pipeline`, with a "PROTOTYPE — wipe me" header |
| Zero production files | Pass |
| Verbatim evidence | Fail: the script hasn't run |
| Archive pointer resolves | Pass |

**What the prototype tests.** It pushes one lead through four cases and prints the full state after each action:
- **A. Strict model:** won and lost are terminal, so the second-quote step should be rejected.
- **B. Reopen the lost lead:** one lead ends up counted as both lost and won.
- **C. Duplicate the lead:** one customer shows as 1 lost and 1 won, and the quote history splits across two records.
- **D. Candidate fix:** lost can go back to quoted, and quotes are kept as a list on one lead.

I haven't seen any output yet, so I'm not claiming a result. Reading the code, I expect A to reject the second quote and B and C to distort the funnel. Treat that as an unverified guess.

**To get a real verdict**, either approve this command and I'll run it and re-issue the block with evidence:
`python3 -I /tmp/claude-0/-tmp-fhlive-mskilw3k/3d792bf6-49e7-4676-a7a4-429fa9f95d64/scratchpad/proto-crm-pipeline/proto_pipeline.py`
or run it yourself and paste the output.

I'll also need the ledger content, or access to it, to clear gate 1 and write the ledger line. I haven't appended anything to the SPIKE LEDGER.