---
title: "A07 – Identification and Authentication Failures"
category: "appsec"
tags: ["owasp", "authentication", "sessions"]
platform: "web"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# A07 – Identification and Authentication Failures

## TL;DR
Weaknesses in confirming identity and managing sessions: weak passwords, no MFA, credential stuffing, broken session management. Formerly "Broken Authentication".

## Common issues
```text
- Permits weak/known/default passwords, no brute-force protection
- Credential stuffing (reused breached passwords)
- No MFA on sensitive access
- Session fixation, predictable/long-lived session IDs
- Session ID in URL, no invalidation on logout/rotation on login
- Weak password recovery (knowledge questions, plaintext reset links)
- Missing/weak account lockout or rate limiting
```

## Testing
```text
- Try default creds, weak password policy, user enumeration (timing/messages)
- Check session cookie flags (HttpOnly, Secure, SameSite)
- Session doesn't rotate on login / isn't invalidated on logout?
- Password reset token entropy / reuse / expiry
```

## Detection (Blue Team)
- Failed-login spikes, credential-stuffing patterns (many users, distributed IPs).
- Impossible travel, new-device logins without MFA.

## Mitigation / Hardening
- **MFA** (phishing-resistant where possible), ban weak/breached passwords (HIBP).
- Rate limiting + smart lockout, generic auth error messages (no enumeration).
- Secure sessions: rotate on login, invalidate on logout, short TTL, `HttpOnly`/`Secure`/`SameSite`.
- Server-generated high-entropy session IDs; use a vetted auth framework, don't roll your own.

## Sources
- [OWASP A07:2021](https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/) · [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)
