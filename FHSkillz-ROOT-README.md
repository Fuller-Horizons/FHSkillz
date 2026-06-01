# FHSkillz — Fuller Horizons Skill Directory

A collection of Claude skills built by Fuller Horizons. Each skill is a self-contained folder (a `SKILL.md` plus optional `references/` and `evals/`) that Claude can load on demand in **Cowork** or **Claude Code**.

## Skills

| Skill | Version | What it does |
|---|---|---|
| [JAIL-PROMPT](JAIL-PROMPT/) | 0.9.0 | Turns a vague goal into either a STOP (wrong tool / flawed idea) or an engineered, verifiable, token-efficient prompt — with a viability gate, discernment over agreeableness, and prompt-chaining for big tasks. |

## Installing a skill

**Cowork:** download the skill's packaged `.skill` file from its [Releases](https://github.com/Fuller-Horizons/FHSkillz/releases) and click **Save skill**.

**Claude Code / manual:** copy the skill's folder (e.g. `JAIL-PROMPT/`) into your skills directory — `~/.claude/skills/` on macOS/Linux or `%USERPROFILE%\.claude\skills\` on Windows. Skills auto-trigger from their descriptions; no command needed.

## Repository layout

```
FHSkillz/
├── README.md           # this file
├── LICENSE             # MIT
└── JAIL-PROMPT/        # one folder per skill
    ├── SKILL.md
    ├── README.md
    ├── CHANGELOG.md
    ├── references/
    └── evals/
```

## Contributing / adding a skill

New skills are built and validated with the **skill-creator** eval loop (draft → run test cases → independent grading → iterate). Each skill ships with its own `evals/` suite and a `CHANGELOG.md`; see a skill's `evals/README.md` for how to re-run its validation.

## License

[MIT](LICENSE) © 2026 Jonathan R. Fuller / Fuller Horizons.
