---
title: "Control testing"
category: "compliance"
tags: ["compliance", "audit", "control-testing"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Control testing

## TL;DR
Control testing verifies that a control is both **designed** effectively and **operating** effectively over time. It's the evidence-gathering core of audits (internal, SOC 2, ISO). Method and sample size depend on control type and frequency.

## Design vs operating effectiveness
```text
Design effectiveness   – if performed as described, would the control prevent/detect the risk?
                         (Test of one: walkthrough / inspect the process.)
Operating effectiveness – did the control actually operate throughout the period?
                         (Test of many: sample across the audit period.)
SOC 2 Type I = design at a point in time. Type II = operating over a period.
```

## Testing methods (increasing rigor)
```text
Inquiry      – ask how it works (weakest alone; corroborate with others).
Observation  – watch the control being performed.
Inspection   – examine evidence/records (tickets, logs, configs, approvals).
Reperformance – independently re-execute the control to confirm the result (strongest).
Use a combination; inquiry alone is never sufficient.
```

## Sampling
```text
- Population = all occurrences in the period (e.g. all deploys, all access grants).
- Sample size scales with control frequency:
    Annual ~1, Quarterly ~2, Monthly ~2-5, Weekly ~5-15, Daily ~20-40, Many/day ~25-60.
- Random, representative selection across the whole period (not just recent).
- Automated controls: test the config + a sample of exceptions (or the full population if feasible).
```

## Examples
```text
Access reviews (quarterly) – inspect the review records for 2 quarters; confirm sign-off + actions.
Change management (many)   – sample deploys; verify each had approval + testing before prod.
Backups (daily)            – sample days; inspect success logs + a restore test.
MFA enforcement (automated) – inspect the config/policy + sample sign-ins for exceptions.
```

## Handling exceptions
```text
- An exception (control failed for a sample) may expand the sample or become a finding.
- Root-cause it; assess severity; feed corrective action (CAPA — see internal-audit-program).
```

## Sources
- [NIST SP 800-53A (assessment procedures)](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final) · [AICPA SOC 2](https://www.aicpa-cima.com/) · related: [evidence-checklist](./evidence-checklist.md), [internal-audit-program](./internal-audit-program.md)
