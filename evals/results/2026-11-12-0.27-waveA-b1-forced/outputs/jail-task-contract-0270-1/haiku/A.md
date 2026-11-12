**Mode:** Default lane, round 1 of 2. Preset: ENGAGEMENT. Not trivial: it involves money, client accounts, and a deadline.

**Lookup:** The project has no record of this owner or business. Everything about them below is User-provided (your brief) or Unknown.

## Round 1: decisions only (all blocking)

1. **What result by spring would count as a win?** *Recommended:* booked estimates or consult requests per month, measured against a baseline from their own records, with March 15, 2027 as the date. The success measure and the readout depend on this.
2. **Advice only, or hands-on setup?** Do you want a plan the owner runs, or do we also set up approved fixes (Google Business Profile, website copy, review requests)? *Recommended:* we plan and set up approved fixes; the owner runs day-to-day. This changes the deliverables and what fits in $6k.
3. **Is the $6k all-in?** Does it cover only our fee, or also ad spend and vendors? *Recommended:* $6k is our fee; ad spend is a separate owner budget with its own approval. A wrong guess here means unapproved spend.
4. **What is "broken," in the owner's words?** Ask for the top two problems they have noticed. We record their words and do not redefine "fixing marketing."

## Draft Task Contract (ENGAGEMENT). DRAFT, not shipped

Fields 3, 4, 5, and 13 depend on Q1–Q4.

1. **Objective:** Get more booked landscaping jobs from marketing before spring 2027, using methods the owner approves. ("Fixing marketing" is User-provided; definition pending Q4.)
2. **Stakeholder:** The owner. Decision fed: which marketing fixes to fund for spring.
3. **Required outcome:** By March 15, 2027, the owner has a measured count of booked jobs or estimates against a baseline, plus a ranked plan they approved. *Estimate:* about 18 weeks from today.
4. **Deliverables:**
   - D1. Channel inventory: website, Google Business Profile, reviews, listings, any ads.
   - D2. Lead-to-job funnel from the last 12 months of records, by month and source.
   - D3. Ranked 90-day plan, five actions maximum, each with owner, cost, date, and a failure threshold.
   - D4. Setup of owner-approved fixes. Scope pending Q2.
   - D5. Spring readout on March 15, 2027: counts against baseline.
   - D6. 60-minute review call.
5. **Constraints:** About $6k total (User-provided; split pending Q3). Target date March 15, 2027 (Assumption A1). Customer data is confidential: reports use counts only, never names or contact details. Passwords never appear in reports or chat.
6. **Non-goals (with why):**
   - Running paid ad campaigns: the owner's money and results risk; needs its own contract.
   - Building a new website: a separate build that the $6k scope cannot absorb.
   - Guaranteeing jobs or leads: demand and crew capacity are outside our control.
   - Hiring, training, or managing crew or office staff: a different skill set.
   - Pricing or job-costing review: needs cost data not in scope.
   - Ongoing social posting after March 15: a recurring service needing its own contract.
   - Messages to the owner's customers: sent only by the owner, after approval.

   **Change-order triggers:** a new goal (hiring, new service line); a new deliverable (website build, ad management, ongoing content); a new audience or data class (customer contact lists, payment data); hours beyond the cap [cap: SRG to set]; a new system touched (CRM install, new ad account).
   **Decision rights:** The owner approves each deliverable and any scope change. You, as SRG lead, decide method disputes. If the owner is unavailable, work pauses; it does not continue on assumption.
7. **Inputs available:** Owner brief (User-provided). Nothing else yet.
8. **Inputs missing** (owner unless noted; day 0 = signing):
   - Company name, location, service area. Day 3. We cannot look up public listings without it.
   - Last 12 months of leads, quotes, and jobs, in any form. Day 5. If late, D2 shows ranges and the readout date moves one day per day late.
   - Read-only access to website, Google Business Profile, review pages. Day 5.
   - Current marketing spend and vendors. Day 5.
   - 30-minute call with whoever answers the phone and takes estimate requests. Day 10.
9. **Assumptions:**
   - A1. Spring target is March 15, 2027 (Estimate). Changes if the owner means another date (Q1).
   - A2. The owner alone approves deliverables and scope (Assumption). Changes if a partner or manager must sign off.
   - A3. Job volume is high enough to count (Estimate). Changes if fewer than about 20 jobs a year: D2 shows ranges only.
   - A4. Spring install decisions mostly happen January to March (Judgment, low confidence). Changes if the owner's data shows otherwise.
