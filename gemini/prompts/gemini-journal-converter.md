# Gemini Journal Converter Prompt for Reflection

Use Gemini to convert a journal export into the Reflection CSV format so you can import entries into the AI journal. Start small, validate the output, then scale up.

## Before You Start

- Have a journal export ready (CSV, JSON, or text)
- Read the Reflection CSV schema:
  - `../../docs/journal-csv-format.md`
- Consider converting in small batches (5-10 entries) to validate output
- For migration guidance:
  - `../../docs/ai-journal-migration-guide.md`

## Prompt

TBD - Gemini prompt to be developed in Phase 2

## Output Checklist

Before importing, verify:
- Dates are present and consistent
- Entry text is complete (no missing paragraphs)
- CSV columns match the Reflection schema
- Commas and line breaks are properly escaped

If anything looks off, re-run with fewer entries or clarify formatting in the prompt.

## Privacy Note

Privacy note: AI prompts may send your journal content to third-party AI services. Review those providers' data policies and remove sensitive entries before use. To keep data local, use the Python converter instead.

## Related Guides

- `../../docs/ai-journal-migration-guide.md`
- `../../docs/journal-csv-format.md`
