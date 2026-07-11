---
title: "Secure coding – validation and output encoding"
category: "appsec"
tags: ["secure-coding", "input-validation", "injection"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Input validation and output encoding

## TL;DR
Most injection (SQLi/XSS/cmd) comes from mixing data with code. Rules: validate input (allow-list), separate data from commands (parameterization), encode output per context.

## Input validation
```text
- Allow-list > deny-list (define what's allowed, not what's forbidden).
- Validate: type, length, range, format (regex), canonical form.
- Validate at the trust boundary (server), NOT only in the client.
- Reject, don't silently "fix" (sanitization is often bypassable).
```

## Separating data from commands (per context)
```java
// SQL – prepared statement (NOT concatenation)
PreparedStatement ps = conn.prepareStatement("SELECT * FROM u WHERE id = ?");
ps.setInt(1, userId);
```
```python
# Command – argv, NOT shell=True with interpolation
subprocess.run(["ping", "-c", "1", host])   # not f"ping {host}" in a shell
```
```javascript
// Output encoding – context-aware
res.send(escapeHtml(userInput));   // HTML context
// framework with auto-escape (React {var}, Jinja autoescape) instead of innerHTML
```

## Context → defense mapping
| Context | Risk | Defense |
|---------|------|---------|
| SQL | SQLi | prepared statements / ORM binding |
| HTML | XSS | HTML entity encoding, auto-escape |
| OS command | command inj. | argv array, no shell, allow-list |
| LDAP | LDAP inj. | escaping DN/filter |
| Path | traversal | canonicalization + allow-list, no `..` |
| Deserialization | RCE | don't deserialize untrusted; code-free formats (JSON) |

## Verification
- SAST (Semgrep/CodeQL) on injection patterns, code review, testing with payloads.

## Sources
- [OWASP Input Validation CS](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) · [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
