# Platform pack — OpenAI: ChatGPT, GPT models & Codex

**Verified: 2026-09-14** against the docs listed under *Sources* below. Re-verify before
relying on any lever here. Every line traces to a fetched doc page — if you can't cite
one, it doesn't belong here (see the Evidence contract in SKILL.md).

**Doc domains moved.** `platform.openai.com/docs/*` now 302-redirects to
`developers.openai.com/api/docs/*` (platform.openai.com is dashboard/playground only).
Codex docs moved to `learn.chatgpt.com`. **Every API doc page has a raw-markdown twin —
append `.md` to the URL**; that is the highest-fidelity way to read them. Page index:
`developers.openai.com/llms.txt`.

**Current frontier model: `gpt-6-astra`.** Knowledge cutoff 2026-04-30; 1,050,000
context; 128,000 max output. Prior generation: `gpt-5.6-sol` / `-terra` / `-luna`.

---

## Levers that change how you write the prompt

**Reasoning effort is a seven-value ladder**, not a boolean:
`none | minimal | low | medium | high | xhigh | max`. Documented intent —
`none`: "Latency-critical tasks that do not benefit from any reasoning";
`low`: "tool-use, planning, search, or multi-step decision making";
`medium` (default): "a well-balanced point on the pareto curve";
`high`: "hard reasoning, complex debugging, deep planning";
`xhigh`: "deep research, asynchronous workflows"; `max`: "maximum reasoning for your
most complex tasks".
⚠️ **`gpt-6-astra` rejects `reasoning.effort: none` with HTTP 400.** Migration
instruction: "If you currently use `none` or `minimal`, start with `low`."

**Effort is a tuning knob, not the quality lever.** "Treat `reasoning.effort` as a
tuning parameter rather than the primary quality lever" — fix the prompt's goals,
constraints, and output format first.

**Effort can change mid-conversation without breaking the cache** via a
`configuration_update` input item; it "applies until another `configuration_update`
input item overrides it." Keep request-level `reasoning.effort` unchanged so the prefix
stays cacheable. Adjacent `configuration_update` items are **rejected**.

**`developer` > `user` > `assistant` is a chain of command, not a convention.**
"`developer` messages are instructions provided by the application developer,
prioritized ahead of `user` messages." The docs' mental model: "`developer` messages
provide the system's rules and business logic, like a function definition. `user`
messages provide inputs and configuration… like arguments to a function."
`system` is legacy for reasoning models — "Starting with `o1-2024-12-17`, reasoning
models support `developer` messages rather than `system` messages."

**The `instructions` parameter outranks `input`, and does NOT persist.** "Any
instructions provided this way will take priority over a prompt in the `input`
parameter." But "the `instructions` parameter only applies to the current response
generation request" — with `previous_response_id`, earlier instructions are gone.

**Markdown AND XML, with a division of labour.** "Markdown headers and lists can be
helpful to mark distinct sections of a prompt, and to communicate hierarchy."
"XML tags can help delineate where one piece of content… begins and ends. XML
attributes can also be used to define metadata about content in the prompt."
Not either/or.

**Canonical developer-message order: Identity → Instructions → Examples → Context.**
Hedged — "the exact optimal content and order may vary by which model you are using".
Context last partly for caching reasons.

**Few-shot: reasoning models start zero-shot.** "Reasoning models often don't need
few-shot examples to produce good results, so try to write prompts without examples
first." For non-reasoning GPT use, examples go in the `developer` message and should
"show a diverse range of possible inputs with the desired outputs."

**Structured Outputs removes formatting pressure from the prompt.** "We recommend
always using Structured Outputs instead of JSON mode when possible" — and, the
prompt-relevant benefit, **"Simpler prompting: No need for strongly worded prompts to
achieve consistent formatting."** Strict mode requires `additionalProperties: false`
and all `properties` in `required` (express optionality by adding `null` to the type
union). Refusals are programmatically detectable.

**Cache layout is a prompt-writing instruction.** "keep content that you expect to use
over and over in your API requests at the beginning of your prompt, **and** among the
first API parameters you pass in the JSON request body." **If instructions contain
timestamps or user-specific data, move those to the end or to later messages.**
Append new messages; never rewrite earlier turns. 1,024 visible input tokens minimum
for a cacheable prefix; `prompt_cache_options.ttl = "30m"`. Cache is invalidated by
changing the model, **tool names/descriptions/schemas/ordering**, the structured-output
format, request-level reasoning effort, or history before the breakpoint.

