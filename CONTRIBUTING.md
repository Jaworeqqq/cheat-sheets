# Współtworzenie

Dzięki za wkład! To repo utrzymuje spójny format, żeby ściągawki były szybkie do przeszukania.

## Zasady

1. **Jedna ściągawka = jeden plik `.md`** w odpowiednim dziale.
2. Zaczynaj od [`_templates/cheatsheet-template.md`](./_templates/cheatsheet-template.md) — zachowaj frontmatter YAML.
3. **Nazwy plików:** `kebab-case`, opisowe (`windows-uac-bypass.md`, nie `notes2.md`).
4. Bloki kodu **zawsze** z językiem: ` ```bash `, ` ```powershell `, ` ```yaml `.
5. Techniki ofensywne dołączaj z sekcjami **Wykrywanie** i **Mitygacja**.
6. Żadnych realnych sekretów, kluczy, danych klientów, IP z prawdziwych zaangażowań.
7. Podawaj **źródła** — linkuj oryginalne badania/dokumentację.

## Workflow

```bash
git checkout -b add/<krotki-opis>
cp _templates/cheatsheet-template.md red-team/recon/moja-sciagawka.md
# ...edytuj...
git add . && git commit -m "add: recon cheatsheet – <temat>"
git push origin add/<krotki-opis>
# otwórz Pull Request
```

## Styl commitów

`typ: krótki opis` — gdzie typ to `add`, `update`, `fix`, `docs`, `refactor`.

## Lint

CI uruchamia `markdownlint`. Sprawdź lokalnie:

```bash
npx markdownlint-cli2 "**/*.md"
```
