---
title: "Windows Event IDs – najważniejsze"
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
Ściągawka najważniejszych zdarzeń do detekcji i DFIR. Security log = wbudowany, Sysmon = bogatsza telemetria (wymaga instalacji).

## Uwierzytelnianie i konta
| ID | Znaczenie | Uwagi |
|----|-----------|-------|
| 4624 | Udane logowanie | Logon Type: 2=lokalne, 3=sieć, 10=RDP |
| 4625 | Nieudane logowanie | Spray/bruteforce = fala 4625 |
| 4634 / 4647 | Wylogowanie | |
| 4648 | Logon z jawnymi poświadczeniami | RunAs / lateral movement |
| 4672 | Nadano uprawnienia admina | Logon konta uprzywilejowanego |
| 4720 / 4726 | Utworzenie / usunięcie konta | |
| 4728 / 4732 | Dodanie do grupy (global/local) | Eskalacja |
| 4740 | Konto zablokowane (lockout) | |

## Kerberos (na DC)
| ID | Znaczenie |
|----|-----------|
| 4768 | TGT request (AS-REQ) — AS-REP roast: type 0 |
| 4769 | TGS request — Kerberoast: encryption 0x17 (RC4) |
| 4771 | Kerberos pre-auth failed (spray) |
| 4662 | Operacja na obiekcie AD — DCSync: prawa replikacji |

## Wykonanie / persystencja
| ID | Znaczenie |
|----|-----------|
| 4688 | Utworzenie procesu (włącz command-line auditing!) |
| 4697 / 7045 | Instalacja usługi (PsExec = PSEXESVC) |
| 4698 | Utworzenie zadania harmonogramu |
| 1102 | Wyczyszczono log Security (anti-forensics!) |

## Sysmon (najcenniejsze)
| ID | Znaczenie |
|----|-----------|
| 1 | Process create (+ hash, cmdline, parent) |
| 3 | Network connection |
| 7 | Image loaded (DLL — hijacking) |
| 8 | CreateRemoteThread (injection) |
| 11 | File create |
| 13 | Registry set (Run keys, persistence) |

## Mitygacja / Hardening
- Włącz **command-line auditing** (4688) i PowerShell ScriptBlock (4104).
- Wdróż Sysmon z dobrą konfiguracją (np. SwiftOnSecurity/Olaf).
- Forward logów do SIEM; alertuj na 1102 (czyszczenie logów).

## Źródła
- [Sysmon config – SwiftOnSecurity](https://github.com/SwiftOnSecurity/sysmon-config)
