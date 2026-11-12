# Website rebuild is a new contract, not an addition to the Nov 3 one

**Status: STOP.** The Nov 3 contract stays in force, unchanged. Nothing on the website starts until a child contract is approved.

**One-line diff:** The request changes the objective from "90-day lead-gen plan" to "lead-gen plan plus website rebuild." It also contradicts the non-goal "no website changes," breaks the "only GA + CRM export" input limit, and goes beyond the $4,500 fixed fee and Dec 1 date (19 days from today).

| Field | Nov 3 contract | Website rebuild would need |
|---|---|---|
| 1 Objective | Lead-gen plan | New objective (underlying need unknown) |
| 4 Deliverables | 8-page plan + call | A site, plus platform, content and launch artifacts |
| 5 Constraints | $4,500, Dec 1, GA + CRM only | New fee, timeline and inputs |
| 6 Non-goals | No website changes | Directly contradicted |
| 14 Approval-required | Customer contact | Add: publishing or DNS changes, hosting/tool spend, site credentials access |

I'm running the default lane (round 1 of 2). These are decisions only. I haven't asked anything I could look up.

**Questions**

1. **Who is asking and who can sign?** Is the rebuild Greenline's request, or your idea? Which Greenline person approves changes to scope and fee? *Recommendation: written approval from the same signer as the Nov 3 contract.*
2. **Separate engagement or inside the $4,500?** *Recommendation: separate child contract with its own fee and date. A rebuild can't fit a $4,500 plan fee without hurting the plan.*
3. **What does "rebuild" mean?** Is it a full redesign on a new platform, or fixing the pages that drive leads (landing pages, forms, mobile, speed)? *Recommendation: scope it from the plan's findings. Deliver the plan first, then size the site work to the channels it picks.*
4. **Why is the site "awful"?** Is it conversion, mobile, outdated look, or SEO? Do you have evidence, such as GA bounce or conversion data? Without a why, any rebuild is a guess.
5. **Who controls the site, domain and hosting, and which platform is it on?** I need this to price and risk it. Credentials would be treated as a secret class and never pasted into the contract.

**Marked assumptions if you don't answer (resolvable, not blocking):**
- **A1:** The plan proceeds on its original scope and date, and the website is deferred. Changes if Q2 says to bundle it.
- **A2:** No website work, quotes or access requests go to Greenline until the child contract is approved.

**Blocking:** Q1 and Q2. Without them I can't set field 14 (authority and spend), so I won't ship a child contract. This follows the skill's rule that no partial contract leaves.

```
JAIL-HANDOFF
status: blocked — child contract needed
facts: Nov 3 contract approved (plan, $4,500, Dec 1, GA+CRM only, no website changes); today is Nov 12
assumptions: A1 plan proceeds unchanged; A2 no website work or outreach pending approval
unknowns: signer/authority; separate fee; rebuild scope; the "why"; site/platform/access
outputs: change-control finding + 5 questions (no contract emitted — fail closed)
next: answers to Q1–Q5 → draft child contract (fields 1–14) → approval → jail-research on current site/GA
approval_required: any customer contact; website changes; hosting/tool spend; site credentials access
```