---
title: "tcpdump – packet capture"
category: "networking"
tags: ["networking", "tcpdump", "traffic-analysis"]
platform: "agnostic"
mitre: []
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# tcpdump

## TL;DR
Command-line packet capture using BPF filters. The go-to for quick capture on servers (no GUI). Capture to a pcap, analyze deeply in Wireshark.

## Basics
```bash
tcpdump -i eth0                      # capture on an interface
tcpdump -i any -n                    # all interfaces, no name resolution
tcpdump -i eth0 -c 100               # stop after 100 packets
tcpdump -i eth0 -w capture.pcap      # write to file (for Wireshark)
tcpdump -r capture.pcap              # read from file
tcpdump -i eth0 -nnvvS               # verbose, no resolution, absolute seq
```

## Filters (BPF)
```bash
# Host / net / port
tcpdump -i eth0 host 10.0.0.5
tcpdump -i eth0 net 10.0.0.0/24
tcpdump -i eth0 port 443
tcpdump -i eth0 src 10.0.0.5 and dst port 80
# Protocols
tcpdump -i eth0 tcp
tcpdump -i eth0 'udp port 53'                 # DNS
tcpdump -i eth0 icmp
# Logical operators
tcpdump -i eth0 'host 10.0.0.5 and (port 80 or port 443)'
tcpdump -i eth0 'tcp[tcpflags] & tcp-syn != 0'   # SYN packets
```

## Useful output options
```bash
tcpdump -i eth0 -A port 80           # print payload as ASCII (cleartext HTTP)
tcpdump -i eth0 -X                    # hex + ASCII
tcpdump -i eth0 -s 0                  # full packet (snaplen 0 = unlimited)
tcpdump -i eth0 -w cap-%H%M.pcap -G 300 -W 10   # rotate every 5 min, keep 10
```

## Common uses
```text
- Confirm connectivity / see who a host is talking to.
- Capture cleartext creds on legacy protocols (HTTP/FTP/telnet) — auth testing.
- Grab a pcap on a server, open in Wireshark for deep analysis.
- Detect scanning (SYN floods), DNS tunneling (many/large TXT).
```

## Sources
- [tcpdump manual](https://www.tcpdump.org/manpages/tcpdump.1.html) · [pcap-filter (BPF)](https://www.tcpdump.org/manpages/pcap-filter.7.html)
