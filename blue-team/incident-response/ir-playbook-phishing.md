---
title: "IR Playbook – Phishing"
category: "blue-team"
tags: ["incident-response", "phishing", "playbook"]
platform: "agnostic"
mitre: ["T1566"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# IR Playbook – Phishing

## TL;DR
Triage a reported/detected phish, determine who clicked/entered creds, contain (revoke sessions, reset), hunt for the same campaign, remediate. Speed on credential/session revocation is critical for AiTM.

## 1. Triage
```text
- Preserve the original email (headers, .eml) — don't just forward.
- Analyze: sender/SPF-DKIM-DMARC, URLs (detonate in sandbox), attachments (hash, sandbox).
- Classify: credential harvest / malware / BEC / AiTM (session theft).
- Scope: who received it? who clicked? who submitted credentials?
```

## 2. Containment
```text
- Block sender/domain/URL at the mail gateway + proxy; sinkhole the domain.
- Pull the message from all mailboxes (e.g. purge/soft-delete across tenant).
- For clickers/credential-submitters:
    * Revoke sessions/tokens (critical vs AiTM — password reset alone is NOT enough).
    * Reset password, require re-MFA, review MFA method changes.
- Isolate hosts if malware executed.
```

## 3. Investigation / hunt
```text
- Sign-in logs: risky/anomalous logins after the click, new MFA registrations.
- Mailbox rules created (auto-forward/hide) = account takeover indicator.
- Hunt the campaign: same URL/sender/subject across the org.
```

## 4. Eradication & recovery
```text
- Remove malicious mail rules, revoke rogue OAuth grants, clean any malware.
- Restore normal access after verifying no persistence.
```

## 5. Post-incident
```text
- Update mail rules/detections, add IOCs, targeted awareness for affected users.
```

## Detection queries (Defender/Sentinel)
```kql
// New inbox forwarding rule (takeover signal)
OfficeActivity | where Operation in ("New-InboxRule","Set-InboxRule")
| where Parameters has_any ("ForwardTo","RedirectTo","DeleteMessage")
```

## Mitigation / Hardening
- Phishing-resistant MFA (FIDO2), block legacy auth, mail auth (DMARC reject).
- Easy "report phishing" button, auto-triage/SOAR, restrict OAuth consent.

## Sources
- [CISA – Phishing Guidance](https://www.cisa.gov/) · [Microsoft – Respond to a compromised account](https://learn.microsoft.com/defender-office-365/)
