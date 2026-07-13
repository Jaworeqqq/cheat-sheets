---
title: "Policy testing (policy-as-code)"
category: "devsecops"
tags: ["iac", "policy-as-code", "opa", "testing"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Policy testing

## TL;DR
Policy-as-code (OPA/Rego, Sentinel, Kyverno, Checkov custom) is code — so it needs tests. Untested policies cause two failures: false negatives (bad config slips through) and false positives (blocking legitimate changes, eroding trust). Unit-test policies with pass/fail fixtures before enforcing.

## Why test policies
```text
- A policy that never fires (bug/typo) gives false assurance — bad configs pass.
- An overly strict policy blocks valid deploys -> developers bypass/disable it.
- Policies evolve; tests catch regressions when you refactor.
```

## Testing approaches by tool
```text
OPA/Rego     – `opa test` with test_ rules; conftest `verify` with fixtures.
Checkov      – custom policy unit tests (pass/fail example resources).
Kyverno      – `kyverno test` with resource + expected-result manifests (CI-friendly).
Sentinel     – built-in test harness with mock data.
```

## OPA/Rego test example
```rego
package main
# policy: deny public S3
deny[msg] { input.acl == "public-read"; msg := "public bucket" }

# test (in *_test.rego)
test_denies_public { deny with input as {"acl": "public-read"} }
test_allows_private { count(deny) == 0 with input as {"acl": "private"} }
```
```bash
opa test . -v
conftest verify -p policy/
kyverno test .
```

## What to cover
```text
- Positive: a compliant resource passes.
- Negative: each violation type is caught.
- Edge cases: missing fields, nested structures, different providers/resource shapes.
- Exceptions: intentional allow-list/skip works as designed.
```

## In the pipeline
```text
- Run policy unit tests on PRs to the policy repo (block merges on failures).
- Then run the policies against real IaC (plan JSON / manifests) as a gate.
- Roll out new policies in warn/dry-run first; promote to enforce after validating impact.
```

## Sources
- [OPA testing](https://www.openpolicyagent.org/docs/latest/policy-testing/) · [Kyverno test](https://kyverno.io/docs/kyverno-cli/) · related: [opa-conftest](./opa-conftest.md), [iac-scanning](./iac-scanning.md)
