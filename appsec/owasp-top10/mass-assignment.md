---
title: "Mass assignment"
category: "appsec"
tags: ["owasp", "mass-assignment", "api-security"]
platform: "web"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Mass assignment

## TL;DR
The app binds client-supplied fields directly to internal objects/models, so an attacker can set fields they shouldn't (e.g. `isAdmin`, `role`, `balance`, `verified`). Maps to OWASP API3 (Broken Object Property Level Authorization). Root cause: trusting the whole request body.

## How it works
```text
Client sends extra JSON fields; the framework auto-binds them to the model:
  POST /api/users {"name":"bob","email":"..."}          # intended
  POST /api/users {"name":"bob","email":"...","role":"admin","isVerified":true}  # attack
If the model updates from the raw body, role/isVerified get set.
```

## Finding it
```text
- Capture a legitimate request; add sensitive fields you observed elsewhere
  (from GET responses, docs, source): role, isAdmin, userId, accountId, price, status.
- Try nested objects and arrays; try on create AND update endpoints.
- Watch for privilege/state changes reflected in the response or subsequent behavior.
```

## Framework flavors
```text
Rails    – strong params (permit) missing -> mass assignment.
Spring   – @ModelAttribute binding without allow-list / @InitBinder.
Node/JS  – Object.assign(model, req.body) / spread of the whole body.
Django   – ModelForm with fields = '__all__'.
Laravel  – $fillable/$guarded misconfigured; ->fill($request->all()).
```

## Detection (Blue Team)
- Unexpected privilege/state changes; requests containing fields not in the UI/form.
- Audit logs of sensitive attribute changes (role, permissions) via non-admin endpoints.

## Mitigation / Hardening
- **Allow-list bindable fields** (explicit DTOs / strong params) — never bind the raw body.
- Separate input models from persistence models; ignore/reject unknown fields.
- Authorize sensitive attribute changes independently (role/permissions via admin-only flows).
- Related: [a01-broken-access-control](./a01-broken-access-control.md), [owasp-api-top10](../api-security/owasp-api-top10.md), [input-validation](../secure-coding/input-validation.md).

## Sources
- [OWASP – Mass Assignment CS](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html) · [OWASP API3:2023](https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/)
