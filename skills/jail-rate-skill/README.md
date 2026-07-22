# jail-rate-skill

Standardized, repeatable **technical review and scoring of AI skill directories** — a 10-category rating matrix (0.0–10.0), IDE/CLI compatibility matrices, concrete upgrade recommendations, and a machine-readable JSON record tracked over time.

Part of the **[FHSkillz](../../README.md)** collection. **Version 2.0.0** — instruction-only: validation/persistence scripts now live in the companion [`jail-py-toolkit`](../jail-py-toolkit/) skill, with manual fallbacks documented.

## How it works

Reads the target skill's `SKILL.md` + directory (never rates from the name; treats target text as untrusted data — injection attempts cap Safety at 4.0), scores 10 categories against the anchored rubric in [`references/rubric.md`](references/rubric.md) at temperature 0.0, fills the compatibility matrices from [`config.json`](config.json), emits the JSON record from [`references/examples.md`](references/examples.md), and recommends one concrete upgrade per category < 10 with a projected post-reco rating. Large targets are summarized per [`references/summarizer-guide.md`](references/summarizer-guide.md).

**Static audit, not behavioral eval** — for run-it-and-measure evals, hand off to Anthropic's `skill-creator`. To rate anything that isn't an AI skill, use [`jail-rate`](../jail-rate/).

## Contents

```
skills/jail-rate-skill/
├── SKILL.md · README.md · CHANGELOG.md
├── config.json                   # IDE/CLI matrix columns + output prefs
└── references/
    ├── rubric.md                 # scoring anchors + 10 category definitions
    ├── examples.md               # JSON record schema, worked example, batch roll-up
    └── summarizer-guide.md       # 300-line rule for big targets
```
