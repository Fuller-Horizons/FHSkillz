# jail-orchestrate

It runs a long or multi-part job as one coordinated system. It only marks a step done when a real result proves it.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.3.0.

## What it does

First, it checks if the job needs more than one agent. Splitting work across agents costs time and focus, so it must earn that cost back. If the job does split, each agent gets one clear job and only the facts that job needs. Either way, the skill keeps a ledger. A ledger is a running list of steps. Each step gets a status and a piece of proof — a file, a log, or a test result — that shows the step is really done. A step only counts as done when that proof exists. This makes the job resumable. You can pick it back up from the last proven step. You never restart from a guess.

## Use it when

- you say "fan this out," "use subagents," or "divide this up."
- a build spans many sessions and you need to resume it without losing your place.
- several agents run at once and you need to catch duplicate work before it ships.

## Don't use it for

- short jobs that fit in one sitting. Just do the work.
- planning how humans run a process, not agents — use [`jail-plan`](../jail-plan/) instead.
- the final independent check on finished work — use [`jail-verify`](../jail-verify/) instead.

## What you get

You get a short decision: one agent, or a squad. You get a step-by-step ledger with a status and proof for each step. You get one merged result, never a stack of separate agent replies stapled together.

## Example

**You ask:**

> We're cutting a release today. Before I keep going, run one pass to check the repo is clean. The skill checks still pass. The plugin file still lists every skill. Only doc files changed. Keep a resume ledger in case this gets cut off.

**It produces:**

```
Gate 1 — Is delegation worth it?
- Independent streams? No — all three checks read the same repo snapshot; they aren't separable workstreams.
- Isolation needed? No — these are mechanical checks, not adversarial review; no verifier-vs-worker split applies here.
- Exceeds one context window? No — three small checks against a 26-skill repo.

Gate 1 says no. This runs SOLO: one agent, sequential, same ledger discipline, no subagents spawned.

Dependency graph (3 nodes, sequential):
1. N1 — frontmatter + link-rot validation (scripts/validate-skills.py)
2. N2 — marketplace.json <-> skills/ folder parity
3. N3 — working-tree scope audit (confirm nothing outside README.md changed)
...
NODE N1 | STATUS: verified | ARTIFACT: `python3 scripts/validate-skills.py` — exit 0, final line "[+] Validation Succeeded! All checks passed." (36 files scanned)
...
NODE N2 | STATUS: verified | ARTIFACT: inline parity check — "marketplace count: 26", "folder count: 26", "match: True", "folders not in marketplace: set()", "marketplace entries with no folder: set()"
...
NODE N3 | STATUS: verified | ARTIFACT: `git status --short` — 13 modified paths, 13/13 match `skills/*/README.md`, 0 outside that pattern
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
