---
title: "OWASP Top 10 (2021) – przegląd"
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
Dziesięć najczęstszych klas ryzyk w aplikacjach webowych. Punkt odniesienia dla threat modelingu, code review i testów.

## Lista
| # | Kategoria | Przykłady | Kluczowa mitygacja |
|---|-----------|-----------|--------------------|
| A01 | Broken Access Control | IDOR, path traversal, brak autoryzacji | deny-by-default, authz po stronie serwera |
| A02 | Cryptographic Failures | plaintext, słabe algorytmy, brak TLS | TLS 1.2+, silne KDF, KMS |
| A03 | Injection | SQLi, XSS, command inj., LDAP | parametryzacja, encoding, walidacja |
| A04 | Insecure Design | brak threat modelingu, złe założenia | secure design patterns, threat modeling |
| A05 | Security Misconfiguration | domyślne hasła, verbose errors, otwarte porty | hardening baseline, IaC scan |
| A06 | Vulnerable & Outdated Components | stare biblioteki z CVE | SCA, patch management, SBOM |
| A07 | Identification & Auth Failures | słabe hasła, brak MFA, session fixation | MFA, silne sesje, rate limit |
| A08 | Software & Data Integrity Failures | niepodpisane update, insecure deserializ. | podpisy, provenance, integrity checks |
| A09 | Security Logging & Monitoring Failures | brak logów, brak alertów | centralne logi, alerty, IR |
| A10 | Server-Side Request Forgery (SSRF) | żądania do internal/metadata | allow-list, blokada RFC1918, IMDSv2 |

## Jak używać
```text
- Threat modeling: przejdź listę per feature ("czy A01 dotyczy tego endpointu?").
- Code review / PR: checklist mapowany na Top 10.
- Testy: pokrycie każdej kategorii (SAST + DAST + manual).
- Głębsze wymagania: OWASP ASVS (weryfikowalne kontrole L1-L3).
```

## Powiązane ściągawki
- [Broken Access Control](./a01-broken-access-control.md)
- Injection: [SQLi](../../red-team/web/sqli.md), [XSS](../../red-team/web/xss.md)
- [SSRF](../../red-team/web/ssrf.md), [JWT attacks](../api-security/jwt-attacks.md)

## Źródła
- [OWASP Top 10](https://owasp.org/Top10/) · [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)
