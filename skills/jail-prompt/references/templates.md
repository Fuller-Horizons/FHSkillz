# Prompt Output Format Templates

Use these pre-engineered output schemas to ensure the generated prompt outputs data in a highly structured, repeatable, and clean format.

---

## 1. JSON Schema (API-friendly Data)
For structured data extraction or tool consumption:
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "DataPayload",
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "string", "pattern": "^[A-Za-z0-9_-]+$" },
          "name": { "type": "string" },
          "value": { "type": "number" },
          "confidence": { "type": "number", "minimum": 0.0, "maximum": 1.0 },
          "verified": { "type": "boolean" }
        },
        "required": ["id", "name", "value", "confidence", "verified"]
      }
    }
  },
  "required": ["items"]
}
```

---

## 2. GFM (GitHub Flavored Markdown) Tables
For comparative analysis or data logs:
```markdown
| Field Name | Type | Value / Range | Grounding Source | Last Checked |
| :--- | :--- | :--- | :--- | :--- |
| `example_id` | String | `usr_01H7` | API Metadata | 2026-06-08 |
| `status` | Enum | `active` \| `paused` | Database Record | 2026-06-08 |
```

---

## 3. Strict Step-by-Step Walkthroughs
For instructions, pipelines, or execution runs:
```markdown
### Step 1: [Short Actionable Verb]
* **Objective**: Clear description of what this step accomplishes.
* **Input**: Files, variables, or state needed.
* **Command/Action**: Specific task or command to run.
* **Verification**: How to know this step succeeded.

### Step 2: [Next Step...]
...
```

---

## 4. Structured Prose Reports
For business or research briefs:
```markdown
# [Title]

## Executive Summary
* **Recommendation**: [Action / Score / Status]
* **Confidence**: [0-100%]
* **Key Blocker/Opportunity**: [One sentence summary]

## Background & Context
[2-3 sentences max]

## Findings
* **Fact**: [Claim] · *Source: [Link Title](file:///path/or/url) (Access Date)*
* **Inference**: [Claim] · *Source-Backed*

## Technical Details
```

---

## 5. Context-Summarizer (Token-Efficient File Processing)
For reading and condensing large datasets or codebase files:
```markdown
### Summary of: [File name / Path]
* **Size & Scope**: [X lines / Y KB]
* **Core Purpose**: [1-sentence description of what this code/file does]
* **Key Definitions**:
  - `SymbolName`: [Description of function, variable, or class]
* **Critical Dependencies**: [List external files or APIs imported]
* **Extracted Insights**: [Key lines, values, or behaviors relevant to the objective]
```

---

## 6. Programmatic Assertion Check Helpers
For writing machine-verifiable exit tests in bash/python:

### Python Validator Snippet:
```python
# Save in scratch/verify_run.py
import json, sys

def assert_schema_and_content():
    try:
        with open('output.json', 'r') as f:
            data = json.load(f)
        assert "items" in data, "Missing 'items' key"
        for item in data["items"]:
            assert "id" in item, "Item missing 'id'"
            assert 0.0 <= item["confidence"] <= 1.0, "Confidence out of bounds"
        print("[+] Verification Succeeded!")
        sys.exit(0)
    except AssertionError as e:
        print(f"[!] Verification Failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    assert_schema_and_content()
```

### Bash Validator Snippet:
```bash
# Verify outputs in terminal
echo "Checking output file presence..."
[ -f "output.json" ] || { echo "File not found!"; exit 1; }
echo "Checking JSON schema..."
python -m json.tool output.json > /dev/null || { echo "Invalid JSON syntax!"; exit 1; }
echo "[+] Validated!"
```

---

## 7. Client Context Translation Map
For maintaining client portability when translating commands to different IDE environments:

| Standard Logic | Antigravity | Cursor | Claude Code |
| :--- | :--- | :--- | :--- |
| **Workspace context** | Local absolute paths | `@Workspace` | Auto-detected |
| **Specific File** | Markdown link `[basename](file:///path)` | `@filename` | `filename` path |
| **Command Execution** | `run_command` tool | Terminal panel | Shell console |
| **Custom Actions** | `/action-name` | Chat prompt | `/plugin-name` |

---

## 8. PII & Secret Redaction Regex Patterns
For scrubbing sensitive parameters from dry-run inputs and logs:

### Python Redactor Script:
```python
import re

def redact_sensitive_data(text):
    # E-mails
    text = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', '[REDACTED_EMAIL]', text)
    # Phone Numbers
    text = re.sub(r'\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}', '[REDACTED_PHONE]', text)
    # API Keys / Secrets (High Entropy Strings)
    text = re.sub(r'(?i)(api_key|secret|password|passwd|token|auth_token|bearer)\s*[:=]\s*["\']?[A-Za-z0-9_\-\.]{12,}["\']?', r'\1: "[REDACTED_SECRET]"', text)
    # IPv4 Addresses
    text = re.sub(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', '[REDACTED_IP]', text)
    return text
```

---

## 9. Structured State-Machine Chain Handoff Template
For chaining multiple prompts with structured state handoffs:

```json
{
  "chain_id": "auth-pipeline-eval-01",
  "current_state": "state_extraction_complete",
  "workflow": {
    "states": ["extract_logs", "analyze_anomalies", "generate_incident_brief"],
    "current_index": 1,
    "total_states": 3
  },
  "context_handoff": {
    "log_summary_path": "scratch/logs_summary.json",
    "detected_ips": ["192.168.1.105", "10.0.0.22"],
    "anomalies_found": 3
  },
  "next_step": {
    "action": "Analyze anomalies and determine if they represent a brute force attack pattern.",
    "expected_input_schema": "scratch/anomalies_schema.json"
  }
}
```


