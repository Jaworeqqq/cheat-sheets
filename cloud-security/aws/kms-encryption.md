---
title: "AWS KMS & encryption"
category: "cloud-security"
tags: ["aws", "kms", "encryption", "key-management"]
platform: "aws"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# AWS KMS & encryption

## TL;DR
KMS manages encryption keys used across AWS services. The security model hinges on **key policies** (who can use/manage a key) plus IAM. A misconfigured key policy can expose data or let an attacker deny access; envelope encryption keeps data keys protected.

## Key concepts
```text
KMS key (CMK)  – customer managed / AWS managed / AWS owned.
Key policy     – the PRIMARY access control on a key (resource policy, always evaluated).
Envelope enc.  – KMS encrypts a data key (DEK); the DEK encrypts the data (see cryptography/key-management).
Grants         – temporary, granular permissions to use a key.
Key rotation   – automatic annual rotation for customer-managed keys (enable it).
```

## Key policy — the crux
```text
Unlike most resources, a KMS key's access is governed by its KEY POLICY (+ IAM).
Pitfalls:
 - Overly broad principal ("AWS":"*") or account root without conditions.
 - kms:* granted widely -> attacker can schedule key deletion (destroy data) or decrypt.
 - Cross-account access via key policy not scoped/audited.
```

## Common misconfigs / attacks
```text
- Resources "encrypted" with an AWS-owned/managed key when a CMK with tight policy is needed.
- kms:ScheduleKeyDeletion abuse -> data destruction (ransom/DoS).
- Broad kms:Decrypt -> read any data protected by the key.
- Unencrypted resources (EBS/S3/RDS/snapshots) — enforce encryption by default.
```

## Detection (Blue Team)
```text
CloudTrail: ScheduleKeyDeletion, DisableKey, PutKeyPolicy, mass Decrypt, GenerateDataKey spikes.
Config: unencrypted volumes/buckets/snapshots; keys without rotation.
```

## Mitigation / Hardening
- Least-privilege **key policies** (scoped principals + conditions); separate key admins from key users.
- Enable automatic key rotation; enforce encryption by default (EBS, S3 SSE-KMS, RDS).
- Guard against deletion: monitor/deny ScheduleKeyDeletion; enable deletion waiting period.
- Use CMKs (not AWS-owned) for sensitive data so you control the policy + audit; SCPs to prevent disabling.
- Related: [cryptography/key-management](../../cryptography/key-management.md), [cloudtrail-detection](./cloudtrail-detection.md).

## Sources
- [AWS KMS best practices](https://docs.aws.amazon.com/kms/latest/developerguide/best-practices.html)
