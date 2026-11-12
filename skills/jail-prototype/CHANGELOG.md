# Changelog — jail-prototype

## 1.2.0 — 2026-07-25 (plugin 0.25.0)

- Step N now ships one fixed SPIKE VERDICT block (QUESTION · SHAPE · TIMEBOX set→actual · LEDGER-CHECK · quoted EVIDENCE · VERDICT · ARCHIVE · CONSUMER) plus a canonical ledger line, replacing prose bullets — the deliverable is now the same shape every run.
- 5-clause fail-closed SHIP GATE before any verdict ships (ledger checked first, throwaway name, zero production-path files, ≥1 quoted surfaced-state observation, resolvable archive pointer); any clause unmet ⇒ `VERDICT: inconclusive`, stop, never promote.
- Rule 6 bound numerically: default one working session, exactly one declared extension, look-questions = exactly 3 radically different variations.
- New behavioral suite `evals/behavioral-0.25/jail-prototype.json` — 4 cases: question-free build request, already-answered ledger hit, look-question variant count, promotion-under-deadline pressure.

## 1.1.0 — 2026-07-22 (plugin 0.23.0)

- SPIKE LEDGER: answered questions registered in project memory and checked before prototyping (retrieve, don't rebuild; premise changes supersede explicitly) + verdicts return to the consuming jail-decide/jail-bmc as labeled evidence.

## 1.0.0
- New kernel skill. Throwaway prototypes that answer a named DESIGN QUESTION — disposable from day one, one command to run, state surfaced; the validated answer graduates, the code dies on a branch. Adapted from Matt Pocock's prototype (MIT) under JAIL evidence rules.