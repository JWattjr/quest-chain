# GenLayer Portal submission

**Contribution type:** Builder → Intelligent Contracts
**Title:** QuestChain — Multi-Stage Quest Settler
**Contribution date:** August 12, 2026

## Notes / Description

Built and deployed MIT-licensed QuestChain, a standalone GenLayer Intelligent Contract for prediction season passes, bingo cards, achievements, streaks, and unlockable quests. Deployment freezes up to eight milestones, per-milestone public HTTPS evidence, prerequisite DAG, points, cutoff, maximum wait, streak bonus, and spec ID. Validators independently return ordered ACHIEVED/FAILED/PENDING facts; deterministic code computes prerequisite-aware bitmasks, points, streaks, unlocks, and a one-time owner claim. Missing evidence stays WAIT, conflict is CONTESTED, and cancellation/max-wait is VOID; replay cannot double-award points. Includes pinned GenVM source, bitmask/claim/adversarial tests, full schema validation, audit, test matrix, and finalized StudioNet/Bradbury consensus evidence. It holds no reward funds.

## Evidence to add

1. GitHub Repository — https://github.com/JWattjr/quest-chain
2. GitHub File — https://github.com/JWattjr/quest-chain/blob/main/contracts/QuestChain.py
3. GitHub File — https://github.com/JWattjr/quest-chain/blob/main/tests/test_quest_chain.py
4. GitHub File — https://github.com/JWattjr/quest-chain/blob/main/docs/SECURITY_AUDIT.md
5. GitHub File — https://github.com/JWattjr/quest-chain/blob/main/docs/TEST_MATRIX.md
6. GitHub File — https://github.com/JWattjr/quest-chain/blob/main/deployments/studionet.json
7. GitHub File — https://github.com/JWattjr/quest-chain/blob/main/deployments/bradbury.json
8. GenLayer Explorer Contract — https://explorer-bradbury.genlayer.com/address/0x12aED2C4701429392cD4a6d21B0C7aC4db8790a8

The repository is private. Grant Portal reviewers repository access before submission.
