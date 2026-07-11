---
title: "Falco – runtime threat detection"
category: "devsecops"
tags: ["containers", "kubernetes", "runtime-security", "falco"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Falco – runtime security

## TL;DR
Falco (CNCF) detects abnormal behavior at runtime by watching kernel syscalls (eBPF) and K8s audit events. It's the "blue team" for containers — catches what image scanning can't (behavior after deploy).

## What it detects
```text
- Shell spawned inside a container (interactive/reverse shell)
- Write to sensitive paths (/etc, binaries), mount of docker.sock
- Unexpected outbound network connections / crypto-miner behavior
- Privilege escalation, use of privileged capabilities
- K8s: exec into pods, secret access, creation of privileged pods
```

## Rule example
```yaml
- rule: Terminal shell in container
  desc: A shell was spawned in a container
  condition: >
    spawned_process and container
    and shell_procs and proc.tty != 0
    and not user_expected_terminal_shell_in_container_conditions
  output: >
    Shell in container (user=%user.name container=%container.name
    proc=%proc.cmdline image=%container.image.repository)
  priority: WARNING
  tags: [container, shell, mitre_execution]
```

## Deploy on Kubernetes
```bash
helm repo add falcosecurity https://falcosecurity.github.io/charts
helm install falco falcosecurity/falco --namespace falco --create-namespace \
  --set driver.kind=ebpf
# Route alerts with Falcosidekick (Slack, SIEM, etc.)
```

## Best practices
```text
- Start with default rules, then tune to cut false positives (label expected behavior).
- Ship alerts to a SIEM/Slack via Falcosidekick; wire into IR.
- Combine with admission control (prevent) — Falco detects, Kyverno/OPA blocks.
- Version custom rules in git; test against known-bad behavior.
```

## Mitigation / Hardening (paired controls)
- Pod Security (restricted), read-only FS, drop capabilities — reduce what Falco must alert on.
- See also: [kubernetes/k8s-security](../kubernetes/k8s-security.md), [containers/docker-hardening](./docker-hardening.md).

## Sources
- [Falco](https://falco.org/) · [Falco rules](https://github.com/falcosecurity/rules)
