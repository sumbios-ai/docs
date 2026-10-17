# Sumbios O documentation

Source of [docs.sumbios.ai](https://docs.sumbios.ai), built with [Mintlify](https://mintlify.com). Every push to `main` deploys.

Read [`AGENTS.md`](AGENTS.md) before editing: it holds the voice rules, the terminology and what may and may not be documented.

## Run it locally

```
npx mint dev
```

Then open http://localhost:3000. Node 20.17 or later.

## Before you push

```
python3 scripts/check_voice.py
npx mint broken-links
```

## Layout

| Path | What |
|---|---|
| `docs.json` | Navigation, theme, brand colours, fonts, logos |
| `style.css` | Brand v3 overrides: solid colours, no shadows, no gradients |
| `index.mdx` | The landing page |
| `getting-started/` … `notifications-and-conversations/` | One folder per area of the app, seeded from the in-app Help on 17 Oct 2026 |
| `reference/` | Ask O commands, integrations |
| `scripts/check_voice.py` | Fails on writing that breaks the voice rules |
