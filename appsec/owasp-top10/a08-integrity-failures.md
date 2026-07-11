---
title: "A08 – Software and Data Integrity Failures"
category: "appsec"
tags: ["owasp", "integrity", "supply-chain", "deserialization"]
platform: "web"
mitre: []
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# A08 – Software and Data Integrity Failures

## TL;DR
Code and data trusted without integrity verification: unsigned updates, insecure deserialization, compromised CI/CD or dependencies. New category in 2021, driven by supply-chain attacks.

## Examples
```text
- Auto-update without signature verification
- Insecure deserialization of untrusted data -> RCE
- Untrusted CDNs / plugins / packages without integrity checks (no SRI)
- CI/CD pipeline that trusts unsigned artifacts
- Dependency confusion / typosquatting
```

## Insecure deserialization
```text
Java   – ysoserial gadget chains (Commons-Collections, etc.)
PHP    – __wakeup/__destruct magic methods (POP chains)
Python – pickle.loads on untrusted data -> arbitrary code
.NET   – BinaryFormatter, TypeNameHandling in Json.NET
Signal: serialized blobs from cookies/params/uploads
```

## Detection (Blue Team)
- Alerts on deserialization of untrusted input, gadget-chain signatures.
- CI/CD provenance checks, unexpected artifact/source changes.

## Mitigation / Hardening
- Verify signatures on updates/artifacts (cosign), Subresource Integrity (SRI) for scripts.
- Don't deserialize untrusted data; use data-only formats (JSON) with strict schemas.
- Secure the pipeline (see devsecops/supply-chain, ci-cd hardening), pin + verify dependencies.
- SLSA provenance, SBOM, signed commits/artifacts.

## Sources
- [OWASP A08:2021](https://owasp.org/Top10/A08_2021-Software_and_Data_Integrity_Failures/) · [ysoserial](https://github.com/frohoff/ysoserial)
