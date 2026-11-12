# Models, run settings and model choice

One reference for which model, which settings, and how to choose. Per-model prompting advice is in [model-guides.md](model-guides.md).


## Claude models

Last verified: 2026-11-12
Re-verify after any model release, and at least every 60 days (repo validation
warns when this date is older). Every other file points here instead of
repeating these facts.

### Models

Per-model prompting advice (blocks to add, lines to remove):
[model-guides.md](model-guides.md).

| Model | Full ID | Alias | Tier | Notes |
|---|---|---|---|---|
| Claude Haiku 5.5 | `claude-haiku-5-5` | `haiku` | fast | Cheapest. Extraction, classification, fixed-schema work behind a machine check. |
| Claude Sonnet 5.5 | `claude-sonnet-5-5` | `sonnet` | standard | Drafting, analysis, grading. Rejects thinking budgets (use effort). |
| Claude Opus 5.5 | `claude-opus-5-5` | `opus` | strong | Everyday default for serious work, merges, checks, writing prompts. jail-prompt runs here at medium. |
| Claude Fable 5.2 | `claude-fable-5-2` | — | frontier | Released 2026-11-09. Hardest open-ended work; lead agent or final check on high-stakes jobs. $8 / $40 per million input / output tokens. |
| Claude Fable 5.1 | `claude-fable-5-1` | `fable` (Claude Code) | frontier | Previous Fable. Use only when 5.2 isn't served or a tested prompt was validated on 5.1. |

**Aliases resolve per host.** In Claude Code: `fable` → Fable 5.1, `best` → the
`fable` target, `opus` → Opus 5.5, `sonnet` → Sonnet 5.5, `haiku` → Haiku 5.5
on the Anthropic API (other providers can map aliases to older models). Gateway
sessions map `fable` to Fable 5. `ANTHROPIC_DEFAULT_FABLE_MODEL` overrides the
`fable` alias. **Pin the full ID whenever the version matters**, always for
Fable.

### Effort

`low` · `medium` · `high` · `xhigh` · `max` (available levels vary by model).
Defaults differ by place. **API:** `medium` on Opus 5.5 and Haiku 5.5;
`high` on Sonnet 5.5 and Fable 5.2. **Claude Code and Claude apps:** `medium`
on Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.2. Always set effort
explicitly rather than relying on a default. Set with Claude Code `--effort` /
`/effort`, skill or subagent frontmatter `effort:`, or API
`output_config.effort`. Effort covers thinking and answer tokens.

### Thinking (Claude 5 family)

- **Always on:** Opus 5.5, Fable 5.2 / 5.1 (adaptive only; `thinking:
  disabled` returns an error on Opus 5.5).
- **On by default:** Sonnet 5.5, Haiku 5.5 (Sonnet 5.5's lowest setting is
  `between_tools`).
- Control depth with effort. Prompts that ask the model to write out its
  reasoning may be refused as "reasoning extraction"; read summarized thinking
  blocks instead. Replies can start with thinking blocks: select blocks by
  type, never by position.
- **Leave room in `max_tokens`** for thinking plus the answer, more at high
  effort (Anthropic reports 128,000 working well for long agentic coding turns
  on Opus 5.5); a tight budget truncates (`stop_reason: max_tokens`).
- **Changing effort between requests breaks the prompt cache**; keep effort
  fixed within a run (per-message effort is in beta).
