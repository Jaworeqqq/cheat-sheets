---
title: "Policy as Code – OPA / Conftest"
category: "devsecops"
tags: ["iac", "opa", "rego", "policy-as-code"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Policy as Code – OPA / Conftest

## TL;DR
Open Policy Agent (OPA) evaluates policies written in Rego against JSON/YAML input. **Conftest** runs OPA policies against config files (Terraform plan, K8s manifests, Dockerfiles) in CI to enforce organizational rules — beyond generic scanners.

## Where it fits
```text
- Generic scanners (Checkov/trivy) catch known misconfigs.
- OPA/Conftest enforces YOUR rules: naming, mandatory tags, allowed regions,
  approved base images, required labels, denied resource types.
- Gatekeeper/Kyverno do the same at K8s admission time (runtime enforcement).
```

## Rego policy example (deny public S3)
```rego
package main

deny[msg] {
  resource := input.resource.aws_s3_bucket[name]
  resource.acl == "public-read"
  msg := sprintf("S3 bucket '%s' must not be public-read", [name])
}

deny[msg] {
  resource := input.resource.aws_instance[name]
  not resource.tags.Owner
  msg := sprintf("EC2 '%s' is missing required tag: Owner", [name])
}
```

## Run in CI
```bash
# Terraform: evaluate the plan as JSON
terraform show -json plan.tfout > plan.json
conftest test plan.json -p policy/

# Kubernetes manifests / Dockerfile
conftest test deployment.yaml -p policy/
conftest test Dockerfile -p policy/

# Test the policies themselves
conftest verify -p policy/
```

## Kubernetes admission (Gatekeeper)
```text
- ConstraintTemplate (Rego logic) + Constraint (parameters/scope).
- Enforces at admission: block privileged pods, require labels, restrict registries.
- dryrun mode first (audit), then enforce.
```

## Best practices
```text
- Version policies in git; unit-test them (conftest verify / OPA test).
- Start in warn/dryrun, then enforce; give clear remediation messages.
- Reuse community bundles; keep policies DRY with Rego functions/libraries.
```

## Sources
- [OPA](https://www.openpolicyagent.org/) · [Conftest](https://www.conftest.dev/) · [Gatekeeper](https://open-policy-agent.github.io/gatekeeper/)
