I couldn't run the harness: executing the script needs approval that wasn't granted. So I traced the three rule variants by hand. The verdict below is therefore unverified by execution and has no reviewer evidence, so it ships as inconclusive.

**Ledger check:** Not done. The project tools (`project_read`, `project_search`) aren't loaded in this session, and no `spike-ledger.md` exists on disk, so I can't tell whether this question was answered before.

**Harness:** `/tmp/claude-0/-tmp-fhlive-2-hqfttd/7f801843-1639-43e0-8d8d-42fd3dd361e5/scratchpad/proto-lead-pipeline-requote.py` (PROTOTYPE, wipe me, stdlib only, sample data, in-memory). Run it with `python3` once you approve execution.

**Hand trace**

Main case: `new → contacted → quoted → lost` ("no"), then "send quote #2".

| Rule variant | Result of "send quote #2" | Records after |
|---|---|---|
| strict (lost is terminal) | `REJECTED lost -> quoted (no path)` | One record, stuck at lost |
| reopen (lost → quoted allowed) | Same record moves to quoted; history keeps both quotes | One record, history shows lost then quoted |
| child (new record linked to parent) | New record `acme-r2`, stage new | Two records; parent stays lost |

Hard cases traced:
- **No at "contacted", before any quote, then asks for a first quote:** strict rejects it. Reopen allows it on the same record, but the stage moves straight to quoted. Child creates a new record.
- **Lost, requoted, lost again:** strict blocks the requote. Reopen and child both take a second loss.

**VERDICT: inconclusive**

```
SPIKE VERDICT
QUESTION:     Does a 4-stage lead pipeline (new, contacted, quoted, won/lost) handle a customer who asks for a second quote after saying no?
SHAPE:        logic
TIMEBOX:      1 session → 1 session · rounds: 0
LEDGER-CHECK: none (project ledger unreachable from this session)
DESIGN:       n/a
EVIDENCE:     none. No reviewer answer; hand trace only.
VERDICT:      inconclusive
ANSWER:       As specified (won/lost terminal, no re-entry), the pipeline does not handle a re-quote after "no": the request has no valid transition. It needs one explicit rule, either reopen-on-same-record or a linked child record. The choice affects win-rate and funnel counts, and that choice is still open.
ARCHIVE:      /tmp/claude-0/-tmp-fhlive-2-hqfttd/7f801843-1639-43e0-8d8d-42fd3dd361e5/scratchpad/proto-lead-pipeline-requote.py
CONSUMER:     jail-decide
```

**Ship gate:** Failed on gate 1 (ledger not checked), gate 4 (no reviewer answer or observed run output), and the run itself is unverified. Hence `inconclusive`.

**Next:** Execute the script to get real output (needs your approval). Then send the "reopen vs child" choice to `jail-decide`, with the funnel-count impact as the criterion. Nothing was written to the project.