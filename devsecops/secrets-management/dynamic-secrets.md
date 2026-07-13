---
title: "Dynamic secrets"
category: "devsecops"
tags: ["secrets-management", "vault", "dynamic-secrets"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# Dynamic secrets

## TL;DR
Instead of a long-lived static credential shared by many apps, dynamic secrets are generated on demand, unique per consumer, short-lived, and automatically revoked. This shrinks the blast radius of a leak, enables per-request attribution, and removes manual rotation. HashiCorp Vault popularized the pattern; clouds offer equivalents.

## Static vs dynamic
```text
Static  – one DB password in a secret store; shared; rotated manually (rarely). Leak = broad, lasting.
Dynamic – Vault creates a NEW DB user/password per request with a TTL; auto-revoked at expiry.
          Leak = limited scope + auto-expires; each consumer is distinct (auditability).
```

## How it works (Vault DB engine example)
```text
1. App authenticates to Vault (workload identity: K8s/AWS IAM/OIDC — no static token).
2. App reads database/creds/<role> -> Vault connects to the DB and CREATES a temp user.
3. Vault returns username/password + a lease (TTL).
4. At TTL (or on revoke), Vault DROPS the temp user. No manual rotation needed.
```
```bash
vault read database/creds/app-role     # unique creds + lease_id + TTL
vault lease revoke <lease_id>          # revoke early (e.g. on compromise)
```

## What supports dynamic secrets
```text
Vault engines – databases, AWS/GCP/Azure (temp cloud creds), PKI (short-lived certs), SSH, RabbitMQ...
Cloud native  – STS AssumeRole / temporary credentials (AWS), Workload Identity tokens (GCP/Azure).
```

## Benefits
```text
- Short TTL = a stolen secret is useless quickly (limits harvest-and-use).
- Per-consumer credentials = precise audit + revocation without impacting others.
- No standing secrets to rotate manually or leak in configs.
```

## Adoption tips
```text
- Authenticate apps via workload identity (not a static token) — see vault-patterns.
- Set TTLs to the shortest workable; handle credential renewal/re-fetch in the app.
- Prefer dynamic (DB/cloud/PKI/SSH) over static wherever the backend supports it.
- Combine with least-privilege roles + audit logging.
```

## Detection (Blue Team)
- Vault audit logs: anomalous credential generation volume; leases not expiring; broad roles.

## Sources
- [Vault dynamic secrets](https://developer.hashicorp.com/vault/docs/secrets/databases) · related: [vault-patterns](./vault-patterns.md), [secrets-vs-keys](../../cryptography/secrets-vs-keys.md)
