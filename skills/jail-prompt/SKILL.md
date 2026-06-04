---
name: jail-prompt
metadata:
  version: 1.4.0
description: Pre-flight workflow that converts a vague desired result into an engineered, verifiable, token-efficient prompt — after deciding whether the task is even worth doing with AI. Use whenever the user states an outcome but hasn't written a real prompt, asks to "make this prompt better," wants to know if AI is the right tool, says they want to use AI "correctly" / "properly" / "without wasting tokens or time," pastes a rough goal, or describes a result they want without a plan. Trigger even when they only state a result and don't ask for prompt help — that's exactly when it's most valuable. Do not trigger for a fully-specified prompt the user just wants executed verbatim, or for plain conversation.
---

# JAIL-PROMPT

Jonathan's Actually Intelligent Logic for Prompting.

**At a glance:** a stakes triage routes each task to the lightest path that still earns the result — **Instant** (clear, low-stakes → straight to the prompt), **Lite** (assumptions + verdict + draft in one reply), or **Full** (Phase 1 Frame & Clarify → Phase 2 Viability gate → Phase 3 Engineer the prompt, pausing for answers). Same three phases underneath; the lane sets the ceremony. References load only when needed: worked examples in `references/examples.md`, source-tiering in `references/sources.md`, failure modes in `references/antipatterns.md`.

Turn a half-formed goal into either a STOP or an engineered prompt that's grounded, verifiable, and lean. Kill bad-fit tasks early; make good ones succeed on the first run.

**Discernment over agreeableness.** Give no praise you haven't verified, and don't go along with a flawed premise just because the user proposed it. The gate stops the wrong *tool*; it must equally flag the wrong *idea*. If the objective is misguided, say so and offer the better path — agreeableness that ships a bad result is a failure, not politeness.

**Stakes triage — first, in one line.** Ask: would a wrong guess cost real time, money, or trust, and is the goal already clear? Then route:

- **Instant** — clear, low-stakes. Skip questions, run the gate silently, return a tight prompt.
- **Lite** — mild ambiguity, modest stakes. Don't stall for a question round: state assumptions, give the GO/STOP verdict, and include the draft prompt in the same reply.
- **Full** — real ambiguity, cost, or consequence. Run all three phases, pausing after Phase 1 for answers.

Speed comes from doing less on easy tasks, never from weakening judgment on hard ones. A STOP is available in every lane, and never skip the gate — in Instant/Lite you run it fast and silently, you don't omit it. When unsure which lane, pick the lighter one and escalate if needed.

## Phase 1 — Frame & Clarify

Ask in one batch: why are you doing this? what result do you want? plus any gap-closing questions. A second round only if genuinely complex.

Never guess silently: state assumptions, and on ambiguity offer 2+ interpretations rather than quietly picking one. Restate the objective in one sentence + a one-line success test, and get the user's nod.

Confirm output format before building — a correct result in the wrong shape still disappoints. Offer a quick multiple choice with a recommended default (table · prose report · bullet summary · step-by-step guide · ready-to-use code/template), plus length/tone if they matter. Whatever they pick becomes the Phase 3 **OUTPUT FORMAT** line — a concrete shape or mini-example, not just named. Instant applies the obvious default; Lite states the default it's assuming.

When the goal is itself a metric ("convert better," "rank higher," "more signups"), anchor the success test to that outcome and how it's measured (e.g. "trial-signup rate, A/B-tested against the current page"), not a proxy like "cleaner copy."

In the Full lane, stop here and wait for answers before opening the gate. (Instant skips the questions; Lite states assumptions and proceeds in one reply.) If the user answers partially or skips, proceed on stated assumptions — marked as assumed — rather than stalling.

## Phase 2 — Viability gate (the core)

Kill fast: run the cheap disqualifiers first and STOP the moment one fails decisively — don't analyze how to enhance or secure a task that's the wrong tool or can't be grounded.

Disqualifiers (short-circuit to STOP on the first decisive failure):

1. **Right tool — and the right tool *for* the LLM?** Would a database query, a calculation, a script, or a human expert beat an LLM outright? If so, say it (a STOP toward the better tool). If an LLM is right, name the capability it needs — live web search, a connector/MCP (GitHub, a CRM, a docs store), a code sandbox, file access, extended thinking — and route the prompt to it, carried into PROCESS/SOURCES. A prompt that needs current data but isn't told to search, or a system it isn't given access to, fails regardless of wording.
2. **Groundable?** Is the answer backable by free, current, authoritative sources? If not, name the gap and the options.
3. **Effort vs. payoff?** Does the value justify the work? Cheap-and-good beats elaborate-and-marginal.

Only once it clears:

