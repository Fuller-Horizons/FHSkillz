# jail-strategy-scan

One strategy-analysis skill, three lanes: **INTERNAL** (evidence-sorted SWOT
→ TOWS strategies), **MACRO** (decision-tied PESTLE with scored factors and
early-warning tripwires), **FULL SWEEP** (both off one shared evidence base,
plus the interaction pass where macro shifts flip internal entries).

Successor to `jail-swot` 1.1.0 + `jail-pestle` 1.1.0, merged at plugin
0.23.0. Rationale: the two skills shared 80% of their chain (contract →
research → red-team → decide → brief → verify), were both commodity formats
whose value came from the same evidence discipline, and were most useful
together — merged, one research sweep serves both lanes and the interaction
pass (previously impossible without running two skills) becomes native.
Legacy asks route here: "SWOT", "TOWS", "PESTLE", "PESTEL",
"macro-environment analysis", "strengths and weaknesses".

What it refuses: aspirations filed as strengths, market weather filed as
opportunity, factors with no link to a named decision, quadrants without a
strategy step, high-magnitude factors without a tripwire.

Chains: jail-task-contract (scope) → jail-research (one sweep) →
jail-red-team (attack the sort) → jail-decide (choices) → jail-exec-brief →
jail-verify. Tripwires hand to jail-memory as monitored entries.

Fallback if chained skills are absent: each step's rule is stated inline in
SKILL.md — the skill runs self-sufficient.
