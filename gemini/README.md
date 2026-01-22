# Gemini Journal Converter for Reflection

Use Gemini to convert journal exports into the Reflection CSV format and migrate into Reflection, the AI journal.

## What this folder contains
- Platform-specific prompts for Gemini
- Examples of input/output conversions
- Guidance tailored to Gemini features

## Capabilities (Gemini)
- **File uploads** for documents and spreadsheets
- **Code execution** for CSV validation and cleanup
- **Google ecosystem integration** (Drive, Sheets)
- **Document understanding** for PDF processing

## How to use
1. Open `./prompts/gemini-journal-converter.md`
2. Upload your export file
3. Run conversion with code execution enabled
4. Download and import to Reflection

## Fallback (no file upload or code execution)
If you don't have access to file uploads or code execution:
- Paste a small export chunk directly
- Convert in batches of 5-10 entries
- Copy the output manually
- Validate output against the CSV schema:
  - `../docs/journal-csv-format.md`

## Privacy Note
Privacy note: AI prompts send your journal content to Google's servers. Review Google's data policies and remove sensitive entries before use. To keep data local, use the Python converter in `../dayone/scripts/` instead.

## Related guides
- `../docs/ai-journal-migration-guide.md`
- `../docs/journal-csv-format.md`
