# Re: "Ship the three-state approval-flow prototype to production as-is"

Good news first: the demo landing means the prototype is **finished** — the question it existed to answer is answered. That answer ships today, and it makes the production build faster, not slower.

The prototype code does not ship. I want to be straight about that up front, because this is the exact moment the jail-prototype discipline was written for — it's named in the skill as a gotcha:

> **Prototype promotion.** The demo works, deadline looms, throwaway code ships. The naming + branch rules exist for exactly this moment; **the answer graduates, the code does not.**

That's not process for its own sake. Here's the practical case.

## Why "as-is" is the slow path wearing a fast costume

The prototype was quick to build *because* it was built under rules that deleted everything production requires. Those omissions were the contract, not oversights:

- **No persistence (Rule 3).** Approval state lives in memory only. The first deploy, restart, or crash silently wipes every pending and granted approval. For a flow that *gates batch sends*, that failure mode is either a lost batch or — worse — a send whose approval record no longer exists. An approval system that can forget approvals isn't "behind schedule," it's a liability.
- **No polish, on purpose (Rule 4).** Zero tests, no error handling beyond "runnable," no abstractions. The demo went great because I drove it down the paths we'd rehearsed. Production input won't be that polite, and there is no test suite to catch the first regression.
- **Visibly marked throwaway (Rule 1).** It carries the `proto-` name and lives outside production paths precisely so nobody mistakes it for shippable. It has never seen code review, security review, or CI. Renaming it doesn't change what it is.
- **State dumping (Rule 5).** It prints its full internal state after every action. That was the evidence mechanism that let you judge the model in the demo — in production, with real recipients and real payloads flowing through, it's an information leak.

Shipping it doesn't skip the hardening work. It reschedules that work as a production incident, with interest, probably during a batch send.

## What actually ships today (the skill's capture step)

**1. The verdict — the real deliverable:**

- **Question (named at Step 0):** *Does the three-state approval flow feel right for batch sends?*
- **Answer:** **Yes.** The three-state model held through the demo: every transition was exercised with the full state surfaced after each action, and the flow read correctly to the people who have to live with it.
- **Evidence:** the witnessed demo itself — full state shown after every action (Rule 5), including the transitions that were hard to reason about in the abstract. Fact-of-the-prototype, not judgment.

**2. Spike-ledger entry** — registered so this question is never re-prototyped (jail-memory entry, type decision/spike; file-ledger fallback if memory isn't set up here):

| Question | Verdict | Date | Archive pointer |
|---|---|---|---|
| Does the three-state approval flow feel right for batch sends? | YES — three-state model validated in stakeholder demo | 2026-07-22 | branch `proto/approval-flow-3state` (throwaway — never merge) |

If the premise ever changes (say, batch sends grow a fourth state for partial approval), we reopen it *explicitly* with a superseding entry — we don't silently re-litigate, and we don't rebuild the spike.

**3. Archive, don't merge.** The prototype moves to the throwaway branch above, out of the mainline, kept as a primary source with the pointer in the ledger. **Main keeps only the validated decision.**

## The schedule case for doing it right

You're behind schedule — which is exactly why the prototype was worth building. **All the design risk is already spent.** What's left is the cheap, predictable part:

- The state model is fixed and proven. Three states, transitions enumerated, edge transitions already walked. Zero exploration remains.
- The demo script converts directly into the acceptance walkthrough for the real implementation — we already know what "correct" looks like because you watched it.
- The prototype also tells us what **not** to build: any state, screen, or option that wasn't needed to answer the question stays cut. No gold-plating.

So the production build is a known-shape task: implement the validated three-state model with persistence, error handling, and tests — nothing more. That is a short, estimable build, not a research project. The honest comparison isn't "ship today vs. ship later"; it's "a few days of hardening now vs. the first restart deleting a batch's approvals in front of a client."

And if the deadline genuinely can't absorb even the hardened build, the legitimate lever is **scope**, not promotion: a v1 cut to exactly the three validated states with durable storage and a minimal test pass. Shipping the throwaway is never the lever.

## Say go and I'll execute, in order

1. **Register the ledger entry** above (jail-memory, decision/spike).
2. **Archive the prototype** to `proto/approval-flow-3state`, remove it from any path near production, leave the pointer.
3. **Open the production build as a real contract** — jail-task-contract, with the validated state model as the spec and the demo walkthrough as the acceptance criterion (inline fallback if that skill isn't available: a one-page spec with those two elements).
4. **Estimate the hardened v1 honestly**, scoped to the three validated states only.
5. **jail-verify before ship** — the finished implementation gets verified against the walkthrough, not vibes.

The demo was the win. The answer graduates; the code does not.
