**Mode:** Default lane (not grill). The Nov 3 contract is already approved, so I'm restating it for the guard check, not re-approving it.

## Guard result: website rebuild is a new contract, not an addition

Your request to rebuild the website changes this contract in three places:

- **Field 4 (deliverables):** adds a rebuilt website, which is a new external, durable artifact.
- **Field 6 (non-goals):** directly contradicts "no website changes."
- **Field 14 (approvals):** a site launch is an external, durable action with spend, and nobody has authorized it.

I have not added it to this contract and have not started any website work. It needs its own contract (see below).

## Original contract, restated (approved Nov 3)

1. **Objective:** Give Greenline Pool Supply (Ronkonkoma) a 90-day plan with three lead-generation channels. *User-provided.*
2. **Stakeholder:** Greenline's decision-maker, who chooses and funds the channels. Name: **Unknown.**
3. **Required outcome:** Plan delivered by Dec 1, each channel with a budget and target cost per lead (CPL), and Greenline signs off in writing.
4. **Deliverables:** (1) one 8-page plan document; (2) one 30-minute walkthrough call.
5. **Constraints:** Fixed fee $4,500; delivery by Dec 1; data limited to Greenline's existing Google Analytics and CRM export. *User-provided.*
6. **Non-goals:** No ad account management. No website changes.
7. **Inputs available:** GA access and the CRM export. *Contents not yet reviewed: Unknown.*
8. **Inputs missing:**
   - 90-day marketing budget. Unknown; provided by Greenline.
   - Historical lead-source and close data to set CPL targets. Unknown whether the CRM export has it; provided by Greenline.
   - Sign-off contact and date. Unknown; provided by Greenline.
9. **Assumptions:**
   - CPL targets come from GA/CRM history. *Assumption.* If the data is missing, targets become labeled **Estimates**.
   - Channel choice is **Judgment**, settled in the plan.
10. **Dependencies:** Greenline supplies GA access and the CRM export, reviews the plan, and signs off in writing.
11. **Material risks:**
    - CRM lacks lead-source fields, so CPL targets are guesses and sign-off is at risk. *Unknown until the export is reviewed.*
    - Timeline: 19 days from today (Nov 12) to Dec 1. Late inputs compress the work.
    - Scope creep: the website request (see guard result).
    - Pressure to contact customers for validation. Blocked by the approval gate.
12. **Success criteria:** Greenline can act on the plan without us and signs off in writing.
13. **Acceptance criteria:**
    - **AC-001:** Plan file is exactly 8 pages. Verification: page count of the final file. *Required.*
    - **AC-002:** Exactly 3 channels, each with a monthly budget and a target CPL. A plan with a channel missing either one **fails** this check. Verification: table check. *Required.*
    - **AC-003:** Every CPL cites GA or CRM data, or is labeled Estimate. Verification: human check of citations. *Required.*
    - **AC-004:** No ad account change, website edit, or customer contact occurred. Verification: activity log review. *Required.*
    - **AC-005:** 30-minute walkthrough held by Dec 1. Verification: calendar record. *Required.*
    - **AC-006:** Written sign-off received. Verification: signed email or document. *Required.* The contract gives no sign-off date, so the deadline is **Unknown**.
14. **Approval-required:** Any contact with Greenline's customers (outreach, surveys, interviews). Any spend. Any ad or website change (already out of scope).

## Proposed child contract: website rebuild (not started)

- **Objective (draft):** Decide whether Greenline gets a website rebuild, and if so, under what separate scope.
- **Fee, timeline, site access, CMS/hosting owner:** Unknown. None are in the original contract.
- **Approval:** Greenline's written approval before any site change, since launching a site is external and durable.
- **Quality check:** "Awful" is a judgment. It needs a scored review (jail-rate) before it drives scope.
- **My recommendation:** Run the website as a separate, separately priced contract after the Dec 1 plan delivery, so it can't put the Dec 1 deadline at risk.

## Decisions I need from you

1. **Website:** Separate contract with its own fee and timing (my recommendation), or drop it from this engagement?
2. **Sign-off:** Who at Greenline signs off, and by what date? The contract doesn't say.
3. **Budget:** Does Greenline have a 90-day marketing budget figure? If not, the plan will propose a range, labeled Estimate.

Also, please send the CRM export. I'll check it for lead-source and close-date fields, which decides whether the CPL targets can be sourced (AC-003).

I've searched the Business Consulting Tools project and found no Greenline material. Once you confirm, I can save this contract there.

```
JAIL-HANDOFF
status: blocked — guard stop on website scope; original contract otherwise unchanged
facts: contract approved Nov 3 (User-provided); delivery Dec 1; fee $4,500 (User-provided)
assumptions: CRM export contains lead-source data (Unknown until reviewed)
unknowns: 90-day budget; sign-off contact and date; CRM contents; website decision
outputs: restated 14-field contract (above); child-contract draft for website (not started)
next: await answers to decisions 1–3, then receive CRM export → jail-research (CPL sourcing) → plan build
approval_required: any customer contact; any spend; any website or ad-account change (out of scope)
```