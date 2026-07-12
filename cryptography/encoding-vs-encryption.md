---
title: "Encoding vs Encryption vs Hashing"
category: "cryptography"
tags: ["cryptography", "encoding", "hashing", "fundamentals"]
platform: "agnostic"
mitre: []
difficulty: "basic"
updated: "2026-07-12"
author: "core"
---

# Encoding vs Encryption vs Hashing

## TL;DR
A common confusion that causes real vulnerabilities. **Encoding** is reversible with no secret (not security). **Encryption** is reversible with a key (confidentiality). **Hashing** is one-way (integrity/verification). Base64 is NOT encryption.

## The three, side by side
| | Purpose | Reversible? | Needs a key? |
|---|---------|-------------|--------------|
| Encoding | data representation/transport | yes, by anyone | no |
| Encryption | confidentiality | yes, with the key | yes |
| Hashing | integrity / verification | no (one-way) | no (but salt/pepper) |

## Encoding (NOT security)
```text
Examples: Base64, hex, URL-encoding, ASCII, Unicode.
Purpose:  safely represent/transport binary data as text.
Reverse:  trivially, no secret needed.
```
```bash
echo -n "secret" | base64        # c2VjcmV0   <- this is NOT protected
echo -n "c2VjcmV0" | base64 -d   # secret     <- anyone can reverse it
```
⚠️ Storing/transmitting a "base64-encoded password" gives ZERO protection.

## Encryption (confidentiality)
```text
Symmetric  – same key encrypts/decrypts (AES-GCM, ChaCha20). Fast; key distribution problem.
Asymmetric – public key encrypts, private key decrypts (RSA, ECC). Solves key distribution.
Needs: a secret key + proper mode (AEAD), IV/nonce handling, key management.
```
```bash
openssl enc -aes-256-cbc -pbkdf2 -in file -out file.enc   # reversible ONLY with the key
```

## Hashing (one-way)
```text
Purpose: verify integrity / store passwords (can't get the input back).
General-purpose (fast): SHA-256, SHA-3 -> for integrity/checksums.
Password hashing (slow, salted): bcrypt, scrypt, argon2 -> NEVER use fast hashes for passwords.
```
```bash
sha256sum file                    # integrity check
# passwords -> argon2/bcrypt with per-user salt, not sha256(password)
```

## Common mistakes
```text
- "We base64 the password" = not protected.
- Encrypting passwords instead of hashing them (should be one-way + salted).
- Using fast hashes (MD5/SHA1) for passwords -> trivially cracked (see password-cracking).
- Confusing encoding with signing/integrity.
```

## Sources
- [OWASP – Cryptographic Storage CS](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · related: [password-cracking](./password-cracking.md)
