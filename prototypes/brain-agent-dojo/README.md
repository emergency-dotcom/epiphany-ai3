# BRaiN™ × Agent Dojo™ — Interactive Prototype

**Epiphany AI3 LLC · Prototype v0.1 · 2026-10-16**

A lightweight, single-page concept for rehearsing a decision, inspecting a transparent rule-based output, and exporting a local JSON **AI Outcome Receipt™**.

## Run on Windows

1. Download the repository ZIP for the prototype/brain-agent-dojo-dashboard branch and extract it.
2. Open the prototypes/brain-agent-dojo/ folder.
3. Double-click Open-Demo.cmd. It opens index.html in the default browser.
4. Adjust the scenario controls, choose Run scenario, optionally use Record event, and choose Download JSON receipt.

No installation, Python, Node.js, build step, browser extension, or internet connection is required to use the demo page once the files are local.

## What it demonstrates

- Three selectable workstreams: field service, healthcare education / safe handoff, and process redesign.
- Interactive evidence, impact, reversibility, human-approval, and evidence-gap controls.
- Visible rule identifiers and a readable event trace.
- A downloadable JSON receipt with inputs, rule output, limitations, and any events recorded during the current page session.
- A responsive dark interface designed to remain usable on modest hardware.

## Hard boundaries

- This is **not an AI agent**: no AI model is called and no inference is performed.
- Recommendations come from explicit JavaScript demo rules in index.html; they are not validated decision logic.
- It does not retrieve or verify real-world evidence, diagnose equipment, or make clinical recommendations.
- No external requests are made; no credentials or patient data should be entered.
- Events exist only in page memory and are lost when the page closes unless the receipt is downloaded.
- The JSON file is a demonstration receipt, not a production CAS3 attestation, signature, trusted timestamp, or cryptographic provenance guarantee. No SHA-256 manifest is generated in this prototype.

## Next engineering gates

1. User review of the concept and workstream priorities.
2. Separate policy/rules module with tests and versioning.
3. Evidence schema with source metadata and explicit status distinctions: observed, user-supplied, inferred, simulated, and independently verified.
4. Add an actual model through a replaceable provider adapter; do not place API keys in browser-side code.
5. Add receipt integrity controls and validation tests.
6. Only then evaluate a voice/avatar connection. Photorealistic animation is intentionally not part of this lightweight local prototype.

**Status:** proposal branch; not merged into the public site.
