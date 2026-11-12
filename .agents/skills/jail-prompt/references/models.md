# Claude models: the one reference

Last verified: 2026-11-12
Re-verify after any model release, and at least every 60 days (repo validation
warns when this date is older). Every other file points here instead of
repeating these facts.

## Models

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

## Effort

`low` · `medium` · `high` · `xhigh` · `max` (available levels vary by model).
Defaults: `medium` on Opus 5.5, Sonnet 5.5, Haiku 5.5, and in Claude apps for
Fable 5.2; `high` on most other models. Set with Claude Code `--effort` /
`/effort`, skill or subagent frontmatter `effort:`, or API
`output_config.effort`. Effort covers thinking and answer tokens.

## Sampling and other settings

- `temperature`, `top_p`, `top_k`: rejected by Sonnet 5.5; Anthropic's
  migration guidance says to remove them. Don't set them for current Claude.
- No `seed`, presence/frequency penalty, or logprobs in the Messages API.
- Available: model, effort, thinking (`adaptive` recommended), structured
  output via tool/JSON schema where the host enforces it, `stop_sequences`,
  tools.

## Safety routing (Fable)

Fable 5.2 blocks high-risk cyber work (penetration testing, exploit writing)
and most research-biology tasks, and answers blocked requests with an older
Opus model. Assign security-testing steps to Opus 5.5 directly so you know
which model did the work.

## Tool-neutral tiers (non-Claude hosts)

Prompts meant to run anywhere name a **tier**; map it on the host:

| Tier | Claude | Other hosts |
|---|---|---|
| fast | Haiku 5.5 | the host's small/fast model |
| standard | Sonnet 5.5 | the host's mid model |
| strong | Opus 5.5 | the host's flagship |
| frontier | Fable 5.2 | the host's top reasoning model, if any |

## Sources (accessed 2026-11-12)
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/skills
- https://platform.claude.com/docs/en/build-with-claude/effort
- https://platform.claude.com/docs/en/models/sonnet-5/migration-guide
- https://www.anthropic.com/claude-fable-and-mythos-5-2
