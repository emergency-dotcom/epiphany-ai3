# NVIDIA foundation for Robot 2K

This directory is the integration boundary between the Robot 2K web twin and separately hosted NVIDIA robotics or world-model runtimes.

## What is actually integrated today

The browser app is self-contained and runs a deterministic synthetic qualification. It records the intended NVIDIA sources, but it does not download model weights, execute CUDA, control a robot, or claim that an NVIDIA runtime is connected.

The adapter in robot2k_adapter.py defines a small JSON contract for an optional service. The endpoint is opt-in and must be supplied explicitly by the operator.

## Source register

| Source | Intended role | License note | Current status |
| --- | --- | --- | --- |
| NVIDIA Isaac GR00T | Vision-language-action policy/reference layer | Repository states Apache 2.0 | Documented candidate |
| NVIDIA IsaacTeleop | Teleoperation and demonstration capture | Review repository and dependencies | Review required |
| NVIDIA Cosmos | World-model and scenario-generation layer | Repository states OpenMDW-1.1 for model materials | Documented candidate |
| NVIDIA Aerial Omniverse Digital Twin | Client, worker, and viewer patterns | Repository includes Apache-2.0 licensing | Documented candidate |

The project must preserve each source's license, copyright, trademark, model, and dependency notices. A source being public does not automatically mean every model, dataset, checkpoint, or dependency is interchangeable.

## Adapter contract

Input to an optional endpoint:

- product: Robot 2K
- scenario: one of the IDs in robot2k/scenarios.json
- authority: READ_ONLY
- human_gate_required: true
- evidence_mode: append-only run record
- synthetic_record: the local run record generated before the request

The endpoint may return observations, proposed actions, metrics, or errors. Robot 2K should treat all returned actions as suggestions until a human review gate is satisfied.

A production adapter still needs:

- model and code version pins;
- hardware and CUDA/driver details;
- data and model provenance;
- timeout and retry boundaries;
- input/output schema validation;
- an explicit stop path;
- red-team and failure testing;
- human approval before physical actuation.

## Why the web twin matters

A robotics stack can produce a technically impressive demo while leaving authority, uncertainty, and failure handling invisible. Robot 2K makes those items first-class records:

**detect → qualify → select → operate → verify → export**

That is the Epiphany AI3 layer. NVIDIA and other open-source projects provide valuable foundations; Epiphany AI3 provides the evidence and stewardship boundary around their use.
