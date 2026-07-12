---
title: "Incident Response Policy"
category: "compliance"
tags: ["policies", "incident-response", "governance"]
platform: "agnostic"
mitre: []
difficulty: "basic"
updated: "2026-07-12"
author: "core"
---

# Incident Response Policy

## TL;DR
The IR policy is the governance document that authorizes and structures incident response: who's in charge, how incidents are classified, reporting obligations, and when to escalate. It sits above the operational runbooks (which are the "how"). Required by most frameworks (ISO 27001 A.5.24-A.5.28, SOC 2, PCI, NIS2/DORA).

## Policy vs plan vs runbook
```text
Policy   – authority, scope, roles, principles, obligations (this document).
Plan     – the overall IR process (NIST phases) — see blue-team/incident-response/ir-process.
Runbooks/playbooks – step-by-step for a scenario (ransomware, phishing, BEC).
```

## What the policy must define
```text
1. Purpose & scope       – what counts as a security incident; systems/data covered.
2. Roles & responsibilities – IR lead, CSIRT members, comms, legal, execs; on-call.
3. Incident classification – severity levels + examples + response SLAs.
4. Reporting & escalation – internal reporting path; regulatory clocks (GDPR 72h, NIS2 24h/72h, etc.).
5. Authority             – who can isolate systems, disable accounts, engage third parties.
6. Communication         – internal + external (customers, regulators, media) approvals.
7. Evidence & legal       – preservation, chain of custody, law enforcement engagement.
8. Post-incident         – lessons learned, review, metrics.
9. Testing               – tabletop/drill cadence.
10. Review               – owner, annual review.
```

## Severity classification (example)
```text
SEV1 – critical systems/data, active attack, regulatory breach -> immediate, 24/7, exec notify.
SEV2 – limited scope, escalation potential -> hours.
SEV3 – single host/low impact -> business day.
```

## Regulatory reporting clocks (know yours)
```text
GDPR   – notify authority within 72h of awareness (if personal-data breach).
NIS2   – early warning 24h, notification 72h, final report 1 month.
DORA   – major ICT incident reporting to competent authority.
PCI    – notify card brands/acquirer per contract; HIPAA per Breach Notification Rule.
```

## Best practices
- Keep the policy concise + approved by leadership; link to plans/runbooks for detail.
- Pre-authorize containment actions so responders don't wait on approvals mid-incident.
- Maintain contact lists (legal, PR, insurer, regulators, IR retainer); test them.
- Related: [ir-process](../../blue-team/incident-response/ir-process.md), [policy-templates](./policy-templates.md), [dora-nis2](../frameworks/dora-nis2.md).

## Sources
- [NIST SP 800-61r2](https://csrc.nist.gov/pubs/sp/800/61/r2/final) · [SANS IR policy templates](https://www.sans.org/information-security-policy/)
