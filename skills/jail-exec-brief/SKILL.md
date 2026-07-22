---
name: jail-exec-brief
metadata:
  version: 1.1.0
description: >-
  Convert complex material — analysis, research, technical findings, project
  state — into concise, DECISION-FORCING executive communication that leads
  with the answer, translates technical issues into business consequences
  (revenue, liability, resilience, competitive position, cost, control,
  timing), and ends with the decision it exists to force — no FYI briefs.
  Use for "summarize this for the board/CEO/client", "make this
  executive-ready", "translate this technical finding", briefing packs,
  decision memos, and as the final voice of a kernel chain. Do NOT use for
  internal working notes, raw research packets (jail-research), full
  decision analysis (jail-decide — this skill presents it), or plain
  recaps of meetings/threads with no executive audience (that's direct
  summarization or jail-cpr's debrief).
---

# JAIL-EXEC-BRIEF

Executives buy decisions, not detail. Lead with the answer, keep the nuance
that changes the decision, cut everything else. [Constitution Rules 1, 6]

## The seven-part structure (default; compress, don't reorder)
1. **Outcome / central finding** — the answer, first sentence, no wind-up.
2. **Material facts** — the few facts the decision rests on, labels intact
   (fact vs analysis stays visible even here — an inference presented as
   fact in a board memo is a Rule-1 violation with consequences).
3. **Assumptions & uncertainties** — what we're taking on faith + honest
   Unknowns. Executives respect a named unknown; they punish a hidden one.
4. **Risks & constraints** — material only, each with its consequence.
5. **Options / implications** — what the reader can actually choose, priced.
6. **Recommendation** — one, clearly, with confidence.
7. **Immediate next actions** — who does what by when.

## Translation rules (technical → business)
Every technical, cybersecurity, AI, compliance, or architecture point is
expressed as its business consequence in one or more of: **revenue ·
liability · resilience · competitive position · cost · control · timing**.
"Unpatched CVE-2026-XXXX on the payment gateway" becomes "a known,
actively-exploited hole in the system that takes payments — fixing it costs
a day; an incident costs customers, breach-notification liability, and the
renewal narrative." Keep the technical identifier in a parenthetical or
appendix for the operators; the sentence must work for the CEO.

## The decision-forcing mandate (what a plain model won't do unprompted)
A brief that informs without forcing anything is a status report wearing a
suit. Every brief ends with: **the named decision this brief serves · the
options, priced · one recommendation · the decision deadline and what delay
costs**. The rare legitimate FYI ("no decision required because X") must
say so explicitly and justify itself — it is the exception, declared, never
the default.

## Audience calibration (pick the row, say which)
| Audience | Length | Leads with | Translation depth |
|---|---|---|---|
| Board / CEO | one page, hard cap | the decision + recommendation | full business-consequence; tech IDs to appendix |
| Operating exec | brief + appendix | finding + what changes this quarter | business-first, operator detail preserved in appendix |
| Line manager | half page | the action needed from their team | light — they speak the domain |

## Craft rules
- **Scale depth to the audience** per the table above; the appendix holds
  what curiosity needs, the brief holds what the decision needs.
- Plain language beats jargon wherever plain language is sufficient; a term
  of art earns its place only when precision requires it.
- **No heading spam, no fragment shorthand, no repetition.** Prose sentences
  in the brief; bullets only where they genuinely clarify.
- Cut any detail that does not change the decision. Preserve any nuance that
  does — brevity that loses a material caveat is a lie of omission.
- Numbers keep their provenance ("per Q2 filings" / "our estimate") — a
  figure with no source reads as fact and will be repeated as one. [Rule 10]

Close with the JAIL-HANDOFF block only when feeding another skill; a brief
delivered to a human ends at next actions — humans don't need YAML.

## Related skills
Decision analysis to present → **jail-decide** runs first. Evidence behind
the brief → **jail-research** packet. Meeting around the brief →
**jail-cpr**. Verify a consequential brief before it ships →
**jail-verify**.

## Gotchas
- **Burying the lede.** Three paragraphs of context before the answer. The
  answer IS sentence one; context follows only as needed.
- **Fact-analysis blending.** "The migration will save $400K" — measured, or
  hoped? The label survives compression or the brief misleads.
- **Jargon smuggling.** Acronyms and stack names the reader must decode.
  Translate or cut.
- **Completeness compulsion.** Shipping everything you know. The appendix
  exists so the brief doesn't have to.
- **Recommendation hedging.** Three "options to consider" and no
  recommendation is analysis, not advice. Recommend one; price the rest.
