# 🔌 cheat-sheets MCP server

A small [Model Context Protocol](https://modelcontextprotocol.io/) server that exposes this
repo to any MCP-capable client (Claude Desktop, IDE extensions, etc.) as searchable tools and
resources. Ask your assistant "how do I detect kerberoasting" and it pulls the relevant sheet
directly — no manual grep. Read-only, local, no secrets.

## Tools

| Tool | What it does |
|------|--------------|
| `search_cheatsheets(query, section?, platform?, tag?, mitre?, limit?)` | Ranked keyword search with frontmatter filters |
| `get_cheatsheet(path)` | Full markdown of one sheet |
| `get_section(path, heading)` | One section only (e.g. `Detection`, `Mitigation`) |
| `list_sections()` | Sections and their sheet counts |
| `refresh_index()` | Rebuild the index from disk after adding/editing sheets |

## Resources

- `cheatsheet://index` — compact index (path · title · tags)
- `cheatsheet://{path}` — read a specific sheet

## Filters (from YAML frontmatter)

- `section` — top-level folder (`red-team`, `blue-team`, `cloud-security`, …)
- `platform` — `aws`, `windows`, `web`, `linux`, …
- `tag` — any frontmatter tag (`kerberos`, `container`, …)
- `mitre` — an ATT&CK id (`T1558`)

## Setup

```bash
cd mcp
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python server.py          # runs on stdio; Ctrl+C to stop
```

## Add to Claude Desktop

Edit `claude_desktop_config.json` (macOS: `~/Library/Application Support/Claude/`,
Windows: `%APPDATA%\Claude\`) and add:

```json
{
  "mcpServers": {
    "cheat-sheets": {
      "command": "python",
      "args": ["/absolute/path/to/cheat-sheets/mcp/server.py"],
      "env": { "CHEATSHEETS_DIR": "/absolute/path/to/cheat-sheets" }
    }
  }
}
```

Restart Claude Desktop; the `cheat-sheets` tools appear in the tool picker.
(`CHEATSHEETS_DIR` is optional — it defaults to the repo root, i.e. this file's parent's parent.)

## Notes

- The index is built at startup from the `.md` frontmatter. After adding/editing sheets, call
  the `refresh_index()` tool to rebuild it live — no server restart needed.
- Path access is constrained to the repo root and `.md` files only.
