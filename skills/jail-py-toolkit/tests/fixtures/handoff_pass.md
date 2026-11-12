# Example

```yaml
JAIL-HANDOFF:
  skill: jail-research
  status: complete
  facts: [market is growing [1], two rivals "Acme, Inc" and Beta]
  assumptions:
    - budget holds  # comment
  unknowns: []
  outputs: [evidence packet]
  confidence: medium
  next: jail-decide
  approval_required: []
  checks:
    cite-check.py: pass
    label-lint.py: n/a
```
