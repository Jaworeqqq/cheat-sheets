---
title: "CSPM / CNAPP – cloud posture"
category: "cloud-security"
tags: ["multi-cloud", "cspm", "cnapp", "posture"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# CSPM / CNAPP – cloud posture management

## TL;DR
CSPM (Cloud Security Posture Management) continuously checks cloud configs against best practices/benchmarks and flags misconfigurations. CNAPP bundles CSPM + workload (CWPP) + IAM (CIEM) + code scanning into one platform.

## Acronyms
```text
CSPM – posture/config misconfigurations (public buckets, open SGs, no encryption)
CWPP – workload protection (VMs, containers, serverless runtime)
CIEM – entitlements/identity (excessive permissions, unused access)
CNAPP – umbrella combining the above + IaC/code scanning (shift-left + runtime)
```

## Open-source tooling
```bash
# Multi-cloud posture scanning
prowler aws                          # AWS (also azure/gcp/k8s)
scoutsuite aws                       # AWS/Azure/GCP HTML report
steampipe query "select ..."         # SQL over cloud APIs (with mods/compliance)
cloudsploit / cloudquery             # inventory + checks
# Kubernetes posture
kubescape scan
```

## What it catches (examples)
```text
- Public storage (S3/GCS/Blob), unencrypted resources
- Overly permissive security groups / firewall rules (0.0.0.0/0)
- IAM: wildcard policies, unused/over-privileged principals (CIEM)
- Missing logging (CloudTrail/flow logs), no MFA on privileged
- Drift from CIS/benchmark baselines
```

## Operating model
```text
- Continuous scanning (not point-in-time), map findings to owners.
- Prioritize by exploitability + exposure (public + high-priv = fix first).
- Combine with IaC scanning (prevent) — CSPM catches drift/runtime reality.
- Feed findings to ticketing/SIEM; track MTTR.
```

## Mitigation / Hardening
- Guardrails via SCP/Azure Policy/Org Policy (prevent misconfig at source).
- Remediate high-exposure findings first; automate remediation where safe.

## Sources
- [Prowler](https://github.com/prowler-cloud/prowler) · [ScoutSuite](https://github.com/nccgroup/ScoutSuite) · [Steampipe](https://steampipe.io/)
