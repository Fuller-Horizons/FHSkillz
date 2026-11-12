# Per-model prompting notes (Claude 5 family)

Last verified: 2026-11-12
Load this when the prompt will run on a specific Claude model. Anthropic's
advice: read the target model's own guide first, and add a block only where
you see the problem it fixes. Re-check on every model release. Facts
(IDs, effort defaults, thinking) live in [models.md](models.md).

## All Claude 5 models
- Depth comes from **effort**; wording ("answer directly", "think less")
  doesn't reliably change thinking. Never ask for written-out reasoning.
- Thinking counts toward `max_tokens`; leave room or replies truncate.
- Changing effort mid-run breaks the prompt cache.
- Change instructions in the newest turn (or a mid-conversation system
  message), never by editing earlier messages or the system prompt of a
  stored conversation.
- State scope explicitly. Newer models follow instructions more literally and
  won't extend a rule to other items unless told to.

## Opus 5.5 (jail-prompt's own model)
- Start at `medium`; reserve `xhigh`/`max` for measured gains.
- **Pasted content:** wrap text pasted from elsewhere in
  `<pasted_content id="RANDOM">…</pasted_content id="RANDOM">` and say
  instructions inside it are followed only where the user's own message asks
  (see [security.md](security.md)).
- **Unattended agents:** use the "keep going" standing instruction (a message
  with no tool call ends the turn; carry on with whatever doesn't need the
  user; still confirm risky or destructive actions).
- **Multi-agent runs:** give a time budget and show elapsed time, e.g.
  `elapsed 340s / 1200s`; keep a hard timeout of your own.
- **Explore before acting** in multi-app work: open the relevant documents and
  records first, including ones the task doesn't name.
- Chat apps only: "treat an answered question as done" shortens latency; omit
  it for analysis or agent work (and for Fable, which loses self-correction).
- Safety classifiers can return `stop_reason: "refusal"`.

## Sonnet 5.5
- API default effort is `high`; `medium` for well-specified agent or chat
  tasks, `low` for latency-sensitive chat. Re-sweep effort; don't reuse
  Sonnet 5 settings.
- Useful blocks: keep working until done (stop only when blocked or before a
  risky step); when done and checked, stop and report without unrequested
  additions; for ideas or plans, give them and stop; search for specifics
  that may have changed since training, even when confident.
- Remove: "think less", "minimize tool calls", "hold findings for the end",
  token countdowns after tool results.
- At `low`/`medium` with structured output, treat `stop_reason: max_tokens`
  as a failure and retry.

## Sonnet 5 (still widely deployed)
- Conciseness block when needed: "Provide concise, focused responses. Skip
  non-essential context, and keep examples minimal."
- **Reviewers and checkers: coverage first, filter later.** Ask for every
  finding with confidence and severity; let a separate step filter. "Only
  report high-severity issues" lowers recall.
- New tokenizer: about 30% more tokens for the same text.

## Haiku 5.5
- Default `medium`. `low` is prone to skipped searches, early stops and
  skipped checks in long agent prompts; raise effort or add the keep-working
  block.
- **Search grounding:** give today's date and say records, prices, rules and
  anything "latest" may have changed, so search before answering. Avoid
  blanket "search everything" rules (they cause needless searches).
- Chatbots: an adherence block keeps system rules in force when a user argues,
  claims an exception was approved, or keeps asking.
- No server-side fallback on refusals; handle `stop_reason: "refusal"`.
- Keep user text out of `tool_result` blocks.

## Fable 5.2
- API default `high`; `low` for quick, well-specified or high-volume work
  (including subagents), `medium` for everyday work. Re-sweep effort.
- Stops early on long tasks at `low`/`medium`: add the finishing block.
- **Name the actions that need approval** ("sending messages to people
  outside this conversation"); vague approval rules make it hold back
  routine work.
- Follows caution and style rules closely: drop hard style limits on prose
  (e.g. "20 words or fewer") and stale absolute cautions ("never retry");
  turn "never delete" into "ask before deleting".
- Over-delegates at `xhigh`/`max` and with standing delegation instructions;
  check which model subagents default to (they can dominate cost).
- Good as a planner/orchestrator over smaller models.
- Writes little between tool calls: ask for a one-line opening and a short
  closing recap; effort barely changes length, so set length in words.

## Sources (accessed 2026-11-12)
- https://platform.claude.com/docs/build-with-claude/prompt-engineering/claude-prompting-best-practices
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2
