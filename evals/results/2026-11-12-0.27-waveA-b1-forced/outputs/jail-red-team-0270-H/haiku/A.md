**Lane: FULL SWEEP.** A $65k fixed-cost hire with commission, aimed at an unmeasured list, is consequential and hard to reverse. Independence: there is no producer model here, so I worked only from your plan. The project has no sales, compensation, or customer-data docs to check it against.

**Steelman:** You have a warm-ish asset (300 past customers who already know your firm), outbound to them is cheaper than cold prospecting, and a dedicated seller frees your time. A hire now, with a 4-month checkpoint, is a disciplined bet with a clear test.

**Model inputs.** Yours: $65k base, 300 accounts, 4-month payback. Everything else is my placeholder, marked as such. Replace these with your numbers before relying on the output.
- Four-month cost: ~$25–27k (base $21.7k + payroll tax + tools). Add ~$13k if you use a recruiter at ~20% of base.
- Average first engagement fee: $8k (placeholder). Delivery margin: 50%. Commission: 10%.
- Break-even on gross profit after commission: ~$65k of fees delivered in the window.

| Funnel (of 300) | Worst | Expected | Best |
|---|---|---|---|
| Valid contact | 50% | 60% | 75% |
| Meeting within 90 days | 4% | 10% | 18% |
| Meeting → win | 15% | 25% | 35% |
| Accounts won | ~1 | ~4.5 | ~14 |
| Won fees (at $8k) | $7k | $36k | $114k |
| Recognized in 4 months (50%, assumed) | $3.5k | $18k | $57k |
| Gross profit in window (40% after commission) | $1.4k | $7k | $23k |

---

**RED-TEAM FINDINGS (ranked by severity × likelihood)**

1. **The 4-month payback fails in the expected case, and in the best case on a margin basis.** Expected in-window gross profit is ~$7k against ~$26k of cost. Even the best case (~$23k) misses on margin. It passes only on a revenue basis, and only in the best case. Expected-case gross profit from this list is ~$14k over the whole campaign, so it does not pay back in year one from these accounts alone. Basis: Inference (placeholder margin, commission, fee, and timing).
   → Fix: state the payback definition (revenue or gross profit). Reprice the hire against your real fee, margin, and commission, or count her new-business pipeline (the plan doesn't yet).
   → falsifier: recompute the table with your actual fee, delivery margin, and commission. Disproved if in-window gross profit reaches ~$26k in the expected funnel.
     · falsifier-status: RUN-NOW → result: confirmed (under placeholder inputs; the expected case fails across the ranges above, and it holds unless the fee is roughly double the placeholder).

2. **The conversion rate of the 300 dormant accounts is unmeasured, and every number above depends on it.** You don't know why they went dormant, how many still have a valid contact, or how many replied in the last year. Dormancy may mean churn, a departed champion, or a bad experience, and a new rep won't fix any of those. Basis: Judgment (no data in hand).
   → Fix: before hiring, export the 300 with last-purchase date, reason-lost (if recorded), contact validity, and last outreach outcome. Segment them by recency.
   → falsifier: if fewer than ~5% replied or bought in the last 12 months, the expected funnel is too optimistic.
     · falsifier-status: HANDOFF → owner: you (or whoever runs the CRM); lab spec: CRM export of the 300 with those five fields, counted into the segments above.

3. **Time to first close is probably longer than the 4-month window.** A new rep needs ramp time, and the first close usually lands after the first meetings. Basis: Judgment.
   → Fix: measure your own cycle, then set the checkpoint against it.
   → falsifier: days from first contact to signed engagement across your last five engagements. Disproved if the median is under ~45 days.
     · falsifier-status: HANDOFF → owner: you; lab spec: pull first-contact and signed dates from CRM or invoices for the last five closed deals.

4. **The plan skips the cheap test of demand.** You are committing $65k+ before checking whether anyone responds. Founder-led outreach to a subset costs almost nothing and tells you the reply rate directly. Basis: Inference.
   → Fix: run a 3–4 week founder-led test on 50 accounts (segmented by recency). Hire only if replies and meetings clear a threshold you set now, for example ≥10 meetings in the test window.
   → falsifier: if the test produces fewer than ~3 meetings from 50 accounts, the hire is premature.
     · falsifier-status: HANDOFF → owner: you; lab spec: 50 accounts, one scripted outreach sequence, log replies, meetings, and wins weekly.

5. **Commission on the existing list pays for revenue that may return anyway, and rewards easy accounts.** If a rep is paid on reactivations, she gets paid for customers who would have come back without her, and she has no incentive to work the hard half. Basis: Inference (incentive mechanism).
   → Fix: pay on new scope or new logos, or on reactivations above a baseline you measure first.
   → falsifier: a holdout split of the list (half worked, half not) shows the reactivation lift. If there is no lift over the holdout, the commission is paying for baseline.
     · falsifier-status: HANDOFF → owner: you; lab spec: random 150/150 split, tracked for 90 days.

6. **A first-year rep working lapsed accounts can make them permanently lost, and first-year sales hires often leave.** Repeated pushy calls can turn a dormant account into a churned one, and her departure leaves you with the damage and no list owner. Basis: Judgment (capped at major by rule; I rank it minor on likelihood).
   → Fix: contact cadence limit, one approved pitch, and a rule that accounts are reassigned to you on departure.
   → falsifier: complaint or unsubscribe rate in the first 30 days of outreach. Disproved if it stays near zero.
     · falsifier-status: HANDOFF → owner: you; lab spec: track unsubscribes, do-not-contact requests, and churn tags for the first 30 days.

**Unknowns (not findings):** average fee, delivery margin, commission rate, recruiter cost, whether she also prospects new logos, who approves pricing and scope today, and whether you have benefits in the offer.

**Survives the attack:** The list is a real asset and cheaper than cold outbound. A dedicated seller can free your time if you are the bottleneck. Setting a 4-month checkpoint is good discipline; it only needs a defined metric and a real baseline.

**Verdict: RETHINK.** The 4-month payback fails in the expected case, and the list's conversion rate is unmeasured. Measure the 300 and run the founder-led 50-account test first, then hire against the numbers. If the CRM shows strong recent engagement, the verdict moves to PROCEED-WITH-FIXES.

**Round log:** round 1 · closed: 0 · new: 0 · open: 6 (no fixes applied yet; re-attack after you revise).

**JAIL-HANDOFF**
```
next: jail-decide
reason: hire-now vs test-first vs lower-fixed-cost structure is a choice among options; re-decide with these findings
inputs: findings 1–6 above; Unknowns list; your actual fee, margin, commission, CRM export of the 300
open_items: 2, 3, 4 need owner data before any hire decision
```