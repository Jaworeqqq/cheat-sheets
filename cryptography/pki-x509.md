---
title: "PKI & X.509 certificates"
category: "cryptography"
tags: ["cryptography", "pki", "x509", "tls"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# PKI & X.509

## TL;DR
Public Key Infrastructure binds identities to public keys via certificates signed by a chain of trust (Root CA → Intermediate → Leaf). X.509 is the certificate format. Trust = valid chain + not expired + not revoked + name matches.

## Chain of trust
```text
Root CA (self-signed, in trust store)
  └─ Intermediate CA (signed by Root)
       └─ Leaf/end-entity cert (signed by Intermediate; your server)
Validation: signature up the chain + validity dates + revocation + hostname (SAN).
```

## Key concepts
```text
CSR   – Certificate Signing Request (public key + identity -> sent to CA)
SAN   – Subject Alternative Name (the hostnames a cert is valid for; CN is legacy)
EKU   – Extended Key Usage (serverAuth, clientAuth, codeSigning)
Revocation – CRL (list) or OCSP (online status); OCSP stapling for performance
Trust store – OS/browser set of trusted Root CAs
```

## Inspecting certs (OpenSSL)
```bash
openssl x509 -in cert.pem -noout -text          # full details
openssl x509 -in cert.pem -noout -dates          # validity
openssl x509 -in cert.pem -noout -ext subjectAltName
# Verify a chain
openssl verify -CAfile chain.pem cert.pem
# Live server chain
openssl s_client -connect example.com:443 -showcerts </dev/null
```

## Security considerations
```text
- Certificate Transparency (CT) logs — monitor for certs issued for your domains
  (detects mis-issuance / attacker infra / new subdomains).
- Certificate pinning — app trusts specific cert/key (blunts MITM, complicates rotation).
- Private key protection — HSM/KMS; compromise = impersonation until revoked.
- Weak/expired certs, missing SAN, self-signed in prod = misconfig (A02).
```

## Detection / defense (Blue Team)
- Monitor CT logs (crt.sh, Cert Spotter) for unexpected issuance.
- Alert on expiring certs; enforce strong keys/algorithms and short lifetimes.

## Sources
- [RFC 5280 (X.509)](https://datatracker.ietf.org/doc/html/rfc5280) · [Certificate Transparency](https://certificate.transparency.dev/) · [Let's Encrypt docs](https://letsencrypt.org/docs/)
