# 🧩 Application Security

Application security from design to testing.

| Subdirectory | Scope |
|--------------|-------|
| [owasp-top10](./owasp-top10/) | One cheat sheet per OWASP Top 10 category (2021) |
| [api-security](./api-security/) | OWASP API Top 10, JWT, OAuth2/OIDC, rate limiting |
| [secure-coding](./secure-coding/) | Per-language patterns (Java, Python, JS, Go) |
| [threat-modeling](./threat-modeling/) | STRIDE, DREAD, attack trees, data flow diagrams |

## Priority backlog
- [x] `owasp-top10/` – overview + **A01–A10 all as separate files**
- [x] `api-security/` – jwt-attacks, oauth-oidc, owasp-api-top10
- [x] `threat-modeling/` – stride, attack-trees
- [x] `secure-coding/` – input-validation, deserialization, ssrf-prevention, csrf-defense
- [x] `api-security/graphql-security.md`, `owasp-top10/asvs-overview.md`
- [x] `secure-coding/secure-headers.md`, `api-security/rate-limiting.md`, `owasp-top10/mass-assignment.md`
- [ ] Todo: `secure-coding/cors`, `api-security/webhooks-security`, `threat-modeling/pasta`
