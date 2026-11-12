# Stopped: this is a change to the contract, not a quiet addition

I haven't added the website rebuild. It conflicts with the approved Nov 3 contract in three places:

- **Non-goal:** "no website changes" is written into the contract, and a rebuild is the opposite.
- **Constraint:** the contract says the work uses only the existing Google Analytics and CRM export. A rebuild needs site access, content, hosting and design decisions.
- **Fee and date:** a rebuild is far more work than the $4,500 and Dec 1 cover.

**One-line diff:** Objective changes from "a 90-day lead-gen plan" to "a plan plus a new website". That touches fields 1–4 and 6, so it needs a child contract or change order.

**The Nov 3 contract stays in force, unchanged.** The plan, the 8-page document, the walkthrough call, the $4,500 fee and the Dec 1 date are not affected. Nothing on the website happens until the new contract is approved.

I'm in default mode, round 1 of 2. I can't write the child contract yet because I can't fill several fields without guessing. Each question has my recommendation.

1. **Who asked for this?** Did anyone at Greenline ask for a new site, or is this your own view? Who there can approve extra scope and fee in writing?
   *Recommend:* don't start until they confirm in writing. "Their current one is awful" is your opinion, so I've recorded it as an Inference and not as a client need.
2. **Why do they need it?** What outcome should a new site produce: more leads, more online orders, or better looks? If the plan's cost-per-lead targets depend on the site converting better, the site is part of the plan's risk.
   *Recommend:* add one line to the plan's risk section, "site conversion is a constraint". That is a recommendation and not a website change, so it stays inside the current contract.
3. **How big is it?** Is it a full rebuild, a refresh of the key pages, or a site audit with a recommended fix list? Does the site sell online?
   *Recommend:* a paid audit first, because the rebuild can't be priced or scheduled without one.
4. **Fee and timing.** What fee and date apply to the website work? Pricing is User-provided, so I won't guess it.
   *Recommend:* a separate fee and date, with Dec 1 unchanged.
5. **Access.** Who provides domain, hosting and CMS access, plus photos and copy, and by when?
   *Recommend:* name one client owner with due dates before work starts.

Once you answer these, I'll draft the child contract (14 fields, ENGAGEMENT preset, client-ready). If you'd rather not open it now, I can write the change-order trigger into the current contract and leave the website for a later engagement.

```
JAIL-HANDOFF
status: blocked — awaiting answers on child-contract scope
facts: Nov 3 contract approved; non-goal "no website changes"; fee $4,500; due Dec 1
assumptions: [Inference] the site is weak, from user opinion only; no client request confirmed
unknowns: client authority for extra scope; website scope tier; website fee and date; site/hosting access; whether any customer contact is needed
outputs: scope-guard decision (no silent addition); original contract unchanged
next: user answers Q1–Q5 → jail-task-contract (child contract) → continue the Nov 3 plan
approval_required: written client approval of any website scope or fee; any contact with Greenline's customers (from the original contract)
```