4. **Enhancement?** What one or two additions would materially improve the result?
5. **Secure?** If the task touches API keys, credentials, secrets, PII, tokens, or system access, bake safe handling into the plan — env vars not hardcoding, least privilege (scoped / read-only / restricted creds), localhost-only binding, nothing logged — and carry each into the prompt's CONSTRAINTS and PROCESS, not just the gate discussion. Least-privilege is the highest-leverage and easiest to forget; make it explicit ("use a restricted, read-only key, never the full secret").

Readiness gate: advance only when confident the output will be efficient, secure, logical, premium — and the goal itself is sound. A flawed premise (bad idea, wrong assumption, XY problem) is a STOP no matter how good a prompt you could write. The bar is high (~99%); never fake the number — name the blocker and resolve it (ask / research / flag), or STOP.

- **GO** (with notes) — gate clear; go to Phase 3.
- **STOP** — wrong tool, ungroundable, low payoff, or readiness unreachable. Say why in a sentence or two, then offer a multiple-choice next step: reframe to make it viable / use the better non-AI approach / proceed with explicit caveats / drop it. Never slide past a STOP into prompt-writing.

High-stakes escalation (optional): if the task is consequential *and* contested (irreversible, money, legal/medical/safety, or expert-disputed claims), add a self-adversarial pass to Phase 3's BEFORE RETURNING — argue the strongest case against the output, then resolve or flag it.

## Phase 3 — Engineer the prompt

Rewrite as a senior prompt engineer would, optimizing for:

- **Goal-driven framing** — convert imperatives into verifiable goals with a loop. *"Add validation"* → *"write tests for invalid inputs, then make them pass."* Give criteria, let the model loop to them.
- **Authority** — source order primary/official → peer-reviewed → reputable secondary; check recency; cross-check consequential claims across 2+ sources; keep fact separate from inference. *(Research-heavy tasks: load `references/sources.md`.)*
- **Simplicity** — only what the goal needs; no unrequested scope. Premium ≠ bloated.
- **Token efficiency** — what's needed, nothing more, in both prompt and expected output.

Decompose if it won't fit one prompt: output a short **chain** of 2–4 sequenced prompts with handoffs and human checkpoints, not a mega-prompt. Even when the user asks for "one prompt," if one can't do the job well, give the chain and explain why, offering a single-prompt fallback. (Distinct stages needing different expertise, separate verification, or human judgment between them — e.g. *extract findings → derive personas → prioritize roadmap → model finances* — are the signal to chain.)

Output each prompt in a copyable block using this skeleton (omit lines that don't apply):
```
ROLE: <expert framing — only if it shifts expertise/standards>
CONTEXT: <user-specific facts, constraints, environment, what's been tried — from Phase 1>
OBJECTIVE: <one sentence>
SUCCESS TEST: <how the output is judged — from Phase 1>
PROCESS: 1) … 2) … 3) …
SOURCES: <tier + recency + cross-check rule, if research is involved>
OUTPUT FORMAT: <show the exact shape, not just its name — a filled mini-example, a header row, or a schema the model copies. e.g. "Markdown table: | Item | Value | Source | Date |", or a 3-line template. A concrete exemplar is the biggest lever for a repeatable deliverable.>
CONSTRAINTS: <scope, length limits, things to avoid — the shape lives in OUTPUT FORMAT>
BEFORE RETURNING: self-check against SUCCESS TEST; 1–5 self-score on grounded / verifiable / scoped / format-matched + confidence (0–100%); flag gaps + assumptions; then surface the 1–2 knobs the user can turn for a different cut (shorter / more sources / regrouped) — a bounded revision handle, not an open loop.
```
Sanity-check the prompt against `references/antipatterns.md` (over-constraining, fake precision, leading-the-witness, unverifiable tests).

**Always surface the engineered prompt before acting — it's the deliverable, not a byproduct.** Output the copyable block first, even when the task is immediately executable and you intend to run it yourself; don't collapse into silently doing the task and returning only the result. This binds every lane: Instant returns the prompt, Lite includes it in the one reply, Full produces it after the gate, and even a big agentic task you mean to run end-to-end shows the prompt that drives it first. Exceptions: a STOP (no prompt), or the user explicitly says *"just do it"* (then state the one-line OBJECTIVE + SUCCESS TEST and proceed).

Then offer to run it. If accepted, execute with the tools Phase 2 identified. If declined, stop cleanly.

**Post-run tighten loop** (one pass, not endless polishing): grade the actual output against its SUCCESS TEST; if it falls short, name the single highest-impact change, apply it, and re-grade once. Then ship with the self-score and any flagged gaps. One targeted fix beats five cosmetic ones; a good-enough result now beats a marginally-better one the user is still waiting on.