10. **Dependencies:** Owner signs after Q1–Q4 are answered. Owner supplies records and access on time. One phone-staff interview. SRG fee: Unknown; needs your number, and the scope must fit inside $6k.
11. **Material risks:**
    - R1. Four months is short for review and profile changes to move bookings (Judgment). Consequence: a "not met" readout, and the owner calls it a miss. Mitigation: measure counted results and track leading indicators (AC-003 thresholds).
    - R2. $6k may not cover advice plus setup (Estimate). Consequence: setup gets cut midway. Mitigation: size D4 after Q2.
    - R3. Records are thin or messy (Inference). Consequence: lower confidence in D2 and the plan.
    - R4. Account access involves credentials (class: credentials). Consequence: lockout or leak. Mitigation: owner adds us as a manager; no passwords shared.
    - R5. Records include customer contact details (class: personal data). Consequence: privacy exposure. Mitigation: aggregate counts only.
    - R6. Owner expects day-to-day marketing run for $6k (Judgment). Consequence: a scope dispute. Mitigation: the signed out-of-scope list.
12. **Success criteria:** The owner can name the channel that brings the most booked jobs and state the spring count against baseline, without asking us to explain the report.
13. **Completion criteria (acceptance criteria):**
    - **AC-001.** Baseline inventory. Action: review each channel the owner gives access to. Expected: one row per channel showing what exists, a Fact label, and a check date. Must-not: a claim about a channel we did not open. Verification: diff of table rows against channels named in D3. Priority: required.
    - **AC-002.** Funnel. Expected: month-by-source table of leads, quotes, and booked jobs; each number labeled Fact (from file) or Estimate (with method). Must-not: an unlabeled number, or any customer name or contact detail. Verification: label-lint plus name-column scan; any hit fails. Priority: required.
    - **AC-003.** Ranked plan. Expected: five actions maximum, each with channel, owner, cost, date, and a failure threshold (e.g., "fewer than 3 new booked estimates by Feb 15: stop"). Must-not: an action with no threshold. Verification: row-by-row checklist. Priority: required.
    - **AC-004.** Spend control. Expected: every cost in D3 has a written owner approval dated before the spend. Must-not: any purchase, listing, or ad launch without it. Verification: named observation of the approval log against each spend line. Priority: required.
    - **AC-005.** Change control. Expected: every edit to a live website, profile, or listing matches a written owner approval. Must-not: an unapproved live edit, or a password in any report. Verification: change log compared line by line with approval log. Priority: required.
    - **AC-006.** Spring readout. Expected: by March 15, 2027, counts of booked estimates, calls, and form leads against the AC-002 baseline, marked met or not met. Must-not: a result with no baseline. Verification: diff against AC-002. Priority: required.
    - **AC-007.** Review call within 5 days of D5; owner's top picks recorded. Priority: nice.
14. **Approval-required actions:** Owner signs the scope. Read-only access grants. Each live change to a website, profile, listing, or customer-facing message. Each spend line, including ad spend and vendor fees. Any message sent in the owner's name. SRG fee amount.

**Gate check:** 14 fields printed. Open UNKNOWNs: Q1–Q4, SRG fee, hours cap, company name and location. **Not shipped.** Once Q1–Q4 are answered, I'll finalize this as the plain-English client copy and leave the handoff out of it.

```yaml
JAIL-HANDOFF:
  skill: jail-task-contract
  status: partial
  facts: [owner brief only; no existing project record]
  assumptions: [A1 March 15 2027 target; A2 owner sole approver; A3 enough job volume; A4 spring decisions Jan-Mar]
  unknowns: [Q1 result metric; Q2 advice vs hands-on; Q3 $6k scope; Q4 "broken" in owner words; company name/location; SRG fee; hours cap]
  outputs: [ENGAGEMENT draft contract, not shipped]
  risks: [R1 timeline; R2 budget fit; R3 thin records; R4 credentials; R5 customer data; R6 expectation gap]
  confidence: low
  next: jail-research (baseline, D1-D2) after round 2 answers
  approval_required: [owner signs scope; read-only access; each live change; each spend line; messages in owner's name; SRG fee]
```