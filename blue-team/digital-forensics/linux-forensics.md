---
title: "Linux forensics"
category: "blue-team"
tags: ["dfir", "forensics", "linux", "triage"]
platform: "linux"
mitre: []
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Linux forensics

## TL;DR
Investigate a compromised Linux host: capture volatile state, collect logs and persistence artifacts, reconstruct a timeline, and extract IOCs. Work on copies, preserve order of volatility, document everything.

## Volatile capture (before touching disk)
```bash
# Live triage (run from trusted binaries / static toolset)
ps auxww; ls -la /proc/*/exe 2>/dev/null      # running procs + backing binaries
ss -tulpanee                                   # connections + owning PIDs
lsof -nP                                        # open files/sockets
cat /proc/<pid>/maps /proc/<pid>/cmdline        # per-process memory map/cmdline
# Memory image: AVML or LiME
sudo ./avml mem.lime
```

## Key log sources
```text
/var/log/auth.log | /var/log/secure   – logins, sudo, SSH (auth events)
/var/log/syslog | /var/log/messages   – general system
journalctl                            – systemd journal (journalctl -o short-iso)
/var/log/wtmp,btmp,lastlog            – login history (last, lastb)
~/.bash_history (+ HISTTIMEFORMAT)     – shell commands (may be tampered)
/var/log/audit/audit.log              – auditd (execve, file access) if enabled
web/app logs                          – /var/log/nginx, apache2, etc.
```

## Persistence locations to check
```text
Cron:     /etc/crontab, /etc/cron.*, /var/spool/cron/*, user crontabs
systemd:  /etc/systemd/system/*, ~/.config/systemd/user/*, timers
Init/rc:  /etc/rc.local, /etc/init.d, /etc/profile.d/*
Shell:    ~/.bashrc, ~/.bash_profile, /etc/bash.bashrc
SSH:      ~/.ssh/authorized_keys (backdoor keys), sshd_config
Accounts: /etc/passwd (uid 0 dupes), /etc/sudoers(.d)
Preload:  /etc/ld.so.preload, LD_PRELOAD (userland rootkits)
Kernel:   lsmod / suspicious modules
```

## Timeline (inode timestamps / filesystem)
```bash
# MACB timeline with Sleuth Kit
fls -r -m / /dev/sda1 > body.txt
mactime -b body.txt -d > timeline.csv
# Super timeline (plaso)
log2timeline.py --storage-file out.plaso /evidence
psort.py -o l2tcsv -w timeline.csv out.plaso
# Quick: recently modified files
find / -xdev -type f -mtime -2 2>/dev/null
stat suspicious_bin                              # atime/mtime/ctime (ctime = harder to fake)
```

## Extracting IOCs
```text
- Hashes of suspect binaries (sha256sum) -> VT/threat intel.
- C2 indicators from ss/netstat + logs; scheduled/persistence entries.
- YARA scan the filesystem/memory (see detection-engineering/yara-rules.md).
```

## Detection (Blue Team)
- New uid 0 accounts, backdoor SSH keys, `/etc/ld.so.preload` entries, hidden kernel modules.
- Cleared/truncated logs, `.bash_history` linked to /dev/null, timestomped binaries (ctime mismatch).
- Cron/systemd units spawning outbound connections.

## Mitigation / Hardening
- Centralize logs off-host (SIEM), enable auditd with a good ruleset, FIM (AIDE) on key paths.
- See [cis-linux](../hardening/cis-linux.md) for baseline; pair with [dfir-triage](./dfir-triage.md).

## Sources
- [SANS Linux DFIR](https://www.sans.org/posters/) · [The Sleuth Kit](https://www.sleuthkit.org/) · [Velociraptor](https://docs.velociraptor.app/) · [AVML](https://github.com/microsoft/avml)
