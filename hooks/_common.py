#!/usr/bin/env python3
"""Shared helpers for the opt-in FHSkillz enforcement hooks (stdlib only).

Kept import-light on purpose: in `off` mode a hook only needs os/sys/json.
Never log or print matched secret/PII values anywhere in this package.
"""
import datetime
import json
import os
import sys

MODES = ("off", "warn", "block")
HOOKS_DIR = os.path.dirname(os.path.abspath(__file__))


def plugin_root():
    return os.environ.get("CLAUDE_PLUGIN_ROOT") or os.path.dirname(HOOKS_DIR)


def mode(name):
    """Resolve mode for gate `name` (e.g. 'QUARANTINE'). Default off."""
    for var in ("FHSKILLZ_HOOK_" + name.upper(), "FHSKILLZ_HOOKS"):
        v = os.environ.get(var, "").strip().lower()
        if v in MODES:
            return v
    return "off"


def read_event():
    """Parse hook JSON from stdin. Malformed/empty -> {} (caller exits 0)."""
    try:
        raw = sys.stdin.read()
        ev = json.loads(raw) if raw.strip() else {}
        return ev if isinstance(ev, dict) else {}
    except Exception:
        return {}


def ledger_path():
    base = os.environ.get("CLAUDE_PLUGIN_DATA") or os.path.join(
        os.path.expanduser("~"), ".fhskillz")
    return os.path.join(base, "gate-ledger.jsonl")


def log_decision(gate, action, tier, result, approver="auto", **extra):
    """Append one GATE-RECORD-shaped JSON line. Never raises."""
    try:
        rec = {
            "gate": gate,
            "action": str(action)[:200],
            "tier": tier,
            "approver": approver,
            "ts": datetime.datetime.now(datetime.timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%SZ"),
            "result": result,
        }
        rec.update(extra)
        p = ledger_path()
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "a", encoding="utf-8") as f:
            f.write(json.dumps(rec, sort_keys=True) + "\n")
    except Exception:
        pass


def load_patterns():
    """Import fh_patterns lazily (only when a gate is active)."""
    scripts = os.path.join(plugin_root(), "skills", "jail-py-toolkit", "scripts")
    if scripts not in sys.path:
        sys.path.insert(0, scripts)
    import fh_patterns  # noqa: E402
    return fh_patterns


def run(main):
    """Wrap a hook main so no exception can break the session."""
    try:
        code = main()
    except SystemExit:
        raise
    except Exception:
        code = 0
    sys.exit(code or 0)
