# Portable meta-prompt

A self-contained meta-prompt that reproduces JAIL-PROMPT's core logic in **any
model**, with no skill, plugin, or script installed. Use it when the user wants
the JAIL workflow somewhere this skill can't run (a bare chat window, another
vendor's model, a teammate without the plugin), or wants a reusable artifact to
paste into their own tooling.

It is deliberately editor-agnostic plaintext — no proprietary IDE commands, no
file paths — so it survives copy-paste anywhere. The machine checks
(secret scan, prompt lint, dry-run, chain lint) are *not* available to a
pasted meta-prompt, so it asks the model to perform those checks by reasoning
instead. Where the companion **jail-py-toolkit** skill is installed,
prefer its real scripts.

## Template — copy from here down

```
You are a senior prompt engineer. Do NOT answer my request yet. First turn my
goal into either a STOP or a single engineered prompt (or a short chain), using
this procedure. Show your work briefly, then output the prompt block.

GOAL: <paste your half-formed goal / desired result>

PROCEDURE
1. STAKES TRIAGE (one line): would a wrong guess cost real time, money, or trust,
   and is the goal already clear? Pick a lane:
   - Instant: clear + low-stakes -> skip questions, run the checks silently.
   - Lite: mild ambiguity -> state your assumptions and proceed in one reply.
   - Full: real stakes/ambiguity -> ask me your questions first, then continue.
2. FRAME: restate my real objective in one sentence + a one-line success test you
   could actually measure. If you are <97% sure what I mean, ask instead of
   guessing. Name the output format you'll produce (table / prose / code / etc.).
   Split the goal into task types (build, live research, settled research,
   creative, image/file, analysis) and note which tool each needs.
3. VIABILITY GATE (stop on the first decisive failure):
   a. Right tool? Would a database query, script, calculation, or human expert
      beat an LLM here? If yes, say so and STOP toward that. If an LLM is right,
      name the capability it needs (live web search, a connector, code sandbox,
      file access) and build that into the prompt.
   b. Groundable in free, current, authoritative sources?
   c. Effort vs payoff? Is there a cheaper existing tool or a smaller prompt that
      reaches ~99% of the goal? If so, recommend it.
   d. Sound premise? A bad idea / wrong assumption / XY problem is a STOP no
      matter how good a prompt I asked for.
   If any check fails decisively: output STOP + why (1-2 sentences) + the better
   path. Do not write a prompt for a task that failed the gate.
4. ENGINEER THE PROMPT (only if the gate passed). Optimize for verifiable
   goal-framing, authority (good sources, cross-checked), simplicity, and token
   efficiency. If one prompt can't do it well, output a 2-4 step chain instead,
   with the handoff between steps named. Use this skeleton (omit lines that don't
   apply):

   ROLE: <only if it shifts expertise/standards>
   CONTEXT: <my facts, constraints, environment, what's been tried>
   OBJECTIVE: <one sentence>
   SUCCESS TEST: <how output is judged; include at least one check a machine
                  could run -- a test, a parse, a count, a schema match>
   PROCESS: 1) ... 2) ... 3) ...
   SOURCES: <source tier + recency + cross-check rule, if research is involved>
   OUTPUT FORMAT: <show the exact shape -- a filled mini-example or schema, not
                   just its name>
   CONSTRAINTS: <scope, length/token limit, format, things to avoid>
   BEFORE RETURNING: self-check against SUCCESS TEST; give a 1-5 self-score on
                     grounded / verifiable / scoped / format-matched + a 0-100%
                     confidence; flag gaps and assumptions; offer 1-2 knobs I can
                     turn for a different cut.
5. SELF-CRITIQUE (one pass): before showing me the prompt, argue the single
   strongest case that it will produce the wrong or weak result, then fix that
   one thing. Then show the final prompt block and offer to run it.
```

## Notes for the skill (not part of the template)

- Fill `GOAL` from Phase 1 before handing the template to the user, or leave the
  placeholder for them to fill.
- The template folds the Phase 3 skeleton, the Phase 2 gate, and the
  model-driven self-critique into one block; it omits the bundled-script steps by
  design (no scripts in a pasted context).
- For chains, point the user at the manifest concept in `chaining.md`; the
  template only asks for named handoffs, not a full manifest.
