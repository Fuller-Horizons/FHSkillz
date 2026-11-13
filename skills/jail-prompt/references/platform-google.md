# Platform pack — Google: Gemini & Antigravity

**Verified: 2026-09-14** against the docs listed under *Sources* below. Re-verify before
relying on any lever here. Every line traces to a fetched doc page — if you can't cite
one, it doesn't belong here (see the Evidence contract in SKILL.md).

Google's Gemini API pages carry visible **"Last updated" dates** — cite them. Current
model lineup at verification: `gemini-3.8-flash` (GA 2026-09-02, "our most intelligent
Flash model, engineered for long-horizon software engineering"), `gemini-3.7-flash`,
`gemini-3.6-flash`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.1-flash-lite`,
`gemini-3.1-pro-preview`, image models `gemini-3.1-flash-image` (Nano Banana 2) and
`gemini-3-pro-image` (Nano Banana Pro). **Knowledge cutoff January 2025.**

**Antigravity is now Antigravity 2.0** — a standalone desktop app, "your AI agents'
central command center." `/docs` redirects to `/docs/getting-started`. The original
Agent Manager "will remain available" but "will eventually be removed."

---

## Levers that change how you write the prompt

**System instructions carry the highest-priority material.** "Prioritize critical
instructions: Place essential behavioral constraints, role definitions (persona), and
output format requirements in the System Instruction or at the very beginning of the
user prompt."

**`thinking_level`, not `thinking_budget`:** `minimal | low | medium | high`.
Documented per-task guidance: "Use minimal or low thinking for fact retrieval or
classification"; "Use default thinking for comparing concepts or creative reasoning";
"Use maximum thinking for advanced coding, math, or multi-step planning." Also:
"Prompt the model to think less for lengthy outputs to save tokens."
**Defaults shifted down** — Gemini 3.5 Flash moved the default from `high` to `medium`
("Best quality for most tasks"), with `low` explicitly improved "for code and agentic
tasks needing lower latency." Current defaults: 3.8/3.7/3.6-flash = `medium`;
3.5-flash-lite = `minimal`; 3.1-pro-preview = `high`. Migration note: "Replace
`thinking_budget` with `thinking_level` enum."

**Thought signatures must be round-tripped.** In stateless mode you "**MUST** always
resend all `thought` blocks exactly as they were received." 3.5 Flash adds automatic
thought preservation (on by default, "may increase token usage").

**Long context: query LAST.** Verified and stated twice —
"In most cases, especially if the total context is long, the model's performance will be
better if you put your query / question at the end of the prompt (after all the other
context)"; and "When working with large datasets (e.g., entire books, codebases, or long
videos), place your specific instructions or questions at the end of the prompt, after
the data context." Use a transition phrase ("Based on the information above…").

**The two ordering rules are compatible:** persona / constraints / output format go in
the system instruction or at the very top; bulk context next; the specific question last.

**Markdown and XML are both explicitly endorsed, with no stated preference.**
"Use consistent structure: Employ clear delimiters to separate different parts of your
prompt. XML-style tags (e.g., `<context>`, `<task>`) or Markdown headings are effective."
Worked examples of both are shown. *(Contrast Anthropic, which prescribes XML.)*

**Few-shot examples are still recommended here.** "We recommend to always include
few-shot examples in your prompts." Maintain consistent formatting across examples to
avoid the model emitting unwanted formats; "Optimal examples number varies; experiment
to avoid overfitting." *(This diverges from OpenAI's zero-shot-first guidance for
reasoning models — do not carry that rule over.)*

**Leave temperature alone on 3.x.** "we strongly recommend keeping them at their default
values for Gemini 3.x models"; "We strongly recommend keeping the temperature parameter
at its default value of 1.0" because lowering it "may lead to unexpected behavior, such
as looping or degraded performance." 3.5 Flash goes further: `temperature`, `top_p`,
`top_k` are no longer recommended — "Remove unnecessary sampling parameters from
configuration." Sole documented exception: on safety-filter fallback responses,
"try increasing the temperature."

**`media_resolution` is a Gemini-3 lever** — it "determines the **maximum number of
tokens allocated per input image or video frame.** Higher resolutions improve the
model's ability to read fine text or identify small details, but increase token usage
and latency." Baseline 258 tokens for images ≤384px per side; larger images tile into
768×768 chunks at 258 tokens each; PDF pages 258 tokens/page. Gemini 3 does **not**
charge for tokens from **native extracted text** in PDFs — a real cost advantage for
document work.

**Structured output:** `response_format` with `"mime_type": "application/json"` +
`schema`. Best practices: use the `description` field to guide the model, strong typing —
**and still prompt for the format in text**. Warning: "Very large or deeply nested
schemas may be rejected," and output is "syntactically correct JSON" but may be
semantically wrong — validate at the app layer. Gemini 3 can combine structured outputs
with built-in tools (Search, URL Context, Code Execution, Function Calling).

**Prefix caching layout:** "Try putting large and common contents at the beginning of
your prompt" and "Try to send requests with similar prefix in a short amount of time."
Implicit caching is on by default for 2.5+; **minimum 4,096 tokens for all Gemini 3.x**
(2,048 for 2.5). Explicit caching is **not supported in the Interactions API**.

**Function calling:** "Keep active set to 10-20 tools maximum"; descriptions should
"Be clear and specific" with "descriptive names without spaces or special characters."

**Date/cutoff clause for Flash:** "For Gemini 3 Flash, add clauses about current date
(2026) and knowledge cutoff (January 2025)." Worth doing in every Gemini prompt that
touches anything time-sensitive.

**Multimodal inputs are equal-class.** "When using text, images, audio, or video, treat
them as equal-class inputs." Anchoring trick when output is too generic: ask the model to
"describe the image(s) or video before providing the task instruction."

⚠️ **Single-image ordering is contradictory in Google's own docs and no page reconciles
them.** Image understanding: "place the text prompt **before** the image." Files prompt
guide: "for prompts containing a single image, it might perform better if that image
(or video) is placed **before** the text prompt." Document processing: "If using a single
page, place the text prompt **after** the page." Treat this as empirically testable —
do not present either direction as settled. For interleaved content the Files guide says
"use whatever order is most natural."

**Prompt decomposition patterns** (documented): break instructions into one-per-prompt;
chain prompts (output feeds forward); aggregate parallel responses. Iteration levers:
different phrasing, analogous task framing, changing content order.

---

## Antigravity specifics

**Slash commands are the primary task-specification lever** (verbatim descriptions):
- `/plan` — "Researches code and generates a reviewable implementation plan artifact."
- `/goal` — "Autonomous execution until the goal is achieved without intermediate pauses."
- `/grill-me` — "Conducts an interactive interview to align on design details and edge cases."
- `/boost` — "Multi-agent deep reasoning for complex bugs, race conditions, and algorithms."
- `/teamwork-preview` — "Collaborative agent teams for repo-scale migrations, simulation, and research."
- `/browser` — "Launches a sandboxed browser subagent for web research and UI inspection."
- `/learn` — "Distills session feedback and corrections into persistent Rules or Skills."
- `/schedule` — "Schedules an instruction as a one-time timer or recurring cron job."
- `/btw` — "Asks a quick contextual question in the background without pausing work."
Plus `/rewind`, `/undo`, `/fork`, `/resume`.

**Documented three-phase workflow** — the closest thing to an official Antigravity
prompting method: **Exploration → Planning → Execution.** Ask the agent to explain how
the codebase resolves the problem *before* changes; request an implementation plan
artifact "listing targeted files, dependencies, and logic overrides"; direct edits only
after plan approval.

**The strongest documented reliability lever:** "The single most effective way to ensure
reliable, correct modifications from an autonomous agent is to provide the agent with a
local verification mechanism (such as unit tests, build commands, or formatting
scripts)." Documented loop: ensure a test suite exists → direct the agent to write tests
first → have it run verification commands → watch and iterate.

**Artifacts are the steering surface.** An Artifact is "a structured deliverable created
by the agent to accomplish its task and communicate its progress and thinking to the
human user," primarily generated during Planning Mode. Types: rich markdown
Implementation Plans, code diffs, architecture diagrams, images, browser recordings,
screenshots, Walkthroughs. Antigravity "supports commenting on these artifacts so you can
provide feedback to Agent for any reason, whether it be to decrease scope of changes,
use a different tech stack, or correct any Agent discrepancies" — then Proceed.
A **Walkthrough** is produced on completion; for browser tasks it "often contain[s]
screenshots and screen recordings."

**Artifact review policy:** **Request Review (recommended)** — the agent "always halts
and requests your explicit approval before proceeding"; or **Always Proceed** — it
"never halts for manual review."

**Rules files.** Global: `~/.gemini/GEMINI.md`, "applied across all workspaces."
Workspace: "`.agents/rules` folder of your workspace or git root" — "Antigravity now
defaults to `.agents/rules`, but still maintains backward support for `.agent/rules`."
**Limit 12,000 characters per file.** `@filename` pulls in other files. CLI best
practices separately says to "Create `GEMINI.md` or `AGENTS.md` at workspace root
documenting directory standards, styling paradigms, test parameters, and deprecation
warnings."

**Rule activation modes (4, verbatim):** *Manual* (activated via at-mention);
*Always On*; *Model Decision* ("Based on a natural language description of the rule, the
model decides whether to apply the rule"); *Glob* (`*.js`, `src/**/*.ts`).
**Model Decision is effectively a description-as-router field** — write it the way you'd
write a skill description.

**Skills replaced workflows.** `SKILL.md` with YAML frontmatter (`name` optional,
defaults to folder name; **`description` required**) in
`<workspace-root>/.agents/skills/<folder>/` or `~/.gemini/config/skills/<folder>/`.
Progressive disclosure: "When a conversation starts, the agent sees a list of available
skills with their names and descriptions," then reads the full SKILL.md if relevant.
**Workflows are deprecated and retire 2026-11-01.** Skills follow "the open Agent Skills
Standard (agentskills.io)."

**Browser verification loop.** Antigravity "can open, read, and actuate a local Chrome
browser." The Browser Subagent captures screenshots "when it wants to solicit your
assessment of the current page state," and all screenshots become commentable artifacts.
It runs "inside a completely separate Chrome profile to protect your personal data."
Design intent, from the launch post: "concerted emphasis for the agent to thoroughly
think through verification of its work, not just the work itself."

**Subagents:** invoked via `invoke_subagent`, spawning "a new concurrent session with a
dedicated role and initial prompt" that "does not inherit the parent's existing
conversation history." Workspace modes `inherit` / `branch` (isolated Git worktrees) /
`share`. Custom subagents are `.md` + frontmatter (`name`, `description` — "Used by
planner for task delegation" — `tools`, `model`, `commandExecutionPolicy`, `skills`,
`plugins`); "The markdown body following `---` defines the subagent's system prompt."
Max nesting depth **10**; an idle subagent re-awakens on message.

**Teamwork (named roles):** **Sentinel** (coordinator, "records your request, routes
tasks, posts periodic progress updates"), **Project Orchestrator** (breaks the brief into
milestones, delegates every unit of work), **Explorers** (read-only research) vs
**Workers** (implementation on "focused, non-overlapping tracks"). Conflict avoidance:
"the Project Orchestrator assigns specific files to individual Workers. Multiple workers
never edit the same file at the same time." Verification gates: **Critic** (reviews code),
**Challenger** ("stress-tests the code by building adversarial test suites"),
**Auditor** (validates against the selected integrity mode).

**Boost** is "an on-demand multi-agent reasoning pipeline designed for challenging
software engineering tasks": orchestrator decomposes into "discrete, verifiable
subtasks" → parallel subagents in "clean, isolated scopes" → "aggregates findings and
runs regression checks." Fit: concurrency bugs, algorithmic optimization, subtle
regressions, deadlocks, cross-file refactors. **Documented time scales:** default agent
= seconds to minutes; Boost = seconds to hours; Teamwork = hours to days. Use this to
pick the right mode rather than over-prompting the default agent.

**Models available inside Antigravity:** Gemini 3.8/3.7/3.6 Flash and Gemini 3.1 Pro;
Claude Sonnet 4.6 (thinking), Claude Opus 4.6 (thinking), GPT-OSS-120b on paid tiers.
Nano Banana 2 is the non-selectable image model for UI mockups, website imagery, and
"system or architecture diagrams." Selection is "sticky between user messages."
**No documented recommendation of which model for which task.**

**Permissions:** Request Review / Proceed in Sandbox / Always Proceed. Default file
scope is "the folders inside your Project and the application's local app data directory."
Terminal Sandbox Mode "restricts agent terminal commands to an isolated sandbox using
native operating system isolation."

**Gemini CLI is a separate product** with its own documented precedence: `GEMINI.md`
loaded from `~/.gemini/GEMINI.md`, then workspace dirs and parents, then auto-discovered
when tools touch directories — **all concatenated**. Alternative names via
`"context": { "fileName": ["AGENTS.md", "CONTEXT.md", "GEMINI.md"] }`. `/memory show`,
`/memory reload`.

---

## Documented anti-patterns

1. **Do not over-engineer prompts for Gemini 3.x.** "Gemini 3 is a reasoning model,
   which changes how you should prompt" — avoid "verbose or overly complex prompt
   engineering techniques used for older models." 3.5 Flash is blunter: such techniques
   "may cause the model to over-analyze."
2. **Do not pad with persuasion.** "Be precise and direct: State your goal clearly and
   concisely. Avoid unnecessary or overly persuasive language."
3. **Do not tune sampling parameters** (see above).
4. **Do not put the question first in long-context prompts.**
5. **Do not pass tokens you don't need.** "if you don't need tokens to be passed to the
   model, it is best to avoid passing them."
6. **Don't assume multi-needle retrieval matches single-needle.** "In cases where you
   might have multiple 'needles'… the model does not perform with the same accuracy."
7. **Inconsistent few-shot formatting leaks** into output; too many examples overfit.
8. **Vague multimodal asks produce generic output** — "describe this image" is the
   named failure.
9. **Don't over-nest schemas**; syntactically valid ≠ semantically correct.
10. **Don't exceed ~10-20 active tools.**
11. **Don't drop thought blocks.**
12. **Don't upload blurry or mis-rotated media** — "Verify that images are correctly
    rotated"; "Rotate pages to the correct orientation before uploading."
13. **Don't let parallel agents share files.**
14. **Don't exceed 12,000 characters per rules file**; don't build new workflows.
15. **Don't skip plan review for non-trivial changes.**

---

## Gaps — state these rather than guessing

- **No standalone official "Gemini 3 prompting guide" PDF** was found on
  ai.google.dev, blog.google, developers.googleblog.com, cloud.google.com, or
  storage.googleapis.com. Third-party press summaries are not official.
- **No "What's new in Gemini 3.8 Flash" page** (`/docs/whats-new-gemini-3.8` 404s).
  The authoritative prompting sources for "Gemini 3.x" are the **3.5 Flash page
  (2026-09-01)** and the **Gemini 3 guide (2026-08-26)** — not a 3.8 doc.
- **Vertex AI / Gemini Enterprise Agent Platform prompt-design pages render
  client-side** and could not be extracted — so no verified Vertex-specific few-shot
  count or component-ordering guidance.
- **Numeric `thinkingBudget` ranges are no longer documented** on the current thinking
  page.
- **Antigravity has no documented prompt-writing guide.** `/docs/cli/prompting/` is
  entirely input mechanics (keybindings, paste, editor). There are **no documented
  good-vs-bad prompt examples** and no Antigravity anti-patterns beyond file-ownership
  and review-policy rules. The only substantive method is Exploration → Planning →
  Execution plus the verification-loop guidance in `/docs/cli/best-practices/`.
- **Antigravity's knowledge base / memory system is not documented in 2.0.** The Nov 2025
  launch blog describes a knowledge base; no current doc page does. In 2.0 the documented
  persistence path is `/learn` → "persistent Rules or Skills" (`/docs/learn/` 404s).
  **Do not assume an automatic memory system exists in 2.0.**
- **No documented precedence between `GEMINI.md` and `AGENTS.md` in Antigravity**, and
  the rules page does not state which wins between global and workspace rules.
- **Antigravity "task lists"** appear only in the Nov 2025 launch blog, not the 2.0 docs
  (`/docs/task-list` 404s) — there is no documented way to request one.
- **No per-model context/output limit table** was surfaced on the Models page fetch; only
  3.5 Flash's figures (1M in / 65k out) were confirmed.

---

## Sources (fetched 2026-09-14)

- Prompt design strategies — `ai.google.dev/gemini-api/docs/prompting-strategies` (updated 2026-06-10)
- Gemini 3 developer guide — `…/docs/gemini-3` (updated 2026-08-26)
- What's new in Gemini 3.5 Flash — `…/docs/whats-new-gemini-3.5` (updated 2026-09-01)
- Thinking — `…/docs/thinking` (updated 2026-09-09)
- Long context — `…/docs/long-context` (updated 2026-06-22)
- Context caching — `…/docs/caching`; Structured output — `…/docs/structured-output`; Function calling — `…/docs/function-calling`; Text generation — `…/docs/text-generation`
- Image understanding — `…/docs/image-understanding`; Document processing — `…/docs/document-processing`; Files API — `…/docs/files`
- Models — `…/docs/models` (updated 2026-09-04); Changelog — `…/docs/changelog` (latest 2026-09-03)
- Antigravity — `antigravity.google/docs/{overview,getting-started,features,models,artifacts,implementation-plan,walkthrough,screenshots,artifact-review,rules-workflows,skills,mcp,subagents,teamwork,boost,slash-commands,agent-settings,faq}`
- Antigravity IDE/CLI — `antigravity.google/docs/ide/browser`, `…/docs/cli/{prompting,best-practices,artifacts}`, `…/docs/migration/workflows-to-skills`
- Introducing Google Antigravity — `antigravity.google/blog/introducing-google-antigravity` (2025-11-18); Antigravity 2.0 — `…/introducing-google-antigravity-2` (2026-05-19)
- GEMINI.md files (Gemini CLI) — `geminicli.com/docs/cli/gemini-md/`
