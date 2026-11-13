# Platform pack — Anthropic: Claude models & Claude Code

**Verified: 2026-09-14** against the docs listed under *Sources* below. Re-verify before
relying on any lever here; this vendor's docs moved domains and consolidated pages
within the last release cycle. Every line in this file traces to a fetched doc page —
if you can't cite one, it doesn't belong here (see the Evidence contract in SKILL.md).

**Doc domains moved.** API/model docs are now `platform.claude.com/docs/en/…`; Claude
Code docs are now `code.claude.com/docs/en/…`. Old `docs.claude.com` /
`docs.anthropic.com` links 302-redirect. The nine classic prompt-engineering
sub-pages (`use-xml-tags`, `prefill-claudes-response`, `chain-of-thought`, …) no
longer exist as separate pages — they were consolidated into one **Prompting best
practices** page plus per-model pages. Citing an old sub-page URL is a dead reference.

---

## Levers that change how you write the prompt

**Structure with XML tags.** "XML tags help Claude parse complex prompts
unambiguously" — consistent, descriptive names, nested naturally
(`<documents>` → `<document index="n">` → `<document_content>` + `<source>`).
XML also works as an *output* format indicator (e.g. asking for prose inside
`<smoothly_flowing_prose_paragraphs>` tags).

**Match prompt style to desired output.** "removing markdown from your prompt can
reduce the volume of markdown in the output."

**Role goes in the system prompt.** "Even a single sentence makes a difference."
If the app needs Claude to identify itself, state the model explicitly — Claude does
not reliably know which model it is.

**Explain *why*, not just what.** `NEVER use ellipses` → `Your response will be read
aloud by a text-to-speech engine, so never use ellipses…` — "Claude is smart enough
to generalize from the explanation."

**Examples: 3–5, relevant / diverse / structured**, wrapped in `<example>` inside
`<examples>`. `<thinking>` tags inside examples propagate the reasoning style.
⚠️ Countervailing current guidance: *"Stop doing: including extensive examples in
tool descriptions and system prompts"* — prefer expressive tool interfaces and a
few canonical examples over an edge-case laundry list.

**Long context: documents first, query last.** For 20k+ token inputs, put the
longform data *above* the query, instructions, and examples. "Queries at the end can
improve response quality by up to 30 percent in tests." Ask Claude to quote relevant
passages before performing the task.

**Effort is the primary dial** — `effort: low | medium | high | xhigh | max`
(default `high`). It shapes *all* output tokens, including thinking and tool calls.
It does **not** control visible response length on Opus 5 — "prompt explicitly for
conciseness instead."

**Thinking is adaptive, not budgeted.** `thinking: {type: "adaptive"}`;
"In internal evaluations, adaptive thinking reliably drives better performance than
extended thinking." Thinking is on by default on Opus 5 / Sonnet 5 and cannot be
turned off at all on the Fable/Mythos 5.x lines.

**Prefer general thinking instructions to prescriptive ones.** "A prompt like 'think
thoroughly' often produces better reasoning than a hand-written step-by-step plan."

**Be explicit about action vs. suggestion.** *"Can you suggest some changes…"* gets
suggestions; *"Change this function to improve its performance"* gets edits.

**Parallel tool calling is default and steerable** in both directions — a
`<use_parallel_tool_calls>` block to encourage, or *"Execute operations sequentially
with brief pauses…"* to reduce.

