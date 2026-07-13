---
title: "OAuth abuse (offensive)"
category: "red-team"
tags: ["web", "oauth", "authentication", "phishing"]
platform: "web"
mitre: ["T1528", "T1550.001"]
difficulty: "advanced"
updated: "2026-07-13"
author: "core"
---

# OAuth abuse (offensive)

## TL;DR
OAuth flows are attacked at the redirect, the consent, and the token. Common wins: stealing authorization codes/tokens via redirect_uri flaws, tricking users into consenting to a malicious app (illicit consent grant), and abusing device-code flow for phishing. Defensive side: [appsec/api-security/oauth-oidc](../../appsec/api-security/oauth-oidc.md).

## Attack surface
```text
redirect_uri – open redirect / loose validation -> steal codes/tokens.
state/PKCE    – missing state (CSRF on callback) / missing PKCE (code interception).
consent       – illicit consent grant: malicious app requests broad scopes, user approves.
device code   – phish a user to enter a code, attacker gets the token (no password/MFA prompt on app).
token         – leakage via Referer/logs/history; replay if aud/exp unchecked.
```

## Illicit consent grant (very effective vs M365/Google)
```text
1. Register an OAuth app (attacker tenant) requesting scopes like Mail.Read, Files.Read.All, offline_access.
2. Send the victim a legit-looking "grant access" link (real IdP consent page).
3. Victim consents -> attacker receives access + refresh tokens to their mailbox/files.
   No password, survives password reset (revoke the grant to stop it). See supply-chain-phishing.
```

## Device-code phishing
```text
- Start a device-code flow; get a user_code + verification URL.
- Lure the victim to the REAL login page to enter the code.
- Poll the token endpoint -> receive tokens once they authenticate (bypasses the app's own login).
```

## redirect_uri / code theft
```text
- Loose matching (prefix/regex) or open redirect on an allowed host -> redirect the code to attacker.
- No PKCE on public clients -> intercept the authorization code and exchange it.
```

## Detection (Blue Team)
- New enterprise app consents to broad scopes; consents to apps from other tenants.
- Token use from anomalous locations; offline_access grants; device-code sign-ins.

## Mitigation / Hardening
- Restrict app consent (admin consent workflow); review third-party app grants regularly.
- Exact redirect_uri allow-list; enforce state + PKCE; validate all token claims.
- Block/limit device-code where unused; phishing-resistant MFA; revoke risky grants.

## Sources
- [Microsoft – Illicit consent grant](https://learn.microsoft.com/security/operations/incident-response-playbook-app-consent) · [MITRE T1528](https://attack.mitre.org/techniques/T1528/)
