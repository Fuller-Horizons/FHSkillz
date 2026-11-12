# Worked example — ENGAGEMENT contract (sales-process diagnostic)

Synthetic data. Client and numbers are invented for illustration.

## Input

> A 12-person commercial cleaning company ("Harbor Clean", synthetic) owner
> says: "We get leads but close too few. I want someone to look at our sales
> process and tell me what to fix. I can spend about $4,500 and want it done
> in four weeks. Draft the scope so we agree before you start."

Mode: default lane (one round, 4 questions). Preset: ENGAGEMENT.
Trivial-ask check: not trivial — several threads, money, client-shared.

## Questions asked (decisions only)
1. "Close too few" — what number would you call too few, and what would you
   call good? (blocking)
2. Which lead sources are in scope (web form, phone, referrals)?
3. Who besides you decides what gets fixed first?
4. Can we read your last 6 months of quotes and outcomes from your CRM or
   spreadsheet?

Answers used in the contract below are marked **User-provided**. Where the
owner did not answer, the contract says Unknown.

## Output — Task Contract (client copy)

**Task Contract: Sales Process Diagnostic for Harbor Clean**

1. **Objective** — Find where leads are lost between first contact and a signed
   job, and rank the fixes. (User-provided: "close too few")
2. **Stakeholder** — The owner. Decision fed: which 2–3 sales fixes to pay for
   next quarter.
3. **Required outcome** — The owner can read a ranked list of fixes, each tied
   to a step in the sales process and to evidence from their own quotes.
4. **Deliverables** — (a) Sales process map, 1 page. (b) Lead-to-job funnel
   table from 6 months of quotes. (c) Ranked fix list, max 7 items. (d) 60-minute
   review call.
5. **Constraints** — Budget about $4,500 (User-provided, not yet signed). Four
   weeks from start. Client data treated as client-confidential; no customer
   names in the final report.
6. **Non-goals (out of scope, with why)** —
   - Building or changing the website: separate goal, needs its own contract.
   - Running ads or paid campaigns: spend and results risk sit outside a diagnostic.
   - Writing sales scripts or email sequences: comes after the diagnostic says what to fix.
   - Hiring or coaching the sales staff: different skill set, needs its own scope.
   - Changing or buying CRM software: no tool choice until the fixes are known.
   - Pricing review: needs cost data not in this scope.
7. **Inputs available** — Owner interview (User-provided). Nothing else yet.
8. **Inputs missing** — Last 6 months of quotes with outcome (owner, by
   day 3). Lead source list (owner, by day 3). 30 minutes with the person who
   answers the phone (owner arranges, by day 7). If late, the end date moves
   one day for each day late.
9. **Assumptions** — (a) "Close too few" means quotes that never become jobs;
   the owner confirms the rate. Would change: if the real problem is too few
   leads, the objective changes and this becomes a new contract. (b) The quote
   data is complete enough to count outcomes. Would change: if more than a
   quarter of quotes have no outcome, deliverable (b) shows ranges only.
10. **Dependencies** — Owner supplying data on time. Phone staff available for
    one interview.
11. **Material risks** — Data is thin or messy (Inference, not yet seen):
    funnel numbers become ranges and the fix list is lower confidence.
    Owner expects fixes to be done, not listed: the owner may judge the work
    a miss; mitigated by the non-goals list above.
12. **Success criteria** — The owner can say which step loses the most jobs and
    what to do first, without asking us to explain the report.
13. **Completion criteria (acceptance criteria)**
    - AC-001 — Quote data received. Action: we load the 6-month file. Expected:
      the funnel table shows count of leads, quotes, and signed jobs for each
      month. Must-not: any customer name appears in the report. Verification:
      named observation — open the table, scan the name column; the check fails
      if a name is found. Priority: required.
    - AC-002 — Sales process map. Action: map is compared to the owner and phone
      interviews. Expected: the owner confirms each step in writing or marks
      corrections. Must-not: a step appears that no interviewee described.
      Verification: human check by owner, because only they know the real
      process. Priority: required.
    - AC-003 — Ranked fix list. Expected: every fix names the step it
      addresses, the evidence (a table row or interview note), an owner, and a
      rough effort (low, medium, high). Must-not: a fix with no evidence line.
      Verification: diff check — count fixes vs. evidence lines; they must be
      equal. Priority: required.
    - AC-004 — Funnel claims. Expected: every number is labeled Fact or
      Estimate with its method. Must-not: an unlabeled number. Verification:
      label-lint script (jail-py-toolkit); manual fallback is to read each
      number and check for its label. Priority: required.
    - AC-005 — Review call held within 5 days of delivery. Expected: owner picks
      the top fixes on the call and we record the picks. Must-not: scope grows
      on the call without a change order. Verification: named observation — the
      call notes list the picks. Priority: nice.
14. **Approval-required actions** — Owner signs this scope. Owner approves any
    access to their quote system (read only). No outreach to their customers.
    No spend beyond the stated fee.

**Change-order triggers.** A request becomes a new contract if it adds a new
goal (for example more leads), a new deliverable (for example a website
rebuild), a new audience, a new data type (for example customer contact
lists), or more than 6 extra hours.

**Decision rights.** The owner approves each deliverable. The owner alone
approves scope changes. If the owner is out, work pauses; it does not continue
on assumption.

## Gate check
14 fields printed. Field 13 has ACs that can fail. Field 14 not empty. No
UNKNOWN left that blocks shipping (the "too few" rate is marked as an
assumption with a confirm step in field 9 and listed below).

```yaml
JAIL-HANDOFF:
  skill: jail-task-contract
  status: partial
  facts: ["Owner interview held; no documents opened yet"]
  assumptions: ["'Close too few' means quotes that never become jobs; owner to confirm the rate", "Quote data is complete enough to count outcomes"]
  unknowns: ["Current close rate and the owner's target", "Whether quote data exists in usable form", "Who else must approve fixes"]
  outputs: ["Task Contract: Sales Process Diagnostic (ENGAGEMENT, client copy)"]
  risks: ["Thin data lowers confidence in the ranked fixes", "Owner may expect fixes to be implemented, not ranked"]
  confidence: medium
  next: jail-research
  approval_required: ["Owner signs scope", "Read-only access to quote system", "No outreach to the client's customers", "No spend beyond stated fee"]
```
