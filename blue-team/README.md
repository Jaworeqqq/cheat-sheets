# 🔵 Blue Team

Detection, response and defense. Mapped by default to [MITRE ATT&CK](https://attack.mitre.org/) and [D3FEND](https://d3fend.mitre.org/).

| Subdirectory | Scope |
|--------------|-------|
| [detection-engineering](./detection-engineering/) | Sigma rules, YARA, detection-as-code |
| [incident-response](./incident-response/) | Playbooks, triage, containment, eradication (NIST 800-61) |
| [threat-hunting](./threat-hunting/) | Hypotheses, hunting queries, TTP hunting |
| [digital-forensics](./digital-forensics/) | DFIR, memory/disk forensics, timeline |
| [siem](./siem/) | Splunk (SPL), Elastic (KQL/EQL), Sentinel (KQL) |
| [logging-monitoring](./logging-monitoring/) | Windows Event IDs, Sysmon, auditd, telemetry |
| [malware-analysis](./malware-analysis/) | Static/dynamic analysis, sandbox, unpacking |
| [hardening](./hardening/) | CIS Benchmarks, OS/service baselines |

## Priority backlog
- [x] `logging-monitoring/windows-event-ids.md`
- [x] `detection-engineering/` – sigma-rules, yara-rules
- [x] `incident-response/` – ir-process, ir-playbook-ransomware
- [x] `threat-hunting/threat-hunting.md`
- [x] `siem/` – splunk-spl, kql-sentinel
- [x] `digital-forensics/dfir-triage.md`, `malware-analysis/static-dynamic-analysis.md`, `hardening/cis-linux.md`
- [x] `hardening/cis-windows.md`, `logging-monitoring/sysmon-config.md`
- [x] `incident-response/` – ir-playbook-phishing, ir-playbook-bec
- [x] `detection-engineering/detection-as-code.md`, `threat-hunting/lateral-movement-hunt.md`, `siem/elastic-eql.md`
- [x] `malware-analysis/memory-forensics.md`, `hardening/macos.md`, `digital-forensics/linux-forensics.md`
- [ ] Todo: `logging-monitoring/linux-auditd`, `threat-hunting/dns-anomaly-hunt`, `incident-response/cloud-ir-aws`
