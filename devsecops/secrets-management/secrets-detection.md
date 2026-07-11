---
title: "Secret detection and management"
category: "devsecops"
tags: ["secrets-management", "gitleaks", "vault"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Secrets – detection and management

## TL;DR
Don't keep secrets in code. Prevent (pre-commit scan), detect (scan history), manage (Vault/KMS/secret manager), rotate after a leak.

## Detection
```bash
# gitleaks – scan repo + history
gitleaks detect --source . --redact -v
gitleaks protect --staged            # pre-commit (before the commit)

# trufflehog – verifies whether a secret is live
trufflehog git file://. --only-verified
trufflehog github --repo=https://github.com/org/repo
```

## Pre-commit (prevention)
```yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.x
    hooks: [{ id: gitleaks }]
```

## Management
```text
HashiCorp Vault  – dynamic secrets, leasing, rotation, transit encryption
Cloud native     – AWS Secrets Manager / KMS, Azure Key Vault, GCP Secret Manager
K8s              – External Secrets Operator (sync with Vault/cloud), Sealed Secrets, SOPS
CI/CD            – OIDC instead of long-lived, masked secrets, environment scoping
```

```bash
# SOPS – encrypt secret files in the repo (KMS/age)
sops -e secrets.yaml > secrets.enc.yaml
sops -d secrets.enc.yaml
```

## Leak response (order matters!)
```text
1. ROTATE/revoke the secret (removing it from git is NOT enough — it's in history/forks).
2. Investigate whether it was used (access logs).
3. Only then clean history (git filter-repo) if needed.
```

## Sources
- [gitleaks](https://github.com/gitleaks/gitleaks) · [trufflehog](https://github.com/trufflesecurity/trufflehog) · [SOPS](https://github.com/getsops/sops)
