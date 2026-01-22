# Claude Journal Converter for Reflection

Use Claude to convert journal exports into the Reflection CSV format and migrate into Reflection, the AI journal.

## What this folder contains
- Platform-specific prompts for Claude
- Examples of input/output conversions
- Guidance tailored to Claude features

## Capabilities (Claude)
- **File uploads** for CSV, JSON, PDF, DOCX, TXT, XLSX exports
- **Artifacts** for reusable outputs and schema-consistent CSV generation
- **Projects** for persistent working context across sessions
- **Analysis tool** for structured data processing

## How to use
1. Open `./prompts/claude-day-one-migration.md`
2. Upload a sample export file
3. Generate CSV as an Artifact
4. Download and validate against the schema

## Fallback (no file upload or artifacts)
If you don't have access to file uploads or Artifacts:
- Paste a small export chunk directly
- Convert in batches of 5-10 entries
- Copy the output manually
- Validate output against the CSV schema:
  - `../docs/journal-csv-format.md`

## Privacy Note
Privacy note: AI prompts send your journal content to Anthropic's servers. Review Anthropic's data policies and remove sensitive entries before use. To keep data local, use the Python converter in `../dayone/scripts/` instead.

## Related guides
- `../docs/day-one-to-reflection.md`
- `../docs/ai-journal-migration-guide.md`
- `../docs/journal-csv-format.md`
