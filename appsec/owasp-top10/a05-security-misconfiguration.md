---
title: "A05 – Security Misconfiguration"
category: "appsec"
tags: ["owasp", "misconfiguration", "hardening"]
platform: "web"
mitre: []
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# A05 – Security Misconfiguration

## TL;DR
Insecure defaults, incomplete configuration, verbose errors, unnecessary features enabled. Includes XXE and missing security headers. The most "operational" of the Top 10.

## Common issues
```text
- Default credentials / accounts left enabled
- Verbose errors / stack traces exposed to users
- Directory listing, exposed admin panels, debug endpoints
- Missing security headers (CSP, HSTS, X-Content-Type-Options)
- Unnecessary services/ports/features enabled
- Cloud storage/services publicly accessible
- Outdated software with default config
```

## Testing
```bash
# Security headers
curl -sI https://example.com | grep -iE 'content-security|strict-transport|x-frame|x-content'
# Broad misconfig / exposure scanning
nuclei -u https://example.com -t exposures/ -t misconfiguration/
nikto -h https://example.com
```

## Key security headers
```text
Content-Security-Policy         – mitigates XSS
Strict-Transport-Security       – enforces HTTPS (HSTS)
X-Content-Type-Options: nosniff – no MIME sniffing
X-Frame-Options / frame-ancestors – clickjacking
Referrer-Policy, Permissions-Policy
```

## Detection (Blue Team)
- Config drift detection, exposure scanning in CI (IaC scan too).
- Alert on debug/admin endpoints reachable externally.

## Mitigation / Hardening
- Hardened baselines (CIS), minimal install, disable defaults/debug.
- Automated, repeatable config via IaC; scan it (see devsecops/iac).
- Ship all security headers; generic error pages; segment cloud access.

## Sources
- [OWASP A05:2021](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/) · [OWASP Secure Headers](https://owasp.org/www-project-secure-headers/)
