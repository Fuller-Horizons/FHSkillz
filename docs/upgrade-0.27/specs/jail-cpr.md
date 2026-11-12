# Spec — jail-cpr (1.5.0 → 1.6.0) · now 8.1 → target 8.8

Changes
1. Description from 1,386 → ≤ 450 chars: keep one compact trigger phrase per lane (DESIGN: build/prep an agenda, CPR for a meeting; COMMIT: personal/team commitment contract for a quarter/"tour"; DEBRIEF: action items/decisions from a transcript, score the period) + the two Do-NOT clauses. Run every trigger case routed to jail-cpr in the suites before and after.
2. Core 183 → ≤ 160 lines: move the full output templates (DESIGN, COMMIT) to `references/templates.md`, keep the field lists inline.
3. Worked examples `references/example-design.md` (a client strategy session: CPR + agenda that sums to duration + pre-work) and `references/example-commit.md` (a 12-week personal tour contract across 4 domains with self-contained testable Results).
4. DEBRIEF: each extracted decision/action carries quote-level provenance and a canonical label (User-provided for attendee statements; Inference for "landed on" reads, flagged).
5. Canonical labels; JAIL-HANDOFF per schema.
Client-facing: yes (documents).

Test scenarios
S1 design: "Build the agenda for a 60-minute meeting with a client (owner + ops manager) to decide which of 3 CRM options to adopt; I need a decision by the end."
  [O] Results section states the decision that must exist by the end, testably
  [O] every agenda item has an owner, time and expected output, and times sum to ≤ 60 min
  [O] includes pre-work so the decision inputs exist before the meeting
S2 debrief: fixture transcript (≈40 lines) with 2 clear decisions, 1 vague "I think we landed on…", 3 actions (one with no owner).
  [O] the vague item is flagged, not promoted to a decision
  [O] the ownerless action is listed as unowned/needs assignment, not given an invented owner
  [O] decisions carry quotes or line references
S3 commit: "Write my 12-week commitment contract: business, health, family. I want to 'get healthier' and 'be more present'."
  [O] vague qualifiers ("healthier", "more present") are turned into testable results with numbers/dates/cadence
  [O] states an explicit end-date deadline
  [O] contains no meeting agenda items
