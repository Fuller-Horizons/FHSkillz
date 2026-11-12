I haven't built anything yet. The jail-prototype skill won't start without a stated question, and "mock something up and see how it feels" doesn't state one. A prototype with no question can't produce an answer. It would only produce an artifact that someone ends up promoting to production.

**Ledger check:** I couldn't read `spike-ledger.md` from here. It's a project doc and I have no project-read tool in this session, and nothing about batch-send turned up on disk. I can't confirm the question hasn't already been answered. If you can paste the ledger's batch-send lines, or tell me there aren't any, I'll treat the ledger check as done.

**What I need from you:** one sentence on what you want to find out about the batch-send screen. Each of these would lead to a different build:

| If your question is... | Shape | What I'd build |
|---|---|---|
| "Does the approval flow feel right for batch sends?" (for example, approve all, per-item, or tiered) | Logic | A small terminal harness that walks a batch through the approval states and prints the full state after every action |
| "Which layout makes a batch scannable and safe to send?" | Look | Exactly 3 radically different layouts of the screen, switchable in one place |
| "Can we actually do X, such as bulk-send with partial failure or retry?" | Feasibility | The thinnest end-to-end spike through the riskiest part |

Here are my defaults, so you can answer in a word. This is my guess, not something from the ledger or your request:

- **Shape:** look/feel, since you said "see how it feels."
- **Question:** "Which of three layouts lets a user review and confirm a batch send without missing a bad recipient?"
- **Timebox:** one working session, with one declared extension.
- **Name and location:** `proto-batch-send`, scratch path only, nothing under production paths.

Reply "go with the default" or give me your own question, and I'll build it. At the end I'll give you the SPIKE VERDICT and add a line to the ledger.