---
title: "IDOR (Insecure Direct Object Reference)"
category: "red-team"
tags: ["web", "idor", "access-control", "owasp"]
platform: "web"
mitre: ["T1190"]
difficulty: "basic"
updated: "2026-07-12"
author: "core"
---

# IDOR

## TL;DR
The app exposes a reference to an object (ID, filename, key) and doesn't verify the requester owns it — so changing the reference accesses someone else's data. A subclass of Broken Access Control (OWASP A01 / API1 BOLA). Simple, common, high-impact.

## Finding it
```text
- Any request carrying an object identifier: /api/orders/1043, ?userId=42,
  filename=invoice_88.pdf, JSON {"account_id": 7}, GraphQL node(id:).
- Change the value to another (adjacent, guessed, or another account's) ID.
- Test everywhere: path, query, body, headers, cookies, multipart fields.
```

## Techniques
```text
- Sequential IDs -> increment/decrement (1043 -> 1042).
- UUIDs/hashes -> harder, but check if leaked elsewhere (listing, referer, other endpoints).
- Method/param swaps -> GET works with authz, does DELETE/PUT skip it?
- Nested/second-order -> ID accepted in one flow, used unchecked in another.
- Mass tools: Burp Autorize (replay with a low-priv session), Turbo Intruder for ranges.
```

## Example
```http
GET /api/v1/orders/1043 HTTP/1.1
Cookie: session=<user-A>
# -> returns user B's order? IDOR (no ownership check).
```

## Detection (Blue Team)
- One account accessing many distinct object IDs, especially sequential ranges.
- 403-then-200 patterns (probing), access to objects the user never created.

## Mitigation / Hardening
- **Enforce ownership server-side** on every object access (`object.owner == currentUser`).
- Deny by default; centralized authorization checks, not per-endpoint ad hoc.
- Unguessable IDs (UUID) are defense-in-depth, NOT a substitute for authorization.
- Authorization tests in CI; see [appsec/owasp-top10/a01-broken-access-control](../../appsec/owasp-top10/a01-broken-access-control.md).

## Sources
- [PortSwigger – IDOR](https://portswigger.net/web-security/access-control/idor) · [OWASP API1 BOLA](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/)
