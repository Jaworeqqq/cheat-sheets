---
title: "Wireshark display filters"
category: "networking"
tags: ["networking", "wireshark", "traffic-analysis"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Wireshark display filters

## TL;DR
Wireshark uses **display filters** (different syntax from tcpdump's BPF capture filters). Filter after capture to find the packets that matter. Key operators: `==`, `!=`, `contains`, `matches`, `&&`, `||`.

## Capture vs display filters
```text
Capture filter (BPF, before capture):   host 10.0.0.5 and port 443
Display filter (Wireshark, after):      ip.addr == 10.0.0.5 && tcp.port == 443
```

## Common display filters
```text
ip.addr == 10.0.0.5                 # to or from host
ip.src == 10.0.0.5 && ip.dst == 8.8.8.8
tcp.port == 443 || udp.port == 53
http                                 # only HTTP
http.request.method == "POST"
dns.qry.name contains "example"
tls.handshake.type == 1              # ClientHello (SNI, JA3)
tcp.flags.syn == 1 && tcp.flags.ack == 0   # SYN (scans)
tcp.analysis.retransmission          # network issues
frame contains "password"            # search payload bytes
```

## Analysis workflows
```text
- Follow Stream (right-click -> Follow -> TCP/HTTP/TLS) to reassemble a conversation.
- Statistics > Conversations / Endpoints — who talks to whom, volumes.
- Statistics > Protocol Hierarchy — what protocols are present.
- File > Export Objects > HTTP — pull transferred files.
- tls.handshake.extensions_server_name — SNI (destinations inside TLS).
```

## Security-relevant hunts
```text
- Cleartext creds: http.authbasic, ftp, telnet, http.request contains "pass"
- DNS tunneling: long/high-entropy dns.qry.name, many TXT
- Beaconing: filter to a suspected C2 IP, look at regular intervals (Time column)
- Exfil: large outbound in Conversations to unusual dst
```

## Sources
- [Wireshark Display Filter Reference](https://www.wireshark.org/docs/dfref/) · [Wireshark User Guide](https://www.wireshark.org/docs/wsug_html_chunked/)
