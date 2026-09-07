# Epiphany AI3 — Robot 2K

Robot 2K is an original basketball-style physical-AI training and qualification twin. It makes robot behavior understandable through a familiar game loop while keeping the important distinction visible:

- a browser simulation is not a deployed robot;
- a score is not proof of safe behavior;
- a model suggestion is not human authority.

**Evidence before authority. Human capability before automation.**

## What is in this branch

- \`index.html\` — a self-contained Robot 2K command center that works without a build step.
- \`robot2k/scenarios.json\` — versioned scenario definitions and pass criteria.
- \`nvidia/manifest.json\` — NVIDIA/open-source source register with license and integration status.
- \`nvidia/robot2k_adapter.py\` — standard-library adapter seam for an externally hosted policy/simulation runtime.
- \`nvidia/README.md\` — source, license, and integration notes.
- \`NOTICE.md\` — attribution and separation of Epiphany work from third-party materials.
- \`.github/workflows/validate.yml\` — lightweight syntax and data validation.

## Architecture

\`\`\`
NVIDIA/open-source robotics runtime
        ↓
Robot 2K scenario and telemetry adapter
        ↓
Robot 2K web twin / training interface
        ↓
Epiphany AI3 evidence, authority, and outcome review
\`\`\`

The web app is intentionally honest about runtime state. Its default runs are labeled **synthetic simulation**. It does not claim that Isaac, GR00T, Cosmos, CUDA, or a physical robot is running in the browser. The adapter provides a controlled boundary for connecting a separately hosted runtime later.

## First scenarios

- Free Throw Precision — repeatable target alignment and release timing.
- Obstacle Recovery — recover from a blocked path without hiding the failure.
- Teleop Handoff — show the transition from policy suggestion to human control.
- Energy Budget — complete a session while reporting energy and thermal assumptions.

Every scenario records its objective, authority state, capabilities, observations, result, and evidence packet.

## NVIDIA foundation

The source register identifies the relevant public repositories and keeps licensing explicit. In this prototype:

- Isaac GR00T is listed as a candidate policy/reference integration and its repository states Apache 2.0.
- NVIDIA Cosmos is listed as a candidate world-model integration and its repository states OpenMDW-1.1 for its model materials.
- Isaac Teleop and other components remain **review required** until their exact repository and dependency licenses are checked.
- NVIDIA names and marks are used only to identify source projects; Robot 2K and Epiphany AI3 are original project names.

Use what we have the right to use. Credit what we did not create. Protect what we did create.

## Run locally

No package installation is required:

1. Open \`index.html\` in a modern browser.
2. Choose a scenario.
3. Select **Run qualification**.
4. Watch the state transition from READY to RUNNING to VERIFYING to COMPLETE.
5. Export the evidence JSON.

For the adapter:

\`\`\`bash
python3 nvidia/robot2k_adapter.py --scenario free-throw-precision
\`\`\`

The adapter emits a local, synthetic run record by default. To connect an external service, supply an endpoint explicitly:

\`\`\`bash
python3 nvidia/robot2k_adapter.py \\
  --scenario obstacle-recovery \\
  --endpoint http://localhost:8000/policy
\`\`\`

The adapter does not send data anywhere unless an endpoint is explicitly provided.

## Safety and scope

Robot 2K is a research and demonstration surface. It is not a medical device, a safety certification, or a robot controller. Keep all real-hardware experiments supervised and isolated. Any future physical integration needs hardware-specific risk review, permissions, logging, human handoff, and a clear rollback path.

## Project identity

Epiphany AI3 LLC — Tucson, Arizona  
Engineered Stewardship™  
“AI doesn’t meter us; we meter AI.”
