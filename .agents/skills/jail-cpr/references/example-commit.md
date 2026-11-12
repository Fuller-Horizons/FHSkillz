# Worked example — COMMIT lane (12-week personal tour)

**Input:** "Write my 12-week commitment contract starting 2026-12-07. Four
domains: business, health, family, community. I want to 'get healthier' and
'be more present'."

**Task contract (inline):** start 2026-12-07 · length 12 weeks · Deadline
2027-02-28 (Sunday) · domains: business, health, family, community. No
meeting; no agenda.

---

# 12-Week Commitment Contract

**DEADLINE:** 2027-02-28 (started 2026-12-07 · 12 weeks)

**Context:** The winter tour of my personal operating plan. **User-provided.**

**Purpose:** I am building the habit of keeping small promises to myself
before I make big ones to others. I want my work to fund a life I am present
in, not one that runs me. This matters now because the last quarter ended with
two missed family dinners a week and no regular exercise. **User-provided**
(my own words, intake).

**Results (each can be checked from this page alone):**
- R1 — Business — By 2027-02-28, 12 weekly reviews are logged (one per Sunday, 30 minutes, notes saved in one file). Check: count the entries; 12 or more passes.
- R2 — Business — By 2027-01-31, send 20 outreach messages to past clients; log date and name. Check: 20 rows in the log.
- R3 — Health ("healthier", defined) — Exercise 3 sessions per week of 30 minutes or more for 12 weeks; a miss week is any week under 3. Pass is 10 of 12 weeks at 3 or more.
- R4 — Health — Weigh in each Monday; the 2027-02-28 reading is at or below the first reading minus 6 pounds. Check: the log.
- R5 — Family ("more present", defined) — Phone in a drawer from 6:00 pm to 8:00 pm on weeknights; pass is 48 of 60 weeknights marked on a wall calendar.
- R6 — Family — One planned 2-hour outing with the family every other Saturday: 6 outings, each dated in the log.
- R7 — Community — Attend 2 board meetings per month (6 total) and complete the 1 action item I take from each, logged by date.

**Carry-forward:** None. **Unknown:** the prior period had no written audit, so
this tour starts without baseline scores; the first Monday weigh-in sets the baseline.

**Check-in cadence:** every Sunday, update the log and mark each Result
on-track or off-track. Final scoring on 2027-02-28 via DEBRIEF.

**Verify gate:** Deadline is an explicit calendar date: PASS. Every Result has
a date or cadence: PASS. No Result needs a third party to confirm it: PASS.
"Healthier" and "present" have operational definitions: PASS. No agenda items
or time-boxed sessions in this document: PASS.

```yaml
JAIL-HANDOFF:
  skill: jail-cpr
  status: complete
  facts: ["Deadline 2027-02-28 is 12 weeks after the 2026-12-07 start"]
  assumptions: ["The person can log weekly; the 6-pound target is the person's own choice, not medical advice"]
  unknowns: ["No prior-period audit exists, so no baseline for R3-R5"]
  outputs: ["12-Week Commitment Contract (DOCX)"]
  evidence: ["Intake request - four domains and two vague goals - User-provided"]
  risks: ["Seven Results across four domains may be too many to sustain"]
  confidence: medium
  next: jail-cpr DEBRIEF at 2027-02-28
  approval_required: []
```
