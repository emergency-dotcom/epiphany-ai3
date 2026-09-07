#!/usr/bin/env python3
"""Robot 2K runtime adapter.

This file is deliberately dependency-free. It creates a local synthetic run
record and can optionally POST that record to an explicitly supplied endpoint.
It does not download model weights, invoke a remote service by default, or
claim that NVIDIA hardware is present.

An externally hosted service can implement the boundary around NVIDIA Isaac,
GR00T, Cosmos, or another qualified runtime. Returned actions remain
suggestions until a separate human approval gate is satisfied.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCENARIO_FILE = ROOT / "robot2k" / "scenarios.json"

METRICS = {
    "free-throw-precision": {"perception": 88, "balance": 81, "planning": 76, "recovery": 72},
    "obstacle-recovery": {"perception": 84, "balance": 73, "planning": 82, "recovery": 91},
    "teleop-handoff": {"perception": 79, "balance": 86, "planning": 70, "recovery": 95},
    "energy-budget": {"perception": 82, "balance": 78, "planning": 87, "recovery": 74},
}


def load_scenarios() -> dict[str, dict[str, Any]]:
    with SCENARIO_FILE.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    return {item["id"]: item for item in payload["scenarios"]}


def build_synthetic_record(scenario_id: str) -> dict[str, Any]:
    scenarios = load_scenarios()
    scenario = scenarios[scenario_id]
    timestamp = datetime.now(timezone.utc).isoformat()
    run_id = "R2-" + timestamp.replace("-", "").replace(":", "").replace(".", "")[:18]

    return {
        "product": "Robot 2K",
        "owner": "Epiphany AI3 LLC",
        "build": "R2-001",
        "run_id": run_id,
        "created_at": timestamp,
        "scenario": scenario_id,
        "scenario_label": scenario["label"],
        "objective": scenario["objective"],
        "authority": "READ_ONLY",
        "human_gate_required": True,
        "runtime": {
            "mode": "SYNTHETIC_LOCAL_RUN",
            "nvidia_runtime_connected": False,
            "physical_action_enabled": False,
        },
        "metrics": METRICS[scenario_id],
        "observations": [
            "Synthetic telemetry generated locally.",
            "No physical robot was moved.",
            "No external endpoint was contacted.",
        ],
        "evidence": [
            {"kind": "CREATED", "message": "Qualification record created."},
            {"kind": "GATE", "message": "Authority held at READ_ONLY."},
            {"kind": "SYNTHETIC", "message": "Local synthetic telemetry captured."},
            {"kind": "REVIEW", "message": "Human review required before any external action."},
        ],
        "source_register": [
            {
                "name": "NVIDIA Isaac GR00T",
                "url": "https://github.com/NVIDIA/Isaac-GR00T",
                "license_note": "Repository states Apache 2.0.",
            },
            {
                "name": "NVIDIA IsaacTeleop",
                "url": "https://github.com/NVIDIA/IsaacTeleop",
                "license_note": "Review exact repository and dependency licenses.",
            },
            {
                "name": "NVIDIA Cosmos",
                "url": "https://github.com/NVIDIA/cosmos",
                "license_note": "Repository states OpenMDW-1.1 for model materials.",
            },
            {
                "name": "NVIDIA Aerial Omniverse Digital Twin",
                "url": "https://github.com/NVIDIA/aerial-omniverse-digital-twin",
                "license_note": "Repository includes Apache-2.0 licensing.",
            },
        ],
    }


def post_json(endpoint: str, payload: dict[str, Any], timeout: float) -> dict[str, Any]:
    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        endpoint,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
    except (urllib.error.URLError, TimeoutError) as exc:
        raise RuntimeError(f"runtime endpoint failed: {exc}") from exc

    try:
        decoded = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError("runtime endpoint returned non-JSON data") from exc

    if not isinstance(decoded, dict):
        raise RuntimeError("runtime endpoint must return a JSON object")
    return decoded


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a Robot 2K qualification record.")
    parser.add_argument("--scenario", required=True, choices=sorted(METRICS))
    parser.add_argument(
        "--endpoint",
        help="Optional explicit POST endpoint for a separately hosted qualified runtime.",
    )
    parser.add_argument("--timeout", type=float, default=8.0)
    args = parser.parse_args()

    record = build_synthetic_record(args.scenario)
    if args.endpoint:
        record["runtime"]["mode"] = "EXTERNAL_ENDPOINT_REQUESTED"
        record["runtime"]["endpoint"] = args.endpoint
        try:
            record["runtime"]["response"] = post_json(args.endpoint, record, args.timeout)
        except RuntimeError as exc:
            record["runtime"]["error"] = str(exc)
            print(json.dumps(record, indent=2), file=sys.stderr)
            return 2

    print(json.dumps(record, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
