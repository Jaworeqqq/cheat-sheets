---
title: "Secrets vs Keys"
category: "cryptography"
tags: ["cryptography", "secrets", "key-management", "fundamentals"]
platform: "agnostic"
mitre: []
difficulty: "basic"
updated: "2026-07-12"
author: "core"
---

# Secrets vs Keys

## TL;DR
"Secret" and "key" are often used interchangeably but managing them differs. A **cryptographic key** is used by an algorithm to encrypt/sign; a **secret** is any sensitive credential (API token, password, connection string). Keys belong in a KMS/HSM; general secrets belong in a secrets manager. Different tools, overlapping principles.

## The distinction
```text
Cryptographic key – input to a crypto operation (AES key, RSA/EC private key, HMAC key).
                    Ideally NEVER leaves the boundary that uses it (HSM/KMS); used, not read.
Secret            – any credential the app needs (DB password, API key, OAuth client secret,
                    TLS private key is BOTH). Apps typically read the value at runtime.
```

## Where each lives
```text
Keys    -> KMS / HSM (AWS KMS, Azure Key Vault keys, GCP KMS, CloudHSM).
           Envelope encryption; key never exposed in plaintext (see key-management).
Secrets -> Secrets manager (Vault, AWS Secrets Manager, Azure Key Vault secrets, GCP Secret Manager),
           delivered to apps via workload identity (see devsecops/secrets-management).
Note: cloud "Key Vaults" hold both keys AND secrets — but the handling differs.
```

## Shared principles
```text
- Never in code, config files, or git (see devsecops/secrets-management/secrets-detection).
- Least-privilege access + full audit logging.
- Rotation (keys: rotate KEKs; secrets: rotate credentials, prefer dynamic/short-lived).
- Encryption in transit + at rest; no plaintext at rest.
```

## Key differences in handling
```text
Keys    – "use, don't read": operations happen inside the KMS/HSM; app gets ciphertext, not the key.
          Rotation via envelope encryption (rotate KEK, re-wrap DEKs).
Secrets – "read at runtime": app fetches the value; prefer dynamic secrets (short TTL, auto-revoke).
          Rotation = issue a new credential and revoke the old.
```

## Quick guidance
```text
- Encrypting/signing data -> a KEY -> KMS/HSM, use envelope encryption.
- App needs a password/token to call something -> a SECRET -> secrets manager + workload identity.
- Prefer dynamic/short-lived over long-lived static for both.
```

## Sources
- [OWASP – Secrets Management CS](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) · related: [key-management](./key-management.md), [vault-patterns](../devsecops/secrets-management/vault-patterns.md)
