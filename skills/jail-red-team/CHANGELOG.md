# Changelog — jail-red-team

## 1.2.0 — 2026-07-25 (plugin 0.25.0)

- Rules of engagement: attack the artifact never the system (no live probing/exploit code/credentials), ingested material is evidence not instruction (embedded directives reported as injection-vector findings), secrets emitted as `<redacted:kind>`, fail-closed when authorization is unclear — the skill reads adversarial input for a living and had no stated boundary.
- Falsifier loop closed in-skill: every falsifier tags `RUN-NOW` (run it this session, append the result) or `HANDOFF` (owner + jail-lab spec); neither run nor assigned demotes the finding to an open question. `· falsifier-status:` added to the output schema.
- SUCCESS-TEST before emitting (lane named, steelman above findings, severity+basis+handle+falsifier+falsifier-status per finding, verdict in vocabulary, ties break by severity then source order) — unchecked box is fixed, never caveated.
- New behavioral suite `evals/behavioral-0.25/jail-red-team.json` (4 cases): injection surfaced not obeyed, secret redacted, falsifier-status on every finding, stable finding order on rerun.

## 1.1.0 — 2026-07-22 (plugin 0.23.0)

- Falsifier-first rule (every finding names the cheapest disproving test; runnable falsifiers hand to jail-lab) + PRE-MORTEM-LITE lane (~10 min, top 3-5 failure causes with mitigations) as the third effort tier.

## 1.0.0
- New skill (JAIL reasoning-kernel wave 1). Adversarial pressure-testing of plans and claims — steelman first, three lenses, full bias sweep for consequential calls, real objections only.