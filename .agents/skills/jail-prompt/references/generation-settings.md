# Per-mode generation settings

Load this when the prompt will run somewhere you control inference parameters (an
API, SDK, or playground). The Phase 3 prompt shapes behavior through *words*;
these knobs shape the same behavior through *configuration* — the layer beneath
the prompt.

## The principle

**A control you set as a parameter beats the same control asked for in a prompt**
— the model can't talk its way around a limit it runs under. A factual prompt
pinned at `temperature 0` literally can't wander as far as one merely *told* not
to. Push controls down to this layer wherever the platform allows; where it
doesn't, the prompt block is the fallback.

This connects to the epistemic mode declared in Phase 1: each mode wants a
different configuration.

## Recommended settings by mode

| Mode | Temperature | Top-P | Presence pen. | Response format | Seed | Observability |
|---|---|---|---|---|---|---|
| **Factual** | 0.0–0.2 | 0.8 | ~0 | Strict JSON schema | Fixed | Logprobs on |
| **Research** | 0.2–0.4 | 0.9 | ~0.2 | JSON + tool calls | Fixed | Logprobs + retrieval tool |
| **Brainstorm** | 0.7–1.0 | 0.95 | 0.5–0.7 | Prose OK | None | — (tag claims `Infer`) |
| **Critique** | 0.3–0.5 | 0.9 | 0.3–0.5 | Structured | Fixed | Route to a *different* model |

Tune temperature *or* top-p, not both. Keep presence penalty near 0 in Factual
mode — rewarding novelty over accuracy *increases* hallucination; it's only
useful in the contrary-case step, to push for genuinely different ground.

## What each knob buys the protocol

- **Temperature / top-p** → the config form of "mode behavior, no drift."
- **Response format (JSON / schema)** → the single most important knob: it's what
  turns the truth-tag schema (see [truth-tagging.md](truth-tagging.md)) from
  free-text theater into something the client rejects when malformed.
- **Seed** → reproducible audits: change one prompt rule, fix the seed, and see
  whether *that* change — not random sampling — moved the result. Serves the
  determinism self-test in Phase 3.
- **Logprobs** → an external check on self-reported tags: if a claim is tagged
  `Known` but token confidence is low, flag the mismatch.
- **Tools / function calling** → how an `[AUTO]` verification step actually
  *runs* (retrieval, a second-model cross-check) instead of sitting as text.

## Availability caveat (verify against current docs)

Provider support varies and changes — confirm before relying on any of these:

- **OpenAI, xAI** — widest set incl. seed, logprobs, logit bias, structured output.
- **Anthropic** — temperature, top-p, top-k, stop, tools/structured output;
  historically no seed, no penalties, no logit bias.
- **Google Gemini** — temperature, top-p/k, response schema, tools; no seed/penalties.
- **Perplexity (Sonar)** — temperature, top-p/k, penalties, plus native search
  grounding (lean on the claim-to-source audit, not the knobs).
- **Consumer web chat apps (all vendors)** — expose essentially none of these;
  there the Phase 3 prompt block and [meta-prompt.md](meta-prompt.md) are your
  only control surface.
