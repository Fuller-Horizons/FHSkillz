# OpenCode CLI runbook — a true Tier-A (cross-provider) council

Verified against OpenCode's docs (opencode.ai/docs — skills & agents pages,
accessed 2026-07-19). OpenCode is the one CLI in the FHSkillz compatibility
matrix where a cross-provider council is **native**: skills load from the
same folders this plugin installs to, and every agent can be pinned to a
different provider's model.

## 1. Install the skills (already covered by the FHSkillz flow)
OpenCode discovers skills from, among others:
- project: `.opencode/skills/<name>/SKILL.md` and `.claude/skills/<name>/SKILL.md`
- global: `~/.config/opencode/skills/<name>/SKILL.md` and `~/.claude/skills/<name>/SKILL.md`

So `scripts/install.sh` (which symlinks every FHSkillz skill into
`~/.claude/skills/`) makes jail-council and the rest of the plugin visible
to OpenCode with no extra step. Frontmatter requirements match this repo's
format (`name` matching the folder, `description` ≤1024 chars). Agents load
a skill with the native `skill` tool: `skill({ name: "jail-council" })`.

## 2. Seat the council — one subagent per provider
Add to `opencode.json` (project root or global config). Model ids are
`provider/model-id`; use `opencode models` to list what your configured
providers offer, and substitute current model ids — the ones below are
placeholders to edit:

```json
{
  "agent": {
    "council-a": {
      "description": "Council member A — answers the council brief independently",
      "mode": "subagent",
      "model": "anthropic/<current-claude-model>",
      "temperature": 0.2,
      "permission": { "edit": "deny", "bash": "deny" }
    },
    "council-b": {
      "description": "Council member B — answers the council brief independently",
      "mode": "subagent",
      "model": "openai/<current-gpt-model>",
      "temperature": 0.2,
      "permission": { "edit": "deny", "bash": "deny" }
    },
    "council-c": {
      "description": "Council member C — answers the council brief independently",
      "mode": "subagent",
      "model": "google/<current-gemini-model>",
      "temperature": 0.2,
      "permission": { "edit": "deny", "bash": "deny" }
    },
    "council-chair": {
      "description": "Council chairman — synthesizes reviewed council material only",
      "mode": "subagent",
      "model": "anthropic/<strongest-available-model>",
      "temperature": 0.1
    }
  }
}
```

Notes (verified behavior):
- Each agent's `model` may point at a **different provider** — that is what
  makes this Tier A. If `model` is omitted a subagent inherits the invoking
  agent's model (that collapses the council to Tier C — always pin models).
- Markdown agent files work too: `.opencode/agents/council-a.md` with the
  same fields in frontmatter and the member brief as the body — useful for
  baking in the Stage-1 brief permanently.
- `permission: edit/bash deny` keeps members read-only answerers; give the
  verification-round agent `webfetch` access instead.

## 3. Run the protocol
From the primary agent (Build), with the skill loaded:
1. **Stage 1:** dispatch the identical member brief to `@council-a`,
   `@council-b`, `@council-c` (or via the Task tool) — one message each,
   no shared context. Collect the three answers.
2. **Anonymize:** the primary agent relabels answers A/B/C, stripping any
   model tells before review.
3. **Stage 3:** send each member the reviewer brief + all anonymized
   answers; collect the three review records.
4. **Stage 4:** any `unresolved_facts` → dispatch a verification agent
   (webfetch-enabled) per disputed fact.
5. **Stage 5:** send `@council-chair` the chairman brief + all material;
   emit the final output template (tier: **A**, roster = the three model
   ids).

## 4. Degradation ladder
- Only one provider key configured → pin three **different models** from
  that provider (Tier B) — still declare the tier honestly.
- No per-agent models available (other CLIs, claude.ai) → Tier C: three
  independent sessions/subagents, anonymized review, same protocol. The
  discipline survives; the diversity doesn't — say so in the output.

## Gotchas
- **Inherited-model collapse.** Forgetting `model:` on a member silently
  yields a same-model council reported as cross-provider. Check the roster
  in the audit appendix against `opencode.json`.
- **Members with tools.** A member with edit/bash can act instead of
  answer. Council members answer; only the verification agent retrieves.
- **Stale model ids.** Provider catalogs move fast — `opencode models`
  before seating; don't ship hardcoded ids in the config you keep.
- **Context bleed.** Pasting member A's answer into member B's Stage-1
  message breaks blindness — Stage 1 is one brief per agent, nothing else.
