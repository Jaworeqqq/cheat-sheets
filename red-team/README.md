# 🔴 Red Team

Techniki ofensywne uporządkowane wg [Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html) / [MITRE ATT&CK](https://attack.mitre.org/).

> ⚠️ Wyłącznie do autoryzowanych testów penetracyjnych, laboratoriów i CTF.

| Podkatalog | Zakres | MITRE (taktyka) |
|-----------|--------|-----------------|
| [recon](./recon/) | Rozpoznanie pasywne/aktywne, skanowanie | Reconnaissance / Discovery |
| [initial-access](./initial-access/) | Phishing, podatne usługi, wejście | Initial Access |
| [exploitation](./exploitation/) | Exploity, RCE, deserializacja | Execution |
| [privilege-escalation](./privilege-escalation/) | [Linux](./privilege-escalation/linux/) · [Windows](./privilege-escalation/windows/) | Privilege Escalation |
| [persistence](./persistence/) | Utrzymanie dostępu | Persistence |
| [lateral-movement](./lateral-movement/) | Pass-the-Hash, RDP, WinRM, pivoting | Lateral Movement |
| [active-directory](./active-directory/) | Kerberoasting, BloodHound, ACL, ADCS | Credential Access / PrivEsc |
| [command-and-control](./command-and-control/) | C2, tunelowanie, beaconing | Command and Control |
| [exfiltration](./exfiltration/) | Wyprowadzanie danych, kanały ukryte | Exfiltration |
| [web](./web/) | SQLi, XSS, SSRF, SSTI, IDOR | — |
| [wireless](./wireless/) | Wi-Fi, BLE, RFID | — |
| [mobile](./mobile/) | Android/iOS | — |
| [tools](./tools/) | Ściągawki narzędzi (nmap, Burp, CrackMapExec...) | — |

## Priorytet do uzupełnienia
- [x] `recon/nmap.md`, `recon/subdomain-enum.md`, `recon/dns-recon.md`
- [x] `active-directory/` – kerberoasting, asreproast, bloodhound, adcs-esc
- [x] `privilege-escalation/` – linux (linux-privesc, suid-gtfobins), windows (windows-privesc, token-impersonation)
- [x] `web/` – sqli, xss, ssrf, file-upload
- [x] `command-and-control/c2-matrix.md`, `exfiltration/exfil-channels.md`
- [ ] Do zrobienia: `recon/nmap` → NSE deep-dive, `wireless/ble`, `mobile/ios`, więcej `tools/` (impacket, mimikatz)
