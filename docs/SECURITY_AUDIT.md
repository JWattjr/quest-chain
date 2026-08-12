# Security and consensus audit: QuestChain

Audit date: 2026-08-12
Scope: `contracts/QuestChain.py`
Method: manual review, full GenVM lint and pinned-runner schema validation, direct-mode adversarial tests, explicit independent-validator execution, and finalized StudioNet receipt/state inspection.

## Result

No unresolved critical or high-severity code issue was found after remediation. The contract does not custody or transfer value.

## Remediated findings

| ID | Severity | Finding | Remediation |
| --- | --- | --- | --- |
| QC-01 | High | Model-generated points or unlocks could make rewards subjective. | Consensus covers milestone statuses only; bitmasks, DAG rules, points, streaks, and unlocks are deterministic. |
| QC-02 | High | Retry or replay could double-award achievements. | Track awarded_mask and expose an owner-only one-time claim. |
| QC-03 | Medium | Missing milestone sources could be interpreted as failure. | Normalize unavailable milestone evidence to PENDING and keep the quest retryable. |

## Verification

- Exact runner pin: `py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6`.
- `genvm-lint check` passes AST and SDK schema validation.
- Direct tests exercise lifecycle, failure, and independent-validator paths.
- AST regression proves nondeterministic closures do not reference `self`.
- StudioNet deployment and consensus transaction are finalized with successful leader execution; exact evidence is in `deployments/studionet.json`.
- Bradbury is accepted only after successful execution and state reads, then finalized independently.

## Residual risk

See `SECURITY.md`. This is an engineering assessment, not formal verification, a financial guarantee, or legal advice.
