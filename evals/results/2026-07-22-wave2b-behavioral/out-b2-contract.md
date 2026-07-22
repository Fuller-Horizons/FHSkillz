# TASK CONTRACT — "Make our onboarding better" (DRAFT v0.1 — blocked, awaiting your answers + nod)

Invoking **jail-task-contract**: this request is ambiguous on the two things that decide everything downstream — *which* onboarding, and *what "better" means*. No serious work starts without a contract, so here is the cross-examination and the draft contract it produced. Nothing executes until the blocking questions are answered and you nod.

---

## 1 · What I looked up first (facts get looked up, never asked)

Before spending any of your attention, I searched the accessible workspace so I only ask you decisions:

- **F1 — Verified fact:** No Fuller Horizons onboarding artifacts exist anywhere in the accessible workspace (`/home/claude/work` — wave2b, FHSkillz repo, eval dirs). A case-insensitive search for "onboarding" returned 12 files; every match is an unrelated test fixture or a generic rubric line — none describe an actual FH onboarding process, checklist, intake form, or metric. (Searched 2026-07-22.)
- **F2 — Verified fact:** The FHSkillz repo describes Fuller Horizons' client work as sell-side business brokering + consulting (`/home/claude/work/FHSkillz/skills/jail-prospect/SKILL.md`, description frontmatter). This *supports* — but does not prove — the inference that "our onboarding" means client onboarding.
- **F3 — User-provided fact:** The full request is "Make our onboarding better." No type, trigger, metric, deadline, deliverable, or authority stated.

Consequence: everything about your current onboarding must come from you. The questions below are decisions and pointers to non-discoverable inputs — not facts I could have looked up.

---

## 2 · Cross-examination — Round 1 of max 2

**Mode: default lane** (3–5 related questions per round, two rounds maximum). Not grill mode: nothing yet indicates a wrong guess is *expensive* — no spend, no external comms, no named production system. **Escalation trigger:** if your answers reveal client PII, regulated data, or money in scope, I switch to grill mode (one question at a time, every branch walked) before execution.

**Q1 — Which onboarding? [BLOCKING]**
(a) **Client onboarding** — a new sell-side or consulting engagement, from signed agreement to working kickoff; (b) **employee/contractor onboarding**; (c) **user onboarding** for a software product or tool.
*My read:* (a), inferred from F2 — but a wrong guess here wastes 100% of the work, so I will not proceed on the inference.

**Q2 — The WHY: what put this on your desk now, and what does "better" mean? [BLOCKING]**
What happened — a lost or stalled deal, a client complaint, it eats too much of your time, no two onboardings run the same, a missed document, something else? Then one sentence: better = faster to kickoff / less of your manual time / stronger client first impression / fewer dropped steps / something else?
*Two guards:* "all of the above" is a conflict to resolve, not transcribe — if that's your answer, rank them. And this question is the XY-problem check: if the real trigger is "prospects go dark before signing," that's a conversion problem *upstream* of onboarding, and polishing onboarding won't fix it — that would be a different contract.

**Q3 — What exists today, and who can hand it to me?**
Per F1, nothing about your current process is discoverable here, so this is a genuine missing input: the current steps in whatever form they exist (doc, checklist, email templates, tool — "it's all in my head" is a valid answer and itself a finding), roughly how many onboardings per year, and who runs them (you, or someone I should hear from).

**Q4 — What deliverable, with what authority?** (this picks the type preset)
(a) **Diagnosis first** — a findings-and-recommendations memo (ANALYSIS preset; *my recommendation*, since Q2 is unanswered we don't yet know what's broken); (b) **a rebuilt onboarding package** — step checklist with owners, intake form, kickoff email drafts, document-request list (BUILD preset); (c) both, sequenced.
And the authority line: my default is that *nothing* goes to a real client and *nothing* is purchased without your explicit sign-off, regardless of your answer — confirm or extend.

**Q5 — Hard constraints.**
A deadline or event this must precede? Anyone besides you who signs off? Confidentiality/compliance realities — NDAs, seller financials, personal data in intake? *If yes to the last part, mode escalates to grill and handling goes strictest-wins (Rule 3).*

*Round discipline:* if Round 1 answers leave gaps, I get one more round. After that, round 3 = marked assumptions, shown — **except blocking items, which keep the stop.**

### Ambiguity split
- **Blocking (stop until answered):** Q1 — which onboarding; Q2 — trigger + definition of "better". Wrong guesses here = wasted work, so no assumption is allowed to cover them.
- **Resolvable (marked assumptions A2–A5 below; I proceed on them once the blockers clear):** audience, deadline, deliverable shape, data sensitivity.

