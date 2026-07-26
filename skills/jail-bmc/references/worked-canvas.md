# Worked example — filled canvas (seed-investment decision)

Load this when checking the SUCCESS-TEST against a real run. One or two
element rows are shown per block; a real canvas often carries more, but
the fixed schema and the checklist walk-through below are the point.

**Subject:** Ledgerly (automated bookkeeping SaaS for solo/small-firm
lawyers, 14 months post-launch). **Decision:** seed-investment go/no-go.
**Stage:** operating.

## Canvas

| Block | Element | Label(V/H) | Evidence ref | Confidence |
| :--- | :--- | :---: | :---: | :---: |
| Customer segments | Solo & 2–5-attorney firms doing their own trust-account bookkeeping | V | [1] | H |
| Customer segments | Larger firms (20+ attorneys) with in-house bookkeepers | H | — | L |
| Value propositions | Automated IOLTA trust-account reconciliation, audit-ready | V | [2] | H |
| Channels | State-bar CLE partnerships (co-marketing) | V | [3] | M |
| Channels | Cold outbound to firms with 20+ attorneys | H | — | L |
| Customer relationships | Self-serve signup + quarterly check-in call | V | [4] | M |
| Revenue streams | $149/mo per firm, seat-based pricing above 5 users | V | [1] | H |
| Key resources | IOLTA-compliance rules engine (proprietary) | V | [5] | H |
| Key activities | Trust-account audit certification maintenance | V | [6] | M |
| Key partnerships | State bar associations (3 states live) | V | [3] | M |
| Key partnerships | Payment processor for trust-account transfers | H | — | L |
| Cost structure | Compliance/audit engineering (~$18K/mo) | V | [5] | H |
| Cost structure | CAC via CLE partnerships (~$620/firm) | V | [3] | M |

## Coherence pass
- Segment ↔ value proposition: the solo/small-firm segment maps directly
  to the IOLTA-reconciliation prop, in that segment's own language —
  holds.
- Revenue ↔ segments: the 20+-attorney segment (H, no evidence) is the
  one seat-based pricing assumes will expand revenue. **Finding:** the
  revenue-growth story leans on an unvalidated segment.
- Unit economics: $149/mo × 11-month avg retention ≈ $1,639 LTV vs $620
  CAC [3] → 2.6:1 at current scale (47 firms); the seat-based upsell that
  would improve this ratio is HYPOTHESIS and is not counted in it.
- Key activities/resources ↔ value proposition: the compliance engine
  [5] the prop depends on is evidenced — holds.

## Top risky assumptions + experiments (jail-lab spec shape)
1. **20+-attorney segment will buy** (impact H, evidence none) — metric:
   signed pilot agreements, higher is better · variable: outbound
   sequence targeting 20+-attorney firms · bound: 60 days, 40 firms, $0
   (existing SDR capacity) · threshold: 3 signed pilots → keep pursuing
   the segment, else demote to won't-pursue.
2. **Payment-processor terms hold at renewal** (impact H, evidence none)
   — metric: written terms confirmation, binary · variable: renegotiation
   ask at renewal · bound: one renewal cycle (30 days) · threshold: terms
   confirmed in writing → keep, else escalate to a backup processor.
3. **CLE-partnership CAC holds beyond 3 states** (impact M, evidence
   weak/comparable-based) — metric: CAC per firm, lower is better ·
   variable: 2 new-state CLE partnerships · bound: one quarter ·
   threshold: CAC ≤ $750/firm → keep, else find channel #2.

## Sources (dated)
[1] Ledgerly billing system export, accessed 2026-07-10.
[2] Product audit-trail feature spec + 3 customer QA logs, accessed 2026-07-10.
[3] State-bar CLE partnership agreements (CA, TX, NY), signed 2025-11 to 2026-03.
[4] Onboarding + check-in call logs, accessed 2026-07-11.
[5] Engineering payroll allocation, accessed 2026-07-11.
[6] SOC 2 Type I audit engagement letter, dated 2026-05-02.

## SUCCESS-TEST walk-through
- Labels intact: every row above carries V or H — present (13/13).
- Coherence pass done: the four checks ran; the revenue↔segment
  contradiction is logged as a finding, not smoothed over.
- Top 3–5 assumptions have experiments: three ranked assumptions each
  carry a full jail-lab spec (metric/variable/bound/threshold) — present.
- No VALIDATED lacks an evidence ref: every V row cites [1]–[6]; every
  row with no ref is labeled H, never V — present.
