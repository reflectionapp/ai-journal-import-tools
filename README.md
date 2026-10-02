# Migrate Your Journal to Reflection AI Journal + Coach (BETA)

Migrate your journal to [Reflection](https://www.reflection.app), AI journal + coach, with tools that convert Day One and other exports into the Reflection CSV format so you can import easily.

## What This Repo Is (and Isn't)

**What it is:** conversion tools and guides that help you turn journal exports into the Reflection CSV format.

**What it isn't:** the Reflection product itself. Reflection is the destination - an AI-powered journal app. This repo is just the migration tooling to get your history in.

**Beta Note:** Every journal and every export file is different, for that purpose we're considering these docs still in beta. If you have suggestions on how to improve or if you notice anything from a specific export file you're using, please let us know. 

## Quick Start

**Recommended: let your AI assistant write the entries.** With Reflection Premium, create a key under
**Settings → Advanced → MCP Keys** and connect Reflection to ChatGPT, Claude or any assistant that supports MCP.
Give it your export and ask it to create the entries. Nothing to convert or upload, and you can check a few entries
before it does the rest. (Entries it creates are tagged `MCP`. It doesn't check for duplicates, so ask it to do one
batch at a time.)

**Or build a CSV (Export → Convert → Import):**

1. Export your journal from Day One (or another app).
2. Convert the export into the Reflection CSV format.
3. Import the CSV in Reflection under **Settings → Advanced → Import & Export**. The app shows what was added,
   replaced and skipped, so you can leave the screen while it runs.

Reflection doesn't read Day One files directly, and photos can't be imported yet.

Most people start with:
- `./docs/day-one-to-reflection.md`

## Migration Guides

- `./docs/day-one-to-reflection.md` - Day One migration
- `./docs/ai-journal-migration-guide.md` - Migration from any app
- `./docs/chatgpt-journal-converter.md` - Use ChatGPT for conversion
- `./docs/journal-csv-format.md` - Reflection CSV schema

## AI Prompt Workflows (ChatGPT, Claude)

You can convert exports using prompts:
- `./chatgpt/prompts/chatgpt-journal-converter.md`
- `./claude/prompts/claude-day-one-migration.md`
- `./dayone/prompts/` (Day One specific)

Prompts work best in small batches so you can validate output before importing.

## Python Converter for Day One

Prefer to keep data local? Use the Python converter in:
- `./dayone/scripts/`

See:
- `./dayone/README.md`

## Reflection CSV Format (Schema)

Reflection imports CSV. To map or validate your data:
- `./docs/journal-csv-format.md`

## Supported Sources

- Day One (via the converter or prompts in `dayone/`; text, dates and tags)
- Any app that exports CSV or JSON (via prompts or manual mapping)

If you want to add another adapter, see:
- `./CONTRIBUTING.md`

## Privacy & Data Handling

Privacy note: AI prompts may send your journal content to third-party AI services. Review those providers' data policies and remove sensitive entries before use. To keep data local, use the Python converter instead.

## About Reflection, the AI Journal

Reflection is an AI-powered journal that offers real-time guidance as you write. It is privacy-focused and provides encryption to help protect your entries. Reflection is available on iOS, Android, MacOS, and the web.

## Contributing

Please read:
- `./CONTRIBUTING.md`

## License & Security

- License: `./LICENSE`
- Security policy: `./SECURITY.md`
