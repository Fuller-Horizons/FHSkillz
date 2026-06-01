<p align="center">
  <img src="banner.png" alt="Fuller Horizons — Skills Repo" width="640">
</p>

# FHSkillz

**A curated repository of skills, workflows, tools, and resources for premium AI-assisted execution.**

FHSkillz bundles every Fuller Horizons Claude skill into a single installable plugin (`fh-skillz`) and registers the repo as a Claude Code plugin marketplace. One command loads all skills at once; a clone-and-symlink script covers any IDE that reads `~/.claude/skills/`.

> ### ⭐ Just want to use a skill on Claude.ai? (no coding)
> **[Download jail-prompt.zip](https://github.com/Fuller-Horizons/FHSkillz/raw/main/dist/jail-prompt.zip)** and follow the **[3-minute install guide →](Install-on-Claude-ai)**

---

## Install

**Claude Code (loads every skill):**

```
/plugin marketplace add Fuller-Horizons/FHSkillz
/plugin install fh-skillz@fh-skillz
```

Restart Claude Code. Skills activate automatically based on their description — nothing to load by hand.

**Any IDE / Cursor / Codex CLI (skills-directory fallback):**

```
curl -fsSL https://raw.githubusercontent.com/Fuller-Horizons/FHSkillz/main/scripts/install.sh | bash
```

Scope to a single project instead: clone, then `./scripts/install.sh .claude/skills`.

**Refresh after an update:**

```
/plugin marketplace update fh-skillz
```

**Claude.ai (web & desktop app):**

Claude.ai doesn't use plugins or marketplaces — you upload each skill as its own ZIP.

1. Turn on **Settings → Capabilities → Code execution & File creation** (skills won't run without it). Requires a Pro, Max, Team, or Enterprise plan.
2. Zip the skill folder so the folder itself is the **root** of the archive (the ZIP must contain `jail-prompt/SKILL.md`, not a loose `SKILL.md`):

   ```
   cd skills && zip -r jail-prompt.zip jail-prompt
   ```

3. In Claude.ai go to **Customize → Skills → "+" → "+ Create skill"** and upload the ZIP. The skill appears in your list and can be toggled on or off.
4. Test with a few prompts to confirm it triggers.

Uploaded skills are private to your account. On Team/Enterprise plans, share them org-wide through organization settings rather than per-user upload.

---

## Available skills

| Skill | What it does |
|---|---|
| [`jail-prompt`](https://github.com/Fuller-Horizons/FHSkillz/tree/main/skills/jail-prompt) | Pre-flight workflow that turns a vague goal into either a **STOP** (when AI is the wrong tool or the idea is flawed) or an engineered, verifiable, token-efficient prompt that succeeds on the first run. |

---

## How it works

Each skill lives in `skills/<name>/` with a `SKILL.md`. Skills are **model-invoked** — Claude fires them based on the `description` field, not by being installed. The `.claude-plugin/marketplace.json` manifest lists every skill and is the single source of truth for what loads.

```
FHSkillz/
├── .claude-plugin/marketplace.json   # install manifest (lists every skill)
├── skills/<name>/
│   ├── SKILL.md                      # required
│   ├── scripts/                      # optional helpers
│   └── references/                   # optional reference docs
├── scripts/                          # new-skill / sync-marketplace / install
└── CLAUDE.md                         # repo guidance for Claude
```

---

## Add a skill

```
./scripts/new-skill.sh my-skill        # scaffold + auto-register
# edit skills/my-skill/SKILL.md  (write a strong description — it's the trigger)
./scripts/sync-marketplace.sh          # ensure manifest matches folders
git add -A && git commit -m "add my-skill skill" && git push
# then in Claude Code:  /plugin marketplace update fh-skillz
```

The **description is the product** — a weak description means a skill that never triggers. Write it as a router: concrete task verbs, file/input types, and trigger keywords.

---

## Conventions

- Folder name == frontmatter `name`, lowercase-hyphenated (`[a-z0-9-]` only).
- Keep `SKILL.md` lean; push long material into `references/` and link it.
- Bump `plugins[0].version` (semver) on any release that changes skills.
- Keep the repo **public** so `/plugin marketplace add` and the raw `install.sh` URL resolve.
