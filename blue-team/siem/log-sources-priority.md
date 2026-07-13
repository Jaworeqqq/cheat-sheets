---
title: "Log sources – what to collect first"
category: "blue-team"
tags: ["siem", "logging", "detection", "strategy"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# Log sources – what to collect first

## TL;DR
You can't ingest everything (cost, noise), so prioritize log sources by detection value. The highest-value sources cover authentication, endpoint process activity, and the cloud control plane — these catch the most attacker behavior per dollar. Build coverage against ATT&CK, not by volume.

## Priority tiers
```text
Tier 1 (do first — highest signal)
 - Authentication: Windows Security (4624/4625/4768/4769), Entra/Okta sign-ins, VPN.
 - Endpoint: EDR telemetry + Sysmon (process create w/ cmdline+hashes, network, image load).
 - Cloud control plane: CloudTrail / Entra Audit / GCP Audit Logs.
 - DNS query logs.

Tier 2 (high value)
 - PowerShell ScriptBlock (4104), command-line auditing (4688).
 - Proxy/web gateway, firewall (esp. egress denies), VPC/NetFlow.
 - Email security (phishing), identity provider audit.

Tier 3 (context / IR)
 - Application logs, database audit, WAF, file/object access (data events),
   DHCP (attribution), physical access.
```

## Selection principles
```text
- Map to ATT&CK: which techniques does a source let you detect? Fill the biggest gaps first.
- Signal-to-noise: prefer sources with detections you'll actually use.
- Attribution: identity + DNS/DHCP tie events to a user/host.
- Retention: keep security-relevant logs long enough for dwell-time investigations (months).
- Protect the logs (immutable/central) — attackers disable logging early.
```

## Common gaps that hurt IR
```text
- No command-line auditing / ScriptBlock -> can't see what PowerShell did.
- No DNS logs -> blind to tunneling/C2 domains.
- No cloud data-event logs -> can't prove what data was accessed.
- Short retention -> can't investigate a months-long intrusion.
```

## Practical rollout
```text
1. Stand up Tier 1 across the fleet; validate parsing + timestamps + timezones.
2. Write detections for the top ATT&CK techniques those sources cover.
3. Add Tier 2/3 as budget + use cases justify; measure coverage over time.
```

## Sources
- [MITRE ATT&CK Data Sources](https://attack.mitre.org/datasources/) · related: [windows-event-ids](../logging-monitoring/windows-event-ids.md), [mitre-attack-mapping](../detection-engineering/mitre-attack-mapping.md)
