# Epistemic truth-tagging

Load this when a factual or research prompt's output will carry claims a reader
might act on. It turns "keep fact separate from inference" from a hope into a
machine-checkable contract: each material claim gets an epistemic tag, and the
tag is a **structured field a linter validates**, not a word the model sprinkles
in prose. Prose tags are theater — a model labeling its own sentence `✓Known` is
pattern-matching the instruction, not inspecting ground truth.

## The three tags

| Tag | Means | Allowed when |
|---|---|---|
| `✓Known` | Directly supported by a nameable source, or a settled fact. | The claim has ≥1 real evidence id (see below), or is uncontested common knowledge. |
| `~Infer` | Reasoned from evidence but not directly verified. | A derivation from stated premises; mark the premises. |
| `?Unknown` | No reliable basis. **Preferred over a confident guess.** | Always available; rewarded, not penalized. |

The failure these guard against: a model under helpfulness pressure relabels a
guess as `~Infer` to sound complete, or over-states `✓Known`. `?Unknown` is the
honest output when grounding is missing — never pad it into a confident answer.

## Schema form (not prose)

Emit tagged claims as structured data the consumer can validate and reject if
malformed:

```json
{
  "claims": [
    {"id": "c1", "text": "...", "status": "Known",   "evidence_count": 2, "source_ids": ["s1","s3"], "derivation_type": "source"},
    {"id": "c2", "text": "...", "status": "Infer",   "evidence_count": 1, "source_ids": ["s2"],      "derivation_type": "reasoned"},
    {"id": "c3", "text": "...", "status": "Unknown", "evidence_count": 0, "source_ids": [],           "derivation_type": "none"}
  ]
}
```

`status` is one of `Known` / `Infer` / `Unknown` (the `✓ ~ ?` glyphs are the
prose shorthand; the field uses the bare word). `derivation_type` records *how*
the claim was reached (`source` / `reasoned` / `none`).

## The hard rule

**A `Known` claim with `evidence_count: 0` or empty `source_ids` is a failure
that triggers a re-query, not a pass.** The whole point is to make an
unevidenced certainty claim impossible to ship silently. `scripts/truth-lint.py`
enforces this.

## Grounding-conditional (be honest about retrieval)

Evidence ids only mean something if the prompt actually had a way to fetch
sources. So the requirement is **conditional on the prompt's SOURCES line**:

- If `SOURCES` declares a retrieval capability (live web search, a connector, a
  document store), then `Known` claims **must** carry evidence ids that point at
  retrieved material — run `truth-lint.py --require-evidence`.
- If the prompt is pure model-knowledge with no retrieval, do **not** fake
  evidence ids. Settled facts may be `Known` with `derivation_type: "settled"`;
  anything contestable drops to `Infer` or `Unknown`. `truth-lint.py` (without
  the flag) still rejects an invalid `status` and a `Known` claim that *claims*
  source ids it doesn't list.

This keeps the schema from inviting the exact fabrication it's meant to stop —
inventing source ids to satisfy a linter is worse than an honest `Unknown`.

## Lint it

```bash
python3 scripts/truth-lint.py claims.json                      # status validity + internal consistency
python3 scripts/truth-lint.py claims.json --require-evidence   # also: every Known needs >=1 evidence id
```

`0` = pass, `1` = a tag violation, `2` = IO/parse error. Fold the relevant
invocation into the prompt's VERIFICATION PLAN as an `[AUTO]` step.
