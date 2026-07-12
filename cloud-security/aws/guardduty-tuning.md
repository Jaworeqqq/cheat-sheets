---
title: "AWS GuardDuty tuning"
category: "cloud-security"
tags: ["aws", "guardduty", "detection", "blue-team"]
platform: "aws"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# AWS GuardDuty tuning

## TL;DR
GuardDuty is AWS's managed threat detection — it analyzes CloudTrail, VPC Flow Logs, and DNS logs (plus optional protection plans) to surface findings without you writing rules. The work is operational: enable org-wide, tune false positives, and route findings to response.

## Enable properly
```text
- Turn on org-wide via a delegated administrator account (all accounts + regions).
- Enable protection plans as needed: S3, EKS, Malware Protection, RDS, Lambda, Runtime Monitoring.
- Export findings to a central account; integrate with Security Hub + EventBridge.
```

## Finding types (categories)
```text
- Reconnaissance (port scans, unusual API from Tor/known-bad IPs).
- Instance compromise (crypto-mining, C2 domains, outbound DoS).
- Account/IAM (anomalous console login, credential exfiltration, disabled logging).
- S3 (anomalous data access), EKS (privileged/exec), Malware (EBS scan hits).
Each has a severity (Low/Medium/High) and MITRE-ish context.
```

## Tuning (reduce noise, keep signal)
```text
- Suppression rules: auto-archive known-benign findings (e.g. approved scanner IPs,
  expected cross-account access) by finding type + criteria.
- Trusted IP lists: reduce false positives from known-good sources (use sparingly — an
  attacker from a trusted IP won't alert).
- Threat IP lists: add your own known-bad IPs to force findings.
- Don't blanket-suppress by severity; suppress by specific, justified criteria.
```

## Response automation
```text
EventBridge rule on GuardDuty findings -> Lambda/Step Functions:
 - Isolate an instance (swap SG), disable a key, snapshot for forensics, notify SOC.
 - Ticket creation + enrichment; feed Sentinel/SIEM.
Prioritize: high severity + IAM/exfil findings first (see cloud-ir-aws).
```

## Detection quality notes
```text
- GuardDuty is detective, not preventive — pair with SCPs/guardrails (prevent) + Config (posture).
- It won't catch everything; supplement with CloudTrail hunting (see cloudtrail-detection).
```

## Sources
- [GuardDuty docs](https://docs.aws.amazon.com/guardduty/) · [Finding types](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-active.html) · related: [cloudtrail-detection](./cloudtrail-detection.md), [terraform-cloud-guardrails](../multi-cloud/terraform-cloud-guardrails.md)
