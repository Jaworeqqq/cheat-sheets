---
title: "Scheduled task & cron abuse"
category: "red-team"
tags: ["persistence", "windows", "linux", "scheduled-tasks"]
platform: "agnostic"
mitre: ["T1053"]
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Scheduled task & cron abuse

## TL;DR
Scheduled tasks (Windows) and cron/systemd timers (Linux) are among the most common persistence mechanisms — they survive reboots and can run as privileged accounts. Attackers create or hijack them; defenders baseline and monitor them.

## Windows scheduled tasks
```powershell
# Create (persistence)
schtasks /create /tn "Updater" /tr "C:\Windows\Temp\impl.exe" /sc onlogon /ru SYSTEM
schtasks /create /tn "Health" /tr "powershell -enc <b64>" /sc minute /mo 30
# Hidden/registered via COM or with a benign-looking name in \Microsoft\Windows\...
# Hijack: modify an existing task's action (if writable) to also run your payload
```

## Linux cron / systemd
```bash
# Cron
(crontab -l 2>/dev/null; echo "*/10 * * * * /tmp/.impl") | crontab -
echo '*/5 * * * * root /path/impl' > /etc/cron.d/health
# systemd timer
# updater.service (ExecStart=/path/impl) + updater.timer (OnCalendar/OnBootSec) -> enable
# Hijack: writable script referenced by a root cron/timer, or writable PATH used by it
```

## OPSEC / stealth
```text
- Benign names + locations mimicking legitimate tasks/timers.
- Trigger variety: onlogon, onstart, on idle, interval, at boot.
- Store payload paths that look native (System32/Temp; /usr/local/bin).
```

## Detection (Blue Team)
```text
Windows – Event 4698 (task created), 4702 (updated); Sysmon; \Tasks XML changes.
          Tasks running LOLBins / encoded PowerShell / from Temp = high signal.
Linux   – auditd on /etc/cron*, crontab files, systemd unit dirs; new timers.
Both    – baseline scheduled jobs (golden image); stack-count rare tasks across hosts.
```

## Mitigation / Hardening
- Baseline + monitor scheduled tasks/cron/timers; alert on new/modified (4698/4702, auditd FIM).
- Least privilege; protect task/cron files + referenced scripts (correct ACLs, no writable PATH).
- Related: [windows-persistence](./windows-persistence.md), [linux-persistence](./linux-persistence.md), blue-team [persistence-hunt](../../blue-team/threat-hunting/persistence-hunt.md).

## Sources
- [MITRE T1053](https://attack.mitre.org/techniques/T1053/)
