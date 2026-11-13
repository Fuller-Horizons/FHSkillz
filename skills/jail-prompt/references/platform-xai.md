# Platform pack — xAI: Grok & Grok Build

**Verified: 2026-09-14** against the docs listed under *Sources* below. Re-verify before
relying on any lever here. Every line traces to a fetched doc page — if you can't cite
one, it doesn't belong here (see the Evidence contract in SKILL.md).

**Naming, settled.** **"Grok Build" is the correct official name** — xAI's agentic
coding CLI, announced 2026-05-25, docs at `docs.x.ai/build/`. Confusingly, there is
*also* a **model** called `grok-build-0.1` (successor to `grok-code-fast-1`, which is
now merely an alias). When a user says "Grok Build," disambiguate: the CLI, or the
model. Docs pages now brand as "SpaceXAI Docs".

**Read the docs verbatim.** Append `.md` to any doc URL for raw source. Page inventory
at `docs.x.ai/llms.txt`; there is also a **Docs MCP server** at `docs.x.ai/api/mcp` —
the best route when you need exact current wording.

---

## The single biggest thing to know

**xAI publishes no current, general prompt-engineering guide for Grok.** `llms.txt`
contains no prompt-engineering page for text or coding (the only `prompting-guide.md`
in the whole inventory is for speech-to-speech voice). The one text/coding guide that
exists — *Prompt Engineering for Grok Code Fast 1* — sits on the old `/docs/guides/`
URL scheme, is **absent from `llms.txt`**, is not linked from current navigation, and
names a model retired 2026-05-15 — yet carries **no deprecation banner**. It is
substantive and still the best xAI prose guidance available, but cite it as **legacy**,
not current canon. There is **no** published prompting guidance specific to `grok-4.6`
or `grok-build-0.1`.

Practical consequence for jail-prompt: when the target is Grok, lean on the *operational*
levers below (which are well documented) and treat prose-style guidance as weaker
evidence than on the other four platforms. Say so in the prompt's CONTEXT.

---

## Levers that change how you write the prompt

**Roles are plain `system` / `user` / `assistant`.** No `developer` role, no top-level
`instructions` parameter.

**Use the Responses API.** Chat Completions is explicitly "Legacy endpoint, limited
updates." Renames: `messages` → `input`, `max_tokens` → `max_output_tokens`.
The Responses API is **stateful by default** (`store: true`, 30-day history) — continue
with `previous_response_id` rather than resending history. Prompt design can lean on
server-side continuity.

**`reasoning_effort` exists: `low | medium | high | xhigh`, default `high`.**
Support: low/medium/high on grok-4.6 and grok-4.5; **`xhigh` is grok-4.6-only and is
"treated as `high`" on grok-4.5.** Documented intent — `low`: "Latency-sensitive
agentic use and simple tool calling"; `medium`: "Complex data analysis and long-context
reasoning"; `high`: "Very challenging problems, complex math, multi-step logic";
`xhigh`: "The hardest problems, where answer quality matters more than response time."
Note the direction: **xAI tells you to drop to `low` for tool-calling loops**, not to
raise it. **"Reasoning cannot be disabled"** on reasoning models.

**Hard parameter incompatibility:** "presencePenalty, frequencyPenalty, and stop cannot
be used with reasoning models. Requests that include them return an error."

**Prompt caching is the most distinctive Grok-specific prompt-construction constraint.**
Cache entries are **per-server**, so routing stickiness is a first-class prompt concern
here in a way it isn't elsewhere. grok-4.6's own page: **"We highly recommend setting a
`prompt_cache_key`"** — without it you risk "full input price on a cache-cold server."
Mechanism: `prompt_cache_key` field (Responses API) or `x-grok-conv-id` header (Chat
Completions), set to "A UUID or your application's session ID."
- Ordering: **"Place system prompts, few-shot examples, and reference documents at the
  [beginning]"** to form a stable cached prefix.
- Immutability: **"Only append new ones. Any edit, removal, or reorder breaks the cache."**
- Reassurance: "Caching only accelerates the prompt processing phase. The model's
  output is identical whether the prompt is served from cache or computed from scratch."
- Verify with `response.usage.prompt_tokens_details.cached_tokens`; zero means
  misconfiguration.

