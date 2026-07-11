---
title: "OWASP Top 10 (2021) – overview"
category: "appsec"
tags: ["owasp", "web", "appsec"]
platform: "web"
mitre: []
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# OWASP Top 10 (2021)

## TL;DR
The ten most common classes of risk in web applications. A reference point for threat modeling, code review and testing.

## The list
| # | Category | Examples | Key mitigation |
|---|----------|----------|----------------|
| A01 | Broken Access Control | IDOR, path traversal, missing authz | deny-by-default, server-side authz |
| A02 | Cryptographic Failures | plaintext, weak algorithms, no TLS | TLS 1.2+, strong KDF, KMS |
| A03 | Injection | SQLi, XSS, command inj., LDAP | parameterization, encoding, validation |
| A04 | Insecure Design | no threat modeling, bad assumptions | secure design patterns, threat modeling |
| A05 | Security Misconfiguration | default passwords, verbose errors, open ports | hardening baseline, IaC scan |
| A06 | Vulnerable & Outdated Components | old libraries with CVEs | SCA, patch management, SBOM |
| A07 | Identification & Auth Failures | weak passwords, no MFA, session fixation | MFA, strong sessions, rate limit |
| A08 | Software & Data Integrity Failures | unsigned updates, insecure deserialization | signing, provenance, integrity checks |
| A09 | Security Logging & Monitoring Failures | no logs, no alerts | central logging, alerts, IR |
| A10 | Server-Side Request Forgery (SSRF) | requests to internal/metadata | allow-list, block RFC1918, IMDSv2 |

## How to use it
```text
- Threat modeling: walk the list per feature ("does A01 apply to this endpoint?").
- Code review / PR: a checklist mapped to the Top 10.
- Testing: cover every category (SAST + DAST + manual).
- Deeper requirements: OWASP ASVS (verifiable L1-L3 controls).
```

## Related cheat sheets
- [Broken Access Control](./a01-broken-access-control.md)
- Injection: [SQLi](../../red-team/web/sqli.md), [XSS](../../red-team/web/xss.md)
- [SSRF](../../red-team/web/ssrf.md), [JWT attacks](../api-security/jwt-attacks.md)

## Sources
- [OWASP Top 10](https://owasp.org/Top10/) · [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)
