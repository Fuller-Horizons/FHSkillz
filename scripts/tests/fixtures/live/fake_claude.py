#!/usr/bin/env python3
"""Fake `claude` CLI for run-live-evals tests: emits realistic stream-json."""
import json
import os
import sys

a = sys.argv[1:]
prompt = a[a.index("-p") + 1] if "-p" in a else ""
log = os.environ.get("FAKE_CLAUDE_LOG")
if log:
    with open(log, "a") as f:
        f.write(json.dumps({"argv": a, "cwd": os.getcwd()}) + "\n")
if os.environ.get("FAKE_CLAUDE_FAIL"):
    print(json.dumps({"type": "system", "subtype": "init"}))
    sys.exit(1)
ev = [
    {"type": "system", "subtype": "init", "session_id": "s1"},
    {"type": "assistant", "message": {"content": [
        {"type": "text", "text": "Loading skill."},
        {"type": "tool_use", "id": "t1", "name": "Skill",
         "input": {"skill": "fh-skillz:jail-research"}}]}},
    {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "t1"}]}},
    {"type": "assistant", "message": {"content": [
        {"type": "tool_use", "id": "t2", "name": "WebSearch", "input": {"query": "x"}}]}},
    {"type": "result", "subtype": "success", "is_error": False, "duration_ms": 1234,
     "num_turns": 3, "result": "ANSWER to: " + prompt[:40], "total_cost_usd": 0.0123},
]
for e in ev:
    print(json.dumps(e))
