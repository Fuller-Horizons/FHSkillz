#!/usr/bin/env python3
"""PreToolUse approval gate: ask a human before external-effect actions."""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as C  # noqa: E402

GATE = "approval_gate"

NEVER = [
    ("pipe-to-shell download", r"\b(?:curl|wget)\b[^\n|;]*\|\s*(?:sudo\s+)?(?:ba|z)?sh\b"),
    ("rm -rf on root/home", r"\brm\s+(?:-[a-zA-Z]*\s+)*-[a-zA-Z]*[rR][a-zA-Z]*\s+(?:--no-preserve-root\s+)?(?:/|~|\$HOME)(?:\s|$|/\*)"),
    ("git push --no-verify", r"\bgit\s+push\b[^\n;|&]*--no-verify\b"),
]
ASK = [
    ("git push", r"\bgit\s+push\b"),
    ("npm publish", r"\bnpm\s+publish\b"),
    ("HTTP write request", r"\b(?:curl|wget)\b[^\n]*(?:-X\s*(?:POST|PUT|DELETE|PATCH)\b|--request\s+(?:POST|PUT|DELETE|PATCH)\b|--data\b|--data-\w+\b|\s-d\s|--post-data\b)"),
    ("recursive delete", r"\brm\s+(?:-[a-zA-Z]*\s+)*-[a-zA-Z]*[rR][a-zA-Z]*[a-zA-Z]*\s+\S"),
    ("kubectl delete", r"\bkubectl\s+delete\b"),
    ("DROP TABLE", r"\bDROP\s+TABLE\b"),
]
MCP_VERBS = re.compile(
    r"send|post|publish|delete|create_event|share|transfer|buy", re.I)


def rm_outside_cwd(cmd, cwd):
    """True if an rm -r target is absolute/parent-relative outside cwd."""
    for m in re.finditer(r"\brm\s+((?:-\S+\s+)+)([^\n;&|]+)", cmd):
        if not re.search(r"[rR]", m.group(1)):
            continue
        for t in m.group(2).split():
            t = t.strip("'\"")
            if t.startswith("-"):
                continue
            full = os.path.normpath(os.path.join(cwd, os.path.expanduser(t)))
            if not (full == cwd or full.startswith(cwd.rstrip("/") + "/")):
                return True
    return False


def classify(ev):
    """Return (tier, label) or None."""
    tool = ev.get("tool_name", "")
    ti = ev.get("tool_input") if isinstance(ev.get("tool_input"), dict) else {}
    if tool == "Bash":
        cmd = ti.get("command") if isinstance(ti.get("command"), str) else ""
        for label, rx in NEVER:
            if re.search(rx, cmd, re.I):
                return "NEVER", label
        cwd = ev.get("cwd") if isinstance(ev.get("cwd"), str) else os.getcwd()
        for label, rx in ASK:
            if label == "recursive delete":
                if rm_outside_cwd(cmd, cwd):
                    return "PER-ACTION", "rm -r outside cwd"
                continue
            if re.search(rx, cmd, re.I):
                return "PER-ACTION", label
    elif tool.startswith("mcp__") and MCP_VERBS.search(tool):
        return "PER-ACTION", "MCP external-effect tool"
    return None


def main():
    m = C.mode("APPROVAL")
    if m == "off":
        return 0
    ev = C.read_event()
    hit = classify(ev)
    if not hit:
        return 0
    tier, label = hit
    tool = ev.get("tool_name", "tool")
    action = "%s: %s" % (tool, label)  # never the raw command (may hold secrets)
    deny = tier == "NEVER" and m == "block"
    reason = ("APPROVAL REQUEST - what: %s; tier: %s; blast radius: external or "
              "hard to undo; reversibility: low; safer alternative: dry-run or "
              "do it manually. %s" % (
                  action, tier,
                  "Blocked (NEVER tier)." if deny else "Human approval required."))
    C.log_decision(GATE, action, tier,
                   "denied" if deny else "pending",
                   "auto" if deny else "pending-human")
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny" if deny else "ask",
        "permissionDecisionReason": reason}}))
    return 0


if __name__ == "__main__":
    C.run(main)
