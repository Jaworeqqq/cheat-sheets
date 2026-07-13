---
title: "Network device hardening"
category: "blue-team"
tags: ["hardening", "network", "routers", "switches"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Network device hardening

## TL;DR
Routers, switches, firewalls, and VPN gateways are high-value targets — compromise means traffic interception, pivoting, and persistence. They're often under-patched and use weak defaults. Harden the management plane, control plane, and data plane; the CISA/NSA guidance on network infrastructure is the reference.

## Management plane (biggest risk)
```text
- No default/shared credentials; unique strong passwords; MFA/TACACS+/RADIUS for admin.
- Disable unused management (Telnet, HTTP) -> SSHv2 / HTTPS only; restrict to a mgmt VLAN/ACL.
- Out-of-band management network; no management from the internet.
- Role-based admin (least privilege), command authorization + accounting (AAA).
- Encrypted config storage; secure the config backups (they contain secrets).
```

## Control plane
```text
- Control-plane policing (CoPP) to protect the CPU from floods.
- Authenticate routing protocols (OSPF/BGP with auth); filter BGP (RPKI, prefix limits).
- Disable unneeded services (CDP/LLDP externally, source routing, proxy ARP).
```

## Data plane
```text
- Port security (limit MACs), disable unused ports, DHCP snooping, Dynamic ARP Inspection.
- BPDU guard / root guard (spanning tree attacks), storm control.
- Segmentation/VLANs + ACLs (see networking/network-segmentation).
```

## Patching & lifecycle (critical)
```text
- Network gear has frequent critical CVEs (VPN gateways especially) — patch promptly.
- Replace end-of-life devices (no patches = permanent risk).
- Verify firmware integrity; watch for implants/persistence in device OS.
```

## Detection (Blue Team)
- Config changes (AAA accounting), new admin sessions/sources, failed logins.
- Unexpected firmware changes; syslog to a central SIEM; NetFlow anomalies.

## Mitigation / Hardening
- Follow CIS/NSA hardening guides; centralize AAA + logging; OOB management; patch aggressively.
- Config backups + change control; monitor for unauthorized changes.
- Related: [firewall-fundamentals](../../networking/firewall-fundamentals.md), [network-segmentation](../../networking/network-segmentation.md).

## Sources
- [CISA/NSA – Network Infrastructure Security Guide](https://www.cisa.gov/) · [CIS Benchmarks (Cisco/network)](https://www.cisecurity.org/cis-benchmarks)
