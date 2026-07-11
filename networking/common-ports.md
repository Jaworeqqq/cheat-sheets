---
title: "Common ports and services"
category: "networking"
tags: ["networking", "ports", "recon"]
platform: "agnostic"
mitre: []
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# Common ports and services

## TL;DR
A quick lookup of ports encountered during scanning — what's listening and what vector to consider.

## Most common
| Port | Service | Notes/vector |
|------|---------|--------------|
| 21 | FTP | anon login, clear-text, bounce |
| 22 | SSH | brute/key, version -> CVE |
| 23 | Telnet | clear-text, legacy |
| 25/465/587 | SMTP | user enum (VRFY), open relay |
| 53 | DNS | AXFR, tunneling |
| 80/443 | HTTP/S | the whole web surface |
| 88 | Kerberos | AD (roasting) |
| 110/143/993/995 | POP3/IMAP | mail, clear-text variants |
| 111/2049 | RPCbind/NFS | NFS exports, no_root_squash |
| 135/139/445 | RPC/NetBIOS/SMB | AD core, EternalBlue, null session |
| 161 | SNMP | community strings (public/private) |
| 389/636 | LDAP/LDAPS | AD enum, null bind |
| 1433 | MSSQL | brute, xp_cmdshell |
| 1521 | Oracle | TNS, brute |
| 3306 | MySQL | brute, weak creds |
| 3389 | RDP | brute, BlueKeep, NLA |
| 5432 | PostgreSQL | brute, COPY TO PROGRAM |
| 5985/5986 | WinRM | remote execution (evil-winrm) |
| 6379 | Redis | no auth -> RCE/webshell |
| 8080/8443 | HTTP alt | panels, proxy, Tomcat |

## Quick scan
```bash
nmap -p- --min-rate 2000 -T4 TARGET       # all ports fast
nmap -sV -sC -p <open> TARGET             # versions + scripts on the ones found
```

## Defense (Blue Team)
- Minimize exposure (least exposure), firewall default-deny, hide management services behind a VPN.

## Sources
- [Nmap – ports](https://nmap.org/book/man-port-scanning-basics.html) · [HackTricks – Pentesting ports](https://book.hacktricks.xyz/)
