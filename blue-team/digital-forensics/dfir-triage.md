---
title: "DFIR – triage and artifacts"
category: "blue-team"
tags: ["dfir", "forensics", "triage"]
platform: "windows"
mitre: []
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# DFIR – triage and artifacts

## TL;DR
Quickly collect key artifacts, build a timeline, and answer: what, when, how, from where. Preserve the order of volatility and chain of custody.

## Collection (Windows)
```text
Triage tooling: KAPE (Kroll), velociraptor, CyLR
RAM:   winpmem / DumpIt / Magnet RAM Capture
Disk:  FTK Imager / dd (bit-for-bit + hash)
```

## Key Windows artifacts
```text
Execution:   Prefetch (C:\Windows\Prefetch), Amcache, ShimCache, SRUM, UserAssist
Persistence: Run keys, Scheduled Tasks, Services, WMI subs, Startup folder
Logon:       Security.evtx (4624/4625/4672), RDP (TerminalServices)
Activity:    $MFT, $UsnJrnl, LNK, Jump Lists, Recent, Shellbags
Network:     DNS cache, netstat, hosts, browser history
```

## Memory analysis (Volatility 3)
```bash
vol -f mem.raw windows.pslist          # processes
vol -f mem.raw windows.pstree          # tree (parent/child anomalies)
vol -f mem.raw windows.netscan         # connections
vol -f mem.raw windows.malfind         # injected code
vol -f mem.raw windows.cmdline         # process command lines
```

## Timeline
```bash
# Super timeline (plaso)
log2timeline.py --storage-file out.plaso disk.img
psort.py -o l2tcsv -w timeline.csv out.plaso
# MFT timeline
MFTECmd.exe -f '$MFT' --csv out
```

## Rules
- Work on **copies**, verify hashes, document every action.
- Order of volatility (RFC 3227): RAM → processes/network → disk → remote logs.

## Sources
- [SANS DFIR posters](https://www.sans.org/posters/) · [Volatility 3](https://github.com/volatilityfoundation/volatility3) · [Eric Zimmerman tools](https://ericzimmerman.github.io/)
