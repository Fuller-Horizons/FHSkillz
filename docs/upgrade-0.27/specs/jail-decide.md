# Spec — jail-decide (1.2.1 → 1.3.0) · now 7.6 → target 8.8

Changes
1. Fix the eval defect: in `evals/behavioral-0.25/jail-decide.json` case `jail-decide-0250-2`, assertions 4 and 5 contradict (one rewards fail-closing on an unnameable owner, the other demands a named owner). Rewrite them so both are satisfiable: owner unnameable → package withheld with the FAIL line naming the missing owner. Extra path allowed: that file only.
2. `references/expected-value.md`: the quantified-lane worksheet — EV as a range (p_low/p_high × benefit − cost), cost of delay per month, payback / break-even, with one fully worked numeric example whose arithmetic is checkable; every input carries Fact/Estimate + source.
3. Worked package `references/example-package.md` (ship-check line first, ≤450-word package, JAIL-HANDOFF).
4. Optional decision-log line for jail-memory (ADR shape: context · decision · consequences · status) when the decision is durable.
5. Client-facing Delivery section (AUTHOR-RULES rule 8).
6. Canonical labels; description ≤ 450 (currently 854).
Client-facing: yes.

Test scenarios
S1 normal: owner of a 12-person HVAC company choosing between hiring a second dispatcher ($52k/yr loaded), buying dispatch software ($400/mo + $3k setup), or doing nothing; current overtime $1,800/mo; decision needed by Dec 15.
  [O] includes a do-nothing option with its cost stated
  [O] states criteria before scoring options
  [O] gives one recommendation with confidence and at least 2 conditions that would change it
  [O] every number used traces to the prompt or is labeled Estimate
S2 thin evidence: "Should we expand to Nassau County?" with no data.
  [O] does not issue a confident recommendation; routes to research or labels criteria judged on Assumption/Unknown
  [O] names the specific evidence needed
S3 draft with violations: user pastes a draft decision memo missing do-nothing and with no owner and asks to "finalize it".
  [O] the first ship-check line shows the real FAILs for the draft as received
  [O] the final package either adds the missing parts or withholds with a named gap — never a silent all-PASS
