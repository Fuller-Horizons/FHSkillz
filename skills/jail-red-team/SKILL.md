---
name: jail-red-team
metadata:
  version: 1.0.0
description: >-
  Adversarially pressure-test a plan, recommendation, analysis, design, or
  belief BEFORE it ships — hidden assumptions, bias patterns, missing
  stakeholders, dependency failures, second-order effects, and the conditions
  that would invalidate it. Use when someone says "poke holes in this",
  "what am I missing", "steelman the other side", "devil's advocate", before
  consequential or irreversible decisions, or when jail-decide/jail-verify
  routes a contested call here. Do NOT use to verify a finished deliverable's
  completeness (jail-verify) or to invent objections against a trivial,
  low-stakes choice.
---

# JAIL-RED-TEAM

Attack the strongest version of the work, find the failure that matters, and
say it plainly. Real objections only — inventing critique to appear rigorous
is its own form of dishonesty.

## Setup
- Restate the claim/plan under attack in its **strongest form** (steelman
  first — demolishing a weak paraphrase proves nothing).
- Independence: prefer a different model/agent/session than the producer;
  same-producer fallback must start from the evidence, not the narrative.
- Scale effort to stakes [Constitution Rule 11]: consequential + contested
  gets the full sweep; modest stakes gets the three lenses only.

## The three lenses (always)
1. **What is missing?** — stakeholders, costs, prerequisites, failure modes,
   the option nobody wrote down (including do-nothing).
2. **What is unrealistic?** — timelines, adoption assumptions, capability
   claims, resourcing, "and then everyone complies."
3. **How does this fail despite good intentions?** — the mechanism of
   failure when everyone executes competently and the world doesn't
   cooperate.

## The full sweep (consequential/contested calls)
- **Hidden assumptions** — unstated premises the conclusion needs; mark each
  with what would disprove it.
- **Unsupported causality** — "X will drive Y" with no mechanism or evidence.
- **Bias patterns** — selection (who's in the sample?), confirmation (what
  disconfirming evidence was never sought?), survivorship (where are the
  failures of this approach?), incentive conflicts (who benefits from this
  conclusion?).
- **Missing stakeholders** — who is affected but unconsulted, and what do
  they break when they push back?
- **Dependency failures** — for each external dependency: what happens when
  it's late, wrong, or gone?
- **Second-order effects** — the response to the plan: competitors, users,
  regulators, incentives it creates.
- **Adversarial interpretation** — how a hostile reader, competitor, or
  auditor reads this artifact.
- **Scenario spread** — best / expected / worst case with the driver of each;
  a plan that only works in the best case fails here.
- **Invalidation conditions** — the observable events that would prove this
  wrong. No conditions = unfalsifiable = flag it.

## Output
```
RED-TEAM FINDINGS (ranked by severity × likelihood)
1. <finding> — severity: critical|major|minor · basis: <evidence/reasoning>
   → fix, mitigation, or the question that must be answered
...
Survives the attack: <what held up, said once, without padding>
Verdict: PROCEED | PROCEED-WITH-FIXES | RETHINK — one sentence why
```
Then the JAIL-HANDOFF block — `next:` producer (fixes), jail-decide
(re-decide with findings), or jail-verify (post-fix check).

## Related skills
Finished-deliverable completeness → **jail-verify**. Re-choosing after
findings → **jail-decide**. Premise so flawed the task shouldn't proceed →
that's jail-prompt's STOP; say so.

## Gotchas
- **Strawman demolition.** Attacking a weaker paraphrase. Steelman first, in
  writing, or the whole exercise is theater.
- **Manufactured objections.** Padding findings to look thorough. Three real
  findings beat ten cosmetic ones; "it holds" is a valid result.
- **Severity flattening.** A critical flaw listed sixth behind five nitpicks.
  Rank by severity × likelihood, critical first, always.
- **Critique without a handle.** Every finding carries its fix, mitigation,
  or the specific question to resolve — otherwise it's just anxiety.
- **Unfalsifiable optimism.** If no observation could invalidate the plan,
  that's a finding — the plan is faith, not strategy.
