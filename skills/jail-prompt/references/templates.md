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
* **Fact**: [Claim] [1] · *Source: [Link Title](file:///path/or/url) (Access Date)*
* **Inference**: [Claim] · *Reasoned from [1]; premise stated*

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
For writing machine-verifiable exit tests. Name the assertions in the SUCCESS TEST so a script or reviewer can run them; typical set:

| Assertion | Pass condition |
| :--- | :--- |
| File present | the named output file exists |
| Parses | output is valid JSON / CSV / Markdown table |
| Required keys | every object has the keys the schema lists (for example `id`, `confidence`) |
| Bounds | numeric fields sit in range (for example confidence between 0.0 and 1.0) |
| Counts | item count or word count falls in the stated range |
| Traceability | every claim carries at least one source id |

Run with whatever the environment has (a test runner, a short script, or a spreadsheet formula); exit code 0 means pass, anything else fails the step. Manual fallback: walk the table by hand against the output.

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

## 8. PII & Secret Redaction Patterns
For scrubbing sensitive values from dry-run inputs and logs. Replace each match with a placeholder, never a partial value:

| Pattern to find | Replace with |
| :--- | :--- |
| e-mail addresses | `[REDACTED_EMAIL]` |
| phone numbers (with or without country code) | `[REDACTED_PHONE]` |
| `api_key`, `secret`, `password`, `token`, `bearer` followed by `:` or `=` and a long value (12+ characters) | `[REDACTED_SECRET]` |
| IPv4 addresses | `[REDACTED_IP]` |

For a machine pass use jail-py-toolkit `secret-scan.py` and `pii-scan.py`; manual fallback: search the text for each pattern above before it goes into a prompt.

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



---

## 10. Evidence-first consulting prompt
For analysis over a client's supplied data where numbers will be presented to someone else (a P&L, a pipeline export, a survey, a vendor quote). Fill the brackets; keep the footer verbatim.

```
METADATA: inputs: [<attached files>] · outputs: [<deliverable>] · params: {temperature: 0.2} · requires: none · produces: [<deliverable>]
ROLE: <only if it shifts standards, e.g. "management consultant reviewing a client's books">
OBJECTIVE: <one sentence: what the client decision is and what this output feeds>

INPUTS (attach):
- <file 1: name, period, source system>
- <file 2 ...>
If an input is missing, say so under Data Gaps and stop that part of the analysis. Do not reconstruct it.

EXTERNAL EVIDENCE (tiered sources, only if the question needs outside benchmarks):
- Tier 1: official or primary (government statistics, regulator filings, vendor documentation)
- Tier 2: peer-reviewed or industry-body publications
- Tier 3: reputable secondary press
Use the highest tier available; give publisher, page, and access date for each source. If no source exists, write Unknown.

OUTPUT: <exact shape: table columns / sections / schema, with one filled example row>

RULES:
- Cite a source for every number (an attached file and cell/section, or an external source id).
- Tag each claim Fact / Inference / Unknown. Fact needs a source; Inference states its reasoning in one line.
- Show calculations (inputs, formula, result) next to each derived figure.
- Never invent a figure. List anything you cannot source under Data Gaps.
- End with three sections: Data Gaps | Assumptions | Confidence (high / medium / low, with the reason).

SUCCESS TEST: [AUTO] every number in OUTPUT appears in an attached file or carries a source id; [AUTO] the three closing sections exist; [HUMAN] a second person can re-derive each calculation from the shown inputs.
```
