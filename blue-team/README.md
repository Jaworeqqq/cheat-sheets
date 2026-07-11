# 🔵 Blue Team

Detekcja, reagowanie i obrona. Domyślnie mapowane na [MITRE ATT&CK](https://attack.mitre.org/) i [D3FEND](https://d3fend.mitre.org/).

| Podkatalog | Zakres |
|-----------|--------|
| [detection-engineering](./detection-engineering/) | Reguły Sigma, YARA, detekcja jako kod |
| [incident-response](./incident-response/) | Playbooki, triage, containment, eradication (NIST 800-61) |
| [threat-hunting](./threat-hunting/) | Hipotezy, hunting queries, TTP hunting |
| [digital-forensics](./digital-forensics/) | DFIR, memory/disk forensics, timeline |
| [siem](./siem/) | Splunk (SPL), Elastic (KQL/EQL), Sentinel (KQL) |
| [logging-monitoring](./logging-monitoring/) | Windows Event IDs, Sysmon, auditd, telemetria |
| [malware-analysis](./malware-analysis/) | Analiza statyczna/dynamiczna, sandbox, unpacking |
| [hardening](./hardening/) | CIS Benchmarks, baseline OS/usług |

## Priorytet do uzupełnienia
- [x] `logging-monitoring/windows-event-ids.md`
- [x] `detection-engineering/` – sigma-rules, yara-rules
- [x] `incident-response/` – ir-process, ir-playbook-ransomware
- [x] `threat-hunting/threat-hunting.md`
- [x] `siem/` – splunk-spl, kql-sentinel
- [x] `digital-forensics/dfir-triage.md`, `malware-analysis/static-dynamic-analysis.md`, `hardening/cis-linux.md`
- [ ] Do zrobienia: `hardening/cis-windows`, `logging-monitoring/sysmon-config`, więcej playbooków IR (BEC, phishing)
