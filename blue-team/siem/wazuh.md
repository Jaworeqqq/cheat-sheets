---
title: "Wazuh – open-source SIEM/XDR"
category: "blue-team"
tags: ["siem", "wazuh", "hids", "detection"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Wazuh

## TL;DR
Wazuh is a free, open-source security platform combining host-based IDS (HIDS), log analysis, FIM, vulnerability detection, and SIEM-like correlation. A common choice for labs and budget-conscious SOCs. Agents on endpoints ship data to a manager that applies rules/decoders.

## Architecture
```text
Agent    – on endpoints; collects logs, FIM, syscheck, SCA, vuln data.
Manager  – decoders + rules, correlation, alerting.
Indexer  – (OpenSearch) stores events for search.
Dashboard – (OpenSearch Dashboards) visualization, alerts, ATT&CK view.
```

## Capabilities
```text
- Log data analysis (syslog, Windows events, cloud, apps).
- File Integrity Monitoring (FIM/syscheck) — detect changes to critical files.
- Security Configuration Assessment (SCA) — CIS benchmark checks.
- Vulnerability detection (correlate installed packages with CVE feeds).
- Active response (run scripts on triggers: block IP, kill process).
- MITRE ATT&CK tagging on rules.
```

## Rules & decoders (detection logic)
```xml
<!-- Custom rule: many failed SSH logins from one source -->
<rule id="100200" level="10" frequency="8" timeframe="120">
  <if_matched_sid>5716</if_matched_sid>   <!-- sshd auth failure -->
  <same_source_ip />
  <description>Possible SSH brute force</description>
  <mitre><id>T1110</id></mitre>
</rule>
```

## Common uses
```text
- FIM on /etc, web roots, registry Run keys -> tamper/persistence detection.
- Windows Event + Sysmon ingestion for endpoint detections.
- SCA to continuously check CIS hardening drift.
- Cloud (CloudTrail/GCP/Azure) module ingestion.
```

## Best practices
```text
- Tune noisy rules; write custom rules/decoders for your apps.
- Enable FIM + SCA on critical assets; feed vuln data.
- Use active response carefully (avoid self-inflicted DoS / lockout).
- Version custom rules in git (detection-as-code). Validate with Atomic Red Team.
```

## Sources
- [Wazuh docs](https://documentation.wazuh.com/) · related: [detection-as-code](../detection-engineering/detection-as-code.md)
