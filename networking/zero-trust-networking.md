---
title: "Zero Trust networking"
category: "networking"
tags: ["networking", "zero-trust", "architecture"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# Zero Trust networking

## TL;DR
Zero Trust replaces "trust the internal network" with "never trust, always verify". Every access request is authenticated, authorized, and encrypted based on identity and device posture — regardless of network location. The network is no longer the security boundary; identity is.

## Core principles (NIST 800-207)
```text
- Never trust based on network location (no implicit trust for "inside the perimeter").
- Verify explicitly: authenticate + authorize every request (identity + device + context).
- Least-privilege access, per-session, just-enough.
- Assume breach: segment, encrypt, monitor everything.
- Continuous verification (not one-time at login).
```

## Building blocks
```text
Identity        – strong authN (phishing-resistant MFA), SSO, per-request authZ.
Device posture  – compliant/managed/healthy device as an access condition (MDM/EDR signals).
Micro-segmentation – per-workload policy (see networking/network-segmentation, service mesh).
Policy engine / PEP – decides + enforces access per request (ZTNA broker, mesh, gateway).
Encryption      – everywhere (mTLS east-west, TLS north-south).
Telemetry       – log + analyze every access for continuous risk evaluation.
```

## ZTNA vs VPN
```text
VPN   – authenticate once -> broad network access ("inside" = trusted). Flat, over-permissive.
ZTNA  – authenticate per application; grant access only to specific apps based on identity+posture;
        apps are "dark" (not network-reachable) until authorized. No lateral network access.
```

## Reference implementations
```text
- Cloud IAM + Conditional Access (Entra) / context-aware access (Google) as the policy engine.
- Service mesh (mTLS + per-service authz) for east-west (see service-mesh-security).
- ZTNA products (identity-aware proxies) replacing VPN for remote access.
- Microsegmentation for workloads; SASE combining ZTNA + SWG + CASB.
```

## Migration approach
```text
1. Inventory identities, devices, apps, and data flows.
2. Strong identity + MFA everywhere; add device posture.
3. Move high-value apps behind an identity-aware proxy (ZTNA) — retire flat VPN access.
4. Micro-segment; enforce least privilege; encrypt east-west.
5. Continuous monitoring + adaptive policy. It's a journey, not a product.
```

## Sources
- [NIST SP 800-207 (Zero Trust)](https://csrc.nist.gov/pubs/sp/800/207/final) · related: [network-segmentation](./network-segmentation.md), [conditional-access](../cloud-security/azure/conditional-access.md), [service-mesh-security](../devsecops/kubernetes/service-mesh-security.md)
