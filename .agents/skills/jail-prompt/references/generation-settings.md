# Run settings: model, effort, tools

Load this when writing the RUN SETTINGS line. The prompt shapes behavior
through words; run settings shape it through configuration. **A control set as
a setting beats the same control asked for in words**, so push controls down
here wherever the host allows.

## What exists

Models, IDs, aliases, effort levels and which settings Claude accepts are in
[models.md](models.md) (dated; re-verified on each model release). In short:
set **model, effort, thinking, tools, and a schema**; never temperature/top_p
for current Claude.

## Picking model and effort

Use the cheapest setting that passes the prompt's SUCCESS TEST and QUALITY BAR
on the test inputs (prompt-testing.md). Starting points:

| Work | Model | Effort |
|---|---|---|
| Extract, classify, reformat to a schema, simple rewrite | Haiku | low |
| Draft, summarize, analyze supplied data, everyday prompts | Sonnet | medium |
| Client-facing analysis, research synthesis, judgment calls, writing other prompts | Opus | medium |
| Contested, high-stakes, multi-step reasoning with many constraints | Opus | high |
| Long agentic build or debugging session | Opus | high or xhigh |
| The hardest open-ended technical work, or a lead agent coordinating cheaper subagents on a high-stakes job, after Opus has fallen short on the test set | Fable 5.2 (`claude-fable-5-2`) | medium |

Move up one step only when a test input fails because of reasoning depth, not
because of missing context or a vague prompt. Those are fixed in the prompt,
not with a bigger model.

## Fable: when, and which version

Fable only when Opus 5.5 fails the test set for reasoning depth, or for the
highest-stakes lead or check step; never for extraction or formatting.
Default `claude-fable-5-2`; `claude-fable-5-1` only when 5.2 isn't served or a
tested prompt was validated on 5.1 (then re-test on 5.2). Never the bare
`fable` alias. Security-testing steps go to Opus 5.5. Facts behind this rule:
[models.md](models.md).

## By epistemic mode

| Mode | Effort | Format control | Other |
|---|---|---|---|
| Factual | medium (high if multi-source) | strict schema | search tool on; Unknown allowed |
| Research | medium–high | schema + source ids | search/fetch on; cite every Fact |
| Brainstorm | low–medium | light | ask for range: "12 options, at least 4 unusual" |
| Critique | medium–high | structured findings | run on a different model from the author when possible |

Variety in Brainstorm comes from the prompt (ask for range and contrast), not
from a temperature setting.

## Reproducibility

There is no seed. For audits: pin the full model ID and effort, use a strict
output schema, keep the test inputs fixed, and run twice. Structural
differences mean the schema isn't pinning the output.

## Prompts that will run outside Claude

Name a **tier** (fast / standard / strong / frontier) instead of a Claude
model, and map it on the host with the table in [models.md](models.md). Give
the host's own reasoning or effort setting if it has one; follow that
vendor's docs for sampling settings.

`RUN SETTINGS: tier strong · effort medium (map per host) · tools: web search`

## The RUN SETTINGS line

Every engineered prompt ends its block with one line, e.g.:

`RUN SETTINGS: model sonnet · effort medium · tools: web search, file read · max_tokens: 16000 (API, leaves room for thinking)`

API runs: include `max_tokens` with room for thinking, keep effort fixed
for the whole run (changing it breaks the prompt cache), and never prefill.

Sources: see [models.md](models.md).
