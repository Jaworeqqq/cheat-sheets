---
title: "Hash identification"
category: "cryptography"
tags: ["cryptography", "hashes", "password-cracking"]
platform: "agnostic"
mitre: []
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# Hash identification

## TL;DR
Before cracking, identify the hash type (it sets the hashcat `-m` mode). Recognize by length, character set, and prefix/format markers.

## Tools
```bash
hashid '5f4dcc3b5aa765d61d8327deb882cf99'
name-that-hash --text '<hash>'       # nth
hashcat --identify hash.txt           # hashcat's own guesser
```

## Recognize by format
```text
32 hex chars        – MD5 or NTLM (context! NTLM from Windows, MD5 elsewhere)
40 hex chars        – SHA1
64 hex chars        – SHA256
128 hex chars       – SHA512
$2a$/$2b$/$2y$...   – bcrypt
$1$...              – md5crypt (Unix)
$5$... / $6$...     – SHA-256 / SHA-512 crypt (Unix /etc/shadow)
$argon2id$...       – Argon2
$krb5tgs$23$...     – Kerberoast (RC4)   -> hashcat -m 13100
$krb5asrep$23$...   – AS-REP roast       -> hashcat -m 18200
aad3b435...:<32hex> – LM:NT (NTLM hash pair)
{SSHA}...           – LDAP salted SHA1
```

## Quick length reference
| Length (hex) | Likely type |
|--------------|-------------|
| 32 | MD5 / NTLM |
| 40 | SHA1 |
| 56 | SHA224 |
| 64 | SHA256 |
| 96 | SHA384 |
| 128 | SHA512 |

## Notes / pitfalls
- Length alone is ambiguous (MD5 vs NTLM both 32 hex) — use context (where it came from).
- Salted/format-prefixed hashes are easier: the `$id$` marker tells you the scheme.
- Once identified → pick the hashcat mode: see [password-cracking](./password-cracking.md).

## Sources
- [hashcat example hashes](https://hashcat.net/wiki/doku.php?id=example_hashes) · [Name-That-Hash](https://github.com/HashPals/Name-That-Hash)
