The prototype answer is in, but I can't pass the ship gate from here, so this ships as **inconclusive**.

```
SPIKE VERDICT
QUESTION:     Which of three layouts makes the onboarding checklist easiest for a new customer to finish?
SHAPE:        look
TIMEBOX:      unknown → unknown (round r1; the prototype session isn't in this conversation)
LEDGER-CHECK: none (not verified; the project spike ledger isn't readable from this session)
EVIDENCE:     "PICK: C · READ FIRST: the progress bar · NOTES: #4 remove the video step · #6 label 'Docs' is unclear"  (user-reported feedback, not a surfaced-state observation from the prototype)
VERDICT:      inconclusive
ARCHIVE:      not provided
CONSUMER:     none
```

**Ship gate, 5 of 5 required:**

1. **Ledger checked before building:** not met. I have no project read tool in this session, so I couldn't check `claude/spike-ledger.md` for a prior answer.
2. **Throwaway name present (`proto-*` or `PROTOTYPE — wipe me`):** unknown. The prototype isn't in this conversation.
3. **Zero files under production paths:** unknown, for the same reason.
4. **Verbatim surfaced-state observation in EVIDENCE:** not met. Your feedback is a judgment ("PICK: C", "READ FIRST: the progress bar"), not a quoted observation of the prototype's state.
5. **ARCHIVE pointer resolves:** not met. No branch or scratch path was given.

**What the feedback does tell us:** layout C was preferred, the progress bar is what people read first, and two changes are proposed: remove the video step (#4) and rename the "Docs" label (#6).

**To close this out:**
- Give me the archive path (branch or scratch folder) and, ideally, the state the prototype showed when someone picked C. With those, I can re-run the gate and ship `answered`.
- Enable a project read/write tool, or paste the ledger line below into `claude/spike-ledger.md` yourself:

`2026-11-12 · Which of three layouts makes the onboarding checklist easiest for a new customer to finish? · inconclusive · archive: <missing> · supersedes:none`

Per the skill, the prototype's code stays out of main. The only thing that should carry forward is the decision (layout C, with the progress bar as its anchor) once it's verified.