---
title: "Supply-chain & third-party phishing"
category: "red-team"
tags: ["initial-access", "phishing", "supply-chain", "social-engineering"]
platform: "agnostic"
mitre: ["T1566", "T1195"]
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# Supply-chain & third-party phishing

## TL;DR
Instead of phishing the target directly, abuse trusted relationships: compromise (or impersonate) a vendor/partner/tool the target already trusts, then deliver the lure through that channel. Trusted-sender context massively boosts success. Authorized engagements only.

## Vectors
```text
- Compromised vendor email -> phish the target from a legitimate, trusted account (BEC-style).
- Trusted SaaS/OAuth app -> malicious OAuth consent / app impersonation.
- Software update / package -> trojanized dependency or update (dependency confusion angle).
- Managed service provider (MSP) access -> pivot into downstream customers.
- Shared collaboration tools (Slack/Teams/Jira) -> lure from an internal-looking source.
```

## Why it works
```text
- The sender/domain/tool is already allow-listed and trusted by users + filters.
- Established business context (real invoices, real projects) makes the pretext believable.
- OAuth consent grants persistent access without a password (survives password resets).
```

## Techniques
```text
- OAuth consent phishing: register an app, request broad Graph scopes, lure the user to consent
  -> tokens to mailbox/files (no credential needed). See cloud-security/azure/entra-enumeration.
- Vendor-email compromise -> reply-chain injection into an existing thread.
- Typosquatted/lookalike partner domains for impersonation.
```

## Detection (Blue Team)
- OAuth app consents to unknown/over-privileged apps; new enterprise app registrations.
- Reply-chain emails with anomalous links/attachments from otherwise-trusted senders.
- Vendor/partner sending from new infrastructure (SPF/DKIM/geo anomalies); first-time app usage.

## Mitigation / Hardening
- Restrict OAuth app consent (admin consent workflow); review third-party app permissions.
- Phishing-resistant MFA; verify high-risk requests out-of-band even from trusted senders.
- Third-party risk management (see compliance/vendor-risk); monitor lookalike domains.
- Least-privilege MSP/vendor access; segment and audit it.

## Sources
- [MITRE T1195](https://attack.mitre.org/techniques/T1195/) · related: [phishing](./phishing.md), [dependency-confusion](../../devsecops/supply-chain/dependency-confusion.md)
