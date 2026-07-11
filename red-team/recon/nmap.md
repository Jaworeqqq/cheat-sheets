---
title: "Nmap – skanowanie i enumeracja"
category: "red-team"
tags: ["recon", "scanning", "nmap"]
platform: "agnostic"
mitre: ["T1046", "T1595"]
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# Nmap – skanowanie i enumeracja

## TL;DR
Mapowanie hostów, portów i usług. Zacznij szeroko (host discovery), potem celowany skan usług + skrypty NSE.

## Komendy
```bash
# Host discovery (ping sweep, bez skanu portów)
nmap -sn 10.10.10.0/24

# Szybki skan top-1000 TCP
nmap -sV -T4 10.10.10.5

# Pełny skan wszystkich portów TCP + wersje + OS + skrypty domyślne
nmap -p- -sV -sC -O -T4 -oA scans/full 10.10.10.5

# UDP top-100 (wolne – ogranicz porty)
nmap -sU --top-ports 100 10.10.10.5

# Konkretne skrypty NSE (np. SMB)
nmap -p445 --script "smb-vuln-*" 10.10.10.5
```

## Wykrywanie (Blue Team)
Masowe SYN do wielu portów w krótkim czasie z jednego źródła.
```sql
-- Splunk: potencjalny port scan
index=firewall action=blocked
| stats dc(dest_port) AS ports by src_ip
| where ports > 100
```
IDS: reguły Suricata/Snort na `stream5`/`sfPortscan`.

## Mitygacja / Hardening
- Rate-limiting i IPS na brzegu sieci.
- Minimalizacja ekspozycji portów (least exposure), segmentacja.
- Firewall drop zamiast reject (utrudnia enumerację).

## Uwagi / Pułapki
- `-T5` bywa nieprzyjazny/gubi wyniki na filtrowanych sieciach — trzymaj się `-T4`.
- `-oA` zapisuje 3 formaty (nmap/gnmap/xml) — przydatne do dalszego parsowania.

## Źródła
- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [MITRE T1046](https://attack.mitre.org/techniques/T1046/)
