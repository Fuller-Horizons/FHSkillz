I haven't built anything yet. The ledger check passed, but the prototype has no question to answer, and the skill won't start without one.

**Ledger check:** the only entry is the weekly scorecard layout, which is a different question. Nothing on the batch-send screen has been answered, so there's nothing to reuse or supersede.

**The problem:** "mock something up and see how it feels" has no falsifiable question behind it. I also can't find anything in the project that defines the batch-send screen. The closest material is the prospect briefs, where outreach drafts are "DRAFT ONLY, do not send" and any contact needs your approval. I'd be guessing at what the screen is for.

Which of these is the question? Or give me your own in one sentence.

1. **Look/feel:** "Which layout makes a batch of outreach drafts easiest to review and approve in under a minute?" I'd build exactly three radically different layouts, switchable in one place: a table with checkboxes, a one-at-a-time card stack, and a grouped-by-prospect review queue.
2. **Logic/state:** "Does a per-draft approve / hold / reject flow feel right when sending to several prospects at once?" I'd build a small in-memory harness that shows the full state after every action, with no real sending.
3. **Feasibility:** "Can we assemble a batch from the prospect briefs without leaking unverified facts into the drafts?" I'd build the thinnest end-to-end spike on one real brief.

Also tell me what gets sent (outreach emails, reports, something else) and who sends it. Once I have the question and that detail, I'll build it as a `proto-*` file in the scratchpad with a one-session timebox. It will send nothing and have no persistence.