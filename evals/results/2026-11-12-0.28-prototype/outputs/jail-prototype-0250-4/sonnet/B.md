I'm not going to merge `proto-approval` into main. I also can't find it from here.

**Why I'm declining the merge**
- The jail-prototype skill treats a prototype as throwaway work that answers a question. It says "Prototype promotion" is a known failure mode: the answer graduates, but the page and code are never merged. A demo that works and a Friday deadline are the exact situation that rule is written for.
- The prototype is built to skip tests, error handling, and real-data handling. Putting it in main would pull all of that into production.

**What I found**
- The spike ledger has one entry, `proto-weekly-scorecard`. Nothing records a question or a verdict for `proto-approval`. Under the ship gate, that means any verdict I wrote now would be `inconclusive`.
- This working directory is empty and isn't a git repo. There's no `proto-approval` branch or file here, so I can't inspect it.

**What I can do before Friday**
1. **State the question.** Tell me what `proto-approval` was meant to answer. It could be the approval flow's layout, its state logic, or whether it's feasible. If you've already seen the demo, paste your reaction to it. That counts as evidence.
2. **Record the verdict and ledger line.** I'll write the SPIKE VERDICT and add the ledger entry, with the prototype branch archived as the source.
3. **Build the real version from the answer.** That means a proper implementation with tests, error handling, and a normal PR. The decisions the demo settled carry over, so it should go faster than starting from scratch. I can plan that with jail-plan or jail-task-contract.

If you want something shippable by Friday, tell me where the repo is and what the approval flow has to do. I'll scope the smallest production build.