**Search is server-side, not prompt-driven.** Web Search is passed as
`{"type": "web_search"}` in `tools`, and the model **automatically invokes it when
appropriate — you don't need to prompt it specifically.** That is a direct contrast
with platforms where you coax search in prose. Options: `allowed_domains` /
`excluded_domains` (**max 5 each, mutually exclusive**), `enable_image_understanding`,
`enable_image_search`.

**X Search is the genuine differentiator.** A separate `x_search` tool with
`allowed_x_handles` / `excluded_x_handles` (**max 20, mutually exclusive**),
`from_date`/`to_date` (ISO8601), `enable_image_understanding`,
`enable_video_understanding`. No other platform in this pack has first-party X/Twitter
retrieval. Billing changes **2026-09-21** to "$5 per 1k posts fetched and $10 per 1k
user profiles fetched" — a real cost line to name in the prompt's CONSTRAINTS.

Full server-side tool set: Web Search, X Search, Code Interpreter, Image Generation,
Collections Search, plus Remote MCP. Code execution runs Python in a sandbox with
**no external network access** and **no persistence between requests**; its page carries
a rare explicit sampling tip — **use temperature 0.0–0.3 for mathematical tasks.**

**Function calling:** `name` (**max 350 tools per request** — unusually high),
`description` ("What the tool does — helps the model decide when to use it"),
`parameters` (JSON Schema). **The schema root must be an object** — "A tool whose
`parameters` root is neither an object nor a union of objects… is rejected with a `400`
error." `tool_choice`: `auto` (default) | `required` | `none` | named.
**Parallel function calling is on by default**; disable with
`parallel_tool_calls: false`. `strict` is **implicitly always true** — you do not need
to ask for well-formed arguments in the prompt.

**Structured outputs are guaranteed — up to numeric ceilings.** "When using supported
schema features, the response is *guaranteed* to match your schema." Enforcement
ceilings, past which you are back to best-effort: `minLength`/`maxLength` to **2,048
characters**; `minItems`/`maxItems` to **256 items**; `minProperties`/`maxProperties` to
**64 properties**. Rejected with 400: zero-variant `enum`/`anyOf`, properties with
schema `true`/`false`, `maxContains`/`minContains`, `items` as an array.
The docs' own examples put the task in the system prompt and **do not restate the
schema** in prose.

