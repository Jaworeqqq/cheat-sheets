---
title: "Azure / Entra ID – enumeration"
category: "cloud-security"
tags: ["azure", "entra", "enumeration"]
platform: "azure"
mitre: ["T1087.004"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Azure / Entra ID enumeration

## TL;DR
Entra ID (formerly Azure AD) is the identity layer for M365/Azure. Enumeration: users, roles, apps/service principals, permissions. Privesc paths often go through app registrations and RBAC roles.

## Recon (unauthenticated / initial)
```bash
# Does the tenant exist, what federation
# https://login.microsoftonline.com/getuserrealm.srf?login=user@corp.com
# AADInternals (PowerShell)
Get-AADIntTenantID -Domain corp.com
Invoke-AADIntUserEnumerationAsOutsider -UserName user@corp.com
```

## Authenticated (AzureHound / az cli)
```bash
az login
az account show
az ad user list --query "[].userPrincipalName"
az role assignment list --all -o table
# Attack path graph (BloodHound for Azure)
azurehound -u user -p 'Pass' list --tenant <id> -o output.json
```

## Privesc paths (common)
```text
- Application Administrator -> add credentials to a high-privilege SP
- Owner on an app/SP        -> take over the application identity
- User Access Administrator -> grant yourself RBAC roles
- Privileged Role Admin     -> grant Entra roles (Global Admin)
- Managed Identity on a VM  -> IMDS -> token -> resources
- Consent grant abuse       -> OAuth phishing -> Graph tokens
```

## Detection (Blue Team)
- Sign-in logs + Audit logs: adding credentials to an SP, role changes, consent grants.
- Anomalies: new app registrations, unusual role assignments, impossible travel.

## Mitigation / Hardening
- PIM (Privileged Identity Management) — just-in-time roles, MFA on privileged.
- Restrict app consent (admin consent workflow), review SPs with credentials.
- Conditional Access, block legacy auth, least-privilege RBAC.

## Sources
- [AzureHound](https://github.com/SpecterOps/AzureHound) · [AADInternals](https://aadinternals.com/) · [MicroBurst](https://github.com/NetSPI/MicroBurst)
