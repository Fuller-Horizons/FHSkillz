---
name: demo-skill
metadata:
  version: 1.0.0
model: opus
description: >-
  A fixture skill used to test host projection. Use when testing.
argument-hint: "[thing]"
allowed-tools: Read, Bash
---

# Demo

Run it:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tool.py --in ${CLAUDE_SKILL_DIR}/references/r.md $ARGUMENTS
```

Prose mention of ${CLAUDE_PLUGIN_ROOT} stays untouched here.

```python
print("${CLAUDE_SKILL_DIR}")
```
