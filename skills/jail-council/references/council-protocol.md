# Council protocol — briefs, review rubric, and output formats

Load at Step 2. These are the exact texts and schemas the orchestrator uses
so every council run is auditable and comparable.

## Member brief (Stage 1 — identical for every member)
```
You are one member of an independent review council. Answer the question
below completely and carefully. You are working alone; you will not see
other answers. Label every material claim: [Fact — source] · [Inference —
from what] · [Estimate] · [Unknown]. Where you can retrieve sources, cite
them with dates. Prefer an honest Unknown to a confident guess.

QUESTION: <the framed question>
ACCURACY RUBRIC (what would make an answer wrong): <from Step 0>
```

## Reviewer brief (Stage 3 — after anonymization)
```
You are reviewing N anonymized answers (A, B, C…) to the same question.
For EACH answer, in order:
1. ERROR HUNT: name at least one concrete error, unsupported claim, or
   material gap — or write "none found" and say what you checked.
2. Score 0–10 on each: factual accuracy · completeness · reasoning
   soundness · evidence quality.
3. One-line verdict.
Then rank all answers best-supported → weakest. Do not reward confidence,
style, or length; reward verifiable correctness. If two answers conflict
on a fact, say which is right and how you know — or flag it UNRESOLVED.
```

## Review record (per reviewer, machine-checkable shape)
```yaml
reviewer: <member-id>          # orchestrator maps ids; answers stay anonymous
reviews:
  - answer: A
    errors_found: ["...", ...]   # or ["none found — checked: ..."]
    scores: {accuracy: 0-10, completeness: 0-10, reasoning: 0-10, evidence: 0-10}
    verdict: "..."
ranking: [B, A, C]
unresolved_facts: ["..."]      # feeds Step 4 verification round
```

## Verification-round dispatch (Step 4)
One targeted brief per disputed fact:
```
Disputed fact: "<exact claim>"
Positions: <A says… / C says…>
Task: settle this with primary/independent sources (jail-research tiers).
Return: verdict · evidence (source · what it shows · URL · date) ·
confidence. If genuinely unsettleable, say so — that becomes dissent.
```

## Chairman brief (Step 5)
```
You are the council chairman. Inputs: all anonymized answers, all review
records, verification-round results. Produce the final answer using ONLY
this material. Rules: evidence beats votes; preserve real dissent; label
per-claim confidence; add nothing the council didn't produce or verify.
```

## Final output template
```
COUNCIL ANSWER — <question>
Tier: A|B|C (<members: model list or "N independent sessions">)
FINAL ANSWER
  <the synthesis — claims labeled, confidence per material claim>
DISSENT REGISTER
  - <minority position> — held by <k of N> · would be decided by: <evidence/observation>
  (or: "none — unanimous after review", only if the error-hunt records support it)
AUDIT APPENDIX
  Ranking table: reviewer × ranking
  Verification round: <disputed fact → verdict → evidence> (or "not needed")
  Errors caught in review: <count + the material ones>
  Cost disclosure: <n_member answers + n reviews + chairman (+ verification)>
JAIL-HANDOFF: …
```

## Sizing guidance (accuracy-first)
- 3 members: default. 5 members: irreversible/legal/safety/money-critical.
- Add the rebuttal round when reviews changed at least one ranking or an
  error-hunt landed a hit — that's when revision has information to use.
- Chairman gets the largest/strongest model available; members can be
  smaller — diversity of the panel matters more than any single member's
  size (a homogeneous panel of giants shares blind spots).
