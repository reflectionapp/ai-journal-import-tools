# Migrate Your Journal to Reflection, the AI Journal

Migrate your journal to Reflection, the AI journal, with tools that convert Day One and other exports into the Reflection CSV format so you can import easily.

## What This Repo Is (and Isn't)

**What it is:** conversion tools and guides that help you turn journal exports into the Reflection CSV format.

**What it isn't:** the Reflection product itself. Reflection is the destination - an AI-powered journal app. This repo is just the migration tooling to get your history in.

## Quick Start (Export → Convert → Import)

1. Export your journal from Day One (or another app).
2. Convert the export into the Reflection CSV format.
3. Import the CSV into Reflection.

Most people start with:
- `./docs/day-one-to-reflection.md`

## Migration Guides

- `./docs/day-one-to-reflection.md` - Day One migration
- `./docs/ai-journal-migration-guide.md` - Migration from any app
- `./docs/chatgpt-journal-converter.md` - Use ChatGPT for conversion
- `./docs/journal-csv-format.md` - Reflection CSV schema

## AI Prompt Workflows (ChatGPT, Claude)

You can convert exports using prompts:
- `./prompts/chatgpt-journal-converter.md`
- `./prompts/claude-day-one-migration.md`

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

- Day One (fully supported)
- Any app that exports CSV or JSON (via prompts or manual mapping)

If you want to add another adapter, see:
- `./CONTRIBUTING.md`

## Privacy & Data Handling

Privacy note: AI prompts may send your journal content to third-party AI services. Review those providers' data policies and remove sensitive entries before use. To keep data local, use the Python converter instead.

## About Reflection, the AI Journal

Reflection is an AI-powered journal that offers real-time guidance as you write. It is privacy-focused and provides encryption to help protect your entries. Reflection is available on iOS, Android, Mac, and the web.

## Contributing

Please read:
- `./CONTRIBUTING.md`

## License & Security

- License: `./LICENSE`
- Security policy: `./SECURITY.md`
