#!/usr/bin/env python3
"""secret-scan.py — flag hardcoded secrets / high-entropy keys in supplied text.

Used by the JAIL-PROMPT Phase 2 "Secure?" check: run it on user-supplied inputs
or files BEFORE generating a prompt, so credentials get replaced with env vars
instead of being baked into the prompt.

Usage:
  secret-scan.py FILE [FILE ...]      # scan files
  secret-scan.py -                    # scan stdin
  echo "..." | secret-scan.py         # (no args) scan stdin

Exit codes: 0 = clean, 1 = secrets found, 2 = usage/IO error.
Stdlib only — no third-party deps, so it runs anywhere Python 3.8+ does.
"""
import sys, re, math, argparse

# (name, compiled pattern). Patterns target well-known credential shapes.
PATTERNS = [
    ("AWS access key id",      re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("OpenAI/Anthropic key",   re.compile(r"\b(?:sk|pk)-[A-Za-z0-9_\-]{20,}\b")),
    ("GitHub token",           re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b")),
    ("Google API key",         re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b")),
    ("Slack token",            re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("Stripe secret key",      re.compile(r"\b[rs]k_(?:live|test)_[A-Za-z0-9]{16,}\b")),
    ("Private key block",      re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----")),
    ("JWT",                    re.compile(r"\beyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\b")),
]

# secret-looking assignments: key/secret/token/password = "longish value"
ASSIGN = re.compile(
    r"""(?ix)\b(api[_-]?key|secret|secret[_-]?key|password|passwd|token|access[_-]?token|client[_-]?secret)\b\s*[:=]\s*['"]([^'"]{8,})['"]"""
)

# Placeholders we should NOT flag (env var refs, obvious dummies).
PLACEHOLDER = re.compile(r"(?i)(your[_-]?|example|placeholder|changeme|xxxx|<[^>]+>|\$\{?[A-Z0-9_]+\}?|os\.environ|getenv|process\.env)")


def shannon(s: str) -> float:
    if not s:
        return 0.0
    counts = {c: s.count(c) for c in set(s)}
    n = len(s)
    return -sum((c / n) * math.log2(c / n) for c in counts.values())


def high_entropy_tokens(line: str):
    """Yield long base64/hex-ish tokens whose entropy suggests a real secret."""
    for tok in re.findall(r"[A-Za-z0-9+/=_\-]{20,}", line):
        if PLACEHOLDER.search(tok):
            continue
        ent = shannon(tok)
        # base64 ~ up to 6 bits/char, hex ~4. Real secrets cluster high.
        if ent >= 4.0 and len(tok) >= 24:
            yield tok, round(ent, 2)


def scan_text(text: str, label: str):
    findings = []
    for i, line in enumerate(text.splitlines(), 1):
        for name, pat in PATTERNS:
            for m in pat.finditer(line):
                findings.append((label, i, name, m.group(0)[:12] + "…"))
        for m in ASSIGN.finditer(line):
            val = m.group(2)
            if not PLACEHOLDER.search(val):
                findings.append((label, i, f"hardcoded {m.group(1).lower()}", val[:6] + "…"))
        for tok, ent in high_entropy_tokens(line):
            # skip if already caught by a named pattern on this line
            if any(f[1] == i for f in findings):
                continue
            findings.append((label, i, f"high-entropy string (H={ent})", tok[:8] + "…"))
    return findings


def main():
    ap = argparse.ArgumentParser(description="Flag hardcoded secrets / high-entropy keys.")
    ap.add_argument("files", nargs="*", help="files to scan; omit or use - for stdin")
    args = ap.parse_args()

    sources = []
    if not args.files or args.files == ["-"]:
        sources.append(("<stdin>", sys.stdin.read()))
    else:
        for f in args.files:
            try:
                with open(f, "r", encoding="utf-8", errors="replace") as fh:
                    sources.append((f, fh.read()))
            except OSError as e:
                print(f"error: cannot read {f}: {e}", file=sys.stderr)
                return 2

    all_findings = []
    for label, text in sources:
        all_findings += scan_text(text, label)

    if not all_findings:
        print("secret-scan: clean — no secrets detected.")
        return 0

    print(f"secret-scan: {len(all_findings)} potential secret(s) found:\n", file=sys.stderr)
    for label, line, name, sample in all_findings:
        print(f"  {label}:{line}: {name} -> {sample}", file=sys.stderr)
    print("\nReplace these with environment variables (e.g. os.environ['API_KEY']) "
          "and use a restricted, read-only credential before generating the prompt.",
          file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
