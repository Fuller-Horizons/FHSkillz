# jail-questionnaire

Builds a questionnaire for someone else to fill in, such as a client intake before an engagement, or the questions you need a CFO or owner to answer before a decision.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.0.0.

## What it does

It asks you only about the send: who gets it, what you need back, and by when. Then it writes a short, plain-English questionnaire, most important questions first, one idea per question, with a space to answer under each. Facts it can already find become "please confirm" items instead of questions.

## Use it when

- You need a discovery intake for a new client or a listing
- A decision is stuck on facts only one person has
- You want "the questions to send them" as a document, not a live chat

## Don't use it for

- Questions Claude should ask you right now — use [`jail-task-contract`](../jail-task-contract/).
- Meeting agendas — use [`jail-cpr`](../jail-cpr/).

Adapted from Matt Pocock's `to-questionnaire` (MIT).
