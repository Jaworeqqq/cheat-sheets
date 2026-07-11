---
title: "AWS CloudTrail – detection"
category: "cloud-security"
tags: ["aws", "cloudtrail", "detection", "blue-team"]
platform: "aws"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# AWS CloudTrail – detection

## TL;DR
CloudTrail logs API activity across AWS — the primary source for detecting attacker actions (recon, privesc, persistence, exfil). Ensure it's org-wide, multi-region, immutable, and analyzed (Athena/GuardDuty/SIEM).

## Baseline setup (prerequisite for detection)
```text
- Org trail, all regions, management + data events (for sensitive S3/Lambda).
- Log to a dedicated, restricted S3 bucket; enable log file validation.
- CloudTrail Lake or ship to SIEM; alert via EventBridge.
```

## High-value events to alert on
```text
Recon        – GetAccountAuthorizationDetails, ListUsers/Roles, GetCallerIdentity bursts
Defense evade – StopLogging, DeleteTrail, PutEventSelectors (disabling logging)
Persistence  – CreateAccessKey, CreateUser, CreateLoginProfile, UpdateAssumeRolePolicy
Privesc      – CreatePolicyVersion, AttachUserPolicy, PassRole to sensitive roles
Cred/exfil   – GetSecretValue bursts, S3 GetObject anomalies, CreateDBSnapshot + share
IAM anomalies – AssumeRole from new/unusual IPs or unusual UserAgents (e.g. Pacu)
```

## Example detection (Athena / SIEM logic)
```sql
-- CloudTrail logging disabled (strong tamper signal)
SELECT eventTime, userIdentity.arn, eventName, sourceIPAddress
FROM cloudtrail_logs
WHERE eventName IN ('StopLogging','DeleteTrail','UpdateTrail','PutEventSelectors')
ORDER BY eventTime DESC;
```

## Detection layers
```text
- GuardDuty – managed anomaly/threat detection (IAM, S3, DNS, malware).
- CloudTrail Lake / Athena – custom hunting queries.
- Config + Access Analyzer – posture drift, public/external access.
- Security Hub – aggregates findings.
```

## Mitigation / Hardening
- Protect the trail (SCP denying StopLogging/DeleteTrail), immutable log bucket (Object Lock).
- Least privilege, alert on the events above, respond via automation (EventBridge → Lambda).

## Sources
- [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/) · [GuardDuty finding types](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-active.html)
