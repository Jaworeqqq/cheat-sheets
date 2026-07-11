---
title: "Azure Storage & SAS token abuse"
category: "cloud-security"
tags: ["azure", "storage", "sas"]
platform: "azure"
mitre: ["T1530", "T1552"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Azure Storage & SAS token abuse

## TL;DR
Azure Storage exposes blobs/files/queues/tables. Risks: anonymous public blob access, leaked account keys (full control), and over-scoped/long-lived SAS (Shared Access Signature) tokens that grant delegated access — often found in code, URLs, and logs.

## Enumeration / access test
```bash
# Anonymous public blob container
curl -s "https://acct.blob.core.windows.net/container?restype=container&comp=list"

# With az CLI (authenticated)
az storage account list -o table
az storage container list --account-name acct --auth-mode login -o table
az storage blob list -c container --account-name acct --auth-mode login

# SAS token in a URL grants access directly:
curl "https://acct.blob.core.windows.net/container/secret.txt?sv=...&sig=..."
```

## Token/key types (privilege)
```text
Account key    – FULL control of the storage account (never embed; rotate if leaked)
SAS (account)  – broad, account-wide delegated access
SAS (service)  – scoped to a container/blob; still often over-permissioned/long TTL
User delegation SAS – backed by Entra ID (revocable, preferred)
Anonymous access – container/blob set to public (data leak)
```

## Abuse scenarios
```text
- Leaked SAS in a mobile app / JS / repo -> read/write data until it expires.
- Leaked account key -> full account takeover, persistence, exfil.
- Public container -> mass data download.
- Writable SAS/container -> tamper content, host malware, poison static sites.
```

## Detection (Blue Team)
- Storage Analytics / diagnostic logs: access via SAS from unusual IPs; anonymous access.
- Defender for Storage: anomalous access, mass download, malware upload.
- Alert on public containers and account key usage.

## Mitigation / Hardening
- Disable anonymous/public access (account-level "AllowBlobPublicAccess=false").
- Prefer Entra ID (RBAC) + **user delegation SAS** (revocable) over account-key SAS.
- Short TTL, least privilege, IP restrictions, HTTPS-only on SAS; rotate account keys / disable key auth.
- Store keys/SAS in Key Vault, never in code/URLs; enable logging + Defender for Storage.

## Sources
- [Azure Storage security guide](https://learn.microsoft.com/azure/storage/blobs/security-recommendations) · [SAS best practices](https://learn.microsoft.com/azure/storage/common/storage-sas-overview)
