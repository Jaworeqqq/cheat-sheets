---
title: "Terraform security"
category: "devsecops"
tags: ["iac", "terraform", "state", "hardening"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Terraform security

## TL;DR
Terraform provisions infrastructure — so its state, credentials, modules, and generated config are all high-value. Secure the state (it often contains secrets), scan the code, pin modules/providers, and gate applies.

## State file security (often overlooked)
```text
- State can contain SECRETS in plaintext (passwords, keys, generated creds).
- Store remote state in an encrypted, access-controlled backend (S3+KMS+DynamoDB lock,
  Terraform Cloud, GCS, Azure Storage) — never commit state to git.
- Enable encryption at rest + versioning + state locking; least-privilege on the backend.
- Treat state like a secret store; audit access.
```

## Code scanning (shift-left)
```bash
trivy config .                 # misconfig scanning (absorbed tfsec)
checkov -d .                   # policy checks
terraform plan -out=plan && terraform show -json plan | conftest test -   # policy-as-code (OPA)
```

## Providers, modules, and pinning
```text
- Pin provider + module versions (required_providers with = or ~>, module ?ref=<tag/sha>).
- Vet third-party modules (registry) — they run with your credentials.
- Private module registry for internal modules; avoid unpinned public modules.
```

## Credentials & secrets
```text
- No hardcoded creds in .tf/.tfvars; use OIDC (CI -> cloud) or a secrets backend.
- Mark sensitive outputs `sensitive = true`; still ends up in state (protect the state).
- .gitignore: *.tfstate, *.tfvars (if they hold secrets), .terraform/.
```

## Pipeline gating
```text
plan -> policy scan (checkov/OPA) -> human review of the plan -> apply.
- Never auto-apply unreviewed plans to prod; separate plan/apply roles.
- Detect drift (terraform plan in CI) to catch out-of-band changes.
```

## Detection (Blue Team)
- Backend audit logs for state access; alert on state read by unexpected identities.
- CI policy-scan failures; drift detection; unpinned modules/providers.

## Mitigation / Hardening
- Encrypted+locked remote state, least privilege, OIDC creds, pinned modules/providers.
- IaC scanning + policy-as-code gates (see [iac-scanning](./iac-scanning.md), [opa-conftest](./opa-conftest.md)).

## Sources
- [Terraform – remote state](https://developer.hashicorp.com/terraform/language/state/remote) · [Checkov](https://www.checkov.io/)
