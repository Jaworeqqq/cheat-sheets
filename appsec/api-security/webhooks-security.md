---
title: "Webhook security"
category: "appsec"
tags: ["api-security", "webhooks", "ssrf"]
platform: "web"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Webhook security

## TL;DR
Webhooks are HTTP callbacks between systems — both directions have risk. **Receiving** webhooks: verify authenticity (anyone can POST to your URL). **Sending** webhooks (user-configurable URLs): guard against SSRF and abuse. Both are commonly overlooked.

## Receiving webhooks (you are the endpoint)
```text
Threats: forged events (anyone can hit the URL), replay, tampering.
Defenses:
 - Verify a signature (HMAC of the body with a shared secret) — the standard (Stripe/GitHub style).
 - Constant-time comparison of signatures; reject on mismatch.
 - Replay protection: include+check a timestamp; reject old events; idempotency keys.
 - Validate payload schema; don't trust amounts/status from the body alone (verify via API).
```
```python
# Verify HMAC signature (pseudocode)
expected = hmac_sha256(secret, raw_body)
if not hmac.compare_digest(expected, header_signature): reject()
if abs(now - payload.timestamp) > 300: reject()   # replay window
```

## Sending webhooks (you call a user-configured URL)
```text
Threat: SSRF — a user sets the webhook URL to http://169.254.169.254 / internal services.
Defenses:
 - Allow-list schemes (https), resolve DNS then block private/link-local/loopback IPs,
   fetch the resolved IP, re-validate on redirects (see secure-coding/ssrf-prevention).
 - Egress controls so the webhook sender can't reach internal/metadata.
 - Sign your outgoing requests so receivers can verify you; document your signing scheme.
 - Rate limit / timeout / retry with backoff; don't leak internal errors to the target.
```

## Detection (Blue Team)
- Webhook sender connecting to internal/metadata IPs (SSRF); floods of unverified inbound webhooks.
- Signature-verification failures spiking (forgery attempts).

## Mitigation / Hardening
- Inbound: HMAC signature + timestamp/replay checks + schema validation + idempotency.
- Outbound: SSRF-safe fetch (allow-list + resolved-IP checks), egress restrictions, sign requests.
- Rotate webhook secrets; scope least privilege on what a webhook can trigger.
- Related: [ssrf-prevention](../secure-coding/ssrf-prevention.md), [rate-limiting](./rate-limiting.md).

## Sources
- [OWASP – SSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html) · [Standard Webhooks](https://www.standardwebhooks.com/)
