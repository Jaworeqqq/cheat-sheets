---
title: "IaC Security Scanning"
category: "devsecops"
tags: ["iac", "terraform", "scanning"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# IaC Security Scanning

## TL;DR
Skanuj Terraform/CloudFormation/Bicep/K8s manifesty pod misconfig **przed** deploymentem (shift-left). Wpinaj w pre-commit i CI, blokuj krytyczne.

## Narzędzia
```bash
# Checkov (szeroki, multi-format)
checkov -d . --compact
checkov -d . --framework terraform --check CKV_AWS_20

# tfsec / trivy (trivy wchłonął tfsec)
trivy config .
trivy config --severity HIGH,CRITICAL ./infra

# KICS
kics scan -p . -o results
# Terrascan
terrascan scan -i terraform
```

## Typowe wykrycia
```text
- S3/bucket publiczny, brak szyfrowania at-rest
- Security group 0.0.0.0/0 na 22/3389/3306
- Brak logowania (CloudTrail/flow logs), brak wersjonowania
- IAM z "*" na Action/Resource
- Hardcoded sekrety w zmiennych
- Brak encryption in transit (TLS)
```

## Integracja
```yaml
# pre-commit
repos:
  - repo: https://github.com/bridgecrewio/checkov
    hooks: [{ id: checkov }]
```
```yaml
# CI – blokuj krytyczne
- run: trivy config --exit-code 1 --severity CRITICAL .
```

## Dobre praktyki
- Baseline + świadome wyjątki (`#checkov:skip=CKV_...:powód`), nie wyłączaj globalnie.
- Łącz z policy-as-code (OPA/Conftest) dla reguł organizacyjnych.
- Skanuj też **plan** (drift, faktyczny stan), nie tylko kod.

## Źródła
- [Checkov](https://www.checkov.io/) · [Trivy config](https://trivy.dev/) · [KICS](https://kics.io/)
