---
title: "Common protocols – security reference"
category: "networking"
tags: ["networking", "protocols", "ports"]
platform: "agnostic"
mitre: []
difficulty: "basic"
updated: "2026-07-12"
author: "core"
---

# Common protocols – security reference

## TL;DR
Quick reference for common protocols: default port, whether traffic is cleartext or encrypted, and the main security consideration. Cleartext protocols are prime targets for sniffing and MITM.

## Reference table
| Protocol | Port | Encrypted? | Security note |
|----------|------|-----------|---------------|
| HTTP | 80 | ❌ | cleartext; use HTTPS + HSTS |
| HTTPS | 443 | ✅ TLS | check TLS config (see cryptography/tls-config) |
| FTP | 21 | ❌ | cleartext creds; use SFTP/FTPS |
| SSH / SFTP | 22 | ✅ | key auth > password; disable root login |
| Telnet | 23 | ❌ | legacy, cleartext — disable |
| SMTP | 25/587 | ⚠️ | use STARTTLS/submission; SPF/DKIM/DMARC |
| DNS | 53 | ❌ | use DoT/DoH; DNSSEC for integrity |
| Kerberos | 88 | ✅ | AD auth; roasting if RC4/weak |
| POP3/IMAP | 110/143 | ⚠️ | use 993/995 (TLS) variants |
| SNMP | 161 | ⚠️ | v1/v2c cleartext community strings; use v3 |
| LDAP | 389 | ❌ | use LDAPS (636) / StartTLS; no null bind |
| SMB | 445 | ⚠️ | require signing; disable SMBv1 |
| LDAPS | 636 | ✅ | encrypted directory |
| RDP | 3389 | ✅* | enforce NLA; brute/BlueKeep risk |
| MSSQL | 1433 | ⚠️ | encrypt connections; strong auth |
| MySQL/PostgreSQL | 3306/5432 | ⚠️ | require TLS; no default creds |
| Redis | 6379 | ❌ | no auth by default -> RCE; bind/ACL/TLS |
| WinRM | 5985/5986 | ⚠️/✅ | 5985 http, 5986 https; used for lateral movement |

\* RDP encrypts by default but weak configs (no NLA) are attackable.

## Cleartext vs encrypted — why it matters
```text
Cleartext (HTTP/FTP/Telnet/SNMPv1/LDAP) -> credentials & data sniffable on the wire,
  trivial MITM on shared/compromised networks. Always prefer the TLS/encrypted variant.
```

## Detection / defense (Blue Team)
- Alert on cleartext protocols carrying credentials (see networking/tcpdump, wireshark-filters).
- Inventory listening services; disable legacy (Telnet, FTP, SMBv1, SNMPv1/2c).

## Mitigation / Hardening
- Prefer encrypted variants everywhere; enforce TLS, signing, and modern auth.
- Segment management protocols (RDP/SSH/WinRM) behind VPN/bastion; least exposure.

## Sources
- [IANA Service Name and Port Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml) · related: [common-ports](./common-ports.md)
