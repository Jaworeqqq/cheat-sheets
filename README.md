# 🛡️ cheat-sheets

Uporządkowana, praktyczna kolekcja ściągawek z zakresu cyberbezpieczeństwa — Red Team, Blue Team, DevSecOps, Cloud Security, AppSec i Compliance. Jedno miejsce, spójny format, szybkie wyszukiwanie.

> ⚠️ **Tylko do celów edukacyjnych i autoryzowanych testów.** Materiały ofensywne (Red Team) używaj wyłącznie w ramach legalnych zaangażowań, laboratoriów CTF i badań, na które masz pisemną zgodę. Zobacz [DISCLAIMER](#-disclaimer).

---

## 📚 Spis treści

| Dział | Zakres |
|-------|--------|
| [🔴 red-team](./red-team/) | Rekonesans, exploitacja, eskalacja uprawnień, AD, C2, exfiltracja |
| [🔵 blue-team](./blue-team/) | Detekcja, IR, threat hunting, forensics, SIEM, malware analysis |
| [⚙️ devsecops](./devsecops/) | CI/CD, kontenery, Kubernetes, IaC, sekrety, SAST/DAST/SCA, supply chain |
| [☁️ cloud-security](./cloud-security/) | AWS, Azure, GCP, multi-cloud |
| [🧩 appsec](./appsec/) | OWASP Top 10, API security, secure coding, threat modeling |
| [📋 compliance](./compliance/) | ISO 27001, SOC 2, NIST, PCI-DSS, GDPR, audyt, zarządzanie ryzykiem |
| [🕵️ osint](./osint/) | Rozpoznanie z otwartych źródeł |
| [🌐 networking](./networking/) | Protokoły, analiza ruchu, pivoting |
| [🔐 cryptography](./cryptography/) | Szyfry, hashe, PKI, łamanie haseł |
| [🔗 references](./references/) | Linki, książki, kursy, standardy |

---

## 🗂️ Jak korzystać

Każdy dział ma własny `README.md` (spis podtematów). Każda ściągawka to jeden plik `.md` w spójnym formacie — patrz [`_templates/cheatsheet-template.md`](./_templates/cheatsheet-template.md).

**Szybkie wyszukiwanie w repo:**

```bash
# Znajdź ściągawkę po słowie kluczowym
grep -rin "kerberoast" --include="*.md" .

# Wypisz wszystkie ściągawki w dziale
find red-team -name "*.md" -not -name "README.md"
```

## 🧭 Konwencje

- **Język:** treść PL/EN (dopuszczalne mieszanie — komendy zawsze EN).
- **Nazwy plików:** `kebab-case.md`, opisowe (np. `linux-privesc-suid.md`).
- **Format:** nagłówek z metadanymi + sekcje `TL;DR`, `Komendy`, `Wykrywanie`, `Mitygacja`, `Źródła`.
- **Bloki kodu:** zawsze z określonym językiem (```bash, ```powershell, ```yaml).
- Każda technika ofensywna **powinna** mieć sekcję *Wykrywanie* i *Mitygacja* (mostek Red→Blue).

## 🤝 Współtworzenie

Zobacz [CONTRIBUTING.md](./CONTRIBUTING.md). W skrócie: skopiuj szablon, wypełnij, otwórz PR. Lint Markdown uruchamia się automatycznie w CI.

## ⚖️ Disclaimer

Repozytorium służy nauce, obronie i autoryzowanym testom bezpieczeństwa. Autorzy nie ponoszą odpowiedzialności za nadużycia. Nie używaj tych materiałów na systemach, do których nie masz jawnej autoryzacji.

## 📄 Licencja

[MIT](./LICENSE) — treść cheatsheetów na [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
