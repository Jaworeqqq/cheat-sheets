---
title: "Blockchain OSINT"
category: "osint"
tags: ["osint", "blockchain", "cryptocurrency", "investigation"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-13"
author: "core"
---

# Blockchain OSINT

## TL;DR
Public blockchains (Bitcoin, Ethereum, etc.) are transparent ledgers: every transaction is visible forever. Blockchain OSINT traces the flow of funds, clusters addresses to entities, and links on-chain activity to real-world identity — used in fraud/ransomware investigations, threat intel, and following illicit finance.

## Fundamentals
```text
- Addresses are pseudonymous, NOT anonymous — all transactions are public and permanent.
- Following the money: inputs/outputs form a graph you can trace.
- Clustering heuristics group addresses likely controlled by one entity (e.g. common-input-ownership).
- Exchanges/services are chokepoints — they often have KYC, so funds reaching them can deanonymize.
```

## What you can do
```text
- Trace funds: from a ransomware/scam address, follow hops to cash-out points.
- Cluster addresses to an entity/wallet; estimate holdings and activity.
- Attribute: link addresses to known services (exchanges, mixers, sanctioned entities) via tags.
- Monitor: watch addresses for new activity (ransomware payments, threat-actor wallets).
```

## Tools & sources
```text
Block explorers  – Etherscan, Blockchain.com, Blockchair (view addresses/txns).
Analytics        – Chainalysis, TRM Labs, Elliptic (commercial; clustering + attribution + risk).
Open-source      – GraphSense, custom graph analysis; OFAC SDN list for sanctioned addresses.
Tagging/intel    – community + commercial address labels (exchanges, scams, mixers).
```

## Obfuscation to be aware of
```text
- Mixers/tumblers (e.g. sanctioned services), CoinJoin — break simple tracing.
- Chain-hopping (swap across chains/DEXes), privacy coins (Monero — largely untraceable), bridges.
- These raise difficulty but analytics + off-ramp KYC often still yield leads.
```

## Use cases (defensive / investigative)
```text
- Ransomware IR: identify the payment address, trace, share intel, inform law enforcement.
- Threat intel: track actor wallets, fund flows between campaigns.
- Fraud/BEC recovery: trace stolen funds to exchanges for freeze requests.
```

## Legality / ethics
- Analyzing public ledger data is generally lawful; handle any linked PII responsibly and involve legal/LE for actioning.

## Sources
- [Etherscan](https://etherscan.io/) · [OFAC SDN](https://sanctionssearch.ofac.treas.gov/) · related: [dark-web-monitoring](./dark-web-monitoring.md)
