---
title: "SSRF prevention (defensive)"
category: "appsec"
tags: ["secure-coding", "ssrf", "defense"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# SSRF prevention (defensive)

## TL;DR
The defensive counterpart to the SSRF attack sheet. Preventing SSRF is hard because of redirects, DNS rebinding, and encoding tricks — layer allow-listing, network controls, and metadata protections. (Attack/exploitation: [red-team/web/ssrf](../../red-team/web/ssrf.md).)

## Why blocklists fail
```text
- Encodings: 127.0.0.1 == 0177.0.0.1 == 2130706433 == [::1] == 127.1
- DNS rebinding: domain resolves to a public IP at validation, internal IP at fetch.
- Redirects: allowed URL 302-redirects to an internal target.
- Alternate schemes: file://, gopher://, dict://
```

## Layered defenses
```text
1. Allow-list destinations (host + scheme) — deny by default.
2. Resolve DNS, then validate the RESOLVED IP is not private/link-local/loopback,
   and fetch that exact IP (prevents rebinding). Re-validate on every redirect.
3. Disable/limit redirects (or validate each hop).
4. Restrict schemes to http/https only.
5. Network egress controls: the service can't reach internal ranges / metadata.
6. Cloud metadata: enforce IMDSv2 (AWS); block 169.254.169.254 at the network.
```

## Safe fetch pattern (pseudocode)
```python
def safe_fetch(url):
    parsed = urlparse(url)
    assert parsed.scheme in ("http", "https")
    assert parsed.hostname in ALLOWED_HOSTS          # allow-list
    ip = resolve(parsed.hostname)
    assert not is_private(ip)                          # block RFC1918/loopback/link-local
    # pin the connection to `ip`; disable redirects OR re-validate each hop
    return http_get(url, allow_redirects=False, resolve_to=ip, timeout=5)
```

## Detection (Blue Team)
- App layer connecting to internal/link-local IPs or metadata endpoints; unusual outbound.

## Mitigation / Hardening (summary)
- Allow-list + resolve-then-validate + fetch-the-resolved-IP; no open redirects.
- Network segmentation so the app can't reach internal/metadata even if validation fails.
- IMDSv2 / metadata protections; least privilege on any role the app carries.

## Sources
- [OWASP – SSRF Prevention CS](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)
