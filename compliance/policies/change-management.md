---
title: "Change Management Policy"
category: "compliance"
tags: ["policies", "change-management", "governance"]
platform: "agnostic"
mitre: []
difficulty: "basic"
updated: "2026-07-13"
author: "core"
---

# Change Management Policy

## TL;DR
Change management ensures changes to systems are reviewed, approved, tested, and documented — reducing outages and preventing unauthorized/insecure changes. It's a core control in every framework (ISO A.8.32, SOC 2 CC8, PCI Req 6) and a favorite audit sampling area. Modern DevOps automates much of it in the pipeline.

## Purpose
```text
- Prevent unauthorized or untested changes reaching production.
- Provide an audit trail (who changed what, when, approved by whom).
- Reduce risk of outages and security regressions; enable rollback.
```

## Core elements
```text
1. Request/record  – every change is logged (ticket/PR) with description + reason.
2. Risk assessment – impact + rollback plan; classify (standard / normal / emergency).
3. Approval        – appropriate reviewer(s); segregation of duties (author != sole approver).
4. Testing         – validate in non-prod; security checks (scans, review).
5. Implementation  – during approved windows; documented steps.
6. Verification/rollback – confirm success; defined rollback if it fails.
7. Documentation   – close the record with outcome (audit evidence).
```

## Change types
```text
Standard  – pre-approved, low-risk, routine (e.g. a templated deploy). Fast-tracked.
Normal    – needs assessment + approval (most changes).
Emergency – expedited for incidents/urgent fixes; approved retrospectively but still recorded.
```

## Modern DevOps mapping
```text
- The PR + review + CI checks + protected-branch/environment approvals IS change management
  when configured well (see devsecops/ci-cd/environment-protection).
- Auditors accept git history + PR approvals + pipeline logs as evidence — if enforced
  (branch protection, required reviewers, no direct-to-prod).
- Separate author and approver; no self-merge to protected branches.
```

## Common audit findings
```text
- Changes deployed without approval / without a ticket.
- Same person authored and approved.
- No testing evidence; no rollback plan.
- Emergency changes never documented after the fact.
```

## Sources
- [ISO 27001 A.8.32](https://www.iso.org/standard/27001) · [ITIL Change Management] · related: [environment-protection](../../devsecops/ci-cd/environment-protection.md), [policy-templates](./policy-templates.md)
