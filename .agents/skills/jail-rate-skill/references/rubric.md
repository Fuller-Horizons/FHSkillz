# Scoring rubric & category definitions

Read this before scoring. Run at **temperature 0.0** and anchor every category to a band first, then refine within it.

## Anchors (apply identically to all 10 categories)

| Band | Meaning |
| :--- | :--- |
| **0.0–2.0** | Absent or broken — the category's concern is not addressed at all. |
| **3.0–4.0** | Implicit/token handling only; no real mechanism. |
| **5.0–6.0** | Present but partial; works in the common case, gaps under stress. |
| **7.0–8.0** | Solid and deliberate; only minor gaps remain. |
| **9.0–10.0** | Best-in-class; explicit, automated, and verifiable. |

Use 0.1 increments only to position *within* a band; do not invent precision the evidence can't support.

## Category definitions
* **Utility & Value** — Frequency of use, impact, and whether it prevents redundant development (build-vs-buy).
* **Clarity of Instructions** — Distinct triage lanes, templates, and visual output examples.
* **Execution Reliability** — Sandbox testing, schema validation, and local config saving (e.g. `prompts.json`).
* **Safety & Guardrails** — Credential safety (least-privilege keys), secret scanners, and prompt-injection defense.
* **Maintainability** — `version` metadata, automated validation scripts, and git commit hooks.
* **Context & Token Efficiency** — Token footprint, context budgets, and summarizer templates.
* **Idempotency & Determinism** — Seed/temperature control and rigid schema execution constraints.
* **Handoff & Collaboration** — Metadata envelopes (dependencies, requirements) for multi-agent chains.
* **Machine-Verifiable Exit Criteria** — Programmatic assertion/test checks instead of human-only review.
* **Client Portability** — Portability reference mapping and editor-agnostic plaintext conventions.