- **Prefill** (writing the start of Claude's reply) is not supported on
  current models; it returns an error.

### Sampling and other settings

- `temperature`, `top_p`, `top_k`: rejected by Sonnet 5.5; Anthropic's
  migration guidance says to remove them. Don't set them for current Claude.
- No `seed`, presence/frequency penalty, or logprobs in the Messages API.
- Sonnet 5's new tokenizer counts roughly 30% more tokens for the same text;
  size budgets and `max_tokens` accordingly.
- Available: model, effort, thinking (`adaptive` recommended), structured
  output via tool/JSON schema where the host enforces it, `stop_sequences`,
  tools.

### Safety routing (Fable)

Fable 5.2 blocks high-risk cyber work (penetration testing, exploit writing)
and most research-biology tasks, and answers blocked requests with an older
Opus model. Assign security-testing steps to Opus 5.5 directly so you know
which model did the work.

### Tool-neutral tiers (non-Claude hosts)

Prompts meant to run anywhere name a **tier**; map it on the host:

| Tier | Claude | Other hosts |
|---|---|---|
| fast | Haiku 5.5 | the host's small/fast model |
| standard | Sonnet 5.5 | the host's mid model |
| strong | Opus 5.5 | the host's flagship |
| frontier | Fable 5.2 | the host's top reasoning model, if any |

### Sources (accessed 2026-11-12)
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/skills
- https://platform.claude.com/docs/en/build-with-claude/effort
- https://platform.claude.com/docs/en/models/sonnet-5/migration-guide
- https://www.anthropic.com/claude-fable-and-mythos-5-2

## Run settings: model, effort, tools

Load this when writing the RUN SETTINGS line. The prompt shapes behavior
through words; run settings shape it through configuration. **A control set as
a setting beats the same control asked for in words**, so push controls down
here wherever the host allows.

### What exists

Models, IDs, aliases, effort levels and accepted settings are in the tables
above (dated; re-verified on each model release). In short:
set **model, effort, thinking, tools, and a schema**; never temperature/top_p
for current Claude.

### Picking model and effort

Use the cheapest setting that passes the prompt's SUCCESS TEST and QUALITY BAR
on the test inputs (testing.md). Starting points:

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

### Fable: when, and which version

Fable only when Opus 5.5 fails the test set for reasoning depth, or for the
highest-stakes lead or check step; never for extraction or formatting.
Default `claude-fable-5-2`; `claude-fable-5-1` only when 5.2 isn't served or a
tested prompt was validated on 5.1 (then re-test on 5.2). Never the bare
`fable` alias. Security-testing steps go to Opus 5.5. Facts behind this rule:
the model table and the Fable safety-routing note above.

### By epistemic mode

| Mode | Effort | Format control | Other |
|---|---|---|---|
| Factual | medium (high if multi-source) | strict schema | search tool on; Unknown allowed |
| Research | medium–high | schema + source ids | search/fetch on; cite every Fact |
| Brainstorm | low–medium | light | ask for range: "12 options, at least 4 unusual" |
| Critique | medium–high | structured findings | run on a different model from the author when possible |

Variety in Brainstorm comes from the prompt (ask for range and contrast), not
from a temperature setting.

### Reproducibility

There is no seed. For audits: pin the full model ID and effort, use a strict
output schema, keep the test inputs fixed, and run twice. Structural
differences mean the schema isn't pinning the output.

### Prompts that will run outside Claude

Name a **tier** (fast / standard / strong / frontier) instead of a Claude
model, and map it on the host with the tool-neutral tier table above. Give
the host's own reasoning or effort setting if it has one; follow that
vendor's docs for sampling settings.

`RUN SETTINGS: tier strong · effort medium (map per host) · tools: web search`

### The RUN SETTINGS line

Every engineered prompt ends its block with one line, e.g.:

`RUN SETTINGS: model sonnet · effort medium · tools: web search, file read · max_tokens: 16000 (API, leaves room for thinking)`

API runs: include `max_tokens` with room for thinking, keep effort fixed
for the whole run (changing it breaks the prompt cache), and never prefill.

Sources: see the list at the end of the first part.

## Model selection for subagent steps

Load this when assigning models in a delegation set (delegation.md) or the
RUN SETTINGS of a reusable prompt. Model facts (IDs, aliases, prices, effort
defaults) are in the dated tables at the top of this file.

### Mode: quality-first (default) or cost-first

`orchestration.mode` sets what "good enough" means for every step.

**quality-first (the default).** The bar is the best output the strongest
model would give.
- The lead agent's merge and the final check run on a strong model (Opus 5.5
  or Fable 5.2), never lower. The check runs on a different strong model from
  the one that produced what it checks (e.g. merge on Opus 5.5, check on Fable
  5.2).
- A cheaper model may keep a step **only with measured proof** that it scores
  the same as the strong model on that step's test items (`agent.selected_by`,
  below). Without proof, the step starts one tier up from the table and
  escalates from there.
- Cheap-first escalation (rule 5 below) still applies, so you pay strong-model
  prices only where the cheap model is proven equal or the item needs it.

**cost-first (only when the user asks for it, e.g. a quick internal draft).**
Cheapest model that passes the step's SUCCESS TEST, as in the table. Say in the
reply that the run was cost-first.

### Measured model selection

For any prompt set that will be reused, run at volume, or shipped to a client,
pick each step's model by test, not by table:

1. Take 3–5 test items for the step (typical, hard, edge; testing.md).
2. Run the step's brief on 2–3 candidate models: the strong model plus the
   one or two cheaper ones you hope to use. Same brief, same effort, same items.
3. Grade blind (labels shuffled, a fresh grader on a strong model) against the
   step's SUCCESS TEST and QUALITY BAR, pass/fail per check.
4. Choose the highest score. A tie goes to the cheaper model. In quality-first
   mode a cheaper model must **tie the strong model**, not just pass.
   With **jail-py-toolkit**: `select-models.py --prompt brief.md --items items.jsonl --checks checks.txt --candidates haiku,sonnet,opus --grader claude-fable-5-2` runs steps 2-4 and prints the record (`--dry-run` first to see the call count). Fallback: run and grade by hand as above.
5. Record it on the step and save it with the prompt in the library, so the
   trial isn't repeated until the model, the brief or the inputs change:

```json
{"selected_by": {
  "date": "2026-11-12",
  "items": 4,
  "candidates": ["haiku", "sonnet", "opus"],
  "scores": {"haiku": "16/16", "sonnet": "16/16", "opus": "16/16"},
  "grader": "fresh opus agent, blind"
}}
```

Re-run the selection when a new model generation ships (e.g. Fable 5.1 → 5.2)
or the step's brief changes. No way to run trials in this session → keep
quality-first defaults and list "model selection not measured" as an Unknown.

### Picking the model per step

| Work in the step | Model | Effort | Escalate to |
|---|---|---|---|
| Extract, classify, scan, reformat to a fixed schema | Haiku | low | Sonnet (failed or Unknown items only) |
| Draft, analyze, compare, grade against a rubric | Sonnet | medium | Opus |
| Lead agent: plan, merge, final synthesis for a client | Opus 5.5 | medium (high if high-stakes) | Fable 5.2 if Opus fails the test set |
| Independent check | A different strong model from the producer (Opus 5.5 or Fable 5.2) | medium | — |
| Security-testing steps | Opus 5.5 (Fable blocks and reroutes them) | medium | — |

A cheap step must have a machine-checkable SUCCESS TEST, so a miss is caught
and escalated rather than shipped. For a prompt set that will be reused, try
each cheap step on 2–3 test items first; if the cheap model fails more than one
in five, start that step one tier up.

Fable version rule (5.2 by default, 5.1 only when 5.2 isn't served or a tested
prompt was validated on 5.1): see "Fable: when, and which version" above.
