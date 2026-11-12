The spike ledger says this question is already answered, so I didn't build a prototype. I couldn't confirm that from the ledger itself.

**Question:** Does the three-state approval flow feel right for batch sends?

**Recorded answer (from your args, not verified):** 2026-06-14, answered: yes, with an explicit needs-changes state. Archive: `proto/approval-flow`. Supersedes: none.

**Why I stopped:** The skill's first rule is to check the ledger before building, and an answered question is retrieved rather than rebuilt. Two things blocked the check:
- The project read tools (`project_read`, `project_search`) aren't available in this session, so I couldn't open `claude/spike-ledger.md`.
- There's no local copy of `claude/` in the working directory.

Because I couldn't see the entry, I also couldn't confirm that the `proto/approval-flow` archive exists. A prototype run now would only repeat an answer you already have.

**What would change this:**
- If the premise has changed, for example the needs-changes state now has a different shape, this needs a new prototype. It should be logged as a superseding entry, not as a silent re-test. Tell me what changed and I'll scope it.
- If you want me to re-verify the 2026-06-14 entry, paste its text here or reconnect the project tools and I'll check it.