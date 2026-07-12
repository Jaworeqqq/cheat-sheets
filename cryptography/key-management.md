---
title: "Key management"
category: "cryptography"
tags: ["cryptography", "key-management", "kms", "hsm"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Key management

## TL;DR
Cryptography is only as strong as its key management. Most real-world crypto failures are key-management failures: hardcoded keys, no rotation, weak generation, keys stored next to the data. Manage the full key lifecycle and keep keys in dedicated systems (KMS/HSM).

## Key lifecycle
```text
Generate  – use a CSPRNG / KMS/HSM; correct length; never predictable seeds.
Store     – in a KMS/HSM or secrets manager; never in code, config, or repos.
Distribute – deliver securely (envelope encryption, wrapping); least access.
Use       – separate keys per purpose (encryption vs signing vs MAC).
Rotate    – periodically + on suspected compromise; support multiple active versions.
Revoke    – invalidate compromised keys; re-encrypt/re-sign as needed.
Destroy   – securely delete retired key material (crypto-shredding).
```

## Envelope encryption (the standard pattern)
```text
- Data Encryption Key (DEK) encrypts the data (symmetric, fast).
- Key Encryption Key (KEK) in the KMS/HSM encrypts (wraps) the DEK.
- Store the wrapped DEK next to the data; the KEK never leaves the KMS.
- To rotate: rotate the KEK (re-wrap DEKs) without re-encrypting all data.
```

## Where to keep keys
```text
Cloud KMS   – AWS KMS, Azure Key Vault, GCP KMS (managed, audited, IAM-controlled).
HSM         – hardware root of trust; keys never leave in plaintext (CloudHSM, on-prem HSM).
Secrets mgr – Vault/cloud secret managers for app secrets (see devsecops/secrets-management).
```

## Principles
```text
- One key per purpose/scope; don't reuse keys across systems or purposes.
- Least privilege on key usage (who can encrypt/decrypt/sign); full audit logging.
- Automate rotation; keep old versions only to decrypt/verify, not to produce new data.
- Never log keys; never commit them (see secrets-detection); crypto-shred on deletion.
```

## Detection (Blue Team)
- KMS audit logs: anomalous decrypt/sign volume, access from unexpected identities/regions.
- Alert on key policy changes, disabled key rotation, use of long-lived static keys.

## Sources
- [NIST SP 800-57 (key management)](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final) · [OWASP – Key Management CS](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html)
