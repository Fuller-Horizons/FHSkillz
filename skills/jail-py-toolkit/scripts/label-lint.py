#!/usr/bin/env python3
"""label-lint.py — enforce the canonical claim-label set (JAIL Constitution).

A claim label is a bracketed `[Label]` or bold `**Label**` / `**Label:**` token
whose text (<= 4 words) contains claim vocabulary (fact, known, infer*, judg*,
verified, missing evidence, estimate, assumption, unknown, speculation,
hypothesis, validated, confirmed, user-provided ...). Every such token must be
exactly one of:
  canonical: Fact, User-provided, Inference, Estimate, Judgment, Assumption, Unknown
  declared domain mapping: VALIDATED, HYPOTHESIS (jail-bmc)
Anything else (Known, Analyst Judgment, Missing Evidence, Verified fact,
Source-Backed Inference, ...) fails. Fenced code blocks, markdown links
`[text](url)` and numeric citations `[n]` are ignored.

--require-evidence : every `Fact` label on a line must have a `[n]` citation
                     on the same line.

Usage:  label-lint.py [--require-evidence] FILE [FILE ...]
Exit codes: 0 = pass, 1 = violations, 2 = usage/IO error.
"""
import re
import sys
import argparse

CANON = {"fact", "user-provided", "inference", "estimate", "judgment",
         "assumption", "unknown"}
DOMAIN = {"validated", "hypothesis"}
# Only these legacy / competing label spellings are flagged. Ordinary bold
# phrases that merely contain a claim word ("Fact bias", "When evidence is
# thin") are headings, not labels, and are ignored (0.27 false-positive fix).
LEGACY = {"known", "✓known", "infer", "~infer", "?unknown", "inferred",
          "source-backed inference", "analyst judgment", "missing evidence",
          "verified fact", "expert judgment", "speculation", "opinion",
          "verified", "user provided"}
VOCAB = re.compile(
    r"(?i)\b(fact|known|infer|inferred|inference|infers|judg(?:e)?ment|"
    r"verified|evidence|estimate|assumption|unknown|speculation|hypothesis|"
    r"validated|confirmed|unverified|opinion|user[- ]provided)\b")
TOKEN = re.compile(r"\[([^\[\]\n]{1,40})\](?![(\[])|\*\*([^*\n]{1,40})\*\*")
CITE = re.compile(r"\[\d+\]")


def norm(s):
    s = s.strip().rstrip(":").strip()
    return re.sub(r"\s+", " ", s)


def lint_text(text, require_evidence=False):
    errs, in_code = [], False
    for n, line in enumerate(text.splitlines(), 1):
        if re.match(r"^\s*```", line):
            in_code = not in_code
            continue
        if in_code:
            continue
        for m in TOKEN.finditer(line):
            raw = m.group(1) if m.group(1) is not None else m.group(2)
            if re.fullmatch(r"\d+|x|X|\s*", raw):
                continue
            label = norm(raw)
            if len(label.split()) > 4 or not VOCAB.search(label):
                continue
            key = label.lower().replace(" ", "-") if label.lower() == "user provided" else label.lower()
            if key in CANON or key in DOMAIN:
                if key == "fact" and require_evidence and not CITE.search(line):
                    errs.append((n, "Fact label without a [n] citation"))
                continue
            if key not in LEGACY:
                continue
            errs.append((n, f"non-canonical label: {label!r} "
                            "(use Fact, User-provided, Inference, Estimate, Judgment, "
                            "Assumption, Unknown)"))
    return errs


def main():
    ap = argparse.ArgumentParser(description="Lint claim labels.")
    ap.add_argument("files", nargs="+")
    ap.add_argument("--require-evidence", action="store_true")
    args = ap.parse_args()
    bad = False
    for f in args.files:
        try:
            with open(f, "r", encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except OSError as e:
            print(f"error: cannot read {f}: {e}", file=sys.stderr)
            return 2
        errs = lint_text(text, args.require_evidence)
        for n, e in errs:
            print(f"{f}:{n}: {e}", file=sys.stderr)
        if errs:
            bad = True
        else:
            print(f"label-lint: {f}: OK")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
