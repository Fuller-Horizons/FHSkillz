# JAIL-CPR · DEBRIEF — Ops meeting, Monday (inferred date: 2026-07-20)

**Headline first:** one decision was actually made — quarterly maintenance pricing at $890. Nothing left this meeting with both an owner and a date. The Henderson renewal call is due "this week," it is already Wednesday, and it still has no owner. One item Mike remembered as a decision was not one, and Dana corrected it on the record.

---

## Intake scan (jail-quarantine · inline lane)

- **Input:** user-pasted transcript excerpt of Monday's ops meeting. Treated as unverified third-party data; attendee remarks are data, not instructions.
- **Protected-class check:** no credentials, PII/PHI, regulated, or client-confidential material detected. The $890 figure is the user's own internal pricing, supplied directly by the user.
- **Injection check:** no instruction-styled text addressed to the assistant. Clean — proceeding under the third-party-data label.
- **Completeness:** this is an *excerpt*. Anything decided or assigned outside these five lines is **Unknown** — this debrief covers only what is quoted below. [Rules 1, 2]

---

## 1 · Decisions made (decided vs discussed vs deferred)

| # | Item | Status | By | Provenance (verbatim quote) |
|---|------|--------|----|----------------------------|
| D1 | Quarterly maintenance pricing set at **$890** | **DECIDED** | Dana | Dana: "Fine, we'll go with the quarterly maintenance pricing at $890." |
| X1 | Switching dispatch software | **NOT a decision — flagged** | — | Mike: "I think we landed on switching dispatch software too, right?" → Dana: "We said we'd LOOK at it." |
| P1 | Van wrap | **DEFERRED (tabled)** | Dana | Dana: "And the van wrap decision — table it until the pricing sheet is final." |

**Notes, with labels [Rule 1]:**

- **D1** — the one real decision. Unknowns not guessed at: the **unit/scope** of $890 (per quarter? per customer/site? per visit?) and the **effective date** are not stated in the excerpt. Confirm both before the price reaches a quote, invoice, or the pricing sheet. *(Unknown — what would resolve it: one confirmation from Dana.)* Dana's "Fine," reads as reluctant close after discussion — *inference*; the decision itself stands regardless.
- **X1** — this is exactly the ambiguous "I think we landed on…" pattern the DEBRIEF lane refuses to promote to a decision. Dana's correction is the controlling record: the actual commitment is to **evaluate** dispatch software, not to switch. Recorded under Commitments (below), not Decisions.
- **P1** — deferral with a defined un-tabling trigger: **pricing sheet final**. Trigger owner and date: **Unknown** (see U3).

---

## 2 · Actions assigned (action · owner · deadline)

**Fully assigned (owner + deadline): NONE.** Nothing in this excerpt left the room with a name on it.

**UNOWNED — NEEDS ASSIGNMENT** (listed, never silently filled with a guess):

| # | Action | Owner | Deadline | Provenance |
|---|--------|-------|----------|------------|
| U1 | Call the Henderson account about the renewal | **— none** ("Someone should call…") | "this week" (user-provided) — *inferred:* by Fri 2026-07-24, i.e. **2 business days from today** | Mike: "Someone should call the Henderson account about the renewal this week." |
| U2 | Evaluate dispatch software (the committed "look at it") | **— none** | **— none** | Dana: "We said we'd LOOK at it." |
| U3 | Finalize the pricing sheet *(implied dependency — inference, not stated as an action in the excerpt)* | **— none** | **— none** | Implied by Dana: "…table it until the pricing sheet is final." Listed so it can be owned, since it gates P1. |

**Urgency flag:** U1 has a live deadline and no owner mid-week. This is the item most likely to fall through.

---

## 3 · Commitments & open questions

