---
title: "Security policy templates"
category: "compliance"
tags: ["compliance", "policies", "governance"]
platform: "agnostic"
mitre: []
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# Security policy templates

## TL;DR
Policies are the documented "what and why" that auditors and staff rely on. Keep them concise, owned, versioned, approved, and reviewed at least annually. This is a starter set + a common structure.

## Standard policy structure
```text
1. Purpose & scope        2. Roles & responsibilities
3. Policy statements      4. Standards/procedures (or references)
5. Exceptions process     6. Enforcement/consequences
7. Review cycle & owner   8. Version history & approval
```

## Core policy set (map to ISO 27001 / SOC 2)
```text
- Information Security Policy (top-level, management intent)
- Access Control Policy (least privilege, RBAC, joiner/mover/leaver, MFA)
- Acceptable Use Policy (AUP)
- Data Classification & Handling Policy (+ retention)
- Cryptography / Key Management Policy
- Incident Response Policy (ties to blue-team/incident-response runbooks)
- Business Continuity / Disaster Recovery Policy (RTO/RPO)
- Change Management Policy
- Vulnerability & Patch Management Policy
- Secure Development Policy (SDLC, code review, dependency mgmt)
- Vendor / Third-Party Risk Policy (DPAs, assessments)
- Backup Policy (schedule, testing, immutability)
- Logging & Monitoring Policy
- Remote Work / BYOD Policy
```

## Access Control Policy – example statements
```text
- Access granted on least-privilege, need-to-know; approved by resource owner.
- MFA required for all remote and privileged access.
- Access reviewed quarterly; revoked within 24h of termination.
- Privileged access is just-in-time and logged.
```

## BC/DR Policy – key parameters
```text
- Define RTO (max downtime) and RPO (max data loss) per critical system.
- Backups tested by restore at a defined cadence; offsite/immutable copies.
- DR plan exercised at least annually; roles and comms defined.
```

## Best practices
- One owner per policy; approved by management; reviewed annually or on major change.
- Link policies to controls and evidence (see [audit/evidence-checklist](../audit/evidence-checklist.md)).
- Make them findable and enforceable — an unread policy is a control gap.

## Sources
- [SANS Security Policy Templates](https://www.sans.org/information-security-policy/) · [ISO 27001 Annex A](../frameworks/iso27001-annex-a.md)
