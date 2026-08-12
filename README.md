# QuestChain — Multi-Stage Quest Settler

A standalone GenLayer Intelligent Contract for season passes, achievement quests, streaks, and unlockable challenges resolved as an exact milestone bitmask.

## GenLayer-native decision

Validators independently classify bounded milestones as ACHIEVED, FAILED, or PENDING. Contract code applies the frozen prerequisite DAG, bitmasks, points, streak bonus, unlocks, and one-time claim.

## Lifecycle and API

`OPEN → WAIT/CONTESTED/RESOLVED/VOID`, followed by an owner-only one-time reward claim. Retryable evidence never awards points; only a resolved milestone mask changes rewards.

Constructor: `quest_id, milestones, cutoff, max_wait, spec_id, streak_bonus_points`. Public methods: `resolve()`, `claim_rewards()`, and `get_state()`.

Every evidence URL is frozen, bounded, public HTTPS. Fetched text is untrusted input; prompts instruct validators to ignore embedded commands. Leader and validator closures snapshot ordinary values and independently re-fetch evidence.

## Live evidence

- [StudioNet contract](https://explorer-studio.genlayer.com/address/0xCd22cE863023387211b6D13Fb2049785F587b903)
- [Bradbury contract](https://explorer-bradbury.genlayer.com/address/0x12aED2C4701429392cD4a6d21B0C7aC4db8790a8)
- Exact StudioNet transaction hashes, constructor arguments, state, and execution results are in `deployments/studionet.json`.

## Verify

```powershell
python -m pip install -r requirements.txt
genvm-lint check contracts/QuestChain.py
python -m pytest tests -q
```

The contract uses a concrete pinned GenVM runner. See `docs/SECURITY_AUDIT.md`, `docs/TEST_MATRIX.md`, and `PORTAL_SUBMISSION.md` for reviewer evidence. This primitive does not custody funds; consumers must wait for GenLayer finality and remain idempotent.
