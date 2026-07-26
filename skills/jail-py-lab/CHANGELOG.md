# Changelog — jail-py-lab

## 1.2.0 — 2026-07-25 (plugin 0.25.0)

- lab-run.py: `measure_from_cmd()` now fails closed on an empty/whitespace-only `--metric-cmd` before `subprocess.run`; SKILL.md documents that `--metric-cmd` executes via the shell (arbitrary code execution) — treat it as trusted, reviewed input only.
- SKILL.md: new Gotchas line on the ledger id race (`entry["id"] = len(entries)` has no locking) — one writer at a time, confirm the prior session's process has exited before a handoff resumes the lab.
- Unified the three ledger readers (`lab-run.py`, `lab-report.py`, `lab-compare.py`) into one shared `scripts/_ledger_io.py` routine so the line-numbered corrupt-line error can't drift further between them; each script's exit-code contract is unchanged — the `_ledger_io` import is wrapped in try/except so a script copied out without its `_ledger_io.py` sibling exits 2 with an actionable message instead of dying with an unhandled `ModuleNotFoundError` (exit 1, which reads as DISCARD).

## 1.1.0 — 2026-07-22 (plugin 0.23.0)

- lab-compare.py: ledger-vs-ledger or span deltas with exit-coded regression check (wired for release gates); SKILL.md notes the toolkit now serves as the FHSkillz suite's own metrics engine (trigger-accuracy ledger).

## 1.0.0
- New skill (JAIL-PY companion, wave 1). Runnable bookkeeping for jail-lab — lab-run.py (measured entries, verdicts) and lab-report.py (trajectory, keep rate, stop condition). Stdlib Python.