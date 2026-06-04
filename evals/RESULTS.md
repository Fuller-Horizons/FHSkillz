# Eval results — jail-prompt

Method note: these are **subagent-proxy** runs (independent judge/grader subagents on the session model), not the live `claude -p` triggering harness. The proxy is a strong signal but not the gold standard — the CLI harness + a true multi-turn exercise remain the open items (see README). Each run uses fresh, independent subagents so nothing grades its own output.

## v1.2.0 — 2026-06-03 (proxy)

### Triggering — 20/20
Two independent judge subagents classified all 20 `trigger_evals.json` queries from the skill **description only** (labels hidden).

- Judge A: 20/20 match to labels.
- Judge B: 20/20 match to labels.
- Inter-judge agreement: 20/20.
- Should-trigger: 10/10 fired. Near-misses: 0/10 false-fires.

The near-miss set held the realistic traps: a finished prompt to run verbatim (#11, #18), plain factual/lookup (#12, #17), verbatim translation (#13), concrete debugging (#14), typo-only proofread (#15), direct creative (#16), theory curiosity (#19), and a direct "summarize the PDF" execution (#20). None tripped the trigger.

### Behavioral — 4/4 cases, all assertions PASS
Each prompt was run against the actual v1.2.0 `SKILL.md` by an executor subagent, then graded by a separate, harsh, independent grader.

| Case | Behavior tested | Verdict |
|---|---|---|
| `lite-lane-one-reply` (new) | Lite lane: assumptions + verdict + draft in one reply; routes to GitHub connector (read-only) | PASS (A1–A4) |
| `connector-routing-live-data` (new) | Routes to live web search; tiering + recency + cross-check; anti-fabrication; explicit no-browse-no-run | PASS (A1–A4) |
| `stop-case-wrong-tool` | STOP on deterministic arithmetic; deterministic alternative + multiple-choice next step | PASS (A1–A4) |
| `discernment-bad-premise` | Flags flawed premise (deliverability/CAN-SPAM/GDPR), declines literal ask, reframes to win-back | PASS (A1–A4) |

The two new v1.2.0 behaviors (Lite lane, connector routing) both validated on first run.

## Still open (carried since 0.9.0)
- Live `claude -p` triggering-harness run (replaces the proxy).
- A genuine multi-turn interactive exercise (these runs were single-turn).
