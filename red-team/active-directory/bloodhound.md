---
title: "BloodHound – AD attack path analysis"
category: "red-team"
tags: ["active-directory", "enumeration", "bloodhound"]
platform: "windows"
mitre: ["T1069", "T1482"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# BloodHound

## TL;DR
Collects AD relationships (memberships, ACLs, sessions, delegations) into a graph and shows the shortest path to Domain Admin. Collection = SharpHound (collector), analysis = BloodHound GUI.

## Collection (SharpHound)
```powershell
# Windows, from a domain-joined host
SharpHound.exe -c All --zipfilename loot.zip
```
```bash
# From Linux, remotely (no implant) – bloodhound-python / netexec
bloodhound-python -u user -p 'Pass' -d corp.local -ns 10.10.10.10 -c All
nxc ldap 10.10.10.10 -u user -p 'Pass' --bloodhound -c All --dns-server 10.10.10.10
```

## Analysis (common queries)
```text
Pre-built:
 - "Find Shortest Paths to Domain Admins"
 - "Find Principals with DCSync Rights"
 - "Shortest Path from Owned Principals"  (mark your accounts as Owned!)

Useful edges:
 GenericAll / GenericWrite / WriteDacl / WriteOwner  -> object takeover
 AddMember  -> add yourself to a group
 ForceChangePassword -> reset a user's password
 AllowedToDelegate / Constrained/Unconstrained delegation
```

## Detection (Blue Team)
- Bursts of LDAP/SAMR queries from one host (enumeration).
- Unusual SharpHound sessions (`--stealth` reduces them, but LDAP is still visible).
- Honeytoken: a decoy account with "interesting" ACLs.

## Mitigation / Hardening
- Reduce excessive ACLs (GenericAll/WriteDacl), enforce tiering (Tier 0/1/2).
- Remove unconstrained delegation, clean up nested group memberships.
- Monitor and reduce paths to DA (regular graph reviews by the blue team).

## Sources
- [BloodHound CE](https://github.com/SpecterOps/BloodHound) · [The Hacker Recipes – AD](https://www.thehacker.recipes/ad/)
