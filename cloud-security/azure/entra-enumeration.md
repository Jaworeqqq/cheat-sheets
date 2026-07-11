---
title: "Azure / Entra ID – enumeracja"
category: "cloud-security"
tags: ["azure", "entra", "enumeration"]
platform: "azure"
mitre: ["T1087.004"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Azure / Entra ID Enumeration

## TL;DR
Entra ID (dawniej Azure AD) to tożsamość dla M365/Azure. Enumeracja: użytkownicy, role, aplikacje/service principale, uprawnienia. Ścieżki privesc często przez app registrations i role RBAC.

## Rozpoznanie (nieuwierzytelnione / wstępne)
```bash
# Czy tenant istnieje, jaki federation
# https://login.microsoftonline.com/getuserrealm.srf?login=user@corp.com
# AADInternals (PowerShell)
Get-AADIntTenantID -Domain corp.com
Invoke-AADIntUserEnumerationAsOutsider -UserName user@corp.com
```

## Uwierzytelnione (AzureHound / az cli)
```bash
az login
az account show
az ad user list --query "[].userPrincipalName"
az role assignment list --all -o table
# Graf ścieżek ataku (BloodHound dla Azure)
azurehound -u user -p 'Pass' list --tenant <id> -o output.json
```

## Ścieżki privesc (typowe)
```text
- Application Administrator -> dodaj credentials do SP z wysokimi uprawnieniami
- Owner na app/SP           -> przejmij tożsamość aplikacji
- User Access Administrator -> nadaj sobie role RBAC
- Privileged Role Admin     -> nadaj role Entra (Global Admin)
- Managed Identity na VM    -> IMDS -> token -> zasoby
- Consent grant abuse       -> phishing OAuth -> tokeny Graph
```

## Wykrywanie (Blue Team)
- Sign-in logs + Audit logs: dodanie credentiali do SP, zmiany ról, consent grants.
- Anomalie: nowe app registrations, nietypowe assumeRole/role assignment, impossible travel.

## Mitygacja / Hardening
- PIM (Privileged Identity Management) — role just-in-time, MFA na uprzywilejowane.
- Ogranicz app consent (admin consent workflow), przegląd SP z credentialami.
- Conditional Access, blokada legacy auth, least privilege RBAC.

## Źródła
- [AzureHound](https://github.com/SpecterOps/AzureHound) · [AADInternals](https://aadinternals.com/) · [MicroBurst](https://github.com/NetSPI/MicroBurst)
