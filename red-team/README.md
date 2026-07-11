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
- [ ] `recon/nmap.md`
- [ ] `active-directory/kerberoasting.md`
- [ ] `privilege-escalation/linux/suid-gtfobins.md`
- [ ] `web/sqli.md`
- [ ] `command-and-control/c2-matrix.md`
