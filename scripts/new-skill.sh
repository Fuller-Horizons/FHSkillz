#!/usr/bin/env bash
# Usage: ./scripts/new-skill.sh my-skill-name
set -euo pipefail
NAME="${1:?Usage: new-skill.sh <skill-name>}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIR="$ROOT/skills/$NAME"
[ -d "$DIR" ] && { echo "Skill '$NAME' already exists."; exit 1; }
mkdir -p "$DIR"
cat > "$DIR/SKILL.md" <<EOF
---
name: $NAME
description: TODO — describe exactly when Claude should use this skill (triggers, inputs, task verbs).
---

# ${NAME//-/ }

## When to use
- TODO

## Instructions
1. TODO
EOF
echo "Created skills/$NAME/SKILL.md"
python3 - "$ROOT/docs/skill-keywords.json" "$NAME" <<'PY'
import json, sys
p, n = sys.argv[1], sys.argv[2]
d = json.load(open(p, encoding="utf-8"))
d["skills"].setdefault(n, {"category": "other", "keywords": ["TODO"], "use_cases": ["TODO"]})
open(p, "w", encoding="utf-8").write(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
PY
echo "Added a TODO keywords entry in docs/skill-keywords.json."
"$ROOT/scripts/sync-marketplace.sh"
echo "Registered in marketplace.json. Edit the description and keywords before committing."
