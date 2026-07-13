---
title: "Wi-Fi wardriving & wireless OSINT"
category: "osint"
tags: ["osint", "wifi", "wardriving", "geolocation"]
platform: "agnostic"
mitre: ["T1595"]
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# Wi-Fi wardriving & wireless OSINT

## TL;DR
Wardriving maps wireless networks by their broadcasts (SSID, BSSID/MAC, encryption, signal) while moving through an area. Combined with public BSSID databases, it enables geolocation of devices/APs and reconnaissance of a target's wireless footprint. Passive collection only; attacking networks needs authorization (see [red-team/wireless/wifi-attacks](../red-team/wireless/wifi-attacks.md)).

## What you collect (passively)
```text
- SSID (network name — may reveal org/vendor/purpose), hidden SSIDs.
- BSSID (AP MAC — vendor via OUI; unique locator).
- Encryption type (open / WEP / WPA2 / WPA3), channel, signal strength.
- GPS coordinates (for mapping) — build a heatmap of a target's APs.
```

## Tools
```text
Kismet          – wireless detector/sniffer, logs networks + clients (Linux).
WiGLE (app + DB) – collect and query the world's largest public BSSID/SSID database.
airodump-ng     – quick survey of nearby networks/clients.
Flipper/phone apps – convenient discovery.
```

## Geolocation via BSSID
```text
- Public databases (WiGLE, and the geolocation services phones use) map BSSID -> physical location.
- Given a BSSID from a photo/log/config, you can often locate where that AP is.
- Conversely, a device's known AP MACs can reveal home/work locations (privacy risk).
```

## Recon uses (authorized)
```text
- Map a target facility's wireless footprint (APs, guest vs corp SSIDs, encryption weaknesses).
- Identify rogue/guest networks, IoT SSIDs, vendor gear (OUI) before a physical/wireless engagement.
- Correlate SSIDs with the org (naming conventions leak structure).
```

## Detection / defense (Blue Team)
- WIDS/WIPS to spot survey/rogue activity; monitor for evil-twin SSIDs.
- Don't broadcast identifying SSIDs; randomize where possible; WPA3 + 802.1X.
- Educate: BSSIDs in photos/configs are locators; strip them.

## Mitigation / Hardening
- Strong wireless (WPA3/802.1X — see wifi-attacks), guest isolation, minimal info in SSIDs.
- Consider opting APs out of geolocation databases (SSID `_nomap` suffix where supported).

## Sources
- [Kismet](https://www.kismetwireless.net/) · [WiGLE](https://wigle.net/) · related: [geolocation](./geolocation.md), [wifi-attacks](../red-team/wireless/wifi-attacks.md)
