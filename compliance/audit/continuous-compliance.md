---
title: "Continuous compliance"
category: "compliance"
tags: ["compliance", "automation", "compliance-as-code"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# Continuous compliance

## TL;DR
Continuous compliance replaces the annual scramble with always-on, automated evidence collection and control monitoring. Instead of proving compliance at a point in time, you continuously verify controls, catch drift immediately, and keep an audit-ready posture year-round.

## Point-in-time vs continuous
```text
Traditional  – manual evidence gathering before an audit; snapshots; gaps between audits.
Continuous   – automated checks run constantly; drift alerts in real time; evidence always current.
Benefit: SOC 2 Type II / ISO surveillance become smoother; risks caught when they appear, not yearly.
```

## What to automate
```text
Config checks     – CSPM/IaC scanning continuously verifies cloud/infra against benchmarks.
Access reviews    – automated collection of who-has-access; flag anomalies/orphans.
Evidence capture  – pull configs, logs, tickets, scan results on a schedule -> evidence store.
Control monitoring – map technical signals to controls; alert when a control fails.
Drift detection   – IaC + policy-as-code catch out-of-band changes.
```

## Tooling
```text
GRC / compliance automation – Vanta, Drata, Secureframe (map controls -> automated tests + evidence).
Cloud                       – Config rules, Security Hub/Defender/SCC, Steampipe/Prowler.
Policy-as-code              – OPA/Conftest, Kyverno (see devsecops/iac/policy-testing).
Custom                      – scheduled scripts writing timestamped evidence to a store.
```

## Compliance-as-code
```text
- Express controls as machine-checkable policies; run them in CI + continuously in prod.
- Version control policies + evidence; changes reviewed like code.
- OSCAL for machine-readable control catalogs/assessments.
```

## Best practices
```text
- Start with your highest-effort/most-frequent controls (access reviews, config, patching).
- Keep a human in the loop for judgment-based controls; automate the mechanical ones.
- Continuous != no auditor — it makes their sampling and your evidence trivial.
- Tie alerts to owners + remediation SLAs; track exceptions.
```

## Sources
- [NIST OSCAL](https://pages.nist.gov/OSCAL/) · related: [control-testing](./control-testing.md), [evidence-checklist](./evidence-checklist.md), [cspm](../../cloud-security/multi-cloud/cspm.md)
