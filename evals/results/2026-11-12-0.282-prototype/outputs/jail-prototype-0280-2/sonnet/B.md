The ship gate fails on two items, so I'm shipping this as `inconclusive`. Your answers are in, but I can't confirm the ledger check or the archive pointer.

- **Ledger:** this session has no project read/write tool, and there is no local `spike-ledger.md`. I couldn't check whether this question was already answered.
- **Archive:** there is no `proto-*` file on disk, so there is nothing for the pointer to resolve to.

The gate fails closed, so I didn't invent either one. Your pick still stands as the finding.

```
SPIKE VERDICT
QUESTION:     Which of three layouts makes the onboarding checklist easiest for a new customer to finish?
SHAPE:        look
TIMEBOX:      one session, one round → one round (r1) · rounds: 1
LEDGER-CHECK: not performed (ledger not reachable this session)
DESIGN:       not recorded (page not available here)
EVIDENCE:     "PROTOTYPE FEEDBACK r1 · PICK: C · READ FIRST: the progress bar · NOTES: #4 remove the video step · #6 label 'Docs' is unclear."
VERDICT:      inconclusive  (ship gate items 1 and 5 unmet; the reviewer's answer itself is clear)
ANSWER:       Layout C is the reviewer's pick, and the progress bar is what they read first, so keep it prominent. Carry two changes forward: drop the video step (#4) and relabel "Docs" (#6).
ARCHIVE:      none resolvable. No proto-* file found in /tmp/fhlive-h_snpf8e.
CONSUMER:     jail-decide
```

**Ledger line:**
`2026-11-12 · onboarding checklist: which of 3 layouts is easiest to finish · inconclusive (pick C; gate unmet: ledger unchecked, archive missing) · archive: none · supersedes:none`

```
JAIL-HANDOFF:
  skill: jail-prototype
  status: partial
  assumptions: ["r1 was the only round and the one declared timebox", "the PICK refers to the prototype's variant C"]
  unknowns: ["whether the ledger already has this question", "where the prototype file lives", "what C looks like, so the answer can't yet be written up as a design spec"]
  outputs: [SPIKE VERDICT]
  evidence: ["PICK: C · READ FIRST: the progress bar · #4 remove the video step · #6 'Docs' unclear"]
  next: jail-decide
  approval_required: ["writing this ledger line to claude/spike-ledger.md (durable project write)"]
  tested: n/a
```

**To promote this to `answered`:**
1. Give me the path or artifact link to the prototype page, and I'll confirm it resolves.
2. Either paste `claude/spike-ledger.md` here, or run this from a session with project access. I'll then do the ledger check and append the line above.

I haven't written anything to the project.