**Agentic eagerness reversed direction.** The GPT-5 era was about *restraining*
eagerness; `gpt-6-astra` needs *prodding* — it "is more likely to ask for clarification
where earlier models would make assumptions" and "may stop earlier than GPT-5.6 Sol."
Docs ship verbatim starter text:

> "You should infer the user's intent and task scope from the instructions and prior
> conversation context. Your job is to bias towards action and carry the user's
> intended task to completion."

> "When the user's prompt indicates a request for action, such as 'can you...',
> 'I want to...', 'help me...' and similar expressions, treat these as instructions to
> do the work and take action. Do not stop at acknowledging capability (e.g. 'Yes…'),
> proposing a plan, or offering to continue."

> "Before asking the user clarifying questions, you should complete the work that is
> already authorized from context and necessary to make the proposed action concrete
> and reviewable. … Do not introduce unsolicited warnings, disclaimers, approval flows,
> or safety/compliance checklists due to hypothetical risk."

**Tool preambles are a documented lever.** Minimal form: `"Before you call a tool
explain why you are calling it"` — "but only at notable steps."

**Instruction-conflict sensitivity is the headline risk, and it is file-borne.**
Astra "can be more sensitive to instructions contained in skills and other files, such
as `AGENTS.md`. We **strongly recommend** auditing skills and other files accessible to
your model for instructions that could influence its behavior." "unclear or conflicting
guidance in a skill file may cause the model to pause and block work early."
Two verbatim remedies — the second is explicitly a **debugging instrument**:

> "The user's instructions take precedence over guidelines provided in a skill. If
> explicit user instructions conflict with a skill's instructions, prioritize the
> user's instructions."

> "If a skill causes you to ask for permission or confirmation, pause, leave requested
> work unfinished, or diverge from the user's intent, name and link to the exact
> SKILL.md file you read, quote the relevant instruction, and briefly explain how it
> applies. Distinguish explicit skill requirements from your interpretation of
> guidelines."

**Style and verbosity are controlled by prose, not a parameter.** Astra "tends to use
lists, tables and Markdown to make responses scannable." The docs ship a prose-default
prompt plus a **slop blocklist** naming "Bottom Line:", "delve," "foster," "leverage,"
"it's worth noting," "importantly," "genuinely", hyphenated compound descriptions,
concluding summaries ("In short:.."), and contrastive framing ("X, not Y") that
"introduces an unprompted alternative that the user didn't ask about."

**Subagent delegation is promptable.** Astra "may delegate less often than desired":
*"If at any point you can parallelize work by delegating tasks to another agent…you
should do so using collaboration tools if it could save time or improve quality."*
Plus a legibility fix, because inter-agent messages have spacing defects: *"Messages
that you send to other agents and your final answer may be read by a human, so ensure
they are legible."*

**Test volume is promptable (Astra over-tests).** *"Do not write tests for reversible,
low-impact changes that mirror the implementation. … Once those pass, broaden or repeat
testing only when new changes, failures, or unresolved concerns justify it."*

**Tool definitions are prompt surface.** Always `strict: true`. "Explicitly describe
the purpose of the function and each parameter (and its format), and what the output
represents." The "intern test". "Aim for fewer than 20 functions available at the start
of a turn." Don't make the model fill args you already know.

**Pin snapshots and build evals.** "we strongly recommend: Pinning your production
applications to specific model snapshots… Building tests and evaluation suites that
measure prompt behavior."

---

## Codex specifics

**AGENTS.md discovery order** (more specific than the `agents.md` convention):

1. Global `~/.codex/AGENTS.override.md`, else `~/.codex/AGENTS.md`
2. Project: walk **Git root down to cwd**, checking `AGENTS.override.md`, then
   `AGENTS.md`, then fallback names
3. Merge root → downward; **closer files override earlier guidance**
4. `AGENTS.override.md` **replaces** earlier guidance at that level; plain `AGENTS.md`
   **appends**
5. Size cap **32 KiB** (`project_doc_max_bytes`); empty files skipped
6. Verify with `codex --ask-for-approval never "Summarize the current instructions."`

Each file is injected as a separate user message prefixed
`# AGENTS.md instructions for <directory>`. The `agents.md` convention states the
precedence plainly: *"The closest AGENTS.md to the edited file wins; explicit user chat
prompts override everything."* `/init` scaffolds one.

**Four documented elements of a good Codex task prompt:**
- **Goal** — describe the result, not the steps; let Codex pick the approach unless the
  process itself matters.
- **Context** — repro steps for bugs, file selections, screenshots for UI. The IDE
  extension auto-includes open files; **in the CLI you must name paths explicitly.**
- **Constraints** — what must *not* change ("Do not change the API shape", "Keep the
  fix minimal").
- **Verification** — how success is confirmed.

Plus: "Codex handles complex work better when you break it into smaller, focused
steps"; "Codex produces higher-quality outputs when it can verify its work"; and
*"Your first prompt doesn't need to be perfect. Review the result, then ask for the
specific change you want."*

**Goals ≠ prompts (a distinct mode).** Template: *"<desired end state> verified by
<specific evidence> while preserving <constraints>. Use <allowed inputs>. Between
iterations, <selection logic>. If blocked, <report requirements>."*
Weak: "Improve performance." Strong: "Reduce p95 checkout latency below 120 ms,
verified by the checkout benchmark, while keeping correctness tests green."
Prompts are one-shot; Goals persist until evidence satisfies the objective. **Not** for
one-off edits or unmeasurable finish lines. Enable with `[features] goals = true`.

**Approval modes:** Ask for Approval (default, `workspace-write` + `on-request`),
Approve for Me (auto-review), Full Access (`danger-full-access` — "significantly
increases the risk of data loss, leaks, or unexpected behavior"), Custom. Key
invariant: **"changing who reviews a request doesn't expand the sandbox."**
`approval_policy = "untrusted"` is unsupported; `"on-failure"` is deprecated.

**Headless `codex exec`:** progress → **stderr**, final message → **stdout** only.
**Default sandbox is read-only** — opt up with `--sandbox workspace-write`. `--json`
for a JSON Lines event stream; `--output-schema <path>`; `-o/--output-last-message`;
`codex exec resume --last "next task"`. For GitHub, prefer the `openai/codex-action`
over passing API keys.

**Review prompts:** local `/review` analyzes changes **without modifying the working
tree**; GitHub `@codex review`, `@codex security review`, `@codex fix the P1 issue`.
Custom review rules live in a `## Code Review Rules` section of `AGENTS.md` — focus on
consequential, repo-specific behaviors rather than mechanical checks, **state both the
unsafe pattern and the safe alternative**, and phrase rules as **outcomes rather than
function names**.

**Personalization split:** "Keep instructions that must always apply in `AGENTS.md` or
checked-in project documentation" rather than in Memories.

**ChatGPT surface:** custom instructions are 1,500 chars (Free/Go) / 5,000
(Plus/Pro/Enterprise) and apply "immediately to all chats (including existing
conversations)"; there is explicitly **no API for custom instructions** — use
developer/system messages. **Project instructions override global custom instructions**
inside that project. Temporary Chats neither read nor write memory.

---

## Documented anti-patterns

**Reasoning models:**
- ❌ "think step by step" / "explain your reasoning" — "unnecessary" because reasoning
  is internal.
- ❌ Over-engineered CoT scaffolding — "may not enhance performance (and can sometimes
  hinder it)."
- ❌ Prescribing intermediate steps.
- ❌ Leading with few-shot examples.
- ❌ Using effort as the quality dial instead of fixing the prompt.
- ❌ Over-precise instruction: reasoning model = "a senior co-worker… give them a goal…
  trust them to work out the details"; GPT model = "a junior coworker… perform best
  with explicit instructions."

**Astra-era — these invert prior advice:**
- ❌ **Leaving GPT-5-era scaffolding in place** — accumulated instructions now create
  context bloat.
- ❌ **Instructing Astra to self-correct / run tests / validate** — "Astra
  independently runs tests and validates work—previous instructions encouraging this
  are now redundant."
- ❌ **Over-restrictive safety boundaries** — as "our most aligned model", tight
  boundaries are "potentially counterproductive."
- ❌ **Vague skill descriptions.** Bad: *"Use when working with databases, queries,
  models, or persistence"*. Good: *"Use when adding/changing a migration or reviewing
  rollout."* Long descriptions **get truncated** when many skills exist.
