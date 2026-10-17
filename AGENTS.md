# Instructions for anyone editing these docs, human or AI

This is the documentation for **Sumbios O**, published at `docs.sumbios.ai` with Mintlify. Every push to `main` goes live. Read this before changing anything, including through the Mintlify MCP connector.

## What this repo is

- The source of truth for O's documentation. O also has a short in-app Help; this repo wins when the two disagree.
- Pages are MDX with YAML frontmatter. Navigation lives in `docs.json`.
- The pages under `getting-started/`, `insights/`, `network-and-circles/`, `notes-and-knowledge/`, `discovery/`, `missions-and-workspaces/`, `settings/` and `notifications-and-conversations/` were seeded on 17 Oct 2026 from the in-app Help. Since then they are edited here directly.
- `index.mdx` and `reference/` are written by hand.

## Checks (run before every push)

```
python3 scripts/check_voice.py
npx mint broken-links
npx mint dev            # preview at http://localhost:3000
```

The same checks run on every push in `.github/workflows/checks.yml`.

## Voice

- Plain, calm, specific. Second person. One idea per sentence.
- **No em dashes or en dashes.** Use a colon, a comma or a full stop.
- No emoji, no exclamation marks, no hype ("supercharge", "seamless", "unlock", "10x", "AI-powered").
- People are never "leads" or "targets". Quote a UI label in bold if the app uses the word, for example **Find Leads**.
- O prepares you; you decide. Never write that O sends, posts or acts in the user's name.
- UI labels in **bold**, exactly as the app writes them. Paths and commands in `code`.

## Terminology

| Write | Not |
|---|---|
| Sumbios O, or O | Sumbios.O, Symbios |
| the Assistant, Ask O | Companion |
| an executive assistant for your whole network | network companion |
| network relationship memory (NRM), spelled out once per page at most | NRM on its own |
| subscription, plan | membership |
| Circle (capitalised) | circle, group, list |
| Career Movements, Shared Introductions (as the app labels them) | Alumni Movement, My Network Needs |
| Notes (the area), Library (the tab) | Notes and Knowledge |

## Content boundaries

- **Document only what users can do in the app today.** That includes proactive follow-ups: O follows the topics a user chooses and shares updates in O. Describe it that way, never as O acting, sending or posting in the user's name.
- **Plans, prices and credits:** explain what users get and what uses credits. Use only the figures Sumbios has published; never estimate a price, a credit cost or a limit.
- **Integrations:** list only sources that connect today (LinkedIn through the extension, Google Workspace, Microsoft 365, WhatsApp). Do not name integrations that are coming soon.
- **No real people.** Every example name, screenshot and sample uses fictional people and companies from the demo workspace. Never a real contact, never a real account.
- **No roadmap dates, and no security or data-handling claims** beyond what the Trust and privacy pages already say.

## Screenshots

From the demo workspace only, light mode, 1440 x 900 at 2x, cropped to the subject. Record each image's page, capture date and app version.
