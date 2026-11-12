I won't merge `proto-approval` into main. The skill is explicit that the prototype never gets merged and only the validated decision does. "The demo works, deadline looms, throwaway code ships" is the specific case it was written to stop.

**What I checked**
- **Spike ledger:** it has one entry, the weekly scorecard layout. Nothing covers the approval flow, so there's no recorded answer and no verdict yet.
- **Workspace:** this directory is empty and isn't a git repo. I can't see `proto-approval`, its branch, or any surfaced-state output from the demo.

**What's missing for the ship gate (5 of 5, or the verdict is `inconclusive`)**
1. **Question:** you haven't stated it. Something like "Does the three-state approval flow feel right for batch sends?"
2. **Evidence:** I need at least one verbatim observation from the demo's surfaced state, and I don't have one.
3. **Archive pointer:** I need a branch or scratch path that actually exists.

**A plan that still hits Friday**
1. Send me the question, the demo output or your observations, and the branch or path.
2. I'll issue the SPIKE VERDICT, add the ledger line, and keep `proto-approval` on its archive branch as a primary source.
3. We then build the real implementation from the validated decision, starting from the demo's behavior. That's a smaller job than it sounds, because the hard design questions are already answered. It's also the only version that gets tests and error handling.

If the demo has to ship as-is on Friday, that's your call as the owner. It would be a new decision, though, and it shouldn't be recorded as a prototype verdict. I'd then suggest logging it as a time-boxed exception with a dated follow-up to replace it.

Do you want to send those three items now so I can write the verdict?