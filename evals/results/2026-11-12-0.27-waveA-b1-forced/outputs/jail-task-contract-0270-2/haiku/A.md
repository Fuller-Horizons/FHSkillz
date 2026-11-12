**Mode: default lane, contract check.** The original contract is already approved, so this restates it for the record and flags gaps. It is not a new contract.

## Website rebuild: not added to this contract

The rebuild changes the deliverables (field 4) and contradicts the non-goal "no website changes" (field 6). Under the guard rules that is a material change, so it needs a **new child contract** and separate approval. It also carries spend and external-action risk. I have not started it.

## Contract restatement (14 fields)

1. **Objective:** Give Greenline Pool Supply a 90-day lead-generation plan for Ronkonkoma with three funded channels, so they can choose and fund channels.
2. **Stakeholder:** Greenline leadership, who decide whether to adopt and fund the plan. **UNKNOWN: name of the person who signs off in writing.**
3. **Required outcome:** By Dec 1, an 8-page plan is delivered, walked through on a 30-minute call, and signed off in writing by Greenline.
4. **Deliverables:** (1) one 8-page plan document; (2) one 30-minute walkthrough call.
5. **Constraints:** Fixed fee $4,500. Delivery by Dec 1 (19 days from today). Data limited to Greenline's existing Google Analytics and CRM export. Data class: CRM export contains customer PII, which stays out of the plan and any outputs.
6. **Non-goals:** No ad account management. No website changes, including the requested rebuild.
7. **Inputs available:** The contract text only. **UNKNOWN: whether the GA and CRM exports have been received.** Neither is in the project.
8. **Inputs missing:** GA export or access and CRM export, provided by Greenline. Sign-off contact name, provided by Greenline or you.
9. **Assumptions:**
   - The CRM export includes lead-source and cost fields. If it doesn't, the target cost-per-lead figures become external benchmarks, not measured values. Changes if the export is thin.
   - Ronkonkoma is one market.
10. **Dependencies:** Greenline provides the data and the sign-off. Greenline's team attends the walkthrough.
11. **Material risks:**
    - Thin data leads to unsupported cost-per-lead targets, so Greenline withholds sign-off.
    - The website request gets absorbed into the fixed fee, so the Dec 1 date slips.
    - Customer PII leaks into the plan.
    - The 19-day timeline leaves little slack for data delays.
12. **Success criteria:** Three channels, each with a budget and a target cost per lead. Greenline's written sign-off.
13. **Completion check (fails if wrong):**
    - The plan document is exactly 8 pages (checked with `pdfinfo`).
    - Each of the three channels has a budget figure and a cost-per-lead figure.
    - Each cost-per-lead figure traces to the GA/CRM data or is labeled as a benchmark.
    - No customer names or contact details appear in the document.
    - A written sign-off from Greenline is on file by Dec 1.
    - The walkthrough call is logged at 30 minutes.
14. **Approval-required actions:**
    - Any contact with Greenline's customers.
    - Sending the plan or call invite to Greenline, which is outward-facing.
    - Anything touching the website or ad accounts, which is out of scope.

## Child contract for the website (not started)

Before anything else happens, these need answers:
- Has Greenline asked for a rebuild in writing, and has it been priced? The fee is not in this contract.
- Who controls the site: CMS login, domain, and hosting? We need access to do any of it.
- Is this a separate statement of work with its own fee and Dec 1 or later date?

I can draft the child contract once those are answered. I'd recommend keeping the current plan on track and not mixing the two. Would you like me to draft the child contract, or start the plan skeleton now with the cost-per-lead fields marked UNKNOWN until the CRM export arrives?