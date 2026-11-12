# FHSkillz enforcement hooks (opt-in)

Four small Python hooks (stdlib only, Python 3.8+) that turn the suite's
disciplines into runtime checks. **Default is off**: unless you opt in, every
hook exits 0 immediately and does nothing.

| Hook | Event / matcher | What it does |
|---|---|---|
| `quarantine_guard.py` | PreToolUse `Write\|Edit\|MultiEdit\|Bash` | Scans file content, edits and commands for secrets and PII using `fh_patterns`. Reports the class only, never the value. |
| `approval_gate.py` | PreToolUse `Bash`, `^mcp__` | Flags external-effect actions (git push, npm publish, curl/wget POST/PUT/DELETE/data, rm -r outside cwd, kubectl delete, DROP TABLE, MCP send/post/publish/delete/create_event/share/transfer/buy). Asks a human to approve. NEVER-tier patterns (`curl ... \| sh`, `rm -rf /`, `git push --no-verify`) are denied in block mode. |
| `verify_gate.py` | Stop | If the last assistant message claims completion and the transcript tail has no `VERIFICATION:` line and no JAIL-HANDOFF with status, it reminds (warn) or blocks once (block). Honors `stop_hook_active`. |
| `handoff_nudge.py` | PreCompact | Prints a one-line nudge to write a jail-handoff baton. Never blocks. |

## Modes

`off` (default) | `warn` | `block`

```
export FHSKILLZ_HOOKS=warn            # enable all gates in warn mode
export FHSKILLZ_HOOK_APPROVAL=block   # per-gate override
```

Per-gate variables: `FHSKILLZ_HOOK_QUARANTINE`, `_APPROVAL`, `_VERIFY`,
`_HANDOFF`. A per-gate value wins over `FHSKILLZ_HOOKS`.

- `warn`: quarantine and verify print to stderr and allow; approval returns `ask`.
- `block`: quarantine and verify exit 2 (verify only once); approval returns `deny` for NEVER-tier, `ask` otherwise.

Malformed hook input never crashes the session (exit 0).

## Ledger

Each decision appends one JSON line to
`${CLAUDE_PLUGIN_DATA}/gate-ledger.jsonl` (or `~/.fhskillz/gate-ledger.jsonl`)
with GATE-RECORD fields: `action`, `tier`, `approver` (`pending-human` or
`auto`), `ts` (ISO-8601 UTC), `result`, plus `gate`. Actions are short labels,
never raw commands or matched values.

```
tail -n 20 ~/.fhskillz/gate-ledger.jsonl | python3 -m json.tool --json-lines
```

## Tests

`python3 -m unittest discover -s hooks/tests -v`
