---
title: "IaC security scanning"
category: "devsecops"
tags: ["iac", "terraform", "scanning"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# IaC security scanning

## TL;DR
Scan Terraform/CloudFormation/Bicep/K8s manifests for misconfigs **before** deployment (shift-left). Wire it into pre-commit and CI, block criticals.

## Tools
```bash
# Checkov (broad, multi-format)
checkov -d . --compact
checkov -d . --framework terraform --check CKV_AWS_20

# tfsec / trivy (trivy absorbed tfsec)
trivy config .
trivy config --severity HIGH,CRITICAL ./infra

# KICS
kics scan -p . -o results
# Terrascan
terrascan scan -i terraform
```

## Common findings
```text
- Public S3/bucket, no at-rest encryption
- Security group 0.0.0.0/0 on 22/3389/3306
- No logging (CloudTrail/flow logs), no versioning
- IAM with "*" on Action/Resource
- Hardcoded secrets in variables
- No encryption in transit (TLS)
```

## Integration
```yaml
# pre-commit
repos:
  - repo: https://github.com/bridgecrewio/checkov
    hooks: [{ id: checkov }]
```
```yaml
# CI – block criticals
- run: trivy config --exit-code 1 --severity CRITICAL .
```

## Best practices
- Baseline + deliberate exceptions (`#checkov:skip=CKV_...:reason`), don't disable globally.
- Combine with policy-as-code (OPA/Conftest) for organizational rules.
- Scan the **plan** too (drift, actual state), not just the code.

## Sources
- [Checkov](https://www.checkov.io/) · [Trivy config](https://trivy.dev/) · [KICS](https://kics.io/)