---

## 3 · Draft contract v0.1 — all 14 fields ("none" and UNKNOWN are answers; vibes are not)

1. **Objective** — **UNKNOWN** (blocked by Q1+Q2). Best candidate, marked *Inference*: "Reduce the time, manual effort, and inconsistency in Fuller Horizons' client onboarding for new brokerage/consulting engagements." XY-watch: the stated ask is "better onboarding"; the underlying need may be conversion, capacity, or client trust — Q2 decides.
2. **Stakeholder** — Jonathan, Fuller Horizons (requester and consumer) [User-provided]. The decision this feeds is **UNKNOWN** — presumably *whether and how to change the way new engagements are run, and what fixing it is worth*. If the ANALYSIS preset applies, this field must name that decision explicitly before v1.0.
3. **Required outcome** — **UNKNOWN** pending Q2. Candidate shape: "the specific onboarding failure is named with evidence, and a fix exists that Jonathan can adopt on the next engagement without new headcount or tools."
4. **Deliverables** — pending Q4. Default proposal [Assumption A4]: **D1** diagnosis memo — findings → ranked recommendations, each with expected outcome, risks, tradeoffs, and reversibility (Rule 6); **D2** (if commissioned) rebuilt onboarding package — step checklist with owners and target times, intake form, kickoff email drafts, document-request list. Named artifacts only; no "improvements" delivered as vibes.
5. **Constraints** — none stated; none discoverable (F1). Pending Q5. Standing regardless of answers: I send nothing external; I spend nothing; confidentiality goes strictest-wins the moment seller/client data enters scope (Rule 3).
6. **Non-goals** (scope fence) — NOT sales/lead-gen funnel work upstream of a signed engagement (if Q2 relocates the problem there, that is a **new contract**, not creep); NOT employee onboarding unless Q1 says so; NOT tool procurement or migration; NOT contacting any real client or prospect.
7. **Inputs available** — the request (F3); environment facts F1–F2; the FHSkillz skill library for downstream steps (jail-diagnose, jail-research, jail-operationalize).
8. **Inputs missing** — current process artifacts or a described walkthrough + annual volume + who runs it (**provider: Jonathan**, or the person he names); the trigger incident/complaint behind "better" (**provider: Jonathan**); any baseline metric — time-to-kickoff, steps dropped, client complaints (**provider: Jonathan**; "no baseline exists" is acceptable and becomes finding #1).
9. **Assumptions** (each marked, with what changes it) —
   - **A1** [Inference, BLOCKING — *not proceeding on it*]: "onboarding" = client onboarding. Basis: F2. Replaced by Q1's answer.
   - **A2**: audience is internal (you). Changes if you want client-facing materials → those artifacts move behind the approval gate (field 14).
   - **A3**: no hard deadline. Changes if Q5 names one → deliverables re-sequence.
   - **A4**: diagnosis-before-rebuild (ANALYSIS before BUILD). Changes if Q4 picks (b).
   - **A5**: no regulated or PII-heavy data in scope. Changes if Q5 says otherwise → grill mode + strictest handling.
10. **Dependencies** — your Round-1 answers (the sole current blocker); access to whoever runs onboarding today if that isn't you; no external systems or third-party decisions identified.
11. **Material risks** (with consequence) —
    - **R1 — Wrong-branch execution:** guessing Q1/Q2 and being wrong = 100% wasted work and a stakeholder who now trusts the process less. This is why those two questions block rather than get assumed.
    - **R2 — XY problem:** onboarding may be the symptom while the disease is conversion or capacity; consequence: a polished onboarding and an unchanged business outcome.
    - **R3 — No-baseline trap:** with no current-state measure, "better" is unfalsifiable; consequence: an endless-revision loop — which is a drifted-contract symptom, not a picky stakeholder. Mitigation: field 13 forces a baseline or a named observation.
    - **R4 — Assumption laundering:** A1 quietly hardening into fact across revisions; mitigation: the label stays attached until Q1 is answered.
12. **Success criteria** — pending Q2. Proposed, to be edited rather than admired: (i) you can name the single biggest onboarding failure and point at its evidence; (ii) the recommended fix is adoptable on the *next* engagement without new spend (unless you authorize spend); (iii) a competent stranger could run an onboarding from D2 alone.
13. **Completion criteria** (testable — Rule 7; finalized at v1.0 per branch) —
    - **ANALYSIS branch:** memo contains ≥1 recommendation with confidence + change-conditions; every finding traces to a provided artifact or a named observation (e.g., "client X waited N days between signature and kickoff"); **fails** if any recommendation rests on an unlabeled assumption or a claim that can't be audited back to its source.
    - **BUILD branch:** a named dry-run — you (or a role-played client) run intake → kickoff using *only* D2; every step requiring unwritten tribal knowledge is logged as a gap; **any gap = not done.**
    - "Report delivered" and "looks good" fail Rule 7 and are not on offer.
14. **Approval-required actions** — **none yet** (no execution has begun). Pre-registered for later [Rule 5], each returning for explicit authorization at the moment it arises: sending anything to a real client or prospect; purchasing or subscribing to any tool; changing any live form, system, or automation; writing client-identifying data to durable storage.

**Type preset:** pending Q4 — **ANALYSIS** (recommended: stakeholder = the change-or-not decision; completion = recommendation with confidence + change-conditions) or **BUILD** (completion = the dry-run check that fails if the package is wrong; risks then add blast radius + rollback). Presets shape fields; they never skip them.

---

## 4 · The gate

**Execution does not begin** until Q1 and Q2 are answered and you nod at (or correct) this draft. If you reply "just do it": per the skip clause I would state fields 1, 13, 14 and proceed — which converts A1 into *your accepted assumption*, coin flip included. The cheapest insurance you can buy is one word answering Q1 and one sentence answering Q2.

## 5 · Contract guard (in force once you nod)

- Revisions that leave **Objective / Stakeholder / Required outcome** materially intact → same contract, revision noted.
- A material change to goal, audience, data classification, deliverable, or authority → **STOP — new or child contract**, with a one-line diff of what changed (Rule 4). "One more thing" that touches deliverables gets noted; "one more thing" that touches fields 1–3 gets a new contract.

---

```yaml
JAIL-HANDOFF:
  skill: jail-task-contract
  status: blocked
  facts:
    - "F1: No FH onboarding artifacts in accessible workspace; all 12 'onboarding' matches are unrelated test fixtures (grep -i, /home/claude/work, 2026-07-22)"
    - "F2: FHSkillz repo frames Fuller Horizons' client work as sell-side business brokering + consulting (skills/jail-prospect/SKILL.md)"
    - "F3: User request verbatim: 'Make our onboarding better.' — no type, trigger, metric, deadline, or deliverable stated"
  assumptions:
    - "A1 (BLOCKING — not being proceeded on): 'onboarding' = client onboarding; inference from F2; replaced by Q1 answer"
    - "A2: internal audience; changes if client-facing materials requested (moves them behind approval gate)"
    - "A3: no hard deadline; changes if Q5 names one"
    - "A4: diagnosis-first (ANALYSIS) before any rebuild (BUILD); changes if Q4 selects rebuild"
    - "A5: no regulated/PII-heavy data in scope; if wrong, escalate to grill mode + strictest handling (Rule 3)"
  unknowns:
    - "Which onboarding: client / employee / product (Q1 — blocking)"
    - "Trigger and definition of 'better' — the WHY and the success metric (Q2 — blocking)"
    - "Current process, annual volume, and owner (Q3)"
    - "Deliverable shape and granted authority (Q4)"
    - "Deadline, sign-off chain, confidentiality constraints (Q5)"
  outputs:
    - "Draft TASK CONTRACT v0.1 (this document, all 14 fields)"
    - "Round-1 cross-examination Q1–Q5 (default lane, round 1 of max 2)"
  evidence:
    - "Workspace search, grep -i 'onboarding' across /home/claude/work · supports F1 · 12 matches, all eval/test fixtures · 2026-07-22"
    - "/home/claude/work/FHSkillz/skills/jail-prospect/SKILL.md description · supports F2 · 2026-07-22"
  risks:
    - "R1: wrong-branch guess on Q1/Q2 = 100% wasted work (why they block instead of being assumed)"
    - "R2: XY problem — onboarding may be the symptom; conversion/capacity may be the disease"
    - "R3: no baseline metric makes 'better' unfalsifiable → endless-revision loop"
  confidence: low   # in the draft's candidate framings, pending answers; the facts themselves are verified
  next: "Jonathan answers Q1-Q5 (minimum Q1-Q2) -> contract v1.0 + nod -> then jail-diagnose or jail-research (ANALYSIS branch) or direct execution with dry-run check (BUILD branch)"
  approval_required: []
```