**`max_turns` caps the agentic loop**, but "max_turns does not directly limit the
number of individual tool calls." Recommended: **1–2** for quick lookups, **3–5** for
balanced research, **10+ or unset** for deep research (unset = "the server applies a
global default cap"). Client-side tools act as checkpoints that **reset the turn
counter**.

**Context compaction is an alternative to prompt trimming.**
`POST /v1/responses/compact` preserves "system prompts, attached files, prior reasoning,
and a compacted record of the turns" and drops "verbose tool output and back-and-forth."
Warnings: **"Treat `encrypted_content` as opaque — do not parse or modify it"**; "The
conversation you compact must already fit in context"; **"At most one compaction per
call."** Consider a smaller model for frequent compaction. grok-4.6's page: "Long agent
loops additionally benefit from context compaction."

**Multi-agent is unique to xAI — and `reasoning_effort` means something different.**
`grok-4.20-multi-agent` orchestrates **4 agents** (`agent_count=4`, or effort
`low`/`medium`) or **16 agents** (`agent_count=16`, or effort `high`/`xhigh`). Here
**`reasoning_effort` changes agent count, not thinking depth** — a genuine prompt-design
trap. Documented prompting patterns: **set explicit scope** ("Tell the agents exactly
what dimensions to cover"), **request structured output** (it "excels when you request
organized, structured responses"), **specify source types**, **break complex tasks into
conversations** (broad then narrow), **provide relevant context and constraints**.

**Context windows:** grok-4.6 **500k** (cutoff 2026-02-01); grok-4.5 **500k**;
grok-4.3 / grok-4.20-* **1M**; grok-build-0.1 **256k**. ⚠️ **grok-4.6 pricing doubles
above 200k prompt tokens** ($2/$6 → $4/$12 per 1M) — an economic reason not to stuff
context.

---

## Grok Build (the CLI) specifics

**It reads Claude's files.** Recognised instruction filenames: `AGENTS.md`, `Agents.md`,
`AGENT.md`, **`CLAUDE.md`, `Claude.md`, `CLAUDE.local.md`**, plus `*.md` inside
`.grok/rules/`, with **`.claude/rules/` and `.cursor/rules/` supported for
compatibility**. Explicitly: "Grok works seamlessly with Claude Code and `AGENTS.md`
instruction files without additional setup." Loaded hierarchically from global
`~/.grok/` then repo root down to cwd; **deeper files take precedence**.

**The one explicit length rule in all of xAI's agent docs:** **"short, specific
instructions are followed more reliably than long ones."** No size cap; files load in
full. **`grok inspect`** lists discovered rules files with paths and approximate token
counts — a real budget tool. Per-session overrides: `--rules` appends;
`--system-prompt-override` replaces the system prompt entirely (note: xAI does not
document what that prompt contains, so you'd be replacing something undocumented).

**Skills:** `SKILL.md` with YAML frontmatter, discovered in `./.grok/skills/`,
`~/.grok/skills/`, plugin dirs, or custom paths. Fields include `name`, `description`,
**`when-to-use`** (extra trigger phrases — a field Claude Code lacks), `paths`,
`allowed-tools`, `argument-hint`, `user-invocable`, `disable-model-invocation`.
Skills auto-become slash commands.

**Plan mode is a first-class prompt-structuring feature.** `/plan`, `/plan <description>`,
or `Shift+Tab`. **"The agent may autonomously enter plan mode when tasks appear
ambiguous."** Review keys: `a` approve, `s` request modifications, `c` comment on
specific lines, `q` exit. Documented targeting: ideal for "Ambiguous architecture,
unclear requirements, or high-impact restructures"; **skip** for "Clear single-path
changes, obvious bug fixes, renames, formatting, or exploratory work."

**Subagents** are "independent child sessions with their own context" returning a
summary to the parent; on by default. Built-ins: general-purpose, explore (read-only),
plan. **Personas** are "behavioral overlays only (tone, focus, contracts)."

**Context commands:** `/context`, `/compact`, `/effort` (change reasoning effort
mid-session), `/model`, `/rewind`, `/fork`, `/resume`, `/deep-research`,
`/create-workflow` + `/workflow`, `/loop` + `/tasks`, `/remember` + `/memory`.

**Headless:** the flag is **`-p, --single <PROMPT>`** ("Send one prompt") — **not
`--print`**. Output formats `plain | json | streaming-json`. Session flags
`-s/--session-id`, `-r/--resume`, `-c/--continue`.

**Permissions:** Ask (default) / Auto (classifier) / Always-approve. **"Deny rules
always take precedence over allow rules"**; evaluation order deny > ask > allow.
Even with remembered grants, **`rm` and `git push` still prompt** unless explicitly
allowed. Sandbox profiles: `workspace`, `read-only`, `strict`.

**Hooks:** `PreToolUse` is **the only blocking event** — exit 0 allows, exit 2 denies;
everything else (timeout, error, malformed) **fails open** and logs.

**Config precedence:** Environment > User (`~/.grok/config.toml`) > Project
(`.grok/config.toml`) > Managed > Requirements. Critical constraint: **"Project
`.grok/config.toml` only contributes `[mcp_servers]`, `[plugins]`, and `[permission]`.
Other sections belong in user config."**

**IDE path is ACP**, not an xAI extension: `grok agent stdio` runs Grok as an ACP agent
over JSON-RPC. MCP config is read from **Claude, Cursor, and project-level** files.
grok-build-0.1 "performs best in agentic harness like Grok Build, Cursor, Hermes Agent,
OpenClaw, Kilo Code, or OpenCode." There is **no official xAI VS Code or JetBrains
plugin** in the docs.

---

## Documented anti-patterns

From the legacy *Prompt Engineering for Grok Code Fast 1* guide — still the only prose
guidance xAI publishes, and its four agent-builder items are the highest-value content:

1. **Don't use XML for tool calls.** "Use native tool calling… We encourage you to use
   it instead of XML-based tool-call outputs, which may hurt performance."
2. **Don't skimp on the system prompt.** "A well-written system prompt which describes
   the task, expectations, and edge-cases the model should be aware of can make a
   night-and-day difference." *(Note this cuts against the "less scaffolding" direction
   at Anthropic/OpenAI/Google — do not carry that advice over to Grok unexamined.)*
3. **Do use XML tags or Markdown to delimit injected context sections.** Endorsed for
   *context framing* — easy to conflate with #1, which is about tool-call *encoding*.
4. **Don't rewrite history.** "We recommend against changing or augmenting the prompt
   history, as that could lead to cache misses and therefore significantly slower
   inference speeds."

Plus, with xAI's own worked pairs:
- ❌ *"Make error handling better."* → ✅ *"My error codes are defined in @errors.ts,
  can you use that as reference to add proper error handling and error codes to @sql.ts
  where I am making queries."*
- ❌ *"Create a food tracker."* → ✅ *"Create a food tracker which shows the breakdown
  of calorie consumption per day divided by different nutrients when I enter a food
  item. Make it such that I can see an overview as well as get high level trends."*
- "Specify relevant file paths, project structures, and dependencies while avoiding
  irrelevant context" — and "Most coding tools will gather the necessary context for
  you on their own."
- **Iterate rather than one-shot:** "Even if the initial output isn't perfect, we
  strongly suggest taking advantage of the uniquely rapid and cost-effective iteration
  to refine your query."
- **Model routing:** fast coding model for **agentic** tasks; frontier Grok for
  **one-shot Q&A**.

Other explicit warnings: long AGENTS.md files; editing prompt history (cache);
omitting a cache key; penalty/stop params on reasoning models; parsing compaction
blobs; non-object tool schema roots; mutually exclusive filters used together;
Chat Completions as legacy; "advanced tool usage patterns are not yet supported in the
Vercel AI SDK."

---

## Gaps — state these rather than guessing

- **No prompt-engineering guidance for grok-4.6 or grok-build-0.1.** grok-4.6's page
  offers two recommendations, both operational (`prompt_cache_key`, compaction).
  grok-build-0.1's model page has none at all.
- **No guidance on how to write prompts for reasoning models** — notably, no statement
  either way about chain-of-thought instructions. Do not assume the OpenAI/Google
  "don't add CoT" rule transfers; it is undocumented here.
- **`reasoning_effort: "none"` is contradicted in xAI's own docs** — the retirement page
  prescribes "grok-4.3 with `none` reasoning effort," while the reasoning page tabulates
  only low/medium/high/xhigh and says "Reasoning cannot be disabled." `grok-4.3` has no
  model page in `llms.txt` at all.
- **No documented temperature / top_p guidance** for text or coding anywhere — the only
  sampling recommendation in the docs is the 0.0–0.3 math tip on the code-execution page.
- **No few-shot guidance, no prompt templates, no prompt-injection defense guidance,
  no tool-description authoring guidance** beyond the one-line `description` note.
- **No documented token budget for AGENTS.md** — `grok inspect` measures, the docs never
  say what a good number is.
- **No documented `max_turns` default value.**
- **No exhaustive model-support list for structured outputs** — only "supported Grok 4
  family models."

---

## Sources (fetched 2026-09-14)

- Models & pricing — `docs.x.ai/developers/models`; grok-4.6 — `…/developers/grok-4-6`; grok-4.5 — `…/models/grok-4.5`; grok-build-0.1 — `…/models/grok-build-0.1`
- Text generation (Responses API) — `docs.x.ai/developers/model-capabilities/text/generate-text`
- Reasoning — `…/text/reasoning`; Structured outputs — `…/text/structured-outputs`; Multi-agent — `…/text/multi-agent`; Responses vs Chat Completions — `…/text/comparison`
- Tools overview · function calling · web search · x search · code execution · tool usage details · advanced usage — `docs.x.ai/developers/tools/…`
- Prompt caching best practices — `docs.x.ai/developers/advanced-api-usage/prompt-caching/best-practices`; Maximizing cache hits — `…/maximizing-cache-hits`
- Context compaction — `docs.x.ai/developers/advanced-api-usage/context-compaction`
- **Prompt Engineering for Grok Code Fast 1 (LEGACY, orphaned, retired model)** — `docs.x.ai/docs/guides/grok-code-prompt-engineering`
- Grok Build — `docs.x.ai/build/{overview,modes-and-commands,settings,settings/reference,cli/headless-scripting}`
- Grok Build features — `docs.x.ai/build/features/{project-rules,skills-plugins-marketplaces,plan-mode,subagents,permissions,hooks,mcp-servers}`
- Release notes — `docs.x.ai/developers/release-notes`; Model retirement — `…/migration/may-15-retirement`
- Introducing Grok Build — `x.ai/news/grok-build-cli` (2026-05-25); Grok Build 0.1 — `x.ai/news/grok-build-0-1`; Grok 4.6 — `x.ai/news/grok-4-6` (2026-08-12); changelog — `x.ai/build/changelog`
- Page inventory — `docs.x.ai/llms.txt`; Docs MCP server — `docs.x.ai/api/mcp`
