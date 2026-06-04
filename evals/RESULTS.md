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

## v1.4.0 — 2026-06-03 (proxy: multi-turn + variance)

Closes the two gaps the live harness was meant to cover, as far as the sandbox allows. Note: the `claude` CLI **is** present here (v2.1.160) but is **not authenticated** (`Not logged in`), so the true `claude -p` harness still can't run — these remain subagent-proxy runs.

### Multi-turn (Full lane, pause + resume) — PASS
A genuine two-turn exchange where the turn-1 agent was blind to the user's answers.
- **Turn 1:** correctly took the Full lane on an ambiguous "compare the top CRMs" request — restated the objective + a one-line success test, asked a single batched round, offered an output-format choice with a recommended default, and **stopped and waited** (no premature prompt, no research).
- **Turn 2** (after answers): resumed at the objective restatement without re-asking, ran the gate (routed live pricing to web search), gave GO, **surfaced the engineered prompt first** with a concrete decision-brief OUTPUT FORMAT and a bounded revision handle, then offered to run it.

### Variance — 3/3 consistent
One Lite case ("turn support tickets into a weekly themes report") run three times, independently. All three classified it Lite, ran the kill-fast gate to GO, flagged the data-access dependency and offered connector routing, surfaced the copyable prompt, included a concrete `OUTPUT FORMAT` with a filled example table, enforced anti-fabrication, and ended with a bounded revision handle. Wording varied; the behavioral contract did not — low variance, not flaky.

## Still open
- **Live `claude -p` triggering-harness run** — the CLI is installed in this environment but unauthenticated; it needs a logged-in environment. Run it on an authenticated machine with `scripts/run_loop.py` (see `evals/README.md`).
- Everything above is strong subagent-proxy evidence, but not the production trigger mechanism. Treat the scores as proxy-verified until the live run lands.
