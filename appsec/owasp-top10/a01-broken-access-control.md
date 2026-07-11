---
title: "A01 – Broken Access Control"
category: "appsec"
tags: ["owasp", "access-control", "idor"]
platform: "web"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# A01 – Broken Access Control

## TL;DR
The most common OWASP risk. A user does something they shouldn't be authorized to: access other people's data (IDOR), admin functions, or bypass authorization. Authorization **must** be enforced server-side.

## Common variants
```text
IDOR                 – /api/orders/123 -> change to 124 (someone else's order)
Missing function-level authz – admin button hidden, but /admin/* endpoint works
Vertical privesc     – regular user -> admin functions
Horizontal privesc   – user A -> user B's data
Metadata manipulation – role/permissions in JWT/cookie edited by the client
CORS misconfig       – Access-Control-Allow-Origin: * + credentials
Path traversal       – ../../etc/passwd
Force browsing       – direct URL to a protected resource
```

## Testing
```text
- Replay requests with another user's session (Burp Autorize) -> same data?
- Change IDs/UUIDs in parameters, JSON bodies, hidden fields.
- Remove/change authorization headers, test methods (GET->POST/PUT/DELETE).
- Test IDOR on exports, attachments, presigned URLs.
```

## Detection (Blue Team)
- Logs: access to many resource IDs by one user, 403 followed by success (bypass).
- Anomalies: a user pulling ID ranges sequentially.

## Mitigation / Hardening
- **Deny by default**; authorization per request server-side (not hiding in the UI).
- Check resource ownership (`resource.owner == currentUser`), don't trust client-supplied IDs.
- Unguessable identifiers (UUIDs) are defense-in-depth, not authorization.
- A central authz mechanism (policy engine), authorization tests in CI.

## Sources
- [OWASP A01:2021](https://owasp.org/Top10/A01_2021-Broken_Access_Control/) · [PortSwigger – Access control](https://portswigger.net/web-security/access-control)
