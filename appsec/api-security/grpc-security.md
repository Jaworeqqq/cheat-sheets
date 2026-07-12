---
title: "gRPC security"
category: "appsec"
tags: ["api-security", "grpc", "authentication"]
platform: "web"
mitre: []
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# gRPC security

## TL;DR
gRPC is a high-performance RPC framework over HTTP/2 using Protocol Buffers. Its security concerns mirror REST/GraphQL — authn/authz, input validation, transport security — but the binary protobuf format and reflection add specifics. The same authorization mistakes (BOLA/BFLA) apply per method.

## Attack surface / recon
```text
- Server reflection (if enabled) exposes the service/method schema — like GraphQL introspection.
- .proto files (leaked/public) reveal all methods, messages, and fields.
Tools: grpcurl (list/describe/call), grpcui (web UI), Postman/BloomRPC, Burp gRPC support.
```
```bash
grpcurl -plaintext target:50051 list                     # services (if reflection on)
grpcurl -plaintext target:50051 describe pkg.Service
grpcurl -plaintext -d '{"id":1}' target:50051 pkg.Service/GetItem
```

## Common issues
```text
- Reflection enabled in production (schema disclosure).
- Missing/weak per-method authorization (BOLA/BFLA — call methods/objects you shouldn't).
- Metadata (auth tokens in gRPC metadata) not validated; trusting client-supplied identity.
- No TLS (plaintext gRPC) -> sniffing/MITM.
- Message-size / streaming abuse -> DoS (unbounded streams, large messages).
- Input validation gaps in message fields (injection into backends).
```

## Detection (Blue Team)
- Reflection queries in prod; unauthorized method calls; oversized/streaming abuse.
- Plaintext gRPC on the wire; anomalous metadata/token usage.

## Mitigation / Hardening
```text
- Disable server reflection in production.
- Enforce TLS/mTLS (mutual auth between services; see service-mesh-security).
- Authenticate + authorize PER METHOD (interceptors/middleware); validate metadata tokens server-side.
- Validate all message fields; set max message size + stream limits + timeouts; rate limit.
- Don't trust client-provided identity/role fields (mass-assignment analog).
```

## Sources
- [gRPC Auth guide](https://grpc.io/docs/guides/auth/) · [grpcurl](https://github.com/fullstorydev/grpcurl) · related: [owasp-api-top10](./owasp-api-top10.md), [rate-limiting](./rate-limiting.md)
