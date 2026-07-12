---
title: "GCP Security Command Center"
category: "cloud-security"
tags: ["gcp", "scc", "cspm", "detection"]
platform: "gcp"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# GCP Security Command Center (SCC)

## TL;DR
SCC is Google Cloud's central security and risk platform: posture management (misconfigs), threat detection (Event Threat Detection, Container Threat Detection), and vulnerability findings — all in one place. The premium/enterprise tiers add active threat detection and attack path analysis.

## What it covers
```text
Posture / misconfig – Security Health Analytics (public buckets, open firewall, weak IAM, no logging).
Threat detection     – Event Threat Detection (parses Cloud Logging for IOCs/anomalies),
                       Container Threat Detection (runtime), VM Threat Detection.
Vulnerabilities      – Web Security Scanner (app vulns), package/OS vulns.
Attack paths         – (enterprise) exploitable chains toward high-value resources.
Sensitive data       – integration with Sensitive Data Protection (DLP) for data risk.
```

## Tiers
```text
Standard   – free; basic Security Health Analytics + some findings.
Premium/Enterprise – Event/Container Threat Detection, attack paths, compliance dashboards,
             continuous exports, and multi-cloud (via connectors).
```

## Event Threat Detection examples
```text
- IAM anomalous grant / self-privilege; service account key abuse.
- Malware/crypto-mining on VMs; connections to known-bad domains/IPs.
- Data exfiltration signals; brute force; disabled logging.
- Persistence: new SSH keys, modified startup scripts.
```

## Operating model
```text
1. Enable SCC at the org level (all projects); pick tier per risk/budget.
2. Triage findings by severity + exploitability (attack paths first).
3. Route findings to workflow: Pub/Sub -> SOAR/ticketing/Chronicle (SIEM).
4. Remediate posture findings; add mute rules for justified false positives.
5. Track compliance dashboards (CIS, PCI, etc.) for audits.
```

## Mitigation / Hardening (paired)
- SCC detects; enforce prevention with Org Policy guardrails + least-privilege IAM.
- Auto-remediate common misconfigs; feed threats to IR.
- Related: [gcp-iam-basics](./gcp-iam-basics.md), [vpc-service-controls](./vpc-service-controls.md), [cspm](../multi-cloud/cspm.md).

## Sources
- [Security Command Center](https://cloud.google.com/security-command-center/docs) · [Event Threat Detection](https://cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview)
