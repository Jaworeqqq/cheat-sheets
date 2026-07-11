---
title: "DFIR – triage i artefakty"
category: "blue-team"
tags: ["dfir", "forensics", "triage"]
platform: "windows"
mitre: []
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# DFIR – triage i artefakty

## TL;DR
Szybkie zebranie kluczowych artefaktów, budowa timeline'u i odpowiedź na: co, kiedy, jak, skąd. Zachowaj kolejność ulotności i chain of custody.

## Zbieranie (Windows)
```text
Triage tooling: KAPE (Kroll), velociraptor, CyLR
RAM:   winpmem / DumpIt / Magnet RAM Capture
Dysk:  FTK Imager / dd (bit-for-bit + hash)
```

## Kluczowe artefakty Windows
```text
Wykonanie:   Prefetch (C:\Windows\Prefetch), Amcache, ShimCache, SRUM, UserAssist
Persistence: Run keys, Scheduled Tasks, Services, WMI subs, Startup folder
Logowanie:   Security.evtx (4624/4625/4672), RDP (TerminalServices)
Aktywność:   $MFT, $UsnJrnl, LNK, Jump Lists, Recent, Shellbags
Sieć:        DNS cache, netstat, hosts, browser history
```

## Analiza pamięci (Volatility 3)
```bash
vol -f mem.raw windows.pslist          # procesy
vol -f mem.raw windows.pstree          # drzewo (anomalie parent/child)
vol -f mem.raw windows.netscan         # połączenia
vol -f mem.raw windows.malfind         # wstrzyknięty kod
vol -f mem.raw windows.cmdline         # linie komend procesów
```

## Timeline
```bash
# Super timeline (plaso)
log2timeline.py --storage-file out.plaso disk.img
psort.py -o l2tcsv -w timeline.csv out.plaso
# MFT timeline
MFTECmd.exe -f '$MFT' --csv out
```

## Zasady
- Pracuj na **kopiach**, weryfikuj hashe, dokumentuj każdą czynność.
- Kolejność ulotności (RFC 3227): RAM → procesy/sieć → dysk → logi zdalne.

## Źródła
- [SANS DFIR posters](https://www.sans.org/posters/) · [Volatility 3](https://github.com/volatilityfoundation/volatility3) · [Eric Zimmerman tools](https://ericzimmerman.github.io/)
