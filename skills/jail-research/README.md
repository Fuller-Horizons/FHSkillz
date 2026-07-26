# jail-research

This skill turns a question into an answer you can trust, backed by real sources you can check.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.3.0.

## What it does

You give it a question and the decision it needs to support. It splits the question into smaller parts, then searches for real sources to answer each part. It writes two things: a short answer in plain language, and an evidence packet — a structured list of every source, what each one proves, and how fresh it is. When sources disagree, it shows both sides instead of picking one and hiding the fight. Anything it could not check gets marked Unknown, not guessed.

## Use it when

- You need a real answer before a decision, not just an opinion.
- Someone asks "what does the data say" or "find evidence for this."
- Another skill, like jail-decide or jail-strategy, needs solid facts first.

## Don't use it for

- Screening a US private company for a sales deal — use [`jail-prospect`](../jail-prospect/) instead.
- Turning facts you already have into a summary — use [`jail-summarize`](../jail-summarize/) instead.

## What you get

A short written answer with numbered citations, plus an evidence packet that lists every source, its date, and any open questions.

## Example

**You ask:**

> One of our clients — a mid-size manufacturer — is deciding whether to lock in a fixed-rate commercial term loan this week or wait to see what the Fed does. What's the Fed's current rate, when's the next decision, and what does the market expect?

**It produces:**

```
# PART 1 — SYNTHESIZED ANSWER

Lock-now-vs-wait comes down to two things: how much room rates have to move, and whether the July 28–29 meeting is likely to be a non-event. On the first, there is no ambiguity — the target range is 3.50%–3.75%, set by a unanimous 12–0 FOMC vote on June 17, 2026 [1] (Fact, high confidence). On the second, the honest answer is that nobody has a confident number. The Fed's own calendar confirms the next decision lands Wednesday, July 29, 2026, around 2:00 p.m. ET, and this is a non-SEP meeting — no updated dot plot, so the Fed won't be signaling its multi-meeting path the way it does at the March, June, September, or December meetings [2] (Fact, high confidence).

...
EVIDENCE PACKET
Objective + consuming decision: Determine the Fed's current policy rate and the
outlook for the July 28-29, 2026 FOMC decision, to support a mid-size
manufacturing client's choice to lock a fixed-rate commercial term loan this
week vs. wait for the Fed.

Questions:
  Q1: What is the Fed's current federal funds rate target range, and how was
      it set?
      Answer: 3.50%-3.75%, set by unanimous 12-0 FOMC vote on 2026-06-17 —
              Fact · high confidence
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
