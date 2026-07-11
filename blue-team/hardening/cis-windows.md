---
title: "Windows hardening (CIS)"
category: "blue-team"
tags: ["hardening", "windows", "cis"]
platform: "windows"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Windows hardening (CIS baseline)

## TL;DR
Reduce the Windows attack surface per the CIS Benchmark / Microsoft security baselines: account policy, LSASS protection, attack surface reduction, logging, service minimization. Deploy via GPO/Intune, verify with tooling.

## Assessment
```powershell
# Microsoft Security Compliance Toolkit (baselines + PolicyAnalyzer)
# or CIS-CAT; quick checks below
auditpol /get /category:*                 # audit policy coverage
Get-MpComputerStatus                       # Defender status
```

## Key areas
```text
Accounts / auth
 - Strong password policy, lockout threshold, disable LM/NTLMv1
 - LAPS for local admin passwords, restrict local admin membership

Credential protection
 - Credential Guard (VBS), LSASS as PPL (RunAsPPL=1)
 - Disable WDigest credential caching

Attack Surface Reduction (Defender ASR rules)
 - Block credential theft from LSASS, Office child processes, obfuscated scripts

Logging (feed to SIEM)
 - Enable command-line auditing (4688), PowerShell ScriptBlock (4104), Sysmon
 - Advanced audit policy: logon, account mgmt, process creation

Services / features
 - Remove Print Spooler where unneeded, disable SMBv1, unused roles
```

## Example (registry hardening)
```powershell
# LSASS as PPL
reg add HKLM\SYSTEM\CurrentControlSet\Control\Lsa /v RunAsPPL /t REG_DWORD /d 1
# Disable WDigest
reg add "HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest" /v UseLogonCredential /t REG_DWORD /d 0
```

## Verification / maintenance
- Deploy baselines via GPO/Intune; monitor drift; patch management (WSUS/Intune).
- Test detections (Atomic Red Team) against the hardened baseline.

## Sources
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) · [Microsoft Security Baselines](https://learn.microsoft.com/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines) · [Defender ASR](https://learn.microsoft.com/defender-endpoint/attack-surface-reduction)
