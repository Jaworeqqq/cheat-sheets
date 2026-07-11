---
title: "A10 – Server-Side Request Forgery (SSRF)"
category: "appsec"
tags: ["owasp", "ssrf", "cloud"]
platform: "web"
mitre: []
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# A10 – Server-Side Request Forgery (SSRF)

## TL;DR
The app fetches a user-controlled URL, letting an attacker reach internal resources (cloud metadata, internal services). Added to the Top 10 in 2021 by community survey. Exploitation detail in the red-team sheet.

## Why it's its own category
```text
- Cloud adoption made internal metadata endpoints (169.254.169.254) high-value targets.
- Modern apps make many server-side outbound requests (webhooks, imports, previews).
- Consistently impactful even if not the most frequent finding.
```

## Attack surface to review
```text
- URL fetchers: webhooks, PDF/image renderers, link previews, imports
- File schema handlers, XML parsers (SSRF via XXE)
- Redirect-following HTTP clients
```

## Detection (Blue Team)
- App layer connecting to internal/link-local IPs or metadata endpoints.
- Outbound request anomalies from services that shouldn't call arbitrary hosts.

## Mitigation / Hardening
- Allow-list destination hosts; block RFC1918/link-local; validate after DNS resolution.
- **IMDSv2** (AWS) / metadata protections; network segmentation (app can't reach metadata).
- Disable unused URL schemes, don't follow redirects to internal hosts.
- Full exploitation + payloads: [red-team/web/ssrf](../../red-team/web/ssrf.md).

## Sources
- [OWASP A10:2021](https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/) · [PortSwigger – SSRF](https://portswigger.net/web-security/ssrf)
