---
title: "Breach data & credential exposure"
category: "osint"
tags: ["osint", "breaches", "credentials"]
platform: "agnostic"
mitre: ["T1589"]
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# Breach data & credential exposure

## TL;DR
Public/leaked breach datasets reveal exposed emails, passwords and PII for a target org. Used (with authorization) to assess credential exposure and seed password spraying; used defensively to protect users. Handle responsibly and legally.

## Checking exposure
```bash
# HaveIBeenPwned – is an email/domain in known breaches (API key for domain search)
curl -s -H "hibp-api-key: $KEY" \
  "https://haveibeenpwned.com/api/v3/breachedaccount/user@example.com"
# Domain-wide breach search (HIBP Domain Search – for domains you own/authorized)

# Password exposure without sending the password (k-anonymity range API)
# SHA1 the password, send first 5 hex chars, match the suffix locally
curl -s https://api.pwnedpasswords.com/range/21BD1   # returns suffixes+counts
```

## Sources of breach data
```text
- HaveIBeenPwned – breach index, Pwned Passwords (k-anonymity)
- Dehashed / IntelX / Snusbase – searchable breach corpora (authorized use)
- Public paste sites / forums – dumps (monitor for your org)
- Combolists / stealer logs – increasingly the real threat (session + creds)
```

## Legal / ethical note
```text
Only use in authorized engagements. Possessing/handling breach data may be regulated;
never expose or re-share PII. Prefer exposure *checks* over holding raw dumps.
```

## Detection / defense (Blue Team)
- Monitor your domains in HIBP; watch for stealer-log/combolist appearances.
- Correlate exposed creds with sign-in attempts (credential stuffing).

## Mitigation / Hardening
- Ban breached passwords (HIBP Pwned Passwords in your auth flow).
- Enforce MFA (esp. phishing-resistant) — neutralizes leaked passwords.
- Proactive resets for exposed accounts; monitor for stealer-log infections.

## Sources
- [HaveIBeenPwned](https://haveibeenpwned.com/) · [Pwned Passwords (k-anonymity)](https://haveibeenpwned.com/API/v3#PwnedPasswords)
