---
title: "Popularne porty i usługi"
category: "networking"
tags: ["networking", "ports", "recon"]
platform: "agnostic"
mitre: []
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# Popularne porty i usługi

## TL;DR
Szybki lookup portów spotykanych podczas skanowania — co słucha i jaki wektor rozważyć.

## Najczęstsze
| Port | Usługa | Uwagi/wektor |
|------|--------|--------------|
| 21 | FTP | anon login, clear-text, bounce |
| 22 | SSH | brute/key, wersja -> CVE |
| 23 | Telnet | clear-text, legacy |
| 25/465/587 | SMTP | user enum (VRFY), open relay |
| 53 | DNS | AXFR, tunneling |
| 80/443 | HTTP/S | cała powierzchnia web |
| 88 | Kerberos | AD (roasting) |
| 110/143/993/995 | POP3/IMAP | poczta, clear-text warianty |
| 111/2049 | RPCbind/NFS | eksporty NFS, no_root_squash |
| 135/139/445 | RPC/NetBIOS/SMB | AD core, EternalBlue, null session |
| 161 | SNMP | community strings (public/private) |
| 389/636 | LDAP/LDAPS | AD enum, null bind |
| 1433 | MSSQL | brute, xp_cmdshell |
| 1521 | Oracle | TNS, brute |
| 3306 | MySQL | brute, weak creds |
| 3389 | RDP | brute, BlueKeep, NLA |
| 5432 | PostgreSQL | brute, COPY TO PROGRAM |
| 5985/5986 | WinRM | zdalne wykonanie (evil-winrm) |
| 6379 | Redis | brak auth -> RCE/webshell |
| 8080/8443 | HTTP alt | panele, proxy, Tomcat |

## Szybki skan
```bash
nmap -p- --min-rate 2000 -T4 TARGET       # wszystkie porty szybko
nmap -sV -sC -p <otwarte> TARGET          # wersje + skrypty na znalezionych
```

## Obrona (Blue Team)
- Minimalizuj ekspozycję (least exposure), firewall default-deny, ukryj usługi zarządzania za VPN.

## Źródła
- [Nmap – ports](https://nmap.org/book/man-port-scanning-basics.html) · [HackTricks – Pentesting ports](https://book.hacktricks.xyz/)
