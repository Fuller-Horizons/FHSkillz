# Evidence: sources and claim labels

Load this when the prompt involves research or factual claims. Part 1: which sources, how recent, how to cross-check. Part 2: tagging each claim Fact / Inference / Unknown so a checker can reject an unsupported one.


## Source tiering & verification reference

Load this when the engineered prompt involves research, factual claims, pricing, statistics, current events, or anything a reader could act on. It is the detailed version of the **Authority** rule in SKILL.md — pull it in when grounding actually matters, skip it for non-factual tasks.

### Source tiers (prefer higher tiers; drop to lower only when forced)

1. **Primary / official** — the entity that owns the fact. Vendor pricing pages, official docs/API references, company filings (10-K, 10-Q, 8-K), government data (.gov), standards bodies, the original dataset or paper. Highest trust for *what a thing is, costs, or officially states*.
2. **Peer-reviewed / expert-reviewed** — journal articles, systematic reviews, reputable standards and technical specs. Highest trust for *empirical claims and mechanisms*.
3. **Reputable secondary** — established outlets and analysts with editorial standards and a correction policy (major newspapers, Reuters/AP, well-known domain publications, Wirecutter/RTINGS-class reviewers). Good for synthesis and context; verify their underlying source where it matters.
4. **Crowd / community** — Reddit, forums, Stack Overflow, star ratings, social posts. Use only for *leads, sentiment, and what to go verify* — never as the sole support for a consequential claim.
5. **Avoid as authority** — SEO listicles, content farms, undated blog posts, vendor marketing copy presented as neutral, and AI-generated pages with no sourcing.

### Recency

State an explicit freshness window appropriate to the domain and reject anything older:
- Prices, availability, rankings, "best X" → **within ~30 days** (often less).
- Software/API behavior, versions → current major version; check release notes/changelog dates.
- Laws, regulations, policies → confirm still in force; check effective/repeal dates.
- Scientific consensus → prefer recent reviews, but a foundational older paper can still be primary.
Always show the date of each consequential source so staleness is visible.

### Cross-checking

- Cross-check any **consequential** claim (one the reader will spend money or make a decision on) against **2+ independent** sources — independent meaning not republishing each other.
- If sources conflict, say so and present the disagreement rather than silently picking one.
- Separate **fact** (sourced, datable) from **inference** (your reasoning on top of it). Label inference as inference.

### Honesty rules (non-negotiable)

- Never claim a source is "verified" you didn't actually check.
- Never state a confidence number you haven't earned.
- If a claim can't be grounded, say "unverified" and flag it — an honest gap beats a confident fabrication.
- No invented statistics, quotes, citations, or URLs. If you're not sure a source exists, don't cite it.

## Epistemic truth-tagging

Load this when a factual or research prompt's output will carry claims a reader
might act on. It turns "keep fact separate from inference" from a hope into a
machine-checkable contract: each material claim gets an epistemic tag, and the
tag is a **structured field a linter validates**, not a word the model sprinkles
in prose. Prose tags are theater: a model labeling its own sentence `Fact` is
pattern-matching the instruction, not inspecting ground truth.

### The three tags

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

### Schema form (not prose)

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

### The hard rule

**A `Fact` claim with `evidence_count: 0` or empty `source_ids` is a failure
that triggers a re-query, not a pass.** The whole point is to make an
unevidenced certainty claim impossible to ship silently. The companion
**jail-py-toolkit** skill's `truth-lint.py` enforces this; without it,
enforce it by inspection: reject any `Fact` with empty evidence and no `settled` basis.

### Grounding-conditional (be honest about retrieval)

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

### Lint it

```bash
## via the companion jail-py-toolkit skill
python3 <jail-py-toolkit>/scripts/truth-lint.py claims.json                    # status validity + internal consistency
python3 <jail-py-toolkit>/scripts/truth-lint.py claims.json --require-evidence # also: every Fact needs >=1 evidence id
```

Manual fallback without the toolkit: reject any `Fact` with empty `source_ids` and no `settled` basis, any `status` outside the three labels, and any `evidence_count` that disagrees with the ids listed.

`0` = pass, `1` = a tag violation, `2` = IO/parse error. Fold the relevant
invocation into the prompt's VERIFICATION PLAN as an `[AUTO]` step.
