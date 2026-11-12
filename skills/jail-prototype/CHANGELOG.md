# Changelog — jail-prototype

## 2.0.1 — 2026-11-12
- From the clean live A/B (2.0.0 lost 4/16 vs 7/16 to 1.2.0): every build reply opens with a PROTOTYPE BRIEF (question, shape, timebox, throwaway name, how variants differ, numbered points, checks run or not, exact send-back); no-question requests propose exactly one question with its shape; SHIP GATE splits into hard clauses (verbatim evidence, no production paths, marking) and recorded ones (ledger, archive, lint), so a clear reviewer answer ships as `answered` even when tooling is unreachable; promotion refusals cite the gate and name polish-to-ship.

## 2.0.0 — 2026-11-12

- **Review pages** for look questions (and anything easier judged by looking): one self-contained HTML file with three switchable variants, numbered review points, answer controls and a Copy-my-answers button whose pasted text is the verdict's evidence; explicit background, viewport, phone-width layout, no outside requests, sample data only. Review channel: lavish-axi on the user's computer → Claude app artifact → local file + pasted answers. Each round regenerates the file with a revisions legend. Review-loop ideas adapted from lavish-axi (github.com/kunchenguid/lavish-axi, MIT, © 2026 Kun Chen). New `references/review-pages.md` (rules + six templates).
- **Ledger check moved to Step 0** (before naming the shape); design direction chosen and stated; SPIKE VERDICT gains DESIGN and ANSWER lines and counts rounds; SHIP GATE clause 6 (artifact-lint) and evidence must be reviewer answers or surfaced state, never the builder's opinion.
- **artifact-lint.py** (jail-py-toolkit) checks review pages; repo validation runs it on HTML worked examples.
- Worked example: `references/example-scorecard-layouts.html` (lint-clean, browser-checked at desktop and 360px) + `references/example-review-round.md`. JAIL-HANDOFF with `tested:`. Description 447 chars with "Do NOT use"; core 137 lines.
- **Sandboxed hosts:** review pages must run without errors inside sandboxed previews (the Claude app blocks `history.replaceState`, storage and similar calls); the example page's deep-link call is guarded, `artifact-lint.py` flags unguarded sandbox-blocked calls, and `scripts/review-page-smoke.js` runs each example page in a browser both directly and in a sandboxed iframe during validation. Found by the owner viewing the example in the Claude app.
- New behavioral cases `evals/behavioral-0.28/jail-prototype.json` (review page, feedback round, promotion pressure, held-out logic question).

## 1.2.0 — 2026-07-25 (plugin 0.25.0)

- Step N now ships one fixed SPIKE VERDICT block (QUESTION · SHAPE · TIMEBOX set→actual · LEDGER-CHECK · quoted EVIDENCE · VERDICT · ARCHIVE · CONSUMER) plus a canonical ledger line, replacing prose bullets — the deliverable is now the same shape every run.
- 5-clause fail-closed SHIP GATE before any verdict ships (ledger checked first, throwaway name, zero production-path files, ≥1 quoted surfaced-state observation, resolvable archive pointer); any clause unmet ⇒ `VERDICT: inconclusive`, stop, never promote.
- Rule 6 bound numerically: default one working session, exactly one declared extension, look-questions = exactly 3 radically different variations.
- New behavioral suite `evals/behavioral-0.25/jail-prototype.json` — 4 cases: question-free build request, already-answered ledger hit, look-question variant count, promotion-under-deadline pressure.

## 1.1.0 — 2026-07-22 (plugin 0.23.0)

- SPIKE LEDGER: answered questions registered in project memory and checked before prototyping (retrieve, don't rebuild; premise changes supersede explicitly) + verdicts return to the consuming jail-decide/jail-bmc as labeled evidence.

## 1.0.0
- New kernel skill. Throwaway prototypes that answer a named DESIGN QUESTION — disposable from day one, one command to run, state surfaced; the validated answer graduates, the code dies on a branch. Adapted from Matt Pocock's prototype (MIT) under JAIL evidence rules.