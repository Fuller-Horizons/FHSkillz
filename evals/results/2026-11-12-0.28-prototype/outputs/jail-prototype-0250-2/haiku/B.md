I couldn't run the harness. The sandbox blocked `python3` and asked for approval, so this is a paper walkthrough of the code, not a run. The verdict below is therefore inconclusive.

**Ledger check:** `claude/spike-ledger.md` has one entry, the 2026-11-12 scorecard layout. It does not have the 2026-06-14 batch-send answer you cited ("yes, with an explicit needs-changes state"), so I didn't treat that answer as established. If the entry lives in another ledger, tell me where and I'll reconcile it. If it's a new question, this prototype is the first answer.

**Prototype:** `/tmp/claude-0/-tmp-fhlive-i2raydlt/93586a14-bdef-47e9-8458-bb9a91e389d4/scratchpad/proto-approval-flow.py` (marked `PROTOTYPE — wipe me`, in-memory only, no production paths). It models a batch of items with three review states (approve / needs-changes / reject) and a send gate that allows sending only when every item is approved. It has six cases.

**Walkthrough results (from reading the code, not executed):**
1. Happy path: approving all items moves the batch to APPROVED, and send succeeds.
2. One item needs-changes: the batch goes to NEEDS_CHANGES and send is blocked.
3. Fix and re-approve: editing the flagged item clears it to pending, and approving it again allows send.
4. Reject: the batch becomes REJECTED. Approving an item afterward still updates the item, but the batch stays REJECTED, so the item shows approved inside a rejected batch.
5. Send with pending items: blocked.
6. Edit after approval: the approval is cleared and send is blocked.

**Findings for your judgment (the question is about feel, so only you can answer it):**
- The `resubmit` step does nothing useful. Editing a flagged item already moves the batch back to pending, so the editor gets no explicit "resubmitted" signal.
- Needs-changes clears silently on edit. Whether that feels right depends on whether the reviewer should be notified.
- Reject is terminal, but item-level approvals still change inside a rejected batch. That is a UI inconsistency to decide on.

**SPIKE VERDICT**
```
QUESTION:     Does the three-state approval flow (approve / needs-changes / reject) feel right for batch sends?
SHAPE:        logic
TIMEBOX:      one session → one session (paper walkthrough only; harness run blocked)
LEDGER-CHECK: none (cited 2026-06-14 entry not found in claude/spike-ledger.md)
EVIDENCE:     none. No surfaced-state output exists because the run was blocked. Ship gate 4 fails.
VERDICT:      inconclusive
ARCHIVE:      /tmp/claude-0/-tmp-fhlive-i2raydlt/93586a14-bdef-47e9-8458-bb9a91e389d4/scratchpad/proto-approval-flow.py
CONSUMER:     none
```

I did not append a ledger line, because an inconclusive verdict doesn't answer the question.

**Next steps:** run it yourself with `python3 <archive path above>` and tell me whether the states look right, or approve the run and I'll capture the output verbatim as EVIDENCE and finish the verdict. Also check whether the 2026-06-14 entry exists somewhere else.