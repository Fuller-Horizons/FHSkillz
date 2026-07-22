# Platform pack feasibility × value review (pre-enhancement input)

*2026-07-19 · Live-researched. Key finding first: **the Agent Skills open standard (Dec 2025) makes "11 separate packs" the wrong architecture.** SKILL.md is now a cross-tool standard with 32+ adopters — OpenAI and Microsoft integrated within 48 hours of publication. One canonical skill set + three delivery channels covers every platform on Jonathan's list; a dedicated pack per platform would create 11 divergent copies of the same disciplines (the exact drift jail-vocab-sync exists to prevent).*

## The matrix

| # | Platform | Mechanism (verified) | Code exec | Feasibility | Value | Verdict |
|---|---|---|:---:|:---:|:---:|---|
| 1 | Claude Code | Native plugin/marketplace (running today) | ✅ | 10 | High | **Canonical home** — already done |
| 2 | Claude desktop (Cowork/chat) | Same plugin | ✅ | 10 | High | Done |
| 3 | claude.ai (web) | Per-skill ZIP upload (Settings → Skills); code exec toggle | ✅* | 8 | Med | **Channel B** — build-zips.sh already exists |
| 4 | OpenCode | Reads `~/.claude/skills` + `.claude/skills` natively; per-agent provider models | ✅ | 10 | High | **Zero work** — plus the only native Tier-A council host |
| 5 | Codex CLI | Agent Skills standard; scans `.agents/skills/`, `~/.agents/skills/` | ✅ | 9 | High | **Channel A** — one-line install.sh extension (symlink to `~/.agents/skills/`) |
| 6 | ChatGPT desktop | "Skills in ChatGPT" — follows the Agent Skills open standard; upload via Skills page | partial | 7 | Med | **Channel B** — plan-gated (GA for Business/Enterprise/Edu; off by default for Enterprise; no desktop↔web sync) |
| 7 | chatgpt.com | Same Skills feature | partial | 7 | Med | Channel B, same caveats |
| 8 | Antigravity | 2026 releases added AGENTS.md + agent-skills setup per multiple guides — **not primary-source verified** | ✅ | 7 (provisional) | Med | Channel A likely via `.agents/skills/`; verify against official docs at rollout |
| 9 | Gemini CLI (gemini-code) | Official skills docs: `.gemini/skills/` + **`.agents/skills/` alias**; `/skills` commands; activation confirmation | ✅ | 9 | Med-High | **Channel A** — covered by the same `~/.agents/skills/` symlink |
| 10 | Gemini online (Gems) | Gems = instruction text only; no SKILL.md, no folders, no code | ❌ | 5 | Low-Med | **Channel C** — the ONLY true adaptation pack: condensed JAIL meta-prompts per skill family (jail-prompt's meta-prompt.md pattern, applied suite-wide) |
| 11 | VS Code (Copilot) | Native agent skills: reads `.github/skills/`, **`.claude/skills/`**, `.agents/skills/` (project) + `~/.claude/skills/`, `~/.agents/skills/` (personal); slash + auto invocation; optional `context: fork` | ✅ | 9 | High | **Zero-to-low work** — reads the Claude paths directly |

\* claude.ai code exec requires the capabilities toggle; skills still install without it (manual fallbacks apply).

## The three channels (instead of 11 packs)

- **Channel A — native SKILL.md** (platforms 1,2,4,5,8,9,11): the canonical repo + extending `scripts/install.sh` to also symlink into `~/.agents/skills/`. One line of maintenance covers five extra tools.
- **Channel B — upload surfaces** (3,6,7): the same skill folders, zipped per skill (`build-zips.sh`) and uploaded. No content divergence.
- **Channel C — instruction-condensed** (10): a "JAIL Gems pack" — one condensed meta-prompt per skill family for surfaces with no skill mechanism. The only genuinely new artifact, and it doubles as the universal fallback for ANY future skill-less surface.

## Consequences for the enhancement contract

1. **Code policy resolves itself**: code-free cores + jail-py companions is exactly what the open standard rewards — tools ignore unknown fields, code-execution availability varies wildly across the 11, and manual fallbacks are what let ONE pack serve all of them. The split architecture is confirmed, not assumed.
2. **Frontmatter stays standard-clean** (name + description + string-map metadata) — already compliant with Codex/Gemini/VS Code/ChatGPT parsing; optional per-tool extensions (e.g. `agents/openai.yaml`) can be added later without breaking anyone.
3. **The dedicated-per-platform-pack idea is REJECTED on value**: 11 copies of 25 skills = 275 files drifting apart. The three-channel model delivers the same reach with one source of truth.

## Sources
- Agent Skills open standard adoption (32+ tools, Codex paths, extension fields): codex.danielvaughan.com 2026-05-05
- Gemini CLI official skills docs (paths, alias, commands): github.com/google-gemini/gemini-cli docs/cli/skills.md
- VS Code agent skills (paths incl. .claude/skills, activation, fork): code.visualstudio.com/docs/agent-customization/agent-skills
- Skills in ChatGPT (standard compliance, upload, plan gating, no-sync caveat): help.openai.com article 20001066
- OpenCode skills + per-agent models: opencode.ai/docs (verified 2026-07-19, see jail-council runbook)
- Antigravity 2026 AGENTS.md/skills reports (provisional): antigravitylab.net, rulesell.com guides

## The locked enhancement contract (6/6 — 100%)

| Input | Decision |
|---|---|
| Target | **Measured behavior**: eval suites run as baseline; failures = the backlog; jail-lab ledgers every change against pass rate |
| Priority | **Even pass, all 25** |
| Evidence | **Run evals + lab loop** (self-contained; no waiting on usage data) |
| Size | **Lean cores, depth on demand** (references added only where evals show need) |
| Rigor | **Stakes-adaptive lanes** in every skill (light lane default, full lane + jail-verify/jail-council escalation when stakes are real) |
| Code | **Split: clean cores + jail-py companions**, confirmed by the cross-platform research above |
| Guardrails | **Per-skill custom defaults + constitutional floor** (Rules 3/5 + quarantine halt un-loosenable) **+ profile knob** (strict/standard/autonomous) above the floor |
