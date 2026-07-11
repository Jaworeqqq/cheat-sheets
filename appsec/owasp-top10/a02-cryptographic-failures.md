---
title: "A02 – Cryptographic Failures"
category: "appsec"
tags: ["owasp", "cryptography", "tls"]
platform: "web"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# A02 – Cryptographic Failures

## TL;DR
Sensitive data exposed through missing or weak cryptography: plaintext storage/transit, weak algorithms, bad key management. Formerly "Sensitive Data Exposure".

## Common failures
```text
- Data in transit without TLS (or TLS misconfigured, downgradable)
- Passwords with fast/unsalted hashes (MD5, SHA1) instead of bcrypt/argon2
- Hardcoded keys / keys in source / weak key generation
- ECB mode, static IV, home-grown crypto
- Sensitive data (PII/PAN/tokens) stored in plaintext or logs
- Weak randomness (Math.random for tokens instead of a CSPRNG)
```

## Testing
```bash
# TLS config / weak ciphers / protocol versions
testssl.sh https://example.com
nmap --script ssl-enum-ciphers -p443 example.com
# Look for secrets/keys
gitleaks detect --source .
```

## Detection (Blue Team)
- TLS scanner in CI/monitoring, alerts on expiring/weak certs.
- DLP on sensitive data in logs / outbound traffic.

## Mitigation / Hardening
- TLS 1.2+ only, HSTS, strong ciphersuites, disable legacy protocols.
- Password hashing: **argon2id / bcrypt / scrypt** with per-user salt.
- Encryption at rest via KMS/HSM, key rotation, no keys in code.
- Use vetted libraries (libsodium, platform crypto), a CSPRNG for tokens.
- Classify data; encrypt/pseudonymize sensitive fields, minimize what you store.

## Sources
- [OWASP A02:2021](https://owasp.org/Top10/A02_2021-Cryptographic_Failures/) · [testssl.sh](https://testssl.sh/)
