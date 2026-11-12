I didn't build a prototype, because I can't find the ledger entry you quoted.

**What I checked**
- The project's `claude/spike-ledger.md` has one entry, dated 2026-11-12: the weekly scorecard layout. There's no 2026-06-14 approval-flow line and nothing about batch sends.
- A search of the working directory for `approval-flow` and `three-state` found nothing. It isn't a git repo, so I couldn't check for a `proto/approval-flow` branch.

**Why I stopped**
- If the entry is real, the Ship Gate says an answered question is retrieved, not rebuilt. Rebuilding it would be the re-litigation the ledger exists to prevent.
- If the entry isn't real, I can't use it as evidence. I also can't pass gate item 5, because there's no archive branch to point to.
- Here's the verdict as you stated it, but I haven't verified it. It would be a retrieved answer, not a new Fact-of-the-prototype:

```
QUESTION:     does the three-state approval flow feel right for batch sends?
LEDGER-CHECK: reuses 2026-06-14 entry (unverified; not in project ledger)
VERDICT:      answered, yes, with an explicit needs-changes state
ARCHIVE:      proto/approval-flow (unresolved)
```

**Pick one**
1. **The entry exists elsewhere**, for example in another repo or ledger. Point me to it. I'll verify it and add the missing line to the project ledger with the original verbatim evidence, and no prototype is needed.
2. **Re-prototype because the premise changed**, for example new batch-size limits or a new approver role. Tell me what changed. I'll open a superseding entry (`supersedes:2026-06-14`) and build a small terminal harness that shows the full state after every action. The three states, in your words, are approved, rejected and needs-changes.
3. **Re-prototype with no changed premise.** I'd rather not, but it's your call. The verdict would then be a fresh answer that duplicates the ledger line.

I'd start with option 1. Do you have the original entry or the proto/approval-flow branch?