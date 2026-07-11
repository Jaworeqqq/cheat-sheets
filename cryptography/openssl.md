---
title: "OpenSSL – practical cheat sheet"
category: "cryptography"
tags: ["cryptography", "openssl", "tls", "pki"]
platform: "agnostic"
mitre: []
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# OpenSSL

## TL;DR
The Swiss Army knife for crypto: keys, CSRs, certs, TLS inspection, file encryption, hashes.

## Keys and certificates
```bash
# RSA / EC private key
openssl genrsa -out key.pem 4096
openssl ecparam -genkey -name prime256v1 -out ec.pem

# CSR
openssl req -new -key key.pem -out req.csr -subj "/CN=example.com/O=Org"

# Self-signed (test/lab)
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes \
  -subj "/CN=localhost"

# Inspect a cert / CSR
openssl x509 -in cert.pem -noout -text
openssl req -in req.csr -noout -text
```

## Inspect a remote server's TLS
```bash
# Certificate + chain + versions/ciphersuites
openssl s_client -connect example.com:443 -servername example.com </dev/null
# Validity dates
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -dates
# Check supported protocol versions
openssl s_client -connect example.com:443 -tls1_2 </dev/null
```

## File encryption
```bash
# AES-256 with a KDF (pbkdf2) – symmetric
openssl enc -aes-256-cbc -pbkdf2 -salt -in file -out file.enc
openssl enc -d -aes-256-cbc -pbkdf2 -in file.enc -out file
```

## Conversions / hashes
```bash
openssl pkcs12 -export -in cert.pem -inkey key.pem -out bundle.pfx   # PEM -> PFX
openssl x509 -in cert.crt -inform DER -out cert.pem                  # DER -> PEM
openssl dgst -sha256 file
openssl rand -hex 32                                                  # random secret
```

## Sources
- [OpenSSL docs](https://docs.openssl.org/) · [SSL Labs (TLS test)](https://www.ssllabs.com/ssltest/)
