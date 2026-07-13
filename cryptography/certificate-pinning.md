---
title: "Certificate pinning"
category: "cryptography"
tags: ["cryptography", "tls", "pinning", "mobile"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# Certificate pinning

## TL;DR
Certificate pinning hardcodes which certificate/public key a client will accept for a server, so a valid-but-attacker-controlled cert (from a compromised or rogue CA) is rejected. It defeats TLS interception/MITM but complicates rotation — pin the public key, not the leaf cert, and always ship a backup pin.

## The problem it addresses
```text
Normal TLS trusts ANY cert signed by a trusted CA. Threats:
 - A rogue/compromised CA issues a valid cert for your domain -> MITM the client.
 - Corporate/interception proxies or malware install a trusted root -> transparent MITM.
Pinning says "only THIS key/cert is acceptable for this server" regardless of CA trust.
```

## What to pin (and why key-pinning wins)
```text
Leaf cert    – breaks every renewal (cert changes) -> operationally painful.
Public key (SPKI)  – survives cert renewal if the KEY is reused -> RECOMMENDED. Pin the SPKI hash.
Intermediate/CA    – pin an issuing CA (less strict; balance security vs flexibility).
Always include a BACKUP pin (a second key) so you can rotate without bricking clients.
```

## Where it's used
```text
- Mobile apps (most common): pin the API's public key so a user-installed proxy can't MITM.
- Some desktop/embedded clients, high-security integrations.
- Web HPKP (HTTP Public Key Pinning) is DEPRECATED (footgun: could brick a site) — don't use it;
  use Certificate Transparency monitoring + Expect-CT instead for web.
```

## Implementation notes
```text
- Mobile: platform config (Android Network Security Config, iOS pinning libs / TrustKit).
- Ship >=2 pins (current + backup key); plan rotation before certs expire.
- Fail closed (reject on mismatch) — that's the point.
- Test rollout carefully: a bad pin + no backup = app can't connect until an update ships.
```

## Trade-offs
```text
+ Strong MITM/rogue-CA protection.
- Operational risk: mispinning or forgetting to rotate can cause outages.
- Attackers with app-tamper capability can bypass pinning (see red-team mobile sheets) — it's
  defense-in-depth against network MITM, not device compromise.
```

## Sources
- [OWASP – Certificate Pinning](https://cheatsheetseries.owasp.org/cheatsheets/Pinning_Cheat_Sheet.html) · related: [pki-x509](./pki-x509.md), [tls-config](./tls-config.md), [android-basics](../red-team/mobile/android-basics.md)
