# Contributing

Thanks for contributing! This repo keeps a consistent format so cheat sheets stay fast to search.

## Rules

1. **One cheat sheet = one `.md` file** in the appropriate section.
2. Start from [`_templates/cheatsheet-template.md`](./_templates/cheatsheet-template.md) — keep the YAML frontmatter.
3. **File names:** `kebab-case`, descriptive (`windows-uac-bypass.md`, not `notes2.md`).
4. Code blocks **always** with a language: ` ```bash `, ` ```powershell `, ` ```yaml `.
5. Include **Detection** and **Mitigation** sections for offensive techniques.
6. No real secrets, keys, client data, or IPs from actual engagements.
7. Cite **sources** — link the original research/documentation.

## Workflow

```bash
git checkout -b add/<short-description>
cp _templates/cheatsheet-template.md red-team/recon/my-cheatsheet.md
# ...edit...
git add . && git commit -m "add: recon cheatsheet – <topic>"
git push origin add/<short-description>
# open a Pull Request
```

## Commit style

`type: short description` — where type is `add`, `update`, `fix`, `docs`, `refactor`.

## Lint

CI runs `markdownlint`. Check locally:

```bash
npx markdownlint-cli2 "**/*.md"
```
