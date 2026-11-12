**Verdict: inconclusive.** The reviewer picked layout C, but the spike doesn't pass the ship gate yet, so I can't promote it.

```
SPIKE VERDICT
QUESTION:     Which of three layouts makes the onboarding checklist easiest for a new customer to finish?
SHAPE:        look
TIMEBOX:      default (1 session, 1 feedback round, no extension) → 1 session, rounds: 1 (r1)
LEDGER-CHECK: unverified - no project tools in this session, so the spike ledger was not searched
DESIGN:       unknown - the prototype build is not in this session
EVIDENCE:     "PICK: C · READ FIRST: the progress bar · NOTES: #4 remove the video step · #6 label 'Docs' is unclear."
VERDICT:      inconclusive
ANSWER:       Reviewer chose layout C as easiest to finish. They looked at the progress bar first. This is one reviewer's answer, so treat it as a lead, not a settled decision.
ARCHIVE:      missing - no prototype file or artifact link in this session
CONSUMER:     none (until the verdict is promoted)
```

**Ship gate:**
1. Ledger checked before building: **not met**. I couldn't read the ledger from here.
2. Throwaway name and PROTOTYPE marking: **unknown**, since I can't see the build.
3. No files under production paths: **unknown**.
4. Verbatim reviewer answer in EVIDENCE: **met**.
5. ARCHIVE pointer resolves: **not met**. No link or path.
6. `artifact-lint` passed or manual check stated: **unknown**.

**Notes #4 and #6** are polish fixes to layout C: remove the video step, and rename the 'Docs' label. They don't change the pick, and the one-round timebox is used up, so I'd carry them as follow-up build items rather than another round.

**To promote this to `answered`, send me:**
- The prototype file path or artifact link, so the archive pointer resolves.
- Confirmation that layout C is the variant the reviewer marked, and its name.
- Whether the ledger already has a question entry, so I can supersede it instead of duplicating it.

Once I have those, I'll re-run the gate and write the ledger line:
`2026-11-12 · Which of three layouts makes the onboarding checklist easiest to finish? · inconclusive (pending archive) · archive: <link> · supersedes:none`

**JAIL-HANDOFF**
```
JAIL-HANDOFF:
  skill: jail-prototype
  status: partial
  assumptions: [reviewer answers are for the current onboarding checklist prototype, round 1]
  unknowns: [ledger contents, prototype archive location, variant names, build marking]
  outputs: [SPIKE VERDICT (inconclusive)]
  evidence: ["PICK: C · READ FIRST: the progress bar · NOTES: #4 remove the video step · #6 label 'Docs' is unclear."]
  next: jail-decide  (only after the archive pointer and ledger check are done)
  approval_required: [none]
  tested: n/a
```