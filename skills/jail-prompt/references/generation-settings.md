# Run settings: model, effort, tools

Load this when writing the RUN SETTINGS line. The prompt shapes behavior
through words; run settings shape it through configuration. **A control set as
a setting beats the same control asked for in words**, so push controls down
here wherever the host allows.

## What exists on current Claude models (checked 2026-11-12)

| Control | Where | Notes |
|---|---|---|
| **Model** | Claude Code `--model` / `/model`, skill frontmatter `model:`, API `model` | Aliases `haiku`, `sonnet`, `opus` track the latest; pin a full ID (e.g. `claude-opus-5-5`) when reproducibility matters. |
| **Effort** | Claude Code `--effort` / `/effort`, skill frontmatter `effort:`, API `output_config.effort` | `low` · `medium` · `high` · `xhigh` · `max` (levels vary by model). Default `medium` on Opus 5.5, Sonnet 5.5, Haiku 5.5; `high` on most others. Covers thinking and answer tokens. |
| **Thinking** | API `thinking` (`adaptive` recommended; `enabled` with `budget_tokens` on models that still accept budgets) | Sonnet 5.5 rejects thinking budgets; use effort. |
| **Structured output** | Tool / JSON schema where the host enforces it | The strongest format control: malformed output is rejected, not hoped against. |
| **Stop sequences** | API `stop_sequences` | End output at a known tag. |
| **Tools** | Host tool settings, skill `allowed-tools` | Least privilege: only what the PROCESS needs. |

**Not available or not accepted:** `temperature`, `top_p`, `top_k` return an
error on Sonnet 5.5, and Anthropic's migration guidance says to remove them;
`seed`, presence/frequency penalties and logprobs are not in the Messages API.
Don't put them in a Claude prompt's settings. On other vendors' models, follow
that vendor's docs.

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

Move up one step only when a test input fails because of reasoning depth, not
because of missing context or a vague prompt. Those are fixed in the prompt,
not with a bigger model.

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

## The RUN SETTINGS line

Every engineered prompt ends its block with one line, e.g.:

`RUN SETTINGS: model sonnet · effort medium · tools: web search, file read · thinking: adaptive (API)`

Sources (accessed 2026-11-12): https://code.claude.com/docs/en/skills ·
https://code.claude.com/docs/en/model-config · https://platform.claude.com/docs/en/build-with-claude/effort ·
https://platform.claude.com/docs/en/models/sonnet-5/migration-guide
