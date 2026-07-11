---
title: "OpenSSL – praktyczna ściągawka"
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
Szwajcarski scyzoryk do krypto: klucze, CSR, certy, inspekcja TLS, szyfrowanie plików, hashe.

## Klucze i certyfikaty
```bash
# Klucz prywatny RSA / EC
openssl genrsa -out key.pem 4096
openssl ecparam -genkey -name prime256v1 -out ec.pem

# CSR
openssl req -new -key key.pem -out req.csr -subj "/CN=example.com/O=Org"

# Self-signed (test/lab)
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes \
  -subj "/CN=localhost"

# Podgląd certu / CSR
openssl x509 -in cert.pem -noout -text
openssl req -in req.csr -noout -text
```

## Inspekcja TLS zdalnego serwera
```bash
# Certyfikat + łańcuch + wersje/ciphersuites
openssl s_client -connect example.com:443 -servername example.com </dev/null
# Data ważności
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -dates
# Sprawdź obsługiwane wersje protokołu
openssl s_client -connect example.com:443 -tls1_2 </dev/null
```

## Szyfrowanie plików
```bash
# AES-256 z KDF (pbkdf2) – symetrycznie
openssl enc -aes-256-cbc -pbkdf2 -salt -in plik -out plik.enc
openssl enc -d -aes-256-cbc -pbkdf2 -in plik.enc -out plik
```

## Konwersje / hashe
```bash
openssl pkcs12 -export -in cert.pem -inkey key.pem -out bundle.pfx   # PEM -> PFX
openssl x509 -in cert.crt -inform DER -out cert.pem                  # DER -> PEM
openssl dgst -sha256 plik
openssl rand -hex 32                                                  # losowy sekret
```

## Źródła
- [OpenSSL docs](https://docs.openssl.org/) · [SSL Labs (test TLS)](https://www.ssllabs.com/ssltest/)
