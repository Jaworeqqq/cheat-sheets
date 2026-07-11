---
title: "HashiCorp Vault – patterns"
category: "devsecops"
tags: ["secrets-management", "vault", "secrets"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# HashiCorp Vault – patterns

## TL;DR
Vault centralizes secrets with auth methods (who), policies (what), and secret engines (what kind). The big wins over static secrets: dynamic (short-lived) credentials, leasing/revocation, and encryption-as-a-service.

## Core model
```text
Auth method  – how a client proves identity (Kubernetes, AppRole, OIDC, AWS IAM, JWT)
Policy       – HCL granting path-based capabilities (read/create/update/delete/list)
Secret engine – kv (static), database (dynamic DB creds), pki (certs), transit (encrypt), aws/gcp/azure (dynamic cloud creds)
Lease/TTL    – secrets expire; revoke on demand or on compromise
```

## Static vs dynamic secrets
```bash
# Static KV v2
vault kv put secret/app/db password=... 
vault kv get secret/app/db

# Dynamic DB creds (Vault creates a short-lived DB user on request)
vault read database/creds/app-role     # returns username/password + lease
# -> revoke automatically at TTL, or: vault lease revoke <lease_id>
```

## Policy example (least privilege)
```hcl
path "secret/data/app/*" {
  capabilities = ["read"]
}
path "database/creds/app-role" {
  capabilities = ["read"]
}
```

## Auth patterns (no static tokens)
```text
Kubernetes  – pod's ServiceAccount JWT -> Vault role -> secrets (no secret in the image)
AppRole     – CI/CD: role_id (config) + secret_id (short-lived, delivered securely)
OIDC/JWT    – GitHub Actions/GitLab OIDC -> Vault role -> short-lived creds
Cloud IAM   – instance identity -> Vault role
```

## Best practices
```text
- Prefer dynamic secrets (DB/cloud) over long-lived static ones.
- Short TTLs + automatic revocation; audit device logging enabled.
- Least-privilege policies per app; no root/broad tokens in apps.
- Auto-unseal (KMS) + Shamir key custody; response-wrapping for secret delivery.
- Transit engine for encrypt/decrypt so apps never handle raw keys.
```

## Detection (Blue Team)
- Vault audit log: anomalous path access, mass reads, policy changes, root token use.

## Sources
- [Vault docs](https://developer.hashicorp.com/vault/docs) · [Vault security model](https://developer.hashicorp.com/vault/docs/internals/security)
