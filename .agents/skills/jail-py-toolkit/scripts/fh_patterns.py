#!/usr/bin/env python3
"""fh_patterns.py — single source of detection patterns (secrets + PII).

Imported by secret-scan.py, pii-scan.py and the F3 hooks (which do
sys.path.insert to this folder). Stdlib only, Python 3.8+.

Public API:
  scan(text, classes=("secret", "pii")) -> list of dict(line=int, cls=str, kind=str)

SAFETY CONTRACT: results never contain the matched value — only the 1-based
line number, the class ("secret" | "pii") and a kind label. Nothing here
prints; callers must not re-derive values either.
"""
import re
import math

# ---------------------------------------------------------------- secrets
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


def shannon(s):
    if not s:
        return 0.0
    counts = {c: s.count(c) for c in set(s)}
    n = len(s)
    return -sum((c / n) * math.log2(c / n) for c in counts.values())


def _has_high_entropy_token(line):
    for tok in re.findall(r"[A-Za-z0-9+/=_\-]{20,}", line):
        if PLACEHOLDER.search(tok):
            continue
        if shannon(tok) >= 4.0 and len(tok) >= 24:
            return True
    return False


def _scan_secrets_line(line):
    kinds = []
    for name, pat in PATTERNS:
        if pat.search(line):
            kinds.append(name)
    for m in ASSIGN.finditer(line):
        if not PLACEHOLDER.search(m.group(2)):
            kinds.append("hardcoded " + m.group(1).lower())
    if not kinds and _has_high_entropy_token(line):
        kinds.append("high-entropy string")
    return kinds


# -------------------------------------------------------------------- PII
SSN_RE = re.compile(r"(?<![\d-])(\d{3})-(\d{2})-(\d{4})(?![\d-])")
CARD_RE = re.compile(r"(?<![\d-])\d(?:[ -]?\d){12,18}(?![\d-])")
ABA_RE = re.compile(r"(?<![\d-])\d{9}(?![\d-])")
DOB_RE = re.compile(
    r"(?i)\b(?:dob|d\.o\.b\.?|date\s+of\s+birth|birth\s?date|born(?:\s+on)?)\b"
    r"[^\n\d]{0,20}"
    r"(?:\d{1,2}[/.-]\d{1,2}[/.-](?:\d{4}|\d{2})\b|\d{4}-\d{2}-\d{2}\b"
    r"|[A-Za-z]{3,9}\.? \d{1,2},? \d{4}\b|\d{1,2} [A-Za-z]{3,9}\.? \d{4}\b)")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(
    r"(?<![\d-])(?:\+?1[ .-]?)?(?:\(\d{3}\)\s?|\d{3}[ .-])\d{3}[ .-]\d{4}(?![\d-])")
ABA_PREFIXES = set(range(0, 13)) | set(range(21, 33)) | set(range(61, 73)) | {80}


def luhn_ok(digits):
    """True if the digit string passes the Luhn checksum."""
    total = 0
    for i, ch in enumerate(reversed(digits)):
        d = int(ch)
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


def aba_ok(digits):
    """True if a 9-digit string is a plausible ABA routing number."""
    if len(digits) != 9 or int(digits[:2]) not in ABA_PREFIXES:
        return False
    d = [int(c) for c in digits]
    return (3 * (d[0] + d[3] + d[6]) + 7 * (d[1] + d[4] + d[7])
            + (d[2] + d[5] + d[8])) % 10 == 0


def ssn_ok(area, group, serial):
    """SSN validity: area not 000/666/9xx, group not 00, serial not 0000."""
    if area == "000" or area == "666" or area.startswith("9"):
        return False
    return group != "00" and serial != "0000"


def _scan_pii_line(line):
    kinds = []
    for m in SSN_RE.finditer(line):
        if ssn_ok(*m.groups()):
            kinds.append("SSN")
            break
    for m in CARD_RE.finditer(line):
        digits = re.sub(r"\D", "", m.group(0))
        if 13 <= len(digits) <= 19 and len(set(digits)) > 1 and luhn_ok(digits):
            kinds.append("payment card number")
            break
    for m in ABA_RE.finditer(line):
        if aba_ok(m.group(0)):
            kinds.append("bank routing number")
            break
    if DOB_RE.search(line):
        kinds.append("date of birth")
    if EMAIL_RE.search(line) and PHONE_RE.search(line):
        kinds.append("email + phone")
    return kinds


def scan(text, classes=("secret", "pii")):
    """Scan text; return [{line, cls, kind}, ...]. Never includes values."""
    out = []
    for i, line in enumerate(text.splitlines(), 1):
        if "secret" in classes:
            for k in _scan_secrets_line(line):
                out.append({"line": i, "cls": "secret", "kind": k})
        if "pii" in classes:
            for k in _scan_pii_line(line):
                out.append({"line": i, "cls": "pii", "kind": k})
    return out


if __name__ == "__main__":
    print("fh_patterns is a library; import it (see module docstring).")