**Tool instructions live in the tool description, not the system prompt.** Don't
repeat across both. Only `tool_choice` *guarantees* a call; prompting ("Always call a
tool first") does not.

**Dial back emphatic language.** "Where you might have said 'CRITICAL: You MUST use
this tool when…', you can use more normal prompting like 'Use this tool when…'."
Blanket defaults ("Default to using [tool]", "If in doubt, use [tool]") now
overtrigger — make them conditional.

**Positive framing beats negative.** "Tell Claude what to do instead of what not to
do." Positive examples beat "don't" instructions.

**Less scaffolding, not more.** Anthropic "removed over 80% of Claude Code's system
prompt for models like Claude Opus 5 and Claude Fable 5 with no measurable loss on
coding evaluations." The target is the "right altitude": specific enough to guide,
flexible enough to be a heuristic — neither hardcoded if-else logic nor platitudes.

**Structured outputs replace prompting for JSON.** `output_config.format` with
`strict: true` uses constrained decoding — "more robust than prompting alone or using
prefilling."

---

## Hard errors — a prompt or call that does these is rejected

| Doing this | Result |
|---|---|
| Prefilled assistant message on the **last** turn | **400** on Claude 4.6+ — prefill is gone as a technique |
| `thinking.budget_tokens` | **400** on Claude 4.7+ — use `effort` |
| `temperature` / `top_p` / `top_k` at non-default values | **400** on Claude 4.7+; Python SDK v1.0+ raises `TypeError` |
| Modified, reordered, or partially dropped thinking blocks | **400** — pass them back byte-identical |
| Forced tool use with manual extended thinking | error |
| Disabling thinking at `xhigh`/`max` effort (Opus 5), or at all on Fable/Mythos 5.x | **400** |

**Append-only history (new).** On Fable 5.1, for accounts created after 2026-08-31,
thinking blocks are valid only in the exact conversation that produced them.
Injecting per-turn reminders, summarizing older turns in place, or changing the system
prompt mid-session invalidates every later thinking block. Use **turn-scoped
mid-conversation system messages** (`clear_at: "next_user_message"`) instead.
"Future models will enforce this for all accounts."

**New tokenizer (Opus 4.7+)** produces 25–35% more tokens than 4.6 — re-baseline
`max_tokens` and cost estimates. Cache minimum dropped 1,024 → 512 tokens.

---

## Claude Code / agent-harness levers

**CLAUDE.md is context, not configuration.** It loads as a user message *after* the
system prompt; "Claude treats them as context, not enforced configuration."
Target **under 200 lines**; files over 4 MiB are skipped. The test: *"Would removing
this cause Claude to make mistakes?" If not, cut it.* And the warning that matters:
**"Bloated CLAUDE.md files cause Claude to ignore your actual instructions!"**

- Include: non-guessable commands, style rules that *differ from defaults*, test
  runners, repo etiquette, architecture decisions, env quirks, gotchas.
- Exclude: anything derivable by reading the code, standard language conventions,
  detailed API docs, frequently-changing info, file-by-file descriptions, "self-evident
  practices like 'write clean code'."
- **Emphasis is scarce:** "If you emphasize many lines, none of them stands out."
- Load order is root → cwd, all **concatenated** (not overriding). Contradictory
  instructions across files mean "Claude may pick one arbitrarily."
- `.claude/rules/*.md` with `paths:` glob frontmatter = path-scoped rules that only
  enter context when Claude touches matching files.
- `AGENTS.md` is **not** read — import it (`@AGENTS.md`) or symlink.
- Escalation ladder when an instruction won't stick: more specific wording →
  path-scoped rule → `--append-system-prompt` → **hook** (deterministic).

**Skill frontmatter is a router.** `description` must state both WHAT and WHEN, in
**third person** (it is injected into the system prompt), ≤1024 chars. SKILL.md body
under 500 lines. References exactly **one level deep** — "Claude may only partially
read files referenced from other referenced files." Build 3+ evaluations before
writing extensive documentation. Set `disable-model-invocation: true` for anything
with side effects.

**Plan mode first — with a cost caveat.** Explore → Plan → Implement → Commit.
But: *"If you could describe the diff in one sentence, skip the plan."* Planning pays
off when the approach is uncertain, the change is multi-file, or the code is unfamiliar.
Spec-first variant: have Claude interview you, write `SPEC.md`, then start a **fresh
session** to execute it.

**Verification loops are the documented #1 lever.** *"Claude stops when the work looks
done. Without a check it can run, 'looks done' is the only signal available, and you
become the verification loop."* Four gate strengths by setup cost: in-prompt
("run the tests after implementing") → `/goal` condition → `Stop` hook → verification
subagent. **Demand evidence, not assertion** — test output, the command and its
return, a screenshot. Adversarial-review caveat: *"A reviewer prompted to find gaps
will usually report some, even when the work is sound"* — tell the reviewer to flag
only gaps affecting correctness or the stated requirements.

**Subagents are for context isolation.** The body is the subagent's *whole* system
prompt; it gets no conversation history, no parent memory, no already-read files.
`description` under 200 characters. Fresh-context review is the point: *"A fresh
context improves code review since Claude won't be biased toward code it just wrote."*

**Hooks are deterministic where CLAUDE.md is advisory.** "Unlike CLAUDE.md
instructions which are advisory, hooks are deterministic and guarantee the action
happens." Use for actions that must happen every time with zero exceptions.

**Headless flags worth knowing:** `-p/--print`, `--output-format json|stream-json`,
`--json-schema`, `--allowedTools` (the space before `*` matters —
`Bash(git diff *)` vs `Bash(git diff*)`), `--permission-mode`, `--append-system-prompt`,
and **`--bare`**, which skips auto-discovery of hooks, skills, commands, subagents,
plugins, MCP and CLAUDE.md — "the recommended mode for scripted and SDK calls, and
will become the default for `-p` in a future release."

**Agent SDK trap:** `claude -p` defaults to the Claude Code system prompt; the **SDK
does not**. The SDK's minimal default "omits Claude Code's security and safety
instructions."

---

## Documented anti-patterns

- **Emphatic over-prompting** — "CRITICAL: You MUST…" causes overtriggering.
- **Verification / double-check instructions on Opus 5** — "remove these instructions
  rather than rewriting them"; they cause over-verification with no quality gain.
- **Anti-markdown blocks on Fable 5.1** — that model already under-formats; remove.
- **"Hold all findings for the final response" on Fable 5.1** — delete; it already
  under-narrates.
- **Telling the model not to think** with thinking disabled on Opus 5 — "these
  increase tag leakage."
- **Asking Claude to explain its reasoning process** — read the thinking blocks.
- **Negative framing** — "Do not use markdown" ✗ vs "compose smoothly flowing prose
  paragraphs" ✓.
- **Over-specification generally** — "longer, more complex prompts aren't inherently
  better."
- **Repeating instructions across system prompt and tool descriptions.**
- **Bloated/overlapping tool sets** — "if engineers cannot definitively identify which
  tool applies… agents cannot be expected to choose better."
- **The kitchen-sink session** → `/clear` between unrelated tasks.
- **Correcting over and over** → after two failed corrections, `/clear` and rewrite
  the prompt. "A clean session with a better prompt almost always outperforms a long
  session with accumulated corrections."
- **Removing or editing tests** — "It is unacceptable to remove or edit tests because
  this could lead to missing or buggy functionality."
- **Chasing every reviewer finding** → over-engineering.
- **Windows-style backslash paths, time-sensitive content, voodoo constants,
  inconsistent terminology** in skills.

**Behavioral inversions between models.** Opus 5 is *more* verbose, self-verifies, and
over-delegates. Fable 5.1 is *less* narrative, under-formats, writes denser prose, and
rewrites whole files. A prompt tuned for one misfires on the other — so state the
target model in the prompt's CONTEXT, and don't carry damping blocks across families.

---

## Stale sources — do not cite as current

`claude.com/blog/best-practices-for-prompt-engineering` (Nov 2025) is still linked
from the official overview but recommends **prefilling** (now a 400 error) and says
XML and role-heavy prompting are "less necessary" — while the current doc still
prescribes both. **Where blog and doc disagree, the doc wins.**

There is no longer a standalone "Claude 4 / Opus 4.5 prompt engineering best
practices" page; that content is the "Migration considerations" section of the
consolidated page plus the per-model pages.

---

## Sources (fetched 2026-09-14)

- Prompting best practices — `platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices` (self-described "living reference"; the master page)
- Prompt engineering overview — `…/prompt-engineering/overview`
- Prompting Claude Opus 5 — `…/prompt-engineering/prompting-claude-opus-5`
- Prompting Claude Fable 5.1 — `…/prompt-engineering/prompting-claude-fable-5-1`
- Effort — `platform.claude.com/docs/en/build-with-claude/effort`
- Thinking — `…/build-with-claude/thinking`; Extended thinking (legacy) — `…/extended-thinking`
- Structured outputs — `…/build-with-claude/structured-outputs`
- Tool use overview — `platform.claude.com/docs/en/agents-and-tools/tool-use/overview`
- Agent Skills best practices — `…/agent-skills/best-practices`
- Opus 5 migration guide — `platform.claude.com/docs/en/models/opus-5/migration-guide`
- Best practices for Claude Code — `code.claude.com/docs/en/best-practices`
- How Claude remembers your project — `code.claude.com/docs/en/memory`
- Skills · Subagents · Hooks · Headless — `code.claude.com/docs/en/{skills,sub-agents,hooks-guide,headless}`
- Modifying system prompts (Agent SDK) — `code.claude.com/docs/en/agent-sdk/modifying-system-prompts`
- Effective context engineering for AI agents — `anthropic.com/engineering/effective-context-engineering-for-ai-agents` (2025-09-29)
- Writing effective tools for AI agents — `anthropic.com/engineering/writing-tools-for-agents` (2025-09-11)
- The new rules of context engineering for Claude 5 generation models — `claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models` (2026-07-24)
- Page inventories: `platform.claude.com/docs/llms.txt`, `code.claude.com/docs/llms.txt`
