# FHSkillz

**Fuller Horizons' Claude skills — bundled as one installable plugin and loadable in a single command.**

FHSkillz packages every Fuller Horizons Claude skill into one plugin (`fh-skillz`) and registers this repo as a Claude Code **plugin marketplace**. One command loads every skill at once; a clone-and-symlink script covers any IDE that reads `~/.claude/skills/`; and each skill is also downloadable as a ZIP for Claude.ai (no coding required).

> **Just want to use a skill on Claude.ai?** No git, no terminal. See the **[3-minute install guide](https://github.com/Fuller-Horizons/FHSkillz/wiki/Install-on-Claude-ai)**.

## Available skills

| Skill | What it does |
|---|---|
| [`jail-prompt`](skills/jail-prompt/) | Pre-flight workflow that turns a vague goal into either a **STOP** (when AI is the wrong tool or the idea is flawed) or an engineered, verifiable, token-efficient prompt that succeeds on the first run. |
| [`company-prospect-research`](skills/company-prospect-research/) | Researches a US private company as a sell-side brokerage / consulting prospect using only free, authoritative sources. Produces a one-page brief with a Likelihood-to-Sell score, a Consulting-Opportunity score, red flags, an outreach hook, and a cited source appendix. |

## Install

**Claude Code (loads every skill):**

```
/plugin marketplace add Fuller-Horizons/FHSkillz
/plugin install fh-skillz@fh-skillz
```

Restart Claude Code. Skills activate automatically based on their `description` — nothing to load by hand. Refresh after an update with `/plugin marketplace update fh-skillz`.

**Any IDE / Cursor / Codex CLI (skills-directory fallback):**

```
curl -fsSL https://raw.githubusercontent.com/Fuller-Horizons/FHSkillz/main/scripts/install.sh | bash
```

Scope to a single project instead: clone, then `./scripts/install.sh .claude/skills`. Re-run anytime to pull latest and re-link.

**Claude.ai (web & desktop, no coding):** download the skill's ZIP from [`dist/`](dist/) and upload it under **Settings → Customize → Skills**. Full walkthrough in the [wiki](https://github.com/Fuller-Horizons/FHSkillz/wiki/Install-on-Claude-ai).

## How it works

Each skill lives in `skills/<name>/` with a `SKILL.md`. Skills are **model-invoked** — Claude fires them based on the `description` field, not by being installed. `.claude-plugin/marketplace.json` lists every skill and is the single source of truth for what loads.

```
FHSkillz/
├── .claude-plugin/marketplace.json   # install manifest (lists every skill)
├── skills/<name>/
│   ├── SKILL.md                      # required — the skill + its trigger description
│   └── references/                   # optional reference docs (progressive disclosure)
├── scripts/                          # new-skill / sync-marketplace / build-zips / install
├── dist/                             # per-skill ZIPs for Claude.ai upload
└── CLAUDE.md                         # repo guidance for Claude when maintaining this repo
```

The marketplace entry uses `strict: false` with an explicit `skills[]` array, so each skill ships as a raw `SKILL.md` folder with **no per-skill `plugin.json`** required.

## Add a skill

```
./scripts/new-skill.sh my-skill        # scaffold skills/my-skill/SKILL.md + auto-register
# edit skills/my-skill/SKILL.md  — write a strong description; it's the trigger
./scripts/sync-marketplace.sh          # ensure the manifest matches the folders
./scripts/build-zips.sh                # refresh dist/ ZIPs for Claude.ai
git add -A && git commit -m "add my-skill skill" && git push
# then in Claude Code:  /plugin marketplace update fh-skillz
```

The **description is the product** — a weak description means a skill that never triggers. Write it as a router: concrete task verbs, file/input types, and trigger keywords.

## Conventions

- One skill = one folder 