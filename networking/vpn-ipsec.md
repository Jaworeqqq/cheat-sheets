---
title: "VPN & IPsec"
category: "networking"
tags: ["networking", "vpn", "ipsec", "encryption"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# VPN & IPsec

## TL;DR
A VPN creates an encrypted tunnel over an untrusted network. IPsec (network layer) secures site-to-site and remote access; WireGuard and TLS-based VPNs are modern alternatives. Security depends on strong crypto, proper auth, and not treating "on the VPN" as "trusted".

## VPN types
```text
IPsec       – network-layer (L3) tunnels; site-to-site + remote access; IKEv2 for key exchange.
WireGuard   – modern, simple, fast; fixed strong crypto (Curve25519, ChaCha20); small codebase.
TLS/SSL VPN – over TLS (OpenVPN, or clientless portals); firewall-friendly (443).
```

## IPsec building blocks
```text
IKE (IKEv2)  – negotiates keys + SAs (Phase 1: secure channel; Phase 2: data SAs).
ESP          – encrypts + authenticates payload (the workhorse; use ESP, not AH-only).
Modes        – Tunnel (whole packet, site-to-site) vs Transport (payload, host-to-host).
Auth         – pre-shared key (PSK) or certificates (prefer certs / EAP for remote users).
```

## Secure configuration
```text
- IKEv2 with strong DH groups (19/20/21 ECP or 14+), AES-GCM, SHA-256+.
- Avoid IKEv1 aggressive mode + PSK (offline crackable); avoid weak DH (1,2,5).
- Certificate-based auth + MFA for remote access; per-user, revocable.
- Perfect Forward Secrecy (PFS) enabled.
```

## Security considerations
```text
- VPN gateways are high-value targets — patch promptly (many critical CVEs historically).
- "On the VPN" != trusted: pair with Zero Trust / device posture, don't grant flat access.
- Split-tunnel vs full-tunnel: trade-off between visibility and performance.
```

## Detection (Blue Team)
- VPN logs: impossible travel, brute force on the portal, logins without MFA, new client versions.
- Alert on config/cert changes; monitor gateway CVEs and exploitation attempts.

## Mitigation / Hardening
- Strong modern crypto (IKEv2/WireGuard), cert-based auth + MFA, patch the gateway.
- Least-privilege network access post-tunnel (segmentation, Zero Trust), log everything.
- Related: [common-protocols](./common-protocols.md), [tls-config](../cryptography/tls-config.md).

## Sources
- [WireGuard](https://www.wireguard.com/) · [NIST SP 800-77 (IPsec VPNs)](https://csrc.nist.gov/pubs/sp/800/77/r1/final)
