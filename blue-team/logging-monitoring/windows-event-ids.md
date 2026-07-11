---
title: "Windows Event IDs – the essentials"
category: "blue-team"
tags: ["logging", "windows", "detection", "dfir"]
platform: "windows"
mitre: []
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# Windows Event IDs (Security / Sysmon)

## TL;DR
A cheat sheet of the most important events for detection and DFIR. Security log = built-in, Sysmon = richer telemetry (requires installation).

## Authentication and accounts
| ID | Meaning | Notes |
|----|---------|-------|
| 4624 | Successful logon | Logon Type: 2=local, 3=network, 10=RDP |
| 4625 | Failed logon | Spray/bruteforce = a wave of 4625 |
| 4634 / 4647 | Logoff | |
| 4648 | Logon with explicit credentials | RunAs / lateral movement |
| 4672 | Admin privileges assigned | Privileged account logon |
| 4720 / 4726 | Account created / deleted | |
| 4728 / 4732 | Added to group (global/local) | Escalation |
| 4740 | Account locked out | |

## Kerberos (on the DC)
| ID | Meaning |
|----|---------|
| 4768 | TGT request (AS-REQ) — AS-REP roast: type 0 |
| 4769 | TGS request — Kerberoast: encryption 0x17 (RC4) |
| 4771 | Kerberos pre-auth failed (spray) |
| 4662 | Operation on an AD object — DCSync: replication rights |

## Execution / persistence
| ID | Meaning |
|----|---------|
| 4688 | Process creation (enable command-line auditing!) |
| 4697 / 7045 | Service installation (PsExec = PSEXESVC) |
| 4698 | Scheduled task creation |
| 1102 | Security log cleared (anti-forensics!) |

## Sysmon (most valuable)
| ID | Meaning |
|----|---------|
| 1 | Process create (+ hash, cmdline, parent) |
| 3 | Network connection |
| 7 | Image loaded (DLL — hijacking) |
| 8 | CreateRemoteThread (injection) |
| 11 | File create |
| 13 | Registry set (Run keys, persistence) |

## Mitigation / Hardening
- Enable **command-line auditing** (4688) and PowerShell ScriptBlock (4104).
- Deploy Sysmon with a good config (e.g. SwiftOnSecurity/Olaf).
- Forward logs to a SIEM; alert on 1102 (log clearing).

## Sources
- [Sysmon config – SwiftOnSecurity](https://github.com/SwiftOnSecurity/sysmon-config)
