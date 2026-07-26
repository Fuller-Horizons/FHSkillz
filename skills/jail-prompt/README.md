# jail-prompt

Turns a vague goal into a prompt that works on the first try — or tells you not to bother.

Part of the **[FHSkillz](../../README.md)** collection. Version 2.0.0.

## What it does

You describe a result you want, and jail-prompt checks whether AI is even the right way to get it. If it is, the skill asks a few sharp questions (or states its assumptions, if the stakes are low), then hands you a finished, copyable prompt. That prompt names the objective, states a pass/fail test, and lists the sources and limits it must respect. If AI is the wrong tool, or the idea itself is flawed, the skill says so — a clear "stop" beats a polished prompt for the wrong job.

## Use it when

- You know the outcome you want but haven't written a real prompt for it yet.
- You want to know if AI is even the right tool before you spend time on a prompt.
- Someone asks you to "use AI properly" and you want to skip the wasted tokens and false starts.
- You have a rough goal — "turn my messy notes into something usable" — and want it made concrete.

## Don't use it for

- Turning a finished analysis into a board-ready decision memo — use [`jail-summarize`](../jail-summarize/) instead.
- Running a full research task yourself — jail-prompt can point you to [`jail-research`](../jail-research/), but it won't gather the sources for you.
- A prompt you've already written and just want run as-is. Run it — don't route it through this skill.

## What you get

A short verdict (go ahead, or stop and here's why), then a copyable prompt block with the goal, the test that proves it worked, the sources it can use, and the format the answer must take.

## Example

**You ask:**

> I run discovery calls with new clients over Zoom — about 12 a month, 45 minutes each. It takes me almost an hour after each one to turn my messy notes into a clean summary for my team. I want a prompt I can reuse: paste in my notes, get back a one-page summary with clear action items.

**It produces:**

```
METADATA:
  inputs: [raw_call_notes]
  outputs: [call_summary]
  params: {temperature: 0.2}
  requires: none
  produces: [call_summary]
ROLE: An experienced consulting engagement manager who writes tight, decision-useful internal call summaries.
CONTEXT: Fuller Horizons runs ~12 client discovery calls a month, 45 minutes each. Summaries go to the internal delivery team, not the client, so they can be direct. The only input is the raw notes pasted below the prompt.
OBJECTIVE: Turn raw discovery-call notes into a one-page internal summary with clear, owned action items.
SUCCESS TEST: (1) [AUTO] word count of the summary is 350-450; (2) [AUTO] output contains a section literally titled "Action Items" formatted as a numbered list, with one line per open item; (3) [HUMAN] a teammate who wasn't on the call can act on each item without asking a follow-up question.
PROCESS:
  1) Read the raw notes once fully before writing anything.
  2) Extract: client name, attendees, one-line context on why they're evaluating Fuller Horizons.
  3) Pull 3-6 key discussion points, in the order that matters to the deal, not the order they were said.
  4) List every commitment, open question, or next step as a numbered action item with an owner (you, the client, or "unassigned" if the notes don't say).
  5) If a section has no supporting material in the notes, write "Not discussed" rather than inferring content.
SOURCES: None. The raw notes are the only source of fact. Do not add outside knowledge about the client, their industry, or Fuller Horizons.
OUTPUT FORMAT:
  ## Client Snapshot
  <2-3 sentences: who, why now, deal stage>
  ## Key Discussion Points
  - <point>
  - <point>
  ## Action Items
  1. [Owner] <action> — due <date or "not stated">
  2. [Owner] <action> — due <date or "not stated">
  ## Confidence
  <one line: any section thin on source material, or "Notes were complete.">
CONSTRAINTS: Max 450 words total. Plain markdown only, no client-side formatting. Never state a fact, number, or commitment that is not traceable to the pasted notes. If the notes don't state a next step for a raised issue, write "None stated" — do not invent one.
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
