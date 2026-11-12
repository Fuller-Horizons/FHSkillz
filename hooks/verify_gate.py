#!/usr/bin/env python3
"""Stop hook: nudge/block once when completion is claimed without a verdict."""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as C  # noqa: E402

GATE = "verify_gate"
CLAIM = re.compile(
    r"\b(?:all\s+tests?\s+pass(?:ed|ing)?|(?:is|are|it's|now)\s+(?:done|complete[d]?)|"
    r"(?:i'?m|i\s+am|we'?re|all)\s+done|task\s+complete[d]?|work\s+(?:is\s+)?complete[d]?|"
    r"(?:successfully\s+)?shipped|done[.!]|complete[.!]|fully\s+implemented)",
    re.I)
VERDICT = re.compile(r"^\s*(?:[-*>#\s]*)VERIFICATION\s*:", re.I | re.M)
HANDOFF = re.compile(r"JAIL-HANDOFF", re.I)
STATUS = re.compile(r"\bstatus\b", re.I)


def _text(entry):
    msg = entry.get("message") if isinstance(entry.get("message"), dict) else entry
    c = msg.get("content")
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        return "\n".join(b.get("text", "") for b in c
                         if isinstance(b, dict) and b.get("type") == "text"
                         and isinstance(b.get("text"), str))
    return ""


def _role(entry):
    msg = entry.get("message") if isinstance(entry.get("message"), dict) else {}
    return entry.get("type") or entry.get("role") or msg.get("role")


def read_tail(path, n=200):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()[-n:]
    except Exception:
        return []
    out = []
    for ln in lines:
        try:
            e = json.loads(ln)
            if isinstance(e, dict):
                out.append(e)
        except Exception:
            continue
    return out


def main():
    m = C.mode("VERIFY")
    if m == "off":
        return 0
    ev = C.read_event()
    if ev.get("stop_hook_active"):
        return 0
    path = ev.get("transcript_path")
    if not isinstance(path, str) or not path:
        return 0
    entries = read_tail(path)
    last = ""
    for e in reversed(entries):
        if _role(e) == "assistant" and _text(e).strip():
            last = _text(e)
            break
    if not last or not CLAIM.search(last):
        return 0
    tail = "\n".join(_text(e) for e in entries[-40:])
    if VERDICT.search(tail):
        return 0
    if HANDOFF.search(tail) and STATUS.search(tail):
        return 0
    msg = ("FHSkillz verify gate: completion was claimed but no 'VERIFICATION:' "
           "verdict or JAIL-HANDOFF status was found. Run jail-verify (or add "
           "evidence) before finishing.")
    if m == "block":
        C.log_decision(GATE, "completion claim without verdict", "PER-ACTION",
                       "denied", "auto")
        sys.stderr.write(msg + "\n")
        return 2
    C.log_decision(GATE, "completion claim without verdict", "AUTO",
                   "pending", "auto")
    sys.stderr.write("REMINDER: " + msg + "\n")
    return 0


if __name__ == "__main__":
    C.run(main)
