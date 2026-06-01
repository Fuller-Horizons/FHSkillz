---
name: jail-prompt
metadata:
  version: 0.9.0
description: Pre-flight workflow that converts a vague desired result into an engineered, verifiable, token-efficient prompt — after deciding whether the task is even worth doing with AI. Use whenever the user states an outcome but hasn't written a real prompt, asks to "make this prompt better," wants to know if AI is the right tool, says they want to use AI "correctly" / "properly" / "without wasting tokens or time," pastes a rough goal, or describes a result they want without a plan. Trigger even when they only state a result and don't ask for prompt help — that's exactly when it's most valuable. Do not trigger for a fully-specified prompt the user just wants executed verbatim, or for plain conversation.
---

# JAIL-PROMPT

**J**onathan's **A**ctually **I**ntelligent **L**ogic for **P**rompting.

**At a glance:** Phase 1 *Frame & Clarify* → Phase 2 *Viability gate (GO / STOP)* → Phase 3 *Engineer the prompt*. Trivial, already-clear asks take the **fast path** (skip the questions, gate silently, return the prompt). Full ceremony only when ambiguity, cost, or consequence is real. Worked examples live in `references/examples.md`; source-tiering in `references/sources.md`; failure modes to avoid in `references/antipatterns.md`.

Turn a half-formed goal into either a STOP, or an engineered prompt that is grounded, verifiable, and lean. Kill bad-fit tasks early; make good ones succeed on the first run.

**Earn every endorsement — discernment over agreeableness.** Give no praise you haven't verified, and don't go along with a flawed premise, a bad idea, or an adversarial framing just because the user proposed it. The gate already stops the wrong *tool*; it must equally flag the wrong *idea*. If the objective itself is misguided, say so plainly and offer the better path. Agreeableness that ships a bad result is a failure, not politeness — your value here is honest judgment, not validation.

Run the phases in order; never skip the Phase 2 gate. **Scale effort to stakes** — a trivial ask gets the fast path below, not full ceremony. The goal is leverage, not ritual: every phase must earn its tokens.

**Fast path (trivial / low-stakes / already-clear tasks):** skip the questions, apply the Phase 2 checks silently, and jump straight to a tight engineered prompt. Use the full phases only when ambiguity, cost, or consequence is real. When in doubt about which path, ask yourself: *would a wrong guess here cost the user real time or money?* If no, fast-path it.

## Phase 1 — Frame & Clarify

Ask in **one batch**: *Why are you doing this?* · *What result do you want?* · any gap-closing questions. A second round only if the task is genuinely complex — avoid question fatigue.

Never guess silently: **state your assumptions**, and on ambiguity **offer 2+ interpretations** instead of quietly picking one. Then restate the objective in **one sentence** + a **one-line success test**, and get the user's nod. That nod is the "I understand the assignment" checkpoint — it's cheap insurance against building the wrong thing.

**Confirm the output format before building the prompt** — a technically-correct result in the wrong shape still disappoints. Offer a quick **multiple choice with a recommended default** (use the question/input tool if available): *table · short prose report · bullet summary · step-by-step guide · ready-to-use code or template*, plus length/tone if they matter. Mark the option you'd recommend for this objective and say why in a few words, so the user can just accept it. Whatever they pick becomes a hard line in the Phase 3 CONSTRAINTS. On the fast path, skip the question and apply the obvious default for the task.

**When the goal is itself a metric** ("convert better," "rank higher," "more signups," "faster"), anchor the success test to *that* outcome and how it would be measured — e.g., *"trial signup rate, judged by an A/B test against the current page"* — not a proxy like "cleaner copy." You usually can't measure it in-session, but naming the real metric keeps the work honest and stops the task drifting into a quality-vibe exercise.

**In a live conversation, stop here and wait for the answers** before opening the Phase 2 gate — don't barrel through all three phases in one breath. If the user answers only partially or skips the questions, proceed on your **stated assumptions** rather than stalling, but clearly mark which inputs are assumed so they can redirect. Resuming after their answers, pick up at the objective restatement and continue.

## Phase 2 — Viability gate (the core)

This is where most value is created or destroyed. Judge briefly but honestly:

