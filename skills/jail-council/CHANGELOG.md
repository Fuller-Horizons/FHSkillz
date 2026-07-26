# Changelog — jail-council

## 1.2.0 — 2026-07-25 (plugin 0.25.0)

- Step 0 gets a "Brief hygiene" bullet: strip/flag embedded instructions,
  secrets, and credentials in source material before drafting the shared
  brief, and treat the question text as untrusted — the identical brief
  reaches every member/reviewer/chairman context unfiltered, so injected
  content multiplies with panel size instead of staying isolated.
- Review record schema (references/council-protocol.md) gains
  `blindness_attestation`, confirming per member that no cross-member text
  existed at Stage 1 and no un-anonymized model tell survived Stage 3
  anonymization; SKILL.md Step 5 makes its presence in the audit appendix a
  shipping gate. Manual check (no toolkit script exists for this): the
  orchestrator eyeballs each raw answer for self-identifying phrasing
  before anonymizing.
- Gotchas compressed 7→4 (folded Convergence theater into Council theater,
  Tier inflation into Chairman laundering as one honesty bullet); full
  detail, including the dropped Skipping-the-verification-round mode,
  moved to a new Failure modes table in references/council-protocol.md and
  linked from SKILL.md.

## 1.1.0 — 2026-07-22 (plugin 0.23.0)

- MINI-COUNCIL lane: 3 members, one anonymized review round, verification only on disputed load-bearing facts, ~half cost — invariants (blindness, anonymization, error-hunt, evidence-beats-votes, audit appendix) unchanged in both lanes.

## 1.0.0
- New kernel skill: the LLM-council pattern (blind first opinions → anonymized adversarial review → verification round on disputed facts → evidence-decided chairman synthesis with dissent register + audit appendix), re-derived under JAIL discipline from Karpathy's llm-council concept (no code reused; repo declares no license — pattern only, attributed as inspiration).
- **Accuracy-first charter per Jonathan's directive:** cost disclosed, never gating; invoking the skill is the Rule-11 justification. Absorbs the wave-3 `model-validation-council` candidate (its "when is a council justified" logic becomes this skill's framing).
- Independence tiers A (cross-provider — native in OpenCode CLI, verified config in references/opencode-runbook.md) / B (same provider, different models) / C (independent same-model sessions), always declared.