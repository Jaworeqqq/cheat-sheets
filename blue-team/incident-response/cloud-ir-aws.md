---
title: "IR Playbook – AWS incident response"
category: "blue-team"
tags: ["incident-response", "aws", "cloud", "playbook"]
platform: "aws"
mitre: []
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# IR Playbook – AWS incident response

## TL;DR
Cloud IR differs from on-prem: the API is the crime scene. Detect via CloudTrail/GuardDuty, contain by isolating identities and resources (without destroying evidence), investigate via logs and snapshots, then eradicate and harden. Preserve evidence (snapshots, logs) before terminating anything.

## Common triggers
```text
- GuardDuty findings (credential exfil, crypto-mining, anomalous API).
- Exposed access keys (GitHub scan, honeytoken), unusual AssumeRole/regions.
- Billing spike (crypto-mining), CloudTrail logging disabled.
```

## 1. Detection & scoping
```bash
# What did the identity do? (CloudTrail Lake / Athena)
# Enumerate actions by the suspect principal, region, time window.
aws cloudtrail lookup-events --lookup-attributes AttributeKey=Username,AttributeValue=<user>
# GuardDuty findings
aws guardduty list-findings --detector-id <id>
```

## 2. Containment (preserve evidence!)
```text
Compromised IAM credentials:
 - Attach an explicit DENY policy / deactivate the access key (don't delete yet).
 - Revoke active sessions (for roles: put a policy denying based on token issue time).
 - Rotate the key after evidence capture.
Compromised EC2 instance:
 - Isolate: replace SG with a no-access one; do NOT terminate.
 - Snapshot the EBS volume + capture memory if possible (evidence).
 - Disable instance profile / rotate its role.
Account-wide: ensure CloudTrail can't be stopped (SCP), protect log bucket.
```

## 3. Investigation
```text
- Timeline from CloudTrail: initial access -> actions -> persistence -> exfil.
- Check for persistence: new IAM users/keys/roles, Lambda backdoors, modified trust policies,
  new access to S3, altered CloudTrail/Config, cross-account role trust.
- VPC Flow Logs / DNS logs for exfil; S3 access logs for data access.
```

## 4. Eradication & recovery
```text
- Remove attacker IAM artifacts, revert trust policy changes, delete rogue resources.
- Rotate all potentially exposed credentials; rebuild compromised instances from clean images.
- Re-enable/repair logging; verify no lingering persistence.
```

## 5. Hardening (post-incident)
```text
- SCPs to prevent disabling CloudTrail/GuardDuty; least privilege; MFA; no long-lived keys (use roles/OIDC).
- Detective controls: GuardDuty, Config rules, Access Analyzer, automated response (EventBridge->Lambda).
- See cloud-security/aws/cloudtrail-detection.md and iam-privesc.md.
```

## Sources
- [AWS IR whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/) · [cloudtrail-detection](../../cloud-security/aws/cloudtrail-detection.md)
