#!/usr/bin/env python3
"""PreToolUse guard: scan outgoing tool input for secrets / PII (class only)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as C  # noqa: E402

GATE = "quarantine_guard"


def main():
    m = C.mode("QUARANTINE")
    if m == "off":
        return 0
    ev = C.read_event()
    ti = ev.get("tool_input")
    if not isinstance(ti, dict):
        return 0
    parts = []
    for k in ("content", "new_string", "command"):
        if isinstance(ti.get(k), str):
            parts.append(ti[k])
    for e in ti.get("edits") or []:
        if isinstance(e, dict) and isinstance(e.get("new_string"), str):
            parts.append(e["new_string"])
    text = "\n".join(parts)
    if not text:
        return 0
    hits = C.load_patterns().scan(text, ("secret", "pii"))
    if not hits:
        return 0
    classes = sorted({h["cls"] for h in hits})
    tool = ev.get("tool_name", "tool")
    label = "%s input contains %s" % (tool, "+".join(classes))
    msg = ("FHSkillz quarantine guard: %s (%d finding(s)). Values withheld. "
           "Remove or replace with an env-var reference before retrying."
           % (label, len(hits)))
    if m == "block":
        C.log_decision(GATE, label, "PER-ACTION", "denied", "auto")
        sys.stderr.write(msg + "\n")
        return 2
    C.log_decision(GATE, label, "PER-ACTION", "pending", "pending-human")
    sys.stderr.write("WARNING: " + msg + "\n")
    return 0


if __name__ == "__main__":
    C.run(main)
