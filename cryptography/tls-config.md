---
title: "Secure TLS configuration"
category: "cryptography"
tags: ["cryptography", "tls", "hardening"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Secure TLS configuration

## TL;DR
TLS protects data in transit. A secure config means: modern protocol versions, strong cipher suites with forward secrecy, valid certificates, and supporting headers (HSTS). Test it — misconfig is common (OWASP A02).

## Protocol versions
```text
TLS 1.3 – preferred (faster handshake, only strong ciphers, forward secrecy by default)
TLS 1.2 – acceptable with a strong cipher list
TLS 1.0/1.1, SSLv3/v2 – DISABLE (deprecated, vulnerable: POODLE, BEAST, etc.)
```

## Cipher suites
```text
- Require forward secrecy (ECDHE key exchange) — a leaked key can't decrypt past traffic.
- Prefer AEAD ciphers: AES-GCM, ChaCha20-Poly1305.
- Avoid: RC4, 3DES, CBC-mode legacy suites, NULL/EXPORT/anon.
TLS 1.3 removes weak options entirely (only 5 strong AEAD suites).
```

## Certificates
```text
- Strong keys (RSA >= 2048, or ECDSA P-256), SHA-256+ signatures.
- Valid chain, correct SAN (hostname), not expired; automate renewal (ACME/Let's Encrypt).
- OCSP stapling to avoid revocation-check latency.
- Monitor CT logs for mis-issuance (see cryptography/pki-x509).
```

## Supporting headers / features
```text
Strict-Transport-Security (HSTS)  – force HTTPS: max-age=63072000; includeSubDomains; preload
- Disable TLS compression (CRIME), renegotiation abuse.
- Consider mTLS for service-to-service / zero-trust.
```

## Example (nginx snippet)
```nginx
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:...;
ssl_prefer_server_ciphers off;      # let TLS 1.3 client choose
ssl_stapling on; ssl_stapling_verify on;
add_header Strict-Transport-Security "max-age=63072000; includeSubDomains" always;
```

## Testing
```bash
testssl.sh https://example.com          # comprehensive local scan
nmap --script ssl-enum-ciphers -p443 example.com
# SSL Labs (external): https://www.ssllabs.com/ssltest/
```

## Detection / defense (Blue Team)
- Continuous TLS scanning in CI/monitoring; alert on weak protocols/ciphers and expiring certs.

## Sources
- [Mozilla SSL Config Generator](https://ssl-config.mozilla.org/) · [testssl.sh](https://testssl.sh/) · [SSL Labs](https://www.ssllabs.com/ssltest/)
