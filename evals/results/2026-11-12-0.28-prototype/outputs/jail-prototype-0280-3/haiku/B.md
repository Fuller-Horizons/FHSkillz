I also added a note to the spike ledger recording that the production request was declined under the prototype rules, so the decision is on record for the project.

JAIL-HANDOFF:
  skill: jail-prototype
  status: blocked
  assumptions: [the "real customer list" is available to the user but not in this session; the B layout verdict still applies to production]
  unknowns: [customer list location and clearance; client recipients; Monday send approval]
  outputs: [spike ledger note added to the project]
  evidence: [scorecard verdict 2026-11-12, layout B, verbatim reviewer answer already in ledger]
  next: jail-task-contract (scope the production build) once the user supplies the data and approvals
  approval_required: [customer data use, production build, sending to clients]
  tested: n/a