---
title: "AWS Security Hub"
category: "cloud-security"
tags: ["aws", "security-hub", "cspm", "posture"]
platform: "aws"
mitre: []
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# AWS Security Hub

## TL;DR
Security Hub is AWS's central aggregator for security findings — it pulls from GuardDuty, Inspector, Macie, Config, IAM Access Analyzer, and third parties into one normalized view (ASFF), runs automated compliance standards (CIS, FSBP, PCI, NIST), and gives you a cross-account security posture score.

## What it does
```text
- Aggregates findings from AWS services + partners into the AWS Security Finding Format (ASFF).
- Runs security STANDARDS (automated checks): AWS Foundational Security Best Practices (FSBP),
  CIS AWS Benchmark, PCI DSS, NIST 800-53.
- Central, cross-account, cross-region view (with a delegated admin in AWS Organizations).
- Feeds automation (EventBridge) and SOAR/SIEM.
```

## Setup
```text
- Enable org-wide via a delegated administrator; auto-enable new accounts.
- Turn on relevant standards (start with FSBP + CIS).
- Integrate finding sources (GuardDuty, Inspector for vulns, Macie for data, Config for posture).
- Aggregate regions to a home region; export to SIEM.
```

## Security Hub vs the sources
```text
GuardDuty    – threat detection (behavioral). Security Hub INGESTS its findings.
Inspector    – vulnerability + network exposure scanning.
Macie        – sensitive data discovery in S3.
Config       – resource config + compliance rules.
Security Hub – the AGGREGATOR + standards + scoring. Not a detector itself; it centralizes.
```

## Operating model
```text
1. Enable + standards across the org; establish the security score baseline.
2. Triage by severity + standard; remediate FSBP/CIS failures (posture).
3. Automate: EventBridge on findings -> ticket / auto-remediation / notify SOC.
4. Suppress justified findings with rules; track exceptions.
5. Trend the score; report to leadership.
```

## Detection / response integration
- Central findings -> Sentinel/Splunk/Chronicle or Amazon Detective for investigation.
- Automated response via EventBridge + Lambda (see cloud-ir-aws).

## Mitigation / Hardening (paired)
- Security Hub detects/aggregates; prevent with SCP guardrails + least privilege.
- Related: [guardduty-tuning](./guardduty-tuning.md), [cloudtrail-detection](./cloudtrail-detection.md), [organizations-scp-patterns](./organizations-scp-patterns.md).

## Sources
- [AWS Security Hub](https://docs.aws.amazon.com/securityhub/) · [ASFF](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html)
