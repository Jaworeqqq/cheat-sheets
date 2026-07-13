---
title: "Microsoft Sentinel onboarding"
category: "cloud-security"
tags: ["azure", "sentinel", "siem", "detection"]
platform: "azure"
mitre: []
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# Microsoft Sentinel onboarding

## TL;DR
Sentinel is Microsoft's cloud-native SIEM/SOAR built on Log Analytics. Onboarding = a Log Analytics workspace + Sentinel enabled + data connectors + analytics rules + automation. It shines for Microsoft-heavy estates (Entra, M365, Defender, Azure) and ingests third-party sources too.

## Architecture
```text
Log Analytics workspace  – stores the data (tables); queried with KQL.
Sentinel                 – analytics rules, incidents, hunting, workbooks, SOAR (playbooks).
Data connectors          – pull logs from sources (native + Syslog/CEF/API/AMA).
Playbooks (Logic Apps)   – automated response (SOAR).
```

## Onboarding steps
```text
1. Create/choose a Log Analytics workspace (plan region, retention, cost).
2. Enable Sentinel on the workspace.
3. Connect data sources (start high-value): Entra ID sign-in/audit, Microsoft 365,
   Defender XDR, Azure Activity, then network/firewall, endpoints, third-party (CEF/Syslog).
4. Enable analytics rules (built-in templates + Microsoft-authored) mapped to MITRE ATT&CK.
5. Set up automation (playbooks) for common responses; configure incident settings.
6. Build workbooks/dashboards; establish hunting queries.
```

## Data connector priorities
```text
Tier 1: Entra ID (sign-ins/audit), Microsoft 365, Defender XDR, Azure Activity.
Tier 2: firewall/NSG flow, DNS, third-party security tools (CEF/Syslog via AMA), threat intel.
Cost note: ingestion is priced per GB — be selective; use basic/auxiliary logs tiers for high-volume, low-query data.
```

## Detections & content
```text
- Analytics rules: scheduled (KQL), Microsoft security (from Defender), fusion (ML correlation),
  anomaly. Enable relevant templates; tune thresholds.
- Content hub: solutions packaging connectors + rules + workbooks per product/source.
- Map coverage to ATT&CK (see mitre-attack-mapping); write custom KQL for gaps (see kql-sentinel).
```

## Cost & tuning
```text
- Ingestion + retention drive cost — filter at the source, use commitment tiers, archive old data.
- Tune noisy rules; suppress known-good; measure alert-to-incident quality.
```

## Sources
- [Microsoft Sentinel docs](https://learn.microsoft.com/azure/sentinel/) · related: [kql-sentinel](../../blue-team/siem/kql-sentinel.md), [defender-for-cloud](./defender-for-cloud.md), [log-sources-priority](../../blue-team/siem/log-sources-priority.md)
