I won't merge `proto-approval` into main. That's the prototype-promotion case this skill is built to stop, and I don't think we need to merge it to hit Friday.

**Why not**
- A prototype's code is throwaway by design. It skips tests, error handling and abstractions (Rule 4), and it holds state only in memory (Rule 3). Cleaning it up means rewriting it as an implementation, and a quick clean-up pass won't get it to production quality.
- A demo that works only proves it runs. The skill treats unwitnessed state as no evidence at all.
- The SHIP GATE fails closed, and "main keeps only the validated decision." The code stays on its archive pointer as a primary source and never gets merged.

**What I couldn't verify**
- The working directory has no git repo, so I can't see a `proto-approval` branch.
- I don't have the project's `spike-ledger.md` available here. Gate item 1 requires checking it before building, so I can't confirm whether this question was already answered.

**A faster route to Friday**
1. Name the question in one sentence, for example "Does the approval flow work for X?".
2. Write down what the demo showed, quoting the state it surfaced verbatim, as the EVIDENCE line.
3. Ship the SPIKE VERDICT and add a ledger line.
4. Build the real implementation from the validated decision, using the prototype as a reference. Re-typing a working flow is much faster than discovering one, so this is usually quick.
5. If time is short, demo from the `proto-approval` branch on Friday, clearly labeled as a prototype, and ship the real implementation right after.

Send me the question the prototype was meant to answer and what the demo surfaced. I'll draft the verdict block and the ledger line. If the branch lives in another repo, point me to it so I can confirm the archive pointer resolves.