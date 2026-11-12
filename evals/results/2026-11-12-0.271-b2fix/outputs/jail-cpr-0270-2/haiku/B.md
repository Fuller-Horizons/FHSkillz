# DEBRIEF: Dana / Rob call

**Labels:** attendee statements are **User-provided**. "Landed on" reads are **Inference** and flagged. Dates are **Inference** from today (Thu 12 Nov 2026) because the transcript only says "Wednesday," "Friday," and "next Friday."

## 1. Decisions made

| # | Decision | By | Evidence | Notes |
|---|---|---|---|---|
| D1 | Effective Monday, the office coordinator does all scheduling. Estimators only quote. | Dana (owner) | L6: "Decision: effective Monday, the office coordinator does all scheduling and estimators only quote." Jon confirms, L7. | **User-provided.** Start date Mon 16 Nov (**Inference**). Coordinator is not named (**Unknown**). |
| D2 | Lease the truck, not buy. | Dana | L13: "Let's lease it. Final answer, we lease the truck." | **User-provided.** $1,150/mo lease vs. $58,000 cash (Rob, L11). Reason: cash is tight until March invoices clear (Dana, L12). Lease term and terms not discussed (**Unknown**). |

## 2. Flagged (not decisions)

- **F1. Crew software vendor.** Rob prefers vendor #2 (L22). Dana says "I think we landed on the second one" but wants price first (L23). **Inference:** not decided. The vendor has not sent a quote (L24), and Dana says "We'll circle back" (L25). This needs a decision once pricing arrives.
- **F2. Quoting turnaround target.** Dana says same-day turnaround (L4). Rob says it depends on D1 (L5). This is a stated goal, not an adopted metric.
- **F3. Website form.** The form has sent leads to a dead inbox since summer (L16). Rob says it needs fixing (L17), Dana agrees someone should (L18), and then "We'll see who has time" (L20). No decision or owner.

## 3. Actions assigned

| # | Action | Owner | Deadline | Source |
|---|---|---|---|---|
| A1 | Tell estimators about the scheduling change | Dana | Friday huddle (**Inference:** Fri 13 Nov) | L9 |
| A2 | Call the dealer for lease paperwork | Rob | Wednesday (**Inference:** Wed 18 Nov, confirm) | L14 |
| A3 | Send a one-page comparison of the two crew-software vendors | Jon | Next Friday (**Inference:** Fri 20 Nov, or 13 Nov, confirm) | L26 |
| A4 | Send the recap | Jon | "Tomorrow" (L36). You plan to send today. | L36 |

## 4. Unowned: needs assignment

- **U1. Fix form routing** so leads reach a live inbox (L17–L20). Highest business impact: leads are being lost now.
- **U2. Train the coordinator on the estimating sheet.** Requested by Rob (L31), agreed by Dana (L32). No owner or date.
- **U3. Holiday schedule** for Rob's crew. Requested by Rob (L28), Dana says "normal stuff" (L29). No owner or date.
- **U4. Request the crew-software vendor quote** (L24–L25). No owner.
- **U5. Name the office coordinator** who takes on D1. The owner is unnamed (**Unknown**).

## 5. Commitments and open questions

- **Open:** crew-software price. Triggers F1 and needs a re-decision (see routing).
- **Open:** who is the coordinator, and does D1 start Monday 16 Nov?
- **Open:** lease term and terms, which affect D2.
- **Open:** who owns the form fix (U1) and holiday schedule (U3).

## 6. Results audit

Skipped. No CPR was written for this meeting. If you want one for the next session, the Results would be D1 and D2 closed, U1–U5 assigned, and F1 decided.

## 7. Routing

- **A1–A4** → your action tracker.
- **D1, D2** → jail-memory as decision records, with dates and owners filled in.
- **U1 (form) and D1 (scheduling)** → jail-plan. A dead inbox going unnoticed since summer points to no lead-intake monitoring, which is a recurring process gap.
- **F1** → jail-decide once the vendor quote arrives.
- **Next session's DESIGN step** → pick up U1–U5 and F1.

---

## Send-ready recap (draft, plain English)

**Subject:** Recap: [date] call, quoting, truck, and next steps

Dana, Rob,

Thanks for the call. Here's what we decided and who has what.

**Decisions**
1. **Scheduling:** Effective Monday, 16 November, the office coordinator handles all scheduling. Estimators only quote. [Name the coordinator.]
2. **Truck:** We're leasing, not buying, at $1,150 a month. This keeps cash available until the March invoices clear.

**Action items**
- **Dana:** Tell the estimators about the scheduling change at Friday's huddle (13 November).
- **Rob:** Call the dealer for the lease paperwork by Wednesday (18 November).
- **Jon:** Send a one-page comparison of the two crew-software vendors by Friday, 20 November.
- **Jon:** Send this recap. [Confirm.]

**Still open (needs an owner)**
- **Website form:** Leads have been going to a dead inbox since summer. [Assign an owner and a date.]
- **Coordinator training:** Train the coordinator on the estimating sheet. [Assign an owner and a date.]
- **Holiday schedule:** Rob's crew needs one. [Assign an owner and a date.]
- **Crew software:** Dana wants pricing before deciding. [Assign who requests the vendor quote.]

Let me know if I've missed anything.

Jon

---

**Before you send:** Confirm the call date so I can fix "Wednesday" and "next Friday," and tell me who should own the four open items. Those are the only parts of the draft I couldn't confirm from the transcript. I can also produce this as a DOCX if you want a formal file.

```
JAIL-HANDOFF:
  skill: jail-cpr
  status: partial
  facts: [D1 scheduling decision (L6); D2 lease decision (L13); $1,150/mo vs $58,000 cash (L11)]
  assumptions: [Call was yesterday; "Wednesday" = 18 Nov 2026; "next Friday" = 20 Nov 2026; "Friday huddle" = 13 Nov 2026; "Monday" = 16 Nov 2026]
  unknowns: [coordinator identity; lease term; crew-software price; owners for U1-U5; actual call date]
  outputs: [DEBRIEF sections 1-7; client recap draft]
  evidence: [transcript lines 4, 5, 6, 7, 9, 11, 12, 13, 14, 15-20, 22-25, 26, 28-32, 36]
  risks: [Form outage leaking leads since summer; F1 read as decided prematurely; unowned items may slip]
  confidence: high
  next: jail-decide on F1 after the vendor quote; jail-plan for lead intake
  approval_required: [Jon to confirm owners for U1-U5 before sending recap; Jon to confirm dates]
```