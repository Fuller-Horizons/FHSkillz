#!/usr/bin/env python3
"""PreCompact hook: one-line nudge to write a jail-handoff baton. Never blocks."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as C  # noqa: E402


def main():
    m = C.mode("HANDOFF")
    if m == "off":
        return 0
    C.read_event()
    C.log_decision("handoff_nudge", "pre-compact nudge", "AUTO", "approved", "auto")
    sys.stderr.write("FHSkillz: context is about to compact - consider running "
                     "jail-handoff to save a baton first.\n")
    return 0


if __name__ == "__main__":
    C.run(main)