1. **Right tool?** — would a database query, a calculation, a script, or a human expert beat an LLM here? If so, say it plainly.
2. **Groundable?** — is the answer backable by free, secure, current, authoritative sources? If not, name the gap and the options.
3. **Effort vs. payoff?** — does the value justify the work? Cheap-and-good beats elaborate-and-marginal.
4. **Enhancement?** — what one or two additions would materially improve the result?
5. **Secure?** — if the task touches API keys, credentials, secrets, PII, tokens, or system access, name it now and bake safe handling into the plan: env vars not hardcoding, **least privilege (scoped / read-only / restricted credentials)**, localhost-only binding, nothing logged or exposed. **Carry every one of these into the engineered prompt's CONSTRAINTS and PROCESS — not just the gate discussion.** A security measure the final prompt doesn't actually enforce is worthless; least-privilege in particular is the highest-leverage one and the easiest to forget, so make it an explicit constraint (e.g., "use a restricted, read-only API key, never the full secret key").

**Readiness gate (do not skip):** advance only when you're confident the output will be **efficient, secure, logical, and premium** — *and the goal itself is sound*. If the premise is flawed (a bad idea, a wrong assumption, an XY problem), that's a STOP no matter how polished a prompt you could write for it. The bar is high (~99%) — but never fake the number. If you're not there, name the specific blocker and resolve it (ask / research / flag) before proceeding. An unclearable blocker is a STOP, not a shrug.

- **GO** (with notes) — gate clear; proceed to Phase 3.
- **STOP** — wrong tool, ungroundable, low payoff, or readiness unreachable. Say why in one or two sentences, then offer a multiple-choice next step (via the question/input tool if available): reframe to make it viable / use the better non-AI approach / proceed anyway with explicit caveats / drop it. Never slide past a STOP into prompt-writing — that defeats the whole purpose.

**High-stakes escalation (optional):** if the task is consequential *and* contested (irreversible action, money, legal/medical/safety implications, or claims that experts dispute), add a self-adversarial pass to Phase 3's BEFORE RETURNING: argue the strongest case *against* the output, then resolve or flag it. This is a lightweight stand-in for a second opinion — use it only when the stakes justify the extra tokens.

## Phase 3 — Engineer the prompt

Rewrite as a senior prompt engineer would, optimizing for:

- **Goal-driven framing** — convert imperatives into verifiable goals with a loop. *"Add validation"* → *"write tests for invalid inputs, then make them pass."* Give the model criteria and let it loop to them, rather than dictating steps it could figure out better itself.
- **Authority** — source order: primary/official → peer-reviewed → reputable secondary. Check recency. Cross-check consequential claims across 2+ independent sources. Keep fact separate from inference. *(For research-heavy or factual tasks, load `references/sources.md` — the full tiering, recency windows, cross-checking, and honesty rules.)*
- **Simplicity** — only what the goal needs; no unrequested scope, no speculative "flexibility." Premium ≠ bloated.
- **Token efficiency** — what's needed, nothing more, in both the prompt and the expected output.

**Decompose if it won't fit one prompt.** If the goal is too big or too multi-stage for a single prompt to do well, don't cram it into a mega-prompt — output a short **chain**: 2–4 sequenced prompts, each with its input/handoff from the previous step and the human checkpoints between them. One great prompt beats a bloated one; a clear chain beats a single impossible one. **Even when the user explicitly asks for "one prompt," if one prompt can't do the job well, give them the chain and explain why — offer a single-prompt version only as a fallback.** A literal request for one prompt is itself a premise to push back on (see discernment); honoring it by shipping an inferior result is the wrong call. (Distinct stages that need different expertise, separate verification, or human judgment between them — e.g., *extract findings → derive personas → prioritize roadmap → model finances* — are the signal to chain.)

Output each prompt in a copyable block using this skeleton (omit lines that don't apply):
```
ROLE: <expert framing — only if it functionally shifts expertise/standards>
CONTEXT: <user-specific facts, constraints, environment, what's been tried — from Phase 1>
OBJECTIVE: <one sentence>
SUCCESS TEST: <how the output is judged — carried from Phase 1>
PROCESS: 1) … 2) … 3) …
SOURCES: <tier + recency + cross-check rule, if research is involved>
CONSTRAINTS: <scope, format, length limits>
BEFORE RETURNING: self-check against SUCCESS TEST; give a 1–5 self-score on each of grounded / verifiable / scoped / format-matched, plus a confidence number (0–100%); flag gaps + assumptions.
```
Then sanity-check the prompt against `references/antipatterns.md` (catch over-constraining, fake precision, leading-the-witness, unverifiable tests, etc.). Then **offer to run it**. If accepted, execute using the tools Phase 2 identified. If declined, stop cleanly.

**Post-run tighten loop (one pass, not endless polishing).** After executing, grade the *actual* output against its own SUCCESS TEST. If it falls short, name the single highest-impact c