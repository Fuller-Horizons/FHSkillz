<p align="center">
  <img src="banner.png" alt="Fuller Horizons — Skills Repo" width="640">
</p>

# FHSkillz

**A curated repository of skills, workflows, tools, and resources for premium AI-assisted execution.**

FHSkillz bundles every Fuller Horizons Claude skill into a single installable plugin (`fh-skillz`) and registers the repo as a Claude Code plugin marketplace. One command loads all skills at once; a clone-and-symlink script covers any IDE that reads `~/.claude/skills/`.

---

## Install

**Claude Code (loads every skill):**

```
/plugin marketplace add Fuller-Horizons/FHSkillz
/plugin install fh-skillz@fh-skillz
```

Restart Claude Code. Skills activate automatically based on their description — nothing to load by hand.

**Cowork / desktop app (clicks only):** **Settings → Customize → Plugins**, find **fh-skillz**, click **Install** (add the marketplace `Fuller-Horizons/FHSkillz` first if it isn't listed). See the [full guide](Install-on-Claude-ai).

**Any IDE / Cursor / Codex CLI (skills-directory fallback):**

```
curl -fsSL https://raw.githubusercontent.com/Fuller-Horizons/FHSkillz/main/scripts/install.sh | bash
```

Scope to a single project instead: clone, then `./scripts/install.sh .claude/skills`.

**Refresh after an update:**

```
/plugin marketplace update fh-skillz
/plugin update fh-skillz
```

**Single skill on Claude.ai web:** build that skill's ZIP locally with `./scripts/build-zips.sh` and upload it under **Settings → Customize → Skills** (ZIPs aren't committed to the repo — the plugin installer rejects nested ZIPs).

---

## Available skills

**27 skills in three layers** (full table in the [repo README](https://github.com/Fuller-Horizons/FHSkillz#available-skills)):

- **Layer 1 — Reasoning kernel:** jail-prompt · jail-task-contract · jail-research · jail-verify · jail-decide · jail-red-team · jail-council · jail-orchestrate · jail-approval-gate · jail-quarantine · jail-memory · jail-lab (adapted from karpathy/autoresearch, MIT) · jail-diagnose · jail-prototype · jail-baton · jail-wayfind (adapted from mattpocock/skills, MIT) · jail-skill-miner
- **Layer 2 — Workflow:** jail-rate · jail-operationalize · jail-exec-brief · jail-rate-skill · jail-prospect
- **Layer 3 — Domain packs:** jail-strategy-scan · jail-bmc · jail-cpr
- **JAIL-PY companions (code execution):** jail-py-toolkit · jail-py-lab

Governed by the [JAIL Constitution](https://github.com/Fuller-Horizons/FHSkillz/blob/main/docs/JAIL-CONSTITUTION.md) (12 system rules + a structured handoff contract) and routed per the [skill graph](https://github.com/Fuller-Horizons/FHSkillz/blob/main/docs/skill-graph.md). Core skills are instruction-only; runnable helpers live in jail-py-* companions with manual fallbacks.

---

## How it works

Each skill lives in `skills/<name>/` with a `SKILL.md`. Skills are **model-invoked** — Claude fires them based on the `description` field. `.claude-plugin/marketplace.json` lists every skill and is the single source of truth for what loads.

```
FHSkillz/
├── .claude-plugin/marketplace.json   # install manifest (lists every skill)
├── skills/<name>/
│   ├── SKILL.md                      # required
│   ├── references/                   # optional reference docs
│   └── scripts/                      # jail-py-* companions only
├── scripts/                          # repo tooling (new-skill / sync / validate / install)
├── docs/                             # legacy + design documents
└── CLAUDE.md                         # repo guidance for Claude
```

---

## Add a skill

```
./scripts/new-skill.sh my-skill        # scaffold + auto-register
# edit skills/my-skill/SKILL.md  (write a strong description — it's the trigger)
./scripts/sync-marketplace.sh          # ensure manifest matches folders
python3 scripts/validate-skills.py     # frontmatter / name / link checks
git add -A && git commit -m "add my-skill skill" && git push
# then in Claude Code:  /plugin marketplace update fh-skillz
```

The **description is the product** — a weak description means a skill that never triggers. Write it as a router: concrete task verbs, file/input types, and trigger keywords.

---

## Conventions

- Folder name == frontmatter `name`, lowercase-hyphenated (`[a-z0-9-]` only).
- Keep `SKILL.md` lean; push long material into `references/` and link it.
- Core skills are instruction-only; runnable helpers live in `jail-py-*` companion skills.
- Bump `plugins[0].version` (semver) on any release that changes skills.
- Keep the repo **public** so `/plugin marketplace add` and the raw `install.sh` URL resolve.
