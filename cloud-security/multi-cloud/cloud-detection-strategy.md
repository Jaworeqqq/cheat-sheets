---
title: "Cloud detection strategy"
category: "cloud-security"
tags: ["multi-cloud", "detection", "logging", "blue-team"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-13"
author: "core"
---

# Cloud detection strategy

## TL;DR
Cloud detection differs from on-prem: the control plane (API) is the primary battleground, logs are the crime scene, and identity is the perimeter. A good strategy layers native services (GuardDuty/Defender/SCC) with centralized logging and custom analytics mapped to cloud attacker behavior.

## The three planes to monitor
```text
Control plane (API)  – who did what: IAM changes, resource creation, disabling logging.
                       Sources: CloudTrail (AWS), Activity/Audit Logs (Azure), Cloud Audit Logs (GCP).
Data plane           – access to data: S3/GCS/Blob object access, DB queries, secret reads.
Network plane        – flows: VPC Flow Logs, DNS logs, firewall logs (exfil/C2/scanning).
```

## Logging foundation (do this first)
```text
- Enable org-wide, multi-region audit logging; ship to a dedicated, immutable log account/bucket.
- Turn on data-event logging for sensitive stores (selectively — cost).
- Flow + DNS logs for network visibility.
- Protect logging from being disabled (SCP/Policy guardrails) — attackers kill logs first.
```

## Detection layers
```text
Native managed    – GuardDuty (AWS), Defender for Cloud (Azure), SCC/Event Threat Detection (GCP).
Posture/CSPM      – catch misconfig drift that creates exposure (see cspm).
Custom analytics  – SIEM queries for cloud TTPs the managed tools miss.
Identity threat   – anomalous logins, MFA changes, impossible travel, token/role abuse.
```

## Cloud attacker behaviors to detect
```text
- Recon: mass Describe/List/get-iam-policy calls; enumeration tooling (Pacu/ScoutSuite UA).
- Persistence: new IAM users/keys/roles, trust-policy changes, backdoor Lambdas/functions.
- Privesc: PassRole abuse, CreatePolicyVersion, role assumption chains.
- Defense evasion: StopLogging/DeleteTrail, disabling GuardDuty/Defender.
- Exfil: unusual data access volumes, snapshot sharing, cross-account copies.
- Credential access: SSRF->metadata token use, secret manager mass reads.
```

## Building the program
```text
1. Log everything relevant + protect the logs.
2. Enable native detection across all accounts/subscriptions/projects.
3. Centralize to a SIEM (Sentinel/Chronicle/Splunk); correlate cross-account + cross-cloud.
4. Add custom detections for gaps; map coverage to ATT&CK for Cloud (see mitre-attack-mapping).
5. Automate response (EventBridge/Logic Apps/Pub/Sub -> isolate/revoke) and IR runbooks.
```

## Sources
- [MITRE ATT&CK – Cloud matrix](https://attack.mitre.org/matrices/enterprise/cloud/) · related: [cloudtrail-detection](../aws/cloudtrail-detection.md), [defender-for-cloud](../azure/defender-for-cloud.md), [scc-deep](../gcp/scc-deep.md)
