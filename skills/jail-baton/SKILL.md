---
name: jail-baton
metadata:
  version: 1.1.0
description: >-
  Compact the current session into a BATON — a handoff document a fresh
  agent (or tomorrow's session, or a smaller-context model) can pick up and
  continue from without re-reading everything: state of work, decisions
  with why, live references to artifacts (never duplicated), next actions,
  and which skills to invoke. Use when context is filling up, a session is
  ending mid-work, the user says "hand this off", "save where we are",
  "continue this later/elsewhere", or work must move to another agent/model
  — and OFFER it proactively on context-pressure signals (long session,
  approaching compaction, recall degrading) instead of waiting to be asked.
  Do NOT use for the in-run structured handoff between skills (the
  JAIL-HANDOFF block) or for storing durable lessons (jail-memory).
---

# JAIL-BATON

A session dies; the work shouldn't. The baton carries exactly what a fresh
context needs to continue — no more (bloat defeats the purpose, especially
for small-context models), no less (gaps force re-derivation). Adapted from
Matt Pocock's `handoff` ([mattpocock/skills](https://github.com/mattpocock/skills),
MIT), extended under JAIL rules.

## The baton (write it in this order)
1. **Objective + contract state** — what the work is for, the task
   contract's current form (or where it lives), and what "done" tests as.
2. **State of play** — done (with proof pointers: commits, files, ledger
   entries) · in-flight (exactly where it stopped, mid-step detail) · not
   started. Claims of done carry their artifact reference — a baton is
   evidence, not memory [Constitution Rule 10].
3. **Decisions so far, with why** — each decision one line + its reason;
   superseded paths noted so the next agent doesn't relitigate them.
4. **Reference, don't duplicate.** Anything already captured in an
   artifact — specs, contracts, ledgers, ADRs, commits, issues — is
   pointed at by path/URL, never pasted. Duplication bloats the baton and
   forks the truth.
5. **Live constraints & gotchas** — the non-obvious things this session
   learned the hard way (the environment quirk, the API limit, the client
   preference) that aren't yet in memory or docs.
6. **Next actions** — the first 1–3 concrete steps, sharpest first; plus
   the known decision points ahead.
7. **Suggested skills** — which JAIL skills the next agent should invoke,
   and for what ("jail-research packet exists at X — extend, don't
   restart").
8. **Approval state** — anything awaiting human authorization travels
   explicitly; a baton never launders a pending approval into an assumed
   yes [Rule 5].

## Rules
- **Offer before it's too late.** On context-pressure signals — a long
  session deep in multi-part work, compaction approaching, earlier details
  getting fuzzy — offer the baton unprompted ("want me to write the baton
  now, while state is still sharp?"). A baton written after degradation
  transmits the degradation.
- **State of play uses the orchestrate ledger shape** (node · scope ·
  status · proving artifact), so a baton can seed a jail-orchestrate
  resume directly and an orchestrate ledger can be pointed at instead of
  rewritten — one shape, two carriers.
- **Redact before writing:** secrets, credentials, and protected data
  never enter a baton (jail-quarantine protected classes apply — a baton
  is a file that travels).
- **Tailor to the stated next purpose.** If the user says what the next
  session is for, weight the baton toward it; carry the rest as one-line
  pointers.
- **Size to the recipient.** A frontier-model baton can be a page; a
  small-context recipient gets the 30-line version with references doing
  the heavy lifting. Say which you wrote.
- **Store it where the next session will look** — workspace scratch, the
  project folder, or where the user directs; name it with date + topic.
- Durable lessons discovered while writing → route to **jail-memory**
  (the baton is transport, not storage).

## Related skills
In-run skill-to-skill handoff → the **JAIL-HANDOFF block** (constitution).
Durable cross-project lessons → **jail-memory**. Resuming a multi-agent
run → **jail-orchestrate**'s ledger (the baton points at it, never
replaces it).

## Gotchas
- **The transcript dump.** Pasting the conversation is not compaction —
  it's moving the context problem. Distill; reference.
- **Fork-the-truth duplication.** Copying a spec into the baton means two
  specs by next week. Point, don't paste.
- **Unproven "done."** A baton that says finished without artifact
  pointers transmits optimism, not state.
- **Secret smuggling.** Batons travel further than sessions — redaction
  is not optional.
- **Baton hoarding.** Ten stale batons are noise; the current one
  supersedes, and dead ones get cleaned.
