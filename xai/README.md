# Grok (xAI) Journal Converter for Reflection

Use Grok to convert journal exports into the Reflection CSV format and migrate into Reflection, the AI journal.

## What this folder contains
- Platform-specific prompts for Grok
- Examples of input/output conversions
- Guidance tailored to Grok features

## Capabilities (Grok / xAI)
- **Files API** with document upload support
- **Document search and citation** for reference
- **Code execution integration** for data cleanup
- **Google Drive integration** (Business/Enterprise plans)

## How to use
1. Open `./prompts/grok-journal-converter.md`
2. Upload a sample export via Files API
3. Convert to Reflection CSV
4. Validate and download before import

## Fallback (no file upload or code execution)
If you don't have access to file uploads or code execution:
- Paste a small export chunk directly
- Convert in batches of 5-10 entries
- Copy the output manually
- Validate output against the CSV schema:
  - `../docs/journal-csv-format.md`

## Privacy Note
Privacy note: AI prompts send your journal content to xAI's servers. Review xAI's data policies and remove sensitive entries before use. To keep data local, use the Python converter in `../dayone/scripts/` instead.

## Related guides
- `../docs/ai-journal-migration-guide.md`
- `../docs/journal-csv-format.md`
