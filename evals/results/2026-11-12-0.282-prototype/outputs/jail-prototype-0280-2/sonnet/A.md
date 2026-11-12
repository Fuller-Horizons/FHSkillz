The prototype artifact and the ledger aren't reachable from this session, so the SHIP GATE fails and the verdict ships as `inconclusive`. The skill requires that. I found no `proto-*` files and no spike ledger on disk. I also have no project read/write tool here, so I couldn't check `claude/spike-ledger.md`.

```
SPIKE VERDICT
QUESTION:     Which of three layouts makes the onboarding checklist easiest for a new customer to finish?
SHAPE:        look
TIMEBOX:      not recorded → not recorded
LEDGER-CHECK: not performed (spike-ledger.md not readable this session)
EVIDENCE:     "PROTOTYPE FEEDBACK r1 · PICK: C · READ FIRST: the progress bar · NOTES: #4 remove the video step · #6 label 'Docs' is unclear."
VERDICT:      inconclusive
ARCHIVE:      none found (no proto-* path or branch resolves)
CONSUMER:     none
```

**Gate results**
1. Ledger checked before building: **fail**, could not read it.
2. Throwaway name present: **unverified**, no artifact found.
3. Zero files under production paths: **unverified**.
4. Verbatim surfaced-state observation: **pass**, your feedback line, quoted above.
5. Archive pointer resolves: **fail**.

**What the feedback says (a lead, not a verified answer)**
- **Layout:** C was the pick.
- **Progress bar:** it was the first thing you read, so keep it prominent in the build.
- **#4:** remove the video step.
- **#6:** the label "Docs" is unclear and needs a clearer name.

**Ledger line to append**
`2026-11-12 · onboarding checklist: which of 3 layouts is easiest to finish · inconclusive (pick C, gate unmet) · archive:none · supersedes:none`

**To upgrade this to `answered`**
- Give me the path or branch of the prototype so I can confirm it exists and is marked as throwaway.
- Let me check `claude/spike-ledger.md` for an earlier entry on this question.
- With those two, I can re-run the gate and re-ship the verdict as `answered`, consumed by `jail-decide`. I haven't written anything to the project.