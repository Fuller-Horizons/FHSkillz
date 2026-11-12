# Gotchas: failure modes seen in practice

Check against these before returning.

- **Collapsing into the task.** Silently doing the work and returning only the result. The engineered prompt is the deliverable; surface the copyable block first, then offer to run it.
- **Praising a flawed premise.** Going along with a bad idea to seem helpful. A flawed premise is a STOP however good the prompt would be. Discernment over agreeableness.
- **Re-engineering a finished prompt.** If the user pasted a complete, runnable prompt and wants it executed verbatim, run it. Do not trigger the workflow.
- **Lane inflation.** Running Full ceremony (a multi-question gate) on a clear, low-stakes ask. Default to the lightest lane that still earns the result.
- **Fake SUCCESS TEST.** A subjective-only test that cannot fail. Require at least one programmatic, machine-checkable check.
- **Reference link rot.** Keep `references/*.md` links relative. Absolute machine-specific paths break the moment the skill is installed elsewhere.
- **Broken chain handoff.** A step that consumes a key no earlier step produces, or per-step tests that pass while the chain goal is missed. Emit a manifest, lint it (`chain-lint.py`, or the manual walk), and grade the chain-level SUCCESS TEST, not just the per-step ones.
- **Chaining the trivial.** Splitting a task one good prompt could handle. Chain only when stages need different expertise, separate verification, or human judgment between them.
- **Self-graded verification.** Asking the answering model to check its own citations or critique its own answer. Route verification to a different model or a retrieval tool; same-model is the fallback.
- **Truth tags as theater.** Prose labels the model assigns to itself. Require the schema form (status plus evidence ids) and validate it (`truth-lint.py`, or the manual no-unevidenced-Fact check). An unevidenced Fact triggers a re-query, not acceptance.
- **Inventing missing inputs.** The user names a file or data set but attaches nothing. List it as an input to attach; never make up numbers to fill the gap.
- **Hand-computing what a tool should compute.** Presenting an LLM-added total as authoritative. Route to a spreadsheet or script (STOP), and offer a multiple-choice next step.
- **Echoing a secret.** Repeating a pasted key in the reply or the prompt. Mask it, switch to an environment variable, recommend least-privilege credentials and rotation.
