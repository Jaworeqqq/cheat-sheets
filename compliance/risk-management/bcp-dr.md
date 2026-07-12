---
title: "Business Continuity & Disaster Recovery (BCP/DR)"
category: "compliance"
tags: ["risk-management", "bcp", "dr", "resilience"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Business Continuity & Disaster Recovery

## TL;DR
BCP keeps the *business* running during disruption; DR restores *IT systems* after an incident. Both are anchored by two metrics — RTO (how fast) and RPO (how much data loss is acceptable) — and are only real if tested. Required by ISO 27001, DORA, and most frameworks.

## Key metrics
```text
RTO (Recovery Time Objective)  – max acceptable downtime for a system/process.
RPO (Recovery Point Objective) – max acceptable data loss (drives backup frequency).
MTD (Maximum Tolerable Downtime) – the outer limit before unacceptable business damage.
Example: RPO 15 min -> replicate/back up at least every 15 min; RTO 1h -> can restore within 1h.
```

## Business Impact Analysis (BIA) — the foundation
```text
- Identify critical business processes and their supporting systems/dependencies.
- Determine impact of downtime over time (financial, legal, reputational).
- Set RTO/RPO per process based on impact (not everything needs the same tier).
- Prioritize recovery order; identify single points of failure.
```

## DR strategies (cost vs speed)
```text
Backup & restore   – cheapest, slowest RTO (restore from backups).
Pilot light        – minimal core running; scale up on failover.
Warm standby       – scaled-down full environment, faster failover.
Hot standby / active-active – near-zero RTO/RPO, most expensive.
Cloud: multi-AZ (HA) vs multi-region (DR); align to RTO/RPO + budget.
```

## Backups (the DR floor)
```text
- 3-2-1 rule: 3 copies, 2 media, 1 offsite. Add: 1 immutable/air-gapped (ransomware).
- Test RESTORES regularly (a backup you can't restore is not a backup).
- Encrypt backups; protect them from the same compromise as production.
```

## Testing (non-negotiable)
```text
- Tabletop walkthroughs, then functional failover tests, then full DR drills.
- Test at least annually (and after major changes); measure actual RTO/RPO vs target.
- Document lessons; update the plan. Untested DR = assumed DR = likely failure.
```

## Sources
- [ISO 22301 (BCM)](https://www.iso.org/standard/75106.html) · [NIST SP 800-34 (contingency planning)](https://csrc.nist.gov/pubs/sp/800/34/r1/final) · related: [ir-playbook-ransomware](../../blue-team/incident-response/ir-playbook-ransomware.md)
