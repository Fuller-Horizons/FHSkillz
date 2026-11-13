# 0.29 round 2: jail-questionnaire 1.0.1 vs no skill (2026-11-13)

HVAC discovery intake, Sonnet 5.5, two blind Sonnet graders.

| | No skill | jail-questionnaire 1.0.1 |
|---|---|---|
| Assertions | 1/7 (14%) | 6/7 (86%) |

- No skill: only described a saved file with a 20-item check plus more; no questionnaire text, no closing question.
- 1.0.1: full questionnaire shown in the reply, 15 numbered questions, plain English, nothing sensitive asked.
- One disagreement: g1 counted the closing "anything else?" catch-all as a 16th question (over the 15 cap); g2 did not. The catch-all is the template's optional closing item, so the orchestrator resolved it as a pass (not blind: labels were already unblinded when this was reviewed).

Combined with round 1 (1/2 vs 0/2, 92% vs 58% assertions): KEEP. Shipped in 0.29.0.
