import json


def _deploy(direct_deploy):
    return direct_deploy(
        "contracts/QuestChain.py", "season-1",
        json.dumps([
            {"id": "signup", "description": "Signup opened", "points": 10, "prerequisite_ids": [], "source_urls": ["https://official.example.org/signup"]},
            {"id": "finale", "description": "Finale completed", "points": 20, "prerequisite_ids": ["signup"], "source_urls": ["https://official.example.org/finale"]},
        ]),
        "2030-01-01T00:00:00Z", "2030-02-01T00:00:00Z", "quest-v1", 5,
    )


def test_resolves_bitmask_points_and_one_time_claim(direct_vm, direct_deploy, direct_owner):
    contract = _deploy(direct_deploy)
    direct_vm.sender = direct_owner
    direct_vm.warp("2030-01-15T00:00:00Z")
    direct_vm.mock_web(r".*", {"status": 200, "body": "official evidence"})
    direct_vm.mock_llm(r".*", json.dumps({
        "evidence_state": "FINAL",
        "milestones": [{"id": "signup", "status": "ACHIEVED"}, {"id": "finale", "status": "ACHIEVED"}],
    }))
    result = contract.resolve()
    assert result["achieved_mask"] == 3
    assert contract.get_state()["total_points"] == 40
    assert direct_vm.run_validator()
    assert contract.claim_rewards()["claimed"] is True
    with direct_vm.expect_revert("already claimed"):
        contract.claim_rewards()


def test_source_outage_is_wait(direct_vm, direct_deploy):
    contract = _deploy(direct_deploy)
    direct_vm.warp("2030-01-15T00:00:00Z")
    direct_vm.mock_web(r".*", {"status": 503, "body": "offline"})
    assert contract.resolve()["state"] == "WAIT"
