# Changelog — jail-council

## 1.1.0 — 2026-07-22 (plugin 0.23.0)

- MINI-COUNCIL lane: 3 members, one anonymized review round, verification only on disputed load-bearing facts, ~half cost — invariants (blindness, anonymization, error-hunt, evidence-beats-votes, audit appendix) unchanged in both lanes.

## 1.0.0
- New kernel skill: the LLM-council pattern (blind first opinions → anonymized adversarial review → verification round on disputed facts → evidence-decided chairman synthesis with dissent register + audit appendix), re-derived under JAIL discipline from Karpathy's llm-council concept (no code reused; repo declares no license — pattern only, attributed as inspiration).
- **Accuracy-first charter per Jonathan's directive:** cost disclosed, never gating; invoking the skill is the Rule-11 justification. Absorbs the wave-3 `model-validation-council` candidate (its "when is a council justified" logic becomes this skill's framing).
- Independence tiers A (cross-provider — native in OpenCode CLI, verified config in references/opencode-runbook.md) / B (same provider, different models) / C (independent same-model sessions), always declared.