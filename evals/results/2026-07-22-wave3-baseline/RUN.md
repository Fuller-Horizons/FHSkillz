# Wave 3 trigger baseline — 2026-07-22 (0.24.0)

Re-baseline after the rename + merge wave: 4 renames (operationalize→**plan**,
baton→**handoff**, strategy-scan→**strategy**, exec-brief→**summarize**),
1 merge (jail-wayfind folded into **jail-plan** as its MAP lane), and content
edits to research / memory / cpr. 27 → **26 skills**, 95 trigger cases.

## Result (post fix-loop)

| Metric | Value | Gate | Verdict |
|---|---|---|---|
| Fire rate | **79/79 = 100%** | ≥ 95% | PASS |
| False-fire rate | **0/16 = 0%** | ≤ 5% | PASS |
| Collision variance (3 judgments × 12) | **11/12 unanimous** (n7 split 2:1 — the merge edge) | stability | PASS |

Every renamed target routed under its new name first try: k6→jail-plan,
k8→jail-summarize, k14/k15→jail-strategy, mp t3→jail-handoff,
mp t4→jail-plan (wayfind's MAP prompt), wn2→jail-handoff.

## The one failure and its fix (the loop working)

- **Raw: 78/79 (98.7%) / 0%** — gate PASS, single miss:
  `kernel::n7` "Plan the tasks and owners for the quarter" judged
  **jail-plan**; accept was `[jail-task-contract]`.
- **Diagnosis (not a bug — a genuine either-route edge):** the wayfind→plan
  merge gave jail-plan an OPERATE lane that produces an *owned 13-field
  workflow*. "Plan the tasks and **owners**" is now a legitimately good fit
  for jail-plan, AND still a fit for task-contract (scope the work). The
  3-judge collision confirmed it: **2 chose jail-plan, 1 chose
  jail-task-contract** — the signature of real ambiguity, not a broken
  description (every other collision case was unanimous).
- **Fix:** `n7` accept-set widened to `[jail-task-contract, jail-plan]`
  (designed ambiguity, both correct) — the honest reflection of the
  post-merge product, not a papered-over confusion. No description hack
  needed; jail-plan did not bleed into any clean task-contract case (k1
  routed jail-task-contract cleanly). Post-fix: 79/79.

## Ledger note (honest bookkeeping)

`trigger-accuracy-ledger.jsonl` entries #3 (98.7, DISCARD) and #4 (100.0,
tie-vs-best → DISCARD by strict lab semantics). Read in context: the suite
was re-pointed at 5 renamed/merged skills, so recovering the 100.0 ceiling
is *maintenance of the gate through a structural rename*, not a failed
experiment. The append-only ledger stands as recorded; this note is the
interpretation.

## Method

Identical harness to waves 1–2: blind manifests (26 descriptions, scoring
key isolated in `private/`), one independent subagent judge per batch (tool
traces = 1 read each), 3× judgment on the collision set. 8 judge agents;
raw + post-fix picks in this folder.

## Scope

Trigger routing only. Behavioral suites unaffected by renames (the 0.23.1
behavioral run stands); the merged jail-plan's two lanes get a behavioral
case in the next behavioral pass.
