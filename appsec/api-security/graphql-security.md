---
title: "GraphQL security"
category: "appsec"
tags: ["api-security", "graphql", "authorization", "dos"]
platform: "web"
mitre: []
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# GraphQL security

## TL;DR
GraphQL's flexibility is its risk: clients shape queries, so a single endpoint exposes introspection, deep/nested query DoS, batching abuse, and per-field authorization gaps. Authorization must be enforced in resolvers, not at the route.

## Introspection abuse
```graphql
# Introspection reveals the entire schema (types, fields, mutations)
{ __schema { types { name fields { name } } } }
```
```text
- Attackers map the full API (hidden fields, admin mutations) via introspection.
- Tools: GraphiQL, InQL (Burp), clairvoyance (recover schema even if introspection off).
- Mitigation: disable introspection in production; don't rely on it being "hidden".
```

## Denial of service (query complexity)
```graphql
# Deeply nested / cyclic query amplifies cost exponentially
{ user { friends { friends { friends { friends { name } } } } } }
```
```text
- Nested relationships -> huge resolver fan-out from a tiny request.
- Aliases multiply cost: same field requested many times under aliases.
- Mitigations: max query depth, cost/complexity analysis, pagination caps, timeouts.
```

## Batching attacks
```graphql
# Array of operations / aliased mutations bypass naive rate limits
[ { query: "mutation { login(pw:\"a\"){token} }" },
  { query: "mutation { login(pw:\"b\"){token} }" } ]
```
```text
- Batched/aliased requests brute-force (login, OTP) under a single HTTP request,
  evading per-request rate limits.
- Mitigation: limit batch size, rate-limit by operation, disable batching if unused.
```

## Authorization (BOLA/BFLA in GraphQL)
```text
- The endpoint is one route; per-object/per-field authz must live in RESOLVERS.
- BOLA: node(id:) or user(id:) returning other users' objects — check ownership.
- BFLA: admin mutations callable by normal users — check role per resolver.
- Field-level: sensitive fields (email, role) exposed on a shared type — authorize per field.
See appsec/api-security/owasp-api-top10.md (API1/API3/API5).
```

## Injection through resolvers
```text
- User input flows into DB/OS/other APIs inside resolvers -> SQLi/NoSQLi/SSRF.
- GraphQL doesn't sanitize for you; treat resolver args as untrusted.
See red-team/web/sqli.md and appsec/secure-coding/input-validation.md.
```

## Detection (Blue Team)
- Introspection queries in prod, abnormally deep/aliased queries, large batched operations.
- Repeated auth mutations under one request (batching brute-force).

## Mitigation / Hardening
- Disable introspection in prod; enforce **query depth + complexity limits** and timeouts.
- Use **persisted (allow-listed) queries** to restrict what clients can send.
- Authorize in every resolver (object, function, field); limit batch size + rate-limit by operation.
- Validate/parameterize resolver inputs; disable unused features (batching, arbitrary filters).

## Sources
- [OWASP – GraphQL CS](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html) · [InQL](https://github.com/doyensec/inql)
