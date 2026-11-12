The ledger already has this question, so I'm stopping at Step 0 and not building a prototype. I couldn't open `claude/spike-ledger.md` to confirm the entry. The project read/search tools aren't available in this session, so this relies on the ledger line you pasted.

**Ledger hit**
- Entry: `2026-06-14 · does the three-state approval flow feel right for batch sends? · answered — yes, with an explicit needs-changes state · proto/approval-flow · supersedes:none`
- Verdict: **answered**. The three-state flow feels right for batch sends, as long as it has an explicit needs-changes state.
- Archive pointer: `proto/approval-flow`. I haven't checked that it still resolves.

The skill says an answered question gets its recorded verdict reported and nothing rebuilt. A rerun needs a changed premise, and then it opens a new entry that supersedes the old one.

**To reopen it,** tell me what changed since 2026-06-14. For example: a different batch size, a new approver role, a rejection path that didn't exist then, or a new reason to doubt the needs-changes state. I'd then write a new falsifiable question and a ledger line with `supersedes:2026-06-14 approval-flow`. I'd wait for your yes before building.

**To use the answer,** I can pass it to `jail-decide` or `jail-memory` as a Fact of the earlier prototype, with the build staying archived.

JAIL-HANDOFF:
  skill: jail-prototype
  status: stop
  assumptions: [ledger line as pasted is accurate]
  unknowns: [spike-ledger.md contents not verified, project tools unavailable; whether proto/approval-flow resolves]
  outputs: [none]
  evidence: ["2026-06-14 · does the three-state approval flow feel right for batch sends? · answered — yes, with an explicit needs-changes state · proto/approval-flow · supersedes:none"]
  next: none
  approval_required: []
  tested: n/a