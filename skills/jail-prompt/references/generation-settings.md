# Run settings: model, effort, tools

Load this when writing the RUN SETTINGS line. The prompt shapes behavior
through words; run settings shape it through configuration. **A control set as
a setting beats the same control asked for in words**, so push controls down
here wherever the host allows.

## What exists on current Claude models (checked 2026-11-12)

| Control | Where | Notes |
|---|---|---|
| **Model** | Claude Code `--model` / `/model`, skill frontmatter `model:`, API `model` | Aliases `haiku`, `sonnet`, `opus`, `fable` resolve per host; pin a full ID (e.g. `claude-opus-5-5`, `claude-fable-5-2`) when the version matters. |
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
| The hardest open-ended technical work, or a lead agent coordinating cheaper subagents on a high-stakes job, after Opus has fallen short on the test set | Fable 5.2 (`claude-fable-5-2`) | medium |

Move up one step only when a test input fails because of reasoning depth, not
because of missing context or a vague prompt. Those are fixed in the prompt,
not with a bigger model.

## Fable: when, and which version

**When Fable at all.** Anthropic positions Opus 5.5 as the everyday default and
Fable for the most ambitious, open-ended technical work, including leading
smaller models as orchestrator or advisor. Fable costs more (5.2: $8 / $40
per million input / output tokens). Use it only when Opus 5.5 fails the test
set for reasoning depth, or the step is a high-stakes final merge or check.
Never for extraction or formatting steps.

**Fable 5.2 vs 5.1. Default: Fable 5.2, pinned by full ID.**
- Pick **`claude-fable-5-2`** for new work: Anthropic reports better coding,
  reasoning and vision, up to 30% faster output, fewer tokens at medium
  effort, and about 55% fewer safety blocks than 5.1.
- Pick **`claude-fable-5-1`** only when (a) the host or gateway doesn't serve
  5.2 yet (the request is rejected), or (b) a saved, tested prompt was
  validated on 5.1 and you need the same behavior. Then re-run its test set
  on 5.2 and move up if it passes.
- **Never write the bare `fable` alias when the version matters.** It
  resolves per host: Claude Code's docs map it to Fable 5.1 (as of
  2026-11-12), gateway sessions to Fable 5, and `ANTHROPIC_DEFAULT_FABLE_MODEL`
  overrides both. `chain-lint.py` warns on the bare alias.
- **Safety routing.** Fable blocks high-risk cyber work (penetration testing,
  exploit writing) and most research-biology tasks, and hands blocked requests
  to an older Opus model. For security-testing steps, assign Opus 5.5
  directly so you know which model did the work.

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
https://platform.claude.com/docs/en/models/sonnet-5/migration-guide ·
https://www.anthropic.com/claude-fable-and-mythos-5-2
