---
name: jail-diagnose
metadata:
  version: 1.0.0
description: >-
  Feedback-loop-first diagnosis of hard defects — bugs, performance
  regressions, failing workflows, broken pipelines, "it sometimes doesn't
  work": build a tight red-capable reproduction signal BEFORE any
  hypothesizing, then minimize → hypothesize → instrument → fix → prove with
  a mandatory regression case. Use when the user says "debug this",
  "diagnose", reports something broken/throwing/failing/slow/flaky, or when
  a fix attempt failed and the cause is unclear. Do NOT use to verify a
  finished deliverable (jail-verify) or to iterate a working thing toward a
  better metric (jail-lab).
---

# JAIL-DIAGNOSE

**The feedback loop IS the skill.** A tight pass/fail signal that goes red
on *this* defect makes everything else mechanical; without one, no amount of
staring at the system will save you. Refuse to hypothesize until the loop
exists. Discipline adapted from Matt Pocock's `diagnosing-bugs`
([mattpocock/skills](https://github.com/mattpocock/skills), MIT),
generalized beyond code and bound to JAIL evidence rules.

## Phase 1 — Build the loop (spend disproportionate effort here)
Construct a repeatable check that fails on the defect. Escalate through, in
rough order of preference:
1. **Failing test** at whatever seam reaches the defect (unit → e2e).
2. **Scripted invocation** — CLI/HTTP call with a fixture input, output
   diffed against known-good.
3. **Replay a captured artifact** — real payload/log/event replayed through
   the path in isolation.
4. **Throwaway harness** — minimal subset of the system (one component,
   mocked deps) exercising the defect path in one call.
5. **Property/fuzz loop** — for "sometimes wrong": run many random inputs,
   catch the failure shape.
6. **Bisection harness** — defect appeared between two known states?
   Automate "boot at state X, check" so the states can be walked.
7. **Differential loop** — same input through old-vs-new (or config A/B),
   diff outputs.
8. **Structured human loop** (last resort) — if only a human can trigger
   it, script their steps precisely so even the manual loop is repeatable.
Non-code defects (a workflow that drops leads, a doc pipeline that mangles
formatting) get the same treatment: a repeatable trigger + a checkable
wrong-output signal.

**Tighten it:** faster (skip unrelated setup) · sharper (assert the exact
symptom, not "didn't crash") · deterministic (pin time, seed randomness,
freeze external inputs). A 2-second deterministic loop is a superpower; a
flaky 30-second one barely counts.

**Flaky defects:** the goal is a *higher reproduction rate*, not instant
purity — loop the trigger ×100, add stress, narrow timing. 50% reproducible
is debuggable; 1% is not.

**Cannot build a loop?** STOP and say so: list what was tried, then ask for
(a) access to the reproducing environment, (b) a captured artifact (logs,
recording, dump), or (c) permission for temporary instrumentation.
**Never proceed to hypotheses without a loop** — that's guessing with
confidence, the exact failure this skill exists to kill.

**Phase-1 done-check:** one named command (or precise procedure) that is
tight and red-capable — it fails on the defect, reliably.

## Phase 2 — Minimize
Shrink the failing case while the loop stays red: smallest input, fewest
components, shortest path. Every removal that keeps it red is information;
the removal that turns it green is a spotlight.

## Phase 3 — Hypothesize & instrument
- State hypotheses explicitly, each with the observation that would confirm
  or kill it [Constitution Rule 1 — inference labeled, not asserted].
- Test the cheapest-decisive hypothesis first; instrument (logs, probes,
  traces) exactly where the hypothesis predicts the divergence.
- The loop adjudicates — not intuition. A hypothesis the loop can't test
  gets reworked until it can.

## Phase 4 — Fix & prove
- Apply the minimal fix for the *confirmed* cause — not the first thing
  that turns the loop green (symptom-patching is a named failure).
- Run the loop: red → green. Then run the surrounding checks (tests, the
  broader suite) — a fix that breaks neighbors isn't done.
- **Mandatory regression case:** the Phase-1 loop (or its distilled test)
  joins the permanent suite so this defect can never silently return.
  [This is the evidence contract's regression rule — no case, no fix.]

## Output
```
DIAGNOSIS
Defect: <one line> · Loop: <the command/procedure> (tight ✓ red-capable ✓)
Minimized to: <smallest failing case>
Cause: <confirmed mechanism> — evidence: <what the loop/instrumentation showed>
Fix: <what changed and why it's minimal>
Proof: loop red→green · neighbors green · regression case: <where it lives>
```
Then the JAIL-HANDOFF block; `next:` jail-verify for consequential fixes,
jail-memory when the root cause is a lesson worth keeping.

## Related skills
Finished-work check → **jail-verify**. Metric improvement on a working
thing → **jail-lab**. Root-cause lesson storage → **jail-memory**
(postmortem). Contested cause on a high-stakes system → **jail-council**.

## Gotchas
- **Hypothesizing loopless.** Confident guesses without a red signal —
  refuse; Phase 1 is not optional.
- **Green-by-symptom.** A patch that silences the signal without touching
  the mechanism. The cause must be *confirmed*, then fixed.
- **Loose loops.** "Run the app and click around" is not a loop. One
  command, red-capable, or keep building.
- **Flake surrender.** "Can't reproduce" usually means the reproduction
  rate is too low — raise it before declaring defeat.
- **Fix without regression case.** The defect will return and cost the
  diagnosis twice. The case ships with the fix, always.
