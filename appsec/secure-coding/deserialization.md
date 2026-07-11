---
title: "Insecure deserialization"
category: "appsec"
tags: ["secure-coding", "deserialization", "rce"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Insecure deserialization

## TL;DR
Deserializing untrusted data can instantiate arbitrary objects and trigger code execution via "gadget chains". Impact ranges from RCE to auth bypass and DoS. Don't deserialize untrusted input with code-capable formats.

## Where it hides
```text
- Session cookies, hidden form fields, API bodies containing serialized blobs
- Caches, message queues, uploaded files
- Look for: base64 blobs starting with rO0 (Java), gASV (Python pickle), TypeNameHandling (.NET)
```

## Language specifics
```text
Java   – ObjectInputStream + gadget chains (ysoserial); prefer avoiding native serialization
PHP    – unserialize() + POP chains (__wakeup/__destruct)
Python – pickle/pyyaml.load on untrusted input = arbitrary code
.NET   – BinaryFormatter (obsolete), Json.NET TypeNameHandling.All
Ruby   – Marshal.load, YAML.load with untrusted input
```

## Detection (Blue Team)
- WAF/log signatures for serialized markers, DNS/HTTP callbacks from gadget execution.
- Alert on deserialization exceptions and unexpected class loading.

## Mitigation / Hardening
- **Don't deserialize untrusted data.** Use data-only formats (JSON/Protobuf) with strict schemas.
- If unavoidable: allow-list expected types, integrity-check (HMAC/signature) the payload.
- Java: `ObjectInputFilter` allow-lists; .NET: avoid `BinaryFormatter`, `TypeNameHandling.None`.
- Python: `yaml.safe_load`, never `pickle` on untrusted input.
- Run deserializers with least privilege / sandboxed.

## Sources
- [OWASP – Deserialization CS](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html) · [ysoserial](https://github.com/frohoff/ysoserial)
