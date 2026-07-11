---
title: "Bluetooth / BLE attacks"
category: "red-team"
tags: ["wireless", "bluetooth", "ble", "iot"]
platform: "agnostic"
mitre: ["T1011"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Bluetooth / BLE

## TL;DR
BLE (Bluetooth Low Energy) is common in IoT/wearables and often weakly secured: no pairing, sniffable traffic, spoofable characteristics. Test only your own/authorized devices.

## Recon / scanning
```bash
# Classic + BLE scan
hcitool lescan
bluetoothctl                     # scan on; devices; info <MAC>
# Rich BLE enumeration (services/characteristics)
sudo bettercap -eval "ble.recon on"
gatttool -b AA:BB:CC:DD:EE:FF --primary   # enumerate GATT services
gatttool -b AA:BB:CC:DD:EE:FF --characteristics
```

## Interaction
```bash
# Read/write characteristics (find handles first)
gatttool -b <MAC> --char-read -a 0x0025
gatttool -b <MAC> --char-write-req -a 0x0025 -n 01
# nRF Connect (mobile) – GUI for GATT exploration/replay
```

## Sniffing / attacks
```text
- Passive sniffing – nRF52840 / Ubertooth + Wireshark (BLE plugin)
- Replay – capture and resend characteristic writes (no auth on many devices)
- MITM – GATTacker / btlejack (hijack established connections)
- Spoofing – clone advertising data / MAC of a peripheral
```

## Detection (Blue Team / defensive)
- Unexpected pairing requests, connection hijack signs, cloned advertisements.

## Mitigation / Hardening
- BLE Secure Connections (LE SC) pairing with MITM protection; avoid "Just Works" for sensitive data.
- Application-layer encryption + authentication on characteristics (don't trust the link layer).
- Bonding, rotate/resolve private addresses (RPA), minimize exposed GATT services.

## Sources
- [btlejack](https://github.com/virtualabs/btlejack) · [OWASP IoT](https://owasp.org/www-project-internet-of-things/)
