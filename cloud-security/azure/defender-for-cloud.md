---
title: "Microsoft Defender for Cloud"
category: "cloud-security"
tags: ["azure", "defender", "cspm", "cwpp"]
platform: "azure"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Microsoft Defender for Cloud (MDC)

## TL;DR
Defender for Cloud is Azure's CNAPP: CSPM (posture/misconfig via Secure Score) plus CWPP (workload protection plans for servers, containers, storage, databases, etc.). It also assesses AWS/GCP when connected, and feeds alerts to Sentinel.

## Two halves
```text
CSPM (posture, mostly free tier)
 - Secure Score, misconfiguration findings, regulatory compliance dashboards.
 - Attack path analysis + cloud security graph (Defender CSPM plan).
CWPP (Defender plans, paid, per resource type)
 - Defender for Servers (EDR/MDE integration, vuln assessment)
 - Defender for Containers (K8s/registry scanning + runtime)
 - Defender for Storage / SQL / Key Vault / App Service / APIs / Resource Manager
```

## Key features
```text
- Secure Score – prioritized hardening recommendations across subscriptions.
- Regulatory compliance – map posture to standards (CIS, PCI, ISO, NIST).
- Security alerts – threat detection per resource (feeds Sentinel/XDR).
- Attack path analysis – graph of exploitable chains (internet-exposed -> priv -> data).
- Multicloud – connect AWS/GCP for unified posture (CSPM across clouds).
```

## Operating model
```text
1. Enable CSPM (posture) across all subscriptions; review Secure Score.
2. Turn on Defender plans for sensitive workloads (servers, containers, storage, SQL).
3. Triage recommendations by exploitability (attack paths) + exposure.
4. Route alerts to Sentinel for correlation + IR; automate responses (Logic Apps/workflow automation).
5. Track compliance dashboards for audits.
```

## Detection (Blue Team)
- MDC alerts (brute force, suspicious access, malware, anomalous API) -> Sentinel incidents.
- Attack-path findings for internet-exposed + high-priv + sensitive-data chains.

## Mitigation / Hardening
- Enable posture everywhere + workload plans on sensitive resources; act on Secure Score.
- Remediate attack paths first (highest real risk); automate remediation where safe.
- Related: [conditional-access](./conditional-access.md), [multi-cloud/cspm](../multi-cloud/cspm.md).

## Sources
- [Defender for Cloud docs](https://learn.microsoft.com/azure/defender-for-cloud/)