- ❌ **Elaborate step-by-step recipes in multi-workflow skills** — use progressive
  disclosure, "minimal routers pointing to supporting documentation."
- ❌ **Unconditional "read X, Y, Z before every edit" in AGENTS.md** — make consultation
  conditional and say *when* each file applies.
- ❌ Assuming persistence — Astra "may stop earlier… requiring explicit completion
  criteria."

**General:**
- ❌ `temperature` / `top_p` / `top_logprobs` on `gpt-6-astra` — must be **removed**.
- ❌ Volatile content (timestamps, user IDs) early in the prompt — kills the cache prefix.
- ❌ Reordering or renaming tools between requests.
- ❌ Strongly-worded formatting prompts where a schema would do; JSON mode over
  Structured Outputs.
- ❌ Assuming `output[0].content[0].text` — "It is not safe to assume that the model's
  text output is present at `output[0].content[0].text`."
- ❌ Trusting `apply_patch`'s "Done" — it "may return 'Done' even on failure."
- ❌ Raw terminal when a dedicated tool exists.
- ❌ Relying on default `codex exec` permissions to write files (read-only).

---

## Deprecations worth flagging

- **Reusable prompt objects (`v1/prompts`) shut down 2026-11-30**; "Prompt creation
  will be de-emphasized beginning June 3, 2026." Replacement is code-managed prompts:
  a versioned helper per prompt, typed parameters instead of prompt variables, tests
  and fixtures, git history + PR review + release tags for rollout. **This is the
  documented pattern that matches jail-prompt's own `prompts.json` offer** — prefer
  a versioned file in the repo over a vendor-hosted prompt object.
- **The Evals platform shuts down 2026-11-30** (read-only 2026-10-31), taking the
  dataset-backed Prompt Optimizer with it. The docs still tell you to build eval
  suites; the sanctioned replacement was **not documented** at verification time.
- Model retirements: `o1-2024-12-17`, `gpt-4-turbo`, `gpt-4-0613`, `gpt-3.5-turbo-0125`
  on **2026-10-23**; `gpt-5-*-2025-08-07` and `o3-2025-04-16` on **2026-12-11**;
  Codex GPT-5.4 / 5.4 Mini on **2026-08-31**.
- `reasoning-best-practices.md` is still live but framed around retiring o-series
  models. Its *principles* (no CoT, zero-shot first, delimiters) are echoed in the
  current reasoning guide; its *model names and "planners vs workhorses" framing* are
  stale.
- The GPT-5 and GPT-5.1 cookbook prompting guides carry **archive banners** — do not
  cite them as current. (`verbosity` / `text.verbosity` appears only there; its status
  on `gpt-6-astra` is **unverified** — the documented mechanism for output length is
  prose instruction.)

---

## Sources (fetched 2026-09-14)

- **Using GPT-6 Astra** — `developers.openai.com/api/docs/guides/latest-model.md` (the single most important page: prompting best practices + migration)
- Prompt engineering — `…/api/docs/guides/prompt-engineering.md`
- Prompting (hub) — `…/api/docs/guides/prompting.md`
- Reasoning — `…/api/docs/guides/reasoning.md`; Reasoning best practices (stale) — `…/reasoning-best-practices.md`
- Function calling — `…/api/docs/guides/function-calling.md`
- Structured Outputs — `…/api/docs/guides/structured-outputs`
- Prompt caching — `…/api/docs/guides/prompt-caching`
- Deprecations — `developers.openai.com/api/docs/deprecations`
- Rethinking skills and prompts for GPT-6 Astra — `developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra` (2026-09-11)
- Codex Prompting Guide (cookbook, not archived) — `developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide` (2026-02-25)
- Using Goals in Codex — `developers.openai.com/cookbook/examples/codex/using_goals_in_codex` (2026-05-09)
- Codex prompting · permission modes · CLI · models · personalize · skills — `learn.chatgpt.com/codex/{prompting,permission-modes,cli,models,personalize,skills-and-plugins}`
- AGENTS.md (Codex) — `learn.chatgpt.com/docs/agent-configuration/agents-md`
- Non-interactive mode · config reference · MCP · GitHub review — `learn.chatgpt.com/docs/{non-interactive-mode,config-file/config-reference,extend/mcp,third-party/github}`
- AGENTS.md convention — `agents.md`
- Page index — `developers.openai.com/llms.txt`
