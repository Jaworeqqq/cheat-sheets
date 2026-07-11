---
title: "Sysmon – deployment and config"
category: "blue-team"
tags: ["logging", "sysmon", "windows", "detection"]
platform: "windows"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Sysmon – deployment and config

## TL;DR
Sysmon (Sysinternals) adds rich, high-fidelity telemetry beyond the Security log: process creation with hashes/command line/parent, network connections, image loads, registry, and more. The config file is where detection value lives.

## Install / manage
```powershell
# Install with a config
sysmon64.exe -accepteula -i sysmonconfig.xml
# Update config after tuning
sysmon64.exe -c sysmonconfig.xml
# Uninstall
sysmon64.exe -u
```
Logs land in: `Applications and Services Logs/Microsoft/Windows/Sysmon/Operational`.

## Highest-value event IDs
```text
1  Process create (+ Hashes, CommandLine, ParentImage) – core
3  Network connection (process -> dest)
7  Image loaded (DLL side-loading/hijacking)
8  CreateRemoteThread (injection)
10 ProcessAccess (LSASS access = cred dumping)
11 FileCreate
13 RegistryValueSet (Run keys, persistence)
22 DNSQuery
23 FileDelete (anti-forensics)
```

## Config philosophy
```xml
<!-- Sysmon uses include/exclude filters; a good base config is essential -->
<!-- Start from a maintained config and TUNE for your environment -->
<Sysmon schemaversion="4.90">
  <EventFiltering>
    <RuleGroup groupRelation="or">
      <ProcessCreate onmatch="include">
        <!-- e.g. catch LOLBins from unusual parents -->
        <ParentImage condition="end with">\winword.exe</ParentImage>
      </ProcessCreate>
    </RuleGroup>
  </EventFiltering>
</Sysmon>
```

## Best practices
```text
- Base config: SwiftOnSecurity or Olaf Hartong's sysmon-modular (ATT&CK-mapped).
- Exclude high-volume noise (your own agents) to control log size.
- Forward to SIEM (WEF/agent); correlate ID 1/3/10 for attack chains.
- Version the config in git; test changes against Atomic Red Team.
```

## Detection examples this enables
- LSASS access (ID 10 → lsass.exe) = credential dumping.
- ID 1 with `-enc`/`FromBase64String` = encoded PowerShell.
- ID 7 DLL loaded from a user-writable path = side-loading.

## Sources
- [Sysmon](https://learn.microsoft.com/sysinternals/downloads/sysmon) · [sysmon-modular (Olaf Hartong)](https://github.com/olafhartong/sysmon-modular) · [SwiftOnSecurity config](https://github.com/SwiftOnSecurity/sysmon-config)
