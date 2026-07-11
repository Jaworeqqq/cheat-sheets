---
title: "IR Playbook – Business Email Compromise (BEC)"
category: "blue-team"
tags: ["incident-response", "bec", "playbook", "fraud"]
platform: "agnostic"
mitre: ["T1114", "T1078"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# IR Playbook – Business Email Compromise (BEC)

## TL;DR
BEC = an attacker with access to (or impersonating) a mailbox commits fraud, usually invoice/payment redirection. Financial and identity incident: contain the account, stop the money, investigate the mailbox.

## 1. Detection signals
```text
- Finance reports a changed bank account / unexpected wire request.
- Anomalous sign-in (impossible travel), MFA method added, legacy-auth login.
- New inbox rules hiding/forwarding messages (esp. containing "invoice","payment","wire").
- Lookalike domain impersonating an executive/vendor.
```

## 2. Containment (identity + money in parallel)
```text
Identity:
 - Revoke all sessions/tokens, reset password, re-enroll MFA, remove attacker MFA methods.
 - Remove malicious inbox/forwarding rules; revoke rogue OAuth app grants.
Money:
 - Immediately contact the bank to recall/hold the transfer (time-critical).
 - Notify finance to freeze/verify pending payments out-of-band (phone, known number).
```

## 3. Investigation
```text
- Audit logs: rule creation, mail access, delegate/forwarding changes, mailbox exports.
- Determine dwell time, what was read/exfiltrated, other targeted mailboxes.
- Identify the initial vector (phish/AiTM/credential stuffing).
```

## 4. Recovery & reporting
```text
- Restore clean access, verify no persistence (rules, apps, delegates).
- Report per policy: fraud/legal, insurer, and authorities (e.g. IC3/FBI, local CERT).
```

## Detection (Blue Team)
```kql
// Mailbox rule forwarding externally
OfficeActivity | where Operation in ("New-InboxRule","Set-InboxRule")
| where Parameters has_any ("ForwardTo","RedirectTo")
```
- Alert on new-domain lookalikes, external auto-forwarding, mass mailbox reads.

## Mitigation / Hardening
- Phishing-resistant MFA, block legacy auth, disable external auto-forwarding by default.
- **Out-of-band verification** for any bank-detail/payment change (process control).
- DMARC enforcement, impersonation protection, restrict OAuth consent.

## Sources
- [FBI IC3 – BEC](https://www.ic3.gov/) · [Microsoft – BEC response](https://learn.microsoft.com/defender-office-365/)
