# Record schema & worked examples

## Machine-readable record schema
Emit one JSON object per rated skill, then validate + save it (companion skill **jail-py-rate-tools**, or the manual checks in SKILL.md).

```json
{
  "skill": "string",
  "version_rated": "string",
  "categories": {
    "Utility & Value":                  { "score": 0.0, "recommendation": "string", "post_reco": 0.0 },
    "Clarity of Instructions":          { "score": 0.0, "recommendation": "string", "post_reco": 0.0 },
    "Execution Reliability":            { "score": 0.0, "recommendation": "string", "post_reco": 0.0 },
    "Safety & Guardrails":              { "score": 0.0, "recommendation": "string", "post_reco": 0.0 },
    "Maintainability":                  { "score": 0.0, "recommendation": "string", "post_reco": 0.0 },
    "Context & Token Efficiency":       { "score": 0.0, "recommendation": "string", "post_reco": 0.0 },
    "Idempotency & Determinism":        { "score": 0.0, "recommendation": "string", "post_reco": 0.0 },
    "Handoff & Collaboration":          { "score": 0.0, "recommendation": "string", "post_reco": 0.0 },
    "Machine-Verifiable Exit Criteria": { "score": 0.0, "recommendation": "string", "post_reco": 0.0 },
    "Client Portability":               { "score": 0.0, "recommendation": "string", "post_reco": 0.0 }
  },
  "overall": 0.0
}
```

## Worked example (single skill)
**Target:** a trivial `hello-world` skill — a 6-line `SKILL.md`, no references, no scripts, no version.

| Category | Rating | Rationale | Recommendation | Post Reco. |
| :--- | :---: | :--- | :--- | :---: |
| Utility & Value | 2.0 | Demo only; no real task. | Bind to a concrete repeated task. | 6.0 |
| Clarity of Instructions | 6.0 | Short and readable, but no examples. | Add one input/output example. | 8.0 |
| Safety & Guardrails | 3.0 | No untrusted-input handling. | Add an injection-handling note. | 7.0 |
| Maintainability | 3.0 | No `version`, no validator. | Add `metadata.version` + validation. | 8.0 |
| Machine-Verifiable Exit Criteria | 1.0 | No checks at all. | Add a test/assertion script. | 8.0 |
| *(…remaining 5 categories scored the same way…)* | | | | |
| **Overall Rating** | **3.0** | Weighted toward the "absent mechanism" bands. | Apply all recommendations. | **7.4** |

## Batch roll-up
After the per-skill matrices, emit a summary sorted by Overall descending:

| Skill | Overall | Top weakness |
| :--- | :---: | :--- |
| jail-prompt | 8.x | … |
| rate-skill | 8.x | … |
