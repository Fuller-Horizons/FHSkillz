# Evidence standards — sourcing, citation, and confidence rules

Load this at Step 3, before gathering evidence. These rules make "empirical,
cited" mean something: what counts as evidence, how to cite it, and how
evidence depth sets confidence. (Alignment note: the tiering mirrors
jail-prompt's `references/sources.md` and the labeling mirrors
company-prospect-research — one house standard, three skills.)

## Source tiers (prefer higher; drop lower only when forced)
1. **Primary / official** — the entity that owns the fact: filings, official
   docs, spec sheets, changelogs, court/regulator records, the original
   dataset/paper. Best for *what a thing is, costs, or officially states*.
2. **Independent measurement** — lab benchmarks, teardowns, audits,
   peer-reviewed studies, CVE/NVD entries, certification bodies. Best for
   *how it actually performs*. This is the workhorse tier for ratings.
3. **Reputable secondary** — established outlets/reviewers with editorial
   standards (major press, Wirecutter/RTINGS-class, respected trade pubs).
   Good for synthesis; check what *their* source was.
4. **Crowd** — app-store reviews, Reddit, forums, star ratings. Valid for
   *pattern evidence only*: recurring themes across many independent voices
   (cite the pattern and where you saw it), never a single anecdote as Fact.
5. **Not evidence** — vendor marketing claims, SEO listicles, undated blogs,
   AI-generated pages without sourcing. A marketing claim may be *reported* as
   the vendor's claim, clearly attributed — it cannot back a score by itself.

## Citation format
Every citation: **source name · what it evidenced · URL · date accessed.**
In the scorecard's Evidence column use compact numbered refs (`[1]`, `[2]`)
that resolve in the Sources list. No citation → the claim is **Judgment** and
is labeled so. Never invent a source, URL, or figure; a fabricated citation is
worse than an honest gap.

## Claim labels
- **Fact** — directly supported by a Tier 1–2 source (or a Tier 3 source whose
  underlying source you checked).
- **Inference** — reasoned from cited evidence; the reasoning is stated.
- **Judgment** — expert read with no direct source; allowed, but labeled, and
  it caps that dimension's confidence at Low.

## Recency
Date every time-sensitive citation and judge staleness against the subject's
cadence: software/SaaS evidence goes stale in ~12 months, hardware over a
model generation, businesses in ~24 months, published research when superseded.
Stale evidence may still be cited — flagged as stale, with confidence lowered.

## Minimums per dimension
- Public subject: aim for **≥ 2 independent pieces of evidence per dimension**,
  at least one Tier 1–2. One source = say so; zero = the score rests on
  Judgment and is labeled + confidence-capped.
- Cross-check any consequential claim (a critical flaw, a headline number)
  across 2+ independent sources before it moves a score.
- Conflicting evidence: cite both sides, score to the better-evidenced side,
  note the conflict in "Why this score."

## Confidence (per dimension → overall)
- **High** — 2+ independent Tier 1–2 sources agree; recent; direct inspection
  where applicable.
- **Medium** — single strong source, or multiple Tier 3; minor staleness.
- **Low** — Judgment-only, crowd-only, stale, or conflicting evidence.
Overall confidence = the weighted center of dimension confidences; state the
single action that would most raise it (e.g. "an independent security audit
would move Security from Low to High").

## Private/internal subjects
External search still runs for the *category* (comparables, benchmarks for the
class) even when the subject itself is private — you can't judge "good for its
kind" without knowing the kind. The subject-specific evidence then comes from
supplied materials, marked as such, and the Sources list states the split.
