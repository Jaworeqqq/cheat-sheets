---
title: "Phishing – initial access"
category: "red-team"
tags: ["initial-access", "phishing", "social-engineering"]
platform: "agnostic"
mitre: ["T1566"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Phishing – initial access

## TL;DR
Vectors: link to a fake login page (credential harvest), malicious attachment (macro/HTA/LNK), or OAuth consent (device code). Always within an authorized engagement and agreed scope.

## Requirements / Context
- A trusted (aged) domain, correct SPF/DKIM/DMARC on the sending infrastructure.
- A pretext tailored to the target (OSINT).

## Techniques
```text
1. Credential harvesting  – Evilginx2 (reverse proxy, also steals session/MFA), GoPhish (landing)
2. Attachment payload      – VBA macros, .lnk → LOLBin, .iso/.img (bypasses MOTW), HTML smuggling
3. OAuth Device Code       – victim enters a code, attacker receives a token (bypasses password)
```

```bash
# GoPhish – campaign framework (landing + tracking)
./gophish   # panel on :3333

# Evilginx2 – phishlet for adversary-in-the-middle (steals session cookie + MFA)
evilginx2 -p ./phishlets
```

## Detection (Blue Team)
- Newly registered / lookalike domains (typosquatting) — monitoring.
- Email gateway: SPF/DKIM/DMARC anomalies, links to fresh domains, HTML with JS blob.
- **Sign-in from an unusual geolocation right after a click** (AiTM → stolen session).

## Mitigation / Hardening
- Phishing-resistant MFA: **FIDO2 / passkeys** (Evilginx cannot bypass it).
- Block legacy auth, restrict OAuth consent, enforce MOTW.
- Training + an easy "report phishing" button.

## Notes / Pitfalls
- FIDO2 defeats AiTM; plain TOTP/SMS does not.

## Sources
- [Evilginx](https://github.com/kgretzky/evilginx2) · [GoPhish](https://getgophish.com/)
