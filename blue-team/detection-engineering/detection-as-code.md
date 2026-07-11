---
title: "Detection as Code"
category: "blue-team"
tags: ["detection-engineering", "ci-cd", "sigma"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Detection as Code (DaC)

## TL;DR
Treat detection rules like software: version-controlled, peer-reviewed, tested, and deployed via CI/CD. Moves detection engineering from clicking in a SIEM UI to a repeatable, auditable pipeline.

## Why
```text
- Version history + rollback for every rule.
- Peer review (PR) catches bad logic and false-positive risk before production.
- Automated testing against known-good/known-bad data.
- Consistent deployment across environments; no drift/undocumented rules.
```

## Repo structure (example)
```text
detections/
  rules/            # Sigma YAML (source of truth, portable)
  tests/            # unit tests: sample events -> expected match/no-match
  .github/workflows/deploy.yml
docs/
```

## Pipeline stages
```text
1. Lint/validate   – sigma check, schema validation, required fields (level, FPs, ATT&CK tag)
2. Test            – run rule logic against sample true/false events
3. Convert         – Sigma -> target backend (Splunk/Sentinel/Elastic) via sigma-cli
4. Deploy          – push to SIEM via API on merge to main
5. Monitor         – track FP rate, rule health, coverage vs ATT&CK
```

## CI example (concept)
```yaml
# on PR: validate + test; on merge: convert + deploy
- run: sigma check rules/
- run: pytest tests/                         # rule unit tests
- run: sigma convert -t splunk rules/ -o out/
- run: ./deploy.sh out/                       # only on main
```

## Best practices
```text
- Source of truth = Sigma (portable); convert per backend.
- Every rule: description, ATT&CK mapping, falsepositives, level, owner.
- Test with Atomic Red Team telemetry; measure coverage (ATT&CK Navigator).
- Track metrics: FP rate, alert volume, MTTD; retire noisy/dead rules.
```

## Sources
- [SigmaHQ](https://github.com/SigmaHQ/sigma) · [Elastic Detection Rules repo](https://github.com/elastic/detection-rules) · [Splunk Security Content](https://github.com/splunk/security_content)