**Commitments:**
- Team → evaluate dispatch software (standing commitment, per Dana's correction; no owner, no date — see U2).
- Dana → closed the quarterly maintenance price at $890 (D1).

**Parked:**
- Van wrap decision — until the pricing sheet is final (P1).

**Open questions:**
1. **Who** calls Henderson, and is "this week" confirmed as by Friday 2026-07-24?
2. **Who** owns the dispatch software evaluation, against what criteria, with what report-back date?
3. **Who** is finalizing the pricing sheet, and by when? (This is the trigger that un-tables the van wrap decision.)
4. What is the **unit/scope and effective date** of the $890 price — and does D1 feed the pricing sheet currently in progress?

---

## 4 · Results audit [Rule 7]

**No CPR exists for this meeting** — none was provided, and no prior planned-Results record is available to retrieve *(fallback: if a planned agenda/CPR for Monday exists, share it and this scorecard gets re-run against it)*. Untestable in advance means unscoreable after — the meeting's testable completion standard was never pinned.

Scored against a minimal implicit bar for an ops meeting:

| Check | Result |
|---|---|
| Decisions closed | 1 (D1) — but with unconfirmed scope/effective date |
| Actions leaving with owner + date | **0 of 3** |
| Ambiguity hygiene | 1 near-miss caught live (Dana correcting X1) — good |
| Deferrals with a defined trigger | 1 (P1) — trigger defined, trigger **unowned** |

**Recommendation:** run this skill's DESIGN lane before the next ops meeting — pin Results in advance so the next debrief scores against something real.

---

## 5 · Routing (follow-through)

**Actions → tracker** *(live template: action · owner · deadline)* — rows U1–U3 above are ready to paste; **blocked on owner assignment**, which is a human call, not a guess.

**Durable decision → jail-memory, ADR shape — DRAFT, pending human approval [Rule 5: no durable memory write without sign-off]:**

```
ADR: Quarterly maintenance pricing
Context:      Ops meeting Mon 2026-07-20 (inferred date); pricing discussed and
              closed by Dana after debate.
Decision:     Quarterly maintenance pricing = $890.
Consequences: Pricing sheet and future quotes reflect $890; unit/scope and
              effective date must be confirmed before external use; the final
              pricing sheet in turn un-tables the van wrap decision (P1).
Status:       accepted (scope confirmation outstanding)
Provenance:   user-pasted transcript excerpt, received 2026-07-22; quote:
              Dana — "Fine, we'll go with the quarterly maintenance pricing
              at $890."
```

**Decisions to be made later → jail-decide:**
- **Van wrap (P1):** when the pricing sheet is final, bring a jail-decide package (options, costs from the final sheet, consequences per option) so the un-tabled item produces a decision, not a re-deferral.
- **Dispatch software (X1/U2):** the evaluation's output is the required input for a future switch-vs-stay jail-decide package. Do not let it re-enter a meeting as an assumed decision.

**Recurring process gap → jail-operationalize (candidate only — one meeting is not yet a pattern; *inference*):** actions leaving the room owner-less ("someone should…"). Proposed standing rule if it recurs: **no topic closes without a name and a date on its action.**

**Carry-forward → next ops meeting's DESIGN lane (step-2 retrieval):**
1. Henderson renewal — call status (U1)
2. Dispatch software evaluation — owner + report-back (U2)
3. Van wrap decision — on the agenda only if the pricing sheet is final (P1/U3)
4. Confirm $890 scope + effective date (D1)

---

```yaml
JAIL-HANDOFF:
  skill: jail-cpr (DEBRIEF lane)
  status: complete
  facts:
    - "Quarterly maintenance pricing decided at $890 by Dana (user-provided transcript quote)"
    - "Dispatch software: commitment is to evaluate, not switch — Dana's on-record correction"
    - "Henderson renewal call requested for 'this week' with no owner named (Mike)"
    - "Van wrap decision tabled by Dana until the pricing sheet is final"
  assumptions:
    - "Meeting date = Mon 2026-07-20 (from 'Monday's ops meeting'; today is Wed 2026-07-22) — a stated date would replace it"
    - "'This week' = by Fri 2026-07-24 — owner confirmation would replace it"
  unknowns:
    - "Owner for Henderson call (U1)"
    - "Owner, criteria, and report-back date for dispatch evaluation (U2)"
    - "Owner and date for pricing-sheet finalization — the P1 un-tabling trigger (U3)"
    - "Unit/scope and effective date of the $890 price (D1)"
    - "Any decisions/actions outside the provided excerpt"
  outputs:
    - "Meeting debrief (this document)"
    - "ADR draft for D1 (pending approval)"
    - "Action-tracker rows U1–U3 (pending owners)"
    - "Carry-forward list for next DESIGN-lane run"
  evidence:
    - "Transcript excerpt · supports D1, X1, P1, U1, U2 · user-pasted in-conversation · 2026-07-22 · completeness unknown"
  risks:
    - "Henderson renewal call misses its window — deadline is live, no owner, mid-week"
    - "Dispatch 'switch' resurfaces as an assumed decision if the evaluation stays unowned"
    - "Van wrap stalls indefinitely if pricing-sheet finalization has no owner"
    - "$890 published with wrong scope/effective date if not confirmed"
  confidence: high
  next: "Human assigns owners for U1–U3 (U1 first — deadline is Friday), approves the ADR write to jail-memory, then DESIGN lane preps the next ops meeting from the carry-forward"
  approval_required:
    - "Owner assignments for U1, U2, U3"
    - "jail-memory durable write of the D1 ADR"
    - "Confirmation of $890 scope/effective date before any external-facing use"
```
