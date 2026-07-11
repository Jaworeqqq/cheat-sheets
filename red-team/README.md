# 🔴 Red Team

Offensive techniques organized by the [Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html) / [MITRE ATT&CK](https://attack.mitre.org/).

> ⚠️ For authorized penetration tests, labs and CTFs only.

| Subdirectory | Scope | MITRE (tactic) |
|--------------|-------|----------------|
| [recon](./recon/) | Passive/active reconnaissance, scanning | Reconnaissance / Discovery |
| [initial-access](./initial-access/) | Phishing, vulnerable services, entry | Initial Access |
| [exploitation](./exploitation/) | Exploits, RCE, deserialization | Execution |
| [privilege-escalation](./privilege-escalation/) | [Linux](./privilege-escalation/linux/) · [Windows](./privilege-escalation/windows/) | Privilege Escalation |
| [persistence](./persistence/) | Maintaining access | Persistence |
| [lateral-movement](./lateral-movement/) | Pass-the-Hash, RDP, WinRM, pivoting | Lateral Movement |
| [active-directory](./active-directory/) | Kerberoasting, BloodHound, ACL, ADCS | Credential Access / PrivEsc |
| [command-and-control](./command-and-control/) | C2, tunneling, beaconing | Command and Control |
| [exfiltration](./exfiltration/) | Data exfiltration, covert channels | Exfiltration |
| [web](./web/) | SQLi, XSS, SSRF, SSTI, IDOR | — |
| [wireless](./wireless/) | Wi-Fi, BLE, RFID | — |
| [mobile](./mobile/) | Android/iOS | — |
| [tools](./tools/) | Tool cheat sheets (nmap, Burp, CrackMapExec...) | — |

## Priority backlog
- [x] `recon/nmap.md`, `recon/subdomain-enum.md`, `recon/dns-recon.md`
- [x] `active-directory/` – kerberoasting, asreproast, bloodhound, adcs-esc
- [x] `privilege-escalation/` – linux (linux-privesc, suid-gtfobins), windows (windows-privesc, token-impersonation)
- [x] `web/` – sqli, xss, ssrf, file-upload
- [x] `command-and-control/c2-matrix.md`, `exfiltration/exfil-channels.md`
- [x] `recon/nmap-nse.md`, `wireless/bluetooth-ble.md`, `mobile/ios-basics.md`, `tools/` (impacket, mimikatz)
- [x] `active-directory/dcsync.md`, `active-directory/delegation.md`, `web/ssti.md`, `recon/smb-enum.md`
- [x] `web/xxe.md`, `web/command-injection.md`, `initial-access/exposed-services.md`, `persistence/golden-ticket.md`
- [ ] Todo: `web/idor`, `active-directory/ntlm-relay`, `exploitation/deserialization-attacks`
