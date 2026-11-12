I haven't built a prototype, because your ledger already answers this question. The skill's ship gate requires an answered question to be retrieved, not rebuilt, unless the premise has changed.

**Ledger hit (from the line you quoted):**
`2026-06-14 · does the three-state approval flow feel right for batch sends? · answered — yes, with an explicit needs-changes state · proto/approval-flow · supersedes:none`

**What to carry into the real plan:** keep the three-state approval flow for batch sends, and add an explicit **needs-changes** state. Only that decision goes into the plan. The prototype code stays on `proto/approval-flow` as a primary source and is never merged.

I couldn't open `claude/spike-ledger.md` in this session, so I'm relying on the line you pasted. I also haven't confirmed that `proto/approval-flow` still exists.

**If something has changed since June**, tell me which of these applies and I'll open a superseding entry (`supersedes:2026-06-14`) and prototype it:
- **Batch size or mix:** for example, much larger batches or mixed recipient types.
- **Approvers:** for example, multiple approvers, or approval delegated to someone else.
- **New states:** for example, partial approval, where some items in a batch pass and others don't.
- **Different question:** for example, a look-and-feel question about the UI, which would need three radically different variants.

If nothing has changed, the verdict stands and no new ledger line is needed. If you want the decision recorded for a downstream skill, I can hand it to `jail-decide` as a Fact-of-the-prototype.