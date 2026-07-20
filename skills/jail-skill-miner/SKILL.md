---
name: jail-skill-miner
metadata:
  version: 1.0.0
description: >-
  Mine a codebase, chat history, or document set for plugin-worthy SKILLS —
  reusable disciplines, not app features — then dedupe candidates against the
  installed plugin before authoring anything. Use when the user asks to
  "extract skills from", "mine this repo/history for skills", "what
  disciplines does this codebase enforce", "should this become a skill", or
  when evaluating candidate-skill lists from other tools/models. Do NOT use
  to author an already-approved skill from scratch (follow repo conventions
  directly) or to rate an existing skill (jail-rate-skill).
---

# JAIL-SKILL-MINER

A JAIL skill is a **reusable discipline** — a way of working that transfers
to unrelated projects. Features (recurrence engines, sync jobs, UI views)
are not skills; they get ported as code. This skill finds the disciplines,
kills the duplicates, and authors only what's approved.

## Stage 1 — MINE
Explore the source (docs/CLAUDE.md first, then enforcement surfaces:
policies, gates, validators, schemas, migrations, test invariants — for chat
history: repeated corrections and rituals). Hunt for, in rank order:
1. **Enforced disciplines** — rules the system makes impossible to violate
   (hard policy layers, DB-level gates, fail-closed paths). Highest value:
   the enforcement point is the teachable core.
2. **Repeated patterns** — the same shape appearing ≥2 times independently
   (e.g. quarantine→review→adopt used for embeddings AND contacts AND
   files).
3. **Workflow rituals** — multi-step procedures with checks between steps
   (commit gates, migration discipline, resume ledgers, clarify loops).

**The 4-box filter — a candidate passes ALL or is discarded (show the boxes):**
- [ ] Generalizes beyond this source (would help an unrelated project)
- [ ] Is a discipline/procedure, not a feature (features → a separate
      "port as code" list)
- [ ] Has a **teachable enforcement point** (where/how it's made unbreakable)
- [ ] Its violation causes a **nameable failure** (state the failure)

## Stage 2 — DEDUP (against the installed plugin)
Read every SKILL.md under the plugin's skills/ directory — actually read
them; list which. Classify each surviving candidate:
- **NEW** — nothing covers it.
- **EXTENDS <skill>** — partially covered; propose the delta as an edit to
  that skill, NOT a new one. Never create a skill an edit would cover.
- **DUPLICATE of <skill>** — covered; discard, citing the covering section.

## Stage 3 — REPORT, then stop
One table: candidate (jail-<kebab>) · source evidence (file:line or
message-ref — **opened and confirmed this session, never from memory**) ·
the discipline in one sentence · the failure it prevents · NEW/EXTENDS/
DUPLICATE · rank (universality × severity-of-failure-prevented). Recommend
a top-3 with one reason each. **STOP and wait for selection — authoring
unapproved skills is scope creep with a commit history.**

## Stage 4 — AUTHOR (approved candidates only)
House format, matching the repo's conventions (FHSkillz: frontmatter
name/version/router-description with negative triggers; lean code-free core;
per-step checks that CAN FAIL; Related-skills routing; Gotchas naming how
people fake compliance; JAIL-HANDOFF block). Then register (sync manifest,
version bump) per repo rules, and route to **jail-rate-skill** for the QA score.

## Self-check before reporting
- Every citation opened this session · every candidate shows its 4 boxes ·
  dedup lists the skills actually read · features cleanly separated into
  the port-as-code list.

## Related skills
Score the authored skill → **jail-rate-skill**. Evidence-gather across a big
source → **jail-research** discipline per mining stream. Approval to author
→ the Stage-3 stop is a **jail-approval-gate** PER-ACTION.

## Gotchas
- **Feature romance.** A clever feature feels skill-worthy; the 4-box filter
  says otherwise. Port it as code and move on.
- **Memory citations.** "I recall lib/policy.ts had a gate" — open it or
  drop it. Unverified evidence poisons the whole report.
- **Dedup theater.** Claiming a dedup pass without reading the existing
  skills. List them by name; it's checkable.
- **Authoring past the stop.** Writing all 8 candidates because they were
  fun. Stage 3's stop is the product — selection is the human's call.
- **One mega-skill.** Merging three distinct disciplines into one skill to
  cut count. One job per skill; count pressure is what EXTENDS is for.
