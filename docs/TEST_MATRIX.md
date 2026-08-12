# Test matrix

| Requirement | Direct test | Integration evidence |
| --- | --- | --- |
| Prerequisite-aware achieved bitmask | Direct mocked GenVM | StudioNet/Bradbury evidence where applicable |
| Deterministic points and streak bonus | Direct mocked GenVM | StudioNet/Bradbury evidence where applicable |
| One-time owner claim rejects replay | Direct mocked GenVM | StudioNet/Bradbury evidence where applicable |
| Source outage remains WAIT | Direct mocked GenVM | StudioNet/Bradbury evidence where applicable |
| Finalized StudioNet deployment and resolve transaction | Direct mocked GenVM | StudioNet/Bradbury evidence where applicable |
| Nondeterministic storage isolation | AST closure regression | Receipt inspected for successful execution |
| Public URL controls | Constructor rejection paths | Frozen official GovInfo HTTPS source |
| Prompt injection boundary | Untrusted evidence schema/prompt | Independent validator re-fetch |
| Replay/finality safety | Terminal/idempotent transition checks | Consumers instructed to wait for finality |

StudioNet evidence must show both protocol `FINALIZED` and leader execution `SUCCESS`; a lifecycle label alone is not a passing test. Bradbury evidence records all five deployment hashes before any finality polling.
