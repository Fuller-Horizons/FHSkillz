# jail-memory

It decides what is worth saving to long-term memory, and what is not.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.4.0.

## What it does

This skill guards your project's memory. Here, memory means small Markdown files that hold facts, decisions, and lessons from past work — not your chat history. Before anything gets saved, it must pass six checks. This stops junk, duplicate entries, and secrets from piling up over time. After a big project ends, it also runs a postmortem — a short review that pulls the lessons worth keeping out of everything that happened — and saves only the parts that pass the gate.

## Use it when

- you want to save a lesson or a decision so your next session can find it — "remember this for later"
- you're about to start work and want to pull up what you already decided
- a project just wrapped, and you want to run a postmortem before you move to the next one
- another skill wants to write to memory, and the write needs a check first

## Don't use it for

- quick notes you only need for this one conversation — that's working context, not memory
- checking raw inbound data before you trust it — use [`jail-quarantine`](../jail-quarantine/) first
- a short note so you can resume tomorrow — use [`jail-handoff`](../jail-handoff/) instead

## What you get

Each saved entry, with its type, where it came from, and what it replaced, if anything. An entry that fails the gate comes back with the reason, not a silent drop.

## Example

**You ask:**

> The Brightleaf intake-bot just shipped. Run the postmortem and save whatever's worth keeping before we move to the next client.

**It produces:**

```
**Candidate 1 — Availity sandbox rate-limits silently (empty 200, no 429).**
1. Provenance ✅ — session 2026-07-25, Brightleaf intake-bot, Jonathan.
2. Worth ✅ — not in Availity's docs, not re-derivable from source control; changes how every future Availity integration handles batch calls.
3. One lesson per entry ✅ — single mechanism, stated with why it matters and how to apply.
4. Dedup ✅ — no existing entry covers Availity's rate-limit behavior. Not a duplicate.
5. Contradiction ✅ — nothing in the index conflicts with this.
6. Safety ✅ — ran jail-py-toolkit's `secret-scan.py` on the drafted entry body: `secret-scan: clean — no secrets detected.` (exit 0).
**Result: PASS → store as new entry.**
...
### Output
- **M0005** · lesson · session 2026-07-25 · Brightleaf intake-bot project · Jonathan · supersedes nothing.
- **M0006** · fact · session 2026-07-25 · Brightleaf intake-bot project · Jonathan · supersedes nothing.
- **M0004** · decision · updated, not superseded — reconfirmed with no change.
- Candidate "project took three weeks" · refused — failed check 2 (Worth): re-derivable from project history, not a lesson.
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
