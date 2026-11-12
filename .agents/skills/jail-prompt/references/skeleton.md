# Phase 3 skeleton: field-by-field notes

Load this when writing the prompt block. SKILL.md carries the one-line version of each field; this file carries the full rule for each. Omit lines that do not apply, but never omit a section the SUCCESS TEST depends on.

## Fields

- **METADATA.** Use YAML with a fixed key set so downstream agents can parse the handoff: `inputs:` `outputs:` `params:` (for example `temperature: 0.0` for idempotent structure) `requires:` `produces:`. Keep every key, even when the value is "none".
- **ROLE.** Expert framing, only if it changes expertise or standards. Otherwise drop it (see role cosplay in [antipatterns.md](antipatterns.md)).
- **CONTEXT.** User-specific facts, constraints, environment, and what has been tried, all taken from Phase 1.
- **OBJECTIVE.** One sentence.
- **SUCCESS TEST.** How the output is judged, from Phase 1. It must include at least one programmatic, machine-checkable check (a test suite run, a script, a count, a schema parse) and must not rely only on subjective review. If the output is rendered or executed downstream, add the malicious-sample assertion from [security.md](security.md).
- **PROCESS.** Numbered steps. Constrain outcomes, not keystrokes.
- **SOURCES.** Tier, recency, and cross-check rule, if research is involved. Name the retrieval capability the prompt has (live search, connector, document store); see [sources.md](sources.md).
- **OUTPUT FORMAT.** Show the exact shape, not just its name: a filled mini-example, a header row, or a schema the model copies (pre-engineered schemas in [templates.md](templates.md)). Mandate a strict JSON Schema when structural predictability matters. For factual or research output, tag each material claim Fact / Inference / Unknown as structured fields (`status`, `evidence_count`, `source_ids`), not prose, so a checker can reject an unevidenced Fact. Prefer Unknown to a confident guess. Details: [truth-tagging.md](truth-tagging.md).
- **CONSTRAINTS.** Scope; length limits (include explicit token budgets or character limits to prevent context bloat); client-portability requirements (stay plaintext or Markdown, avoid proprietary IDE commands); things to avoid.
- **VERIFICATION PLAN.** What to check next. Mark each step [AUTO] (a tool or second model runs it) or [HUMAN]. Lead with the check most likely to falsify the output, not the easiest confirmation. If [AUTO] checks disagree, mark the result provisional.
- **BEFORE RETURNING.** Self-check against the SUCCESS TEST; 1-5 self-score on grounded / verifiable / scoped / format-matched plus confidence (0-100%); flag gaps and assumptions; then surface the one or two knobs the user can turn for a different cut (shorter, more sources, regrouped). That is a bounded revision handle, not an open loop.

## Chains

Even when the user asks for "one prompt", if one cannot do the job well, give the chain and explain why, and offer a single-prompt fallback. Signals to chain: distinct stages needing different expertise, separate verification, or human judgment between them (for example extract findings, derive personas, prioritize a roadmap, model finances). When you chain, load [chaining.md](chaining.md) and emit the manifest alongside the prompt blocks. Lint it with `chain-lint.py`; manual fallback: every key a step `requires` must be produced by an earlier step or declared in `inputs`, and per-step and chain-level SUCCESS TESTs must exist. A broken handoff is caught here, before a single token runs.

## Gate detail (Phase 2)

- **Right tool.** Capabilities to name when the LLM is right: live web search, a connector or MCP (GitHub, Notion, CRM, and so on), a code sandbox, file access, extended thinking. Route the prompt to them and carry the requirement into PROCESS and SOURCES. A prompt that needs current data but is not told to search, or a system it is not given access to, fails regardless of wording.
- **Delegation.** If the task or a sub-task matches another installed skill's triggers (`docx`, `jail-rate`, `jail-research`, `jail-decide`, `jail-verify`, `jail-prospect`, a frameworks skill), recommend that skill instead of writing a new prompt.
- **Build vs. buy.** Before suggesting a custom build, search repositories and marketplaces (GitHub, VS Code Marketplace, npm, PyPI) for an existing free tool, and weigh paid or off-the-shelf options for high-effort goals. Cost counts in tokens and in the user's own effort. If a far cheaper path reaches 99% of the goal, recommend it, even if it is a smaller prompt, a non-AI tool, or a purchased product.
- **Readiness.** The bar is about 99%. A flawed premise (bad idea, wrong assumption, XY problem) is a STOP however good the prompt would be. Name the blocker and resolve it (ask, research, flag) or STOP.

## After the prompt

- Sanity-check against [antipatterns.md](antipatterns.md) (over-constraining, fake precision, leading the witness, unverifiable tests), then lint.
- Self-critique, one round. Where a second model or a retrieval tool exists, send the critique and any citation check there; same-model critique is the fallback. Where this skill cannot run (another model, a bare chat), hand over [meta-prompt.md](meta-prompt.md).
- Offer to save the approved prompt to a project-local `prompts.json` or a file under `prompts/` for reuse, then offer to run it. If accepted, execute with the tools Phase 2 identified. If declined, stop cleanly.
- Post-run tighten loop, one pass: grade the actual output against the SUCCESS TEST; if it falls short, name the single highest-impact change, apply it, re-grade once. One targeted fix beats five cosmetic ones.
- Dry run (high-stakes prompts): draft a mock output and confirm the declared OUTPUT FORMAT holds it. Determinism self-test: for prompts that declare `temperature: 0.0` and a strict schema, generate against the same mock twice and diff the structures. Identical structure confirms the idempotency METADATA promises; a diff means the schema is not pinning the output.
