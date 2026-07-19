# JAIL-RATE

Universal, evidence-based **0.0–10.0 rating** of anything — software, codebases, hardware, people (professional/public roles only), ideas, programs, services, content — on a weighted rubric matched to the subject type, with **cited empirical evidence behind every score** and a projected post-improvement rating (current → potential).

Part of the **[FHSkillz](../../README.md)** collection. Version 2.0.0.

## How it works

1. **Classify** the subject → pick the matching rubric from [`references/rubric-library.md`](references/rubric-library.md) (8 built-in types + a meta-procedure for anything else).
2. **Declare the rubric first** — dimensions, weights (sum 100%), why each weight fits the type. User-supplied weights win.
3. **Gather empirical evidence** — live research by default, per [`references/evidence-standards.md`](references/evidence-standards.md): tiered sources, every citation with URL + date accessed, claims labeled Fact / Inference / Judgment. Private subjects are rated from supplied materials and say so.
4. **Score** to shared calibration anchors (no grade inflation; critical flaws cap a dimension at ≤ 4.0).
5. **Recommend & project** — ranked impact×effort fixes and a labeled current → projected scorecard.

## Boundaries

People are rated on **professional performance in a public role, from public verifiable evidence only** — never personal lives, protected attributes, or rumor. AI skill directories route to [`rate-skill`](../rate-skill/); sell-side company prospecting routes to [`company-prospect-research`](../company-prospect-research/).

## Contents

```
skills/jail-rate/
├── SKILL.md
├── README.md · CHANGELOG.md
└── references/
    ├── rubric-library.md         # 8 per-type weighted rubrics + derive-your-own procedure
    └── evidence-standards.md     # source tiers, citation format, confidence rules
```
