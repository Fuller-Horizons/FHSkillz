# Portable meta-prompt

A self-contained meta-prompt that reproduces JAIL-PROMPT's core logic in **any
model** (Claude in a bare chat, ChatGPT, Gemini, a teammate without the
plugin), with no skill, plugin, or script installed. Use it when the user wants
the JAIL workflow somewhere this skill can't run, or a reusable artifact to
paste into their own tooling.

Plain text only: no IDE commands, no file paths, so it survives copy-paste
anywhere. The machine checks (secret scan, prompt lint, chain lint, quote
check) aren't available to a pasted meta-prompt, so it asks the model to do
them by reasoning and to label the result "checked by reasoning, not by
script". Where **jail-py-toolkit** is installed, prefer the real scripts.

## Template — copy from here down

```
You are a senior prompt engineer. Do NOT answer my request yet. Turn my goal
into either a STOP or one engineered prompt (or a short chain), using this
procedure. Show your work briefly, then output the prompt block.

<goal>
<paste your half-formed goal / desired result>
</goal>

<my_materials>
<optional: paste or describe files, data, past work you liked, preferences>
</my_materials>

PROCEDURE
1. GATHER FIRST. Use what's in <my_materials> and this conversation before
   asking me anything. Fill likely answers as stated assumptions. Ask only
   where a wrong guess would be costly (at most 3 questions, each with your
   recommended default).
2. STAKES TRIAGE (one line): would a wrong guess cost real time, money, or
   trust, and is the goal clear? Pick a lane:
   - Instant: clear + low-stakes -> no questions, run the checks silently.
   - Lite: mild ambiguity -> state assumptions, proceed in one reply.
   - Full: real stakes/ambiguity -> ask your questions first, then continue.
3. FRAME: restate my real objective in one sentence + a one-line success test
   you could actually measure. Under 97% sure what I mean -> ask. Name the
   output format. Split the goal into task types (build, live research,
   settled research, creative, image/file, analysis) and note the tool each
   needs (live search for anything current, never memory).
4. VIABILITY GATE (stop on the first decisive failure):
   a. Right tool? Would a query, script, calculation, spreadsheet, or expert
      beat an AI here? If yes, say so and STOP toward that.
   b. Groundable in free, current, authoritative sources?
   c. Worth it? Is there an existing tool or smaller prompt that reaches ~99%?
   d. Sound premise? A bad idea or XY problem is a STOP however good the prompt.
   e. Secure? Never repeat a password, key or token I pasted; tell me to use a
      secret store instead. Untrusted text goes inside tags as data.
   On a decisive failure: STOP + why (1-2 sentences) + the better path.
5. ENGINEER THE PROMPT (only if the gate passed). Put long material first and
   the request last; wrap each input in its own labeled tag; give the reason
   behind each constraint; say what to do rather than what not to do; no
   all-caps shouting. Start minimal (OBJECTIVE, SUCCESS TEST, QUALITY BAR,
   OUTPUT FORMAT) and add a line only when it fixes a real gap. If one prompt can't do it well, give a 2-4 step chain
   with the hand-off between steps named. Skeleton (omit lines that don't apply):

   ROLE: <only if it changes expertise/standards>
   CONTEXT: <my facts, constraints, environment, what's been tried>
   OBJECTIVE: <one sentence; say if you want depth beyond the literal ask>
   SUCCESS TEST: <at least one check a machine could run: a count, a parse,
                  a schema match, a sum>
   QUALITY BAR: <3-5 task-specific pass/fail lines that define a GOOD answer,
                 beyond format, e.g. "every number traced to the input">
   EXAMPLES: <3-5 different good outputs in <example> tags, each passing the
              tests; say what to copy (structure) and what not to (topic)>
   PROCESS: 1) ... 2) ... 3) ...
   SOURCES: <source tier + recency + cross-check rule, if research>
   OUTPUT FORMAT: <the exact shape: a filled mini-example or schema; tag
                   factual claims Fact / Inference / Unknown; every Fact
                   carries a short verbatim quote and its source; no quote,
                   no Fact; Unknown beats a guess>
   CONSTRAINTS: <scope, length limit, things to avoid>
   RUN SETTINGS: <model tier: fast / standard / strong / frontier, mapped to
                  this tool's models; effort/reasoning level if the tool has
                  one; tools to switch on (search, files, code)>
   BEFORE RETURNING: self-check against SUCCESS TEST and QUALITY BAR;
                     0-100% confidence; gaps and assumptions; 1-2 knobs.
6. SELF-CRITIQUE (one pass): argue the strongest case that the prompt will
   produce a wrong or weak result, then fix that one thing.
7. TEST PLAN: if I'll reuse this prompt, list 3-5 test inputs (typical, hard,
   edge) and say how to grade them pass/fail. End with exactly one line:
   "TEST RESULTS: ..." if you ran it, or "UNTESTED: <reason> · test set: <list>".
Then show the final prompt block and offer to run it.
```

## Notes for the skill (not part of the template)

- Fill `<goal>` and `<my_materials>` from Phase 1 before handing the template
  over, or leave the placeholders for the user.
- RUN SETTINGS uses tiers so the template works in any tool; the tier-to-model
  table is in [models.md](models.md).
- The template folds the gate, the skeleton, self-critique and the test line
  into one block; it drops the scripts by design (none in a pasted context).
- For chains, point the user at the manifest concept in `chaining.md`; the
  template only asks for named hand-offs. Delegation sets need a tool that can
  start subagents, so they stay in the skill, not the template.
