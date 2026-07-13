---
title: "eBPF for runtime security"
category: "devsecops"
tags: ["containers", "ebpf", "runtime-security", "kubernetes"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# eBPF for runtime security

## TL;DR
eBPF runs sandboxed programs in the Linux kernel to observe (and enforce on) syscalls, network, and process events with low overhead — no kernel modules. It powers modern runtime security and observability tools (Falco, Tetragon, Cilium) that detect and block malicious behavior inside containers and hosts.

## Why eBPF for security
```text
- Kernel-level visibility: see every syscall, network flow, file access, process exec.
- Low overhead + safe: verified programs, no custom kernel modules.
- Container-aware: correlate events to pods/containers/namespaces.
- Enforcement: some tools can block (kill/deny), not just alert.
```

## Tools
```text
Falco       – runtime threat detection (rules on syscalls); alert-focused (see containers/falco-runtime).
Tetragon    – Cilium's eBPF security observability + enforcement (can kill on policy violation).
Cilium      – eBPF CNI: network policy (L3-L7), identity, encryption, observability (Hubble).
Tracee (Aqua) – eBPF runtime detection + forensics.
```

## What it detects at runtime
```text
- Shell spawned in a container; exec into pods.
- Unexpected network connections / DNS (C2 beaconing signals).
- Sensitive file access (/etc/shadow), capability abuse, privilege escalation.
- Writes to binaries, kernel module loads, ptrace, unusual syscalls.
- Container escapes / host namespace access.
```

## Enforcement example (Tetragon concept)
```text
Policy: if a process in namespace X executes /bin/bash -> kill it.
eBPF hooks the exec syscall, matches the policy, and terminates the process in-kernel.
-> Prevention, not just detection (vs Falco's alert-then-respond model).
```

## Detection vs prevention
```text
Detect  – Falco/Tracee: rich alerts -> SIEM/IR (respond).
Prevent – Tetragon/Cilium: block at the kernel (kill/deny) for high-confidence policies.
Pair with admission control (prevent bad pods) + Pod Security (see kubernetes/*).
```

## Best practices
- Tune rules to cut false positives; start in observe mode, then enforce high-confidence policies.
- Feed events to a SIEM; correlate with K8s audit + admission.
- Related: [falco-runtime](./falco-runtime.md), [k8s-security](../kubernetes/k8s-security.md), [network-policies](../kubernetes/network-policies.md).

## Sources
- [eBPF](https://ebpf.io/) · [Tetragon](https://tetragon.io/) · [Falco](https://falco.org/) · [Cilium](https://cilium.io/)
