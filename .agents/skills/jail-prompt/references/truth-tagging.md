# Epistemic truth-tagging

Load this when a factual or research prompt's output will carry claims a reader
might act on. It turns "keep fact separate from inference" from a hope into a
machine-checkable contract: each material claim gets an epistemic tag, and the
tag is a **structured field a linter validates**, not a word the model sprinkles
in prose. Prose tags are theater: a model labeling its own sentence `Fact` is
pattern-matching the instruction, not inspecting ground truth.

## The three tags

Canonical labels (JAIL Constitution): **Fact**, **Inference**, **Unknown**. The
full six-label set also has User-provided, Estimate, and Judgment for prose
output; the structured claim block below uses the three that a linter can
check against evidence.

| Tag | Means | Allowed when |
|---|---|---|
| `Fact` | Directly supported by a nameable source, or a settled fact. | The claim has at least one real evidence id (see below), or is uncontested common knowledge (`derivation_type: "settled"`). |
| `Inference` | Reasoned from evidence but not directly verified. | A derivation from stated premises; mark the premises. |
| `Unknown` | No reliable basis. **Preferred over a confident guess.** | Always available; rewarded, not penalized. |

Legacy aliases still parse: `Known` / `✓Known` = Fact, `Infer` / `~Infer` =
Inference, `?Unknown` = Unknown. Write the canonical labels in new prompts.

The failure these guard against: a model under helpfulness pressure relabels a
guess as Inference to sound complete, or over-states Fact. Unknown is the
honest output when grounding is missing; never pad it into a confident answer.

## Schema form (not prose)

Emit tagged claims as structured data the consumer can validate and reject if
malformed:

```json
{
  "claims": [
    {"id": "c1", "text": "...", "status": "Fact",      "evidence_count": 2, "source_ids": ["s1","s3"], "derivation_type": "source"},
    {"id": "c2", "text": "...", "status": "Inference", "evidence_count": 1, "source_ids": ["s2"],      "derivation_type": "reasoned"},
    {"id": "c3", "text": "...", "status": "Unknown",   "evidence_count": 0, "source_ids": [],           "derivation_type": "none"}
  ]
}
```

`status` is one of `Fact` / `Inference` / `Unknown`. `derivation_type` records
*how* the claim was reached (`source` / `reasoned` / `settled` / `none`).

## The hard rule

**A `Fact` claim with `evidence_count: 0` or empty `source_ids` is a failure
that triggers a re-query, not a pass.** The whole point is to make an
unevidenced certainty claim impossible to ship silently. The companion
**jail-py-toolkit** skill's `truth-lint.py` enforces this; without it,
enforce it by inspection: reject any `Fact` with empty evidence and no `settled` basis.

## Grounding-conditional (be honest about retrieval)

Evidence ids only mean something if the prompt actually had a way to fetch
sources. So the requirement is **conditional on the prompt's SOURCES line**:

- If `SOURCES` declares a retrieval capability (live web search, a connector, a
  document store), then `Fact` claims **must** carry evidence ids that point at
  retrieved material — run `truth-lint.py --require-evidence`.
- If the prompt is pure model-knowledge with no retrieval, do **not** fake
  evidence ids. Settled facts may be `Fact` with `derivation_type: "settled"`;
  anything contestable drops to `Inference` or `Unknown`. `truth-lint.py` (without
  the flag) still rejects an invalid `status` and a `Fact` claim that *claims*
  source ids it doesn't list.

This keeps the schema from inviting the exact fabrication it's meant to stop —
inventing source ids to satisfy a linter is worse than an honest `Unknown`.

## Lint it

```bash
# via the companion jail-py-toolkit skill
python3 <jail-py-toolkit>/scripts/truth-lint.py claims.json                    # status validity + internal consistency
python3 <jail-py-toolkit>/scripts/truth-lint.py claims.json --require-evidence # also: every Fact needs >=1 evidence id
```

Manual fallback without the toolkit: reject any `Fact` with empty `source_ids` and no `settled` basis, any `status` outside the three labels, and any `evidence_count` that disagrees with the ids listed.

`0` = pass, `1` = a tag violation, `2` = IO/parse error. Fold the relevant
invocation into the prompt's VERIFICATION PLAN as an `[AUTO]` step.
