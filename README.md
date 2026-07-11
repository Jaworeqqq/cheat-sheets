# 🛡️ cheat-sheets

A well-organized, practical collection of cybersecurity cheat sheets — Red Team, Blue Team, DevSecOps, Cloud Security, AppSec and Compliance. One place, one consistent format, fast lookup.

> ⚠️ **For educational purposes and authorized testing only.** Use offensive (Red Team) material exclusively within legal engagements, CTF labs and research for which you have written authorization. See [Disclaimer](#-disclaimer).

---

## 📚 Table of Contents

| Section | Scope |
|---------|-------|
| [🔴 red-team](./red-team/) | Recon, exploitation, privilege escalation, AD, C2, exfiltration |
| [🔵 blue-team](./blue-team/) | Detection, IR, threat hunting, forensics, SIEM, malware analysis |
| [⚙️ devsecops](./devsecops/) | CI/CD, containers, Kubernetes, IaC, secrets, SAST/DAST/SCA, supply chain |
| [☁️ cloud-security](./cloud-security/) | AWS, Azure, GCP, multi-cloud |
| [🧩 appsec](./appsec/) | OWASP Top 10, API security, secure coding, threat modeling |
| [📋 compliance](./compliance/) | ISO 27001, SOC 2, NIST, PCI-DSS, GDPR, audit, risk management |
| [🕵️ osint](./osint/) | Open-source intelligence |
| [🌐 networking](./networking/) | Protocols, traffic analysis, pivoting |
| [🔐 cryptography](./cryptography/) | Ciphers, hashes, PKI, password cracking |
| [🔗 references](./references/) | Links, books, courses, standards |

---

## 📈 Coverage status

The repo has foundational cheat sheets filled in for every section (70+ documents) plus a skeleton for the rest. Each section `README.md` has a "priority backlog" list (checked = done).

| Section | Filled cheat sheets (examples) |
|---------|--------------------------------|
| red-team | nmap, subdomain-enum, phishing, reverse-shells, linux/windows privesc, kerberoasting, asreproast, bloodhound, adcs-esc, pass-the-hash, C2, SQLi, XSS, SSRF, wifi, burp, netexec |
| blue-team | windows-event-ids, sigma, yara, IR (process + ransomware), threat-hunting, splunk-spl, kql, dfir-triage, malware-analysis, cis-linux |
| devsecops | actions-hardening, docker, k8s-security, iac-scanning, secrets-detection, sast-dast-sca, sbom-cosign |
| cloud-security | aws iam/s3, entra-enumeration, gcp-iam |
| appsec | owasp-top10, broken-access-control, jwt, stride, input-validation |
| compliance | frameworks-overview, iso27001, nist-csf, pci-dss, gdpr, evidence-checklist, risk-assessment |
| osint / networking / cryptography | google-dorking, recon-frameworks, common-ports, ssh-tunneling, password-cracking, openssl |

## 🗂️ How to use

Each section has its own `README.md` (index of subtopics). Each cheat sheet is a single `.md` file in a consistent format — see [`_templates/cheatsheet-template.md`](./_templates/cheatsheet-template.md).

**Quick search across the repo:**

```bash
# Find a cheat sheet by keyword
grep -rin "kerberoast" --include="*.md" .

# List all cheat sheets in a section
find red-team -name "*.md" -not -name "README.md"
```

## 🧭 Conventions

- **Language:** English (commands always in English).
- **File names:** `kebab-case.md`, descriptive (e.g. `linux-privesc-suid.md`).
- **Format:** metadata header + `TL;DR`, `Commands`, `Detection`, `Mitigation`, `Sources` sections.
- **Code blocks:** always with an explicit language (```bash, ```powershell, ```yaml).
- Every offensive technique **should** carry a *Detection* and *Mitigation* section (Red→Blue bridge).

## 🤝 Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md). In short: copy the template, fill it in, open a PR. Markdown lint runs automatically in CI.

## ⚖️ Disclaimer

This repository is for learning, defense and authorized security testing. The authors take no responsibility for misuse. Do not use this material against systems you are not explicitly authorized to test.

## 📄 License

[MIT](./LICENSE) — cheat-sheet content under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
