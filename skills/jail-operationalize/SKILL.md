---
name: jail-operationalize
metadata:
  version: 1.0.0
description: >-
  Convert a recommendation, decision, or idea into an executable OPERATING
  WORKFLOW — trigger, inputs, actions, tool, owner, approval, output,
  evidence, metric, frequency, risk, and a testable completion standard.
  Use when analysis stops at "you should…" and someone has to actually run
  it: "make this operational", "turn this into a process", "how do we
  actually do this", "who does what", or downstream of jail-decide. Do NOT
  use for one-off task planning (jail-task-contract) or multi-agent run
  coordination (jail-orchestrate).
---

# JAIL-OPERATIONALIZE

A recommendation nobody can run is a wish. This skill's contract: every idea
leaves as a workflow a named owner could execute next Monday without asking
what was meant. [Constitution Rules 6, 7]

## The 13-field workflow spec (every field, every workflow; "n/a" must be earned)
1. **Trigger** — the observable event or schedule that starts the workflow.
   "Ongoing" is not a trigger.
2. **Inputs** — what must exist at start, and where it comes from.
3. **Actions** — numbered steps, each starting with a verb, each small
   enough that "did it happen?" has a yes/no answer.
4. **Tool** — the specific system/skill each step runs in (least complex
   capable tool [Rule 11]; deterministic code beats a model where either
   works).
5. **Owner** — a named person or role per step. "The team" owns nothing.
6. **Approval** — which steps pause for a human, per jail-approval-gate
   tiers; irreversible/external/durable steps default to per-action. [Rule 5]
7. **Output** — the artifact each cycle produces, by name and location.
8. **Evidence** — what proves a cycle actually ran (log, file, record) —
   claims of completion need artifacts.
9. **Metric** — the number that says the workflow is working, with its
   current baseline and direction of good.
10. **Frequency** — cadence or SLA.
11. **Risk** — top failure modes + what the runner does when a step fails
    (retry / stop / escalate to whom). [Rule 6]
12. **Next action** — the single first step that starts adoption, with owner
    and date.
13. **Completion standard** — the testable check that one cycle is done-done
    [Rule 7], and (if the workflow is finite) what retires it.

## Method
- Start from the decision/recommendation and its evidence (jail-decide
  package or equivalent). If the recommendation is still contested, route to
  jail-red-team first — operationalizing a bad idea just industrializes it.
- Draft the 13 fields. Walk the workflow as its owner on a bad day: missing
  input, tool down, approver on vacation. Patch what breaks (field 11).
- Right-size ceremony: a weekly two-step check needs two crisp steps, not a
  governance framework. The 13 fields compress; they don't inflate.

## Output
The filled 13-field spec (table or labeled list), then the JAIL-HANDOFF
block — `next:` jail-verify (readiness check: owners real? permissions
exist? metric measurable today?) or jail-lab (if the metric should drive an
improvement loop).

## Related skills
Choosing what to do → **jail-decide** (first). One-time task framing →
**jail-task-contract**. Delegating across agents → **jail-orchestrate**.
Metric-driven iteration on the running workflow → **jail-lab**.

## Gotchas
- **Recommendation cosplay.** Restating "you should do X" across 13 fields
  without adding executable detail. Field 3's yes/no test catches this.
- **Ownerless steps.** "The team" / "someone" = nobody. A name or a role
  with a person in it, per step.
- **Metric-free workflows.** No metric means no way to notice it's failing.
  If no number exists yet, field 12's first action is creating the baseline.
- **Evidence gap.** A workflow whose cycles leave no artifact will be
  reported as running long after it stopped.
- **Ceremony inflation.** Thirteen fields is the maximum structure, not the
  minimum prose. Small workflow, small spec.
