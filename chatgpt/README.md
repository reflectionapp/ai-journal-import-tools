# ChatGPT Journal Converter for Reflection

Use ChatGPT to convert journal exports into the Reflection CSV format and migrate into Reflection, the AI journal.

## What this folder contains
- Platform-specific prompts for ChatGPT
- Examples of input/output conversions
- Guidance tailored to ChatGPT features

## Capabilities (ChatGPT)
- **File uploads** for CSV/JSON exports
- **Code Interpreter / data analysis** to validate and transform CSV
- **Canvas** for iterative editing and formatting
- **Downloadable artifacts** for easy CSV export

## How to use
1. Open `./prompts/chatgpt-journal-converter.md`
2. Upload a small export sample (5-10 entries)
3. Run the prompt and validate output
4. Scale up to full export once validated

## Fallback (no file upload or code execution)
If you don't have access to file uploads or Code Interpreter:
- Paste a small export chunk directly into the chat
- Convert in batches of 5-10 entries
- Copy the CSV output manually
- Validate output against the CSV schema:
  - `../docs/journal-csv-format.md`

## Privacy Note
Privacy note: AI prompts send your journal content to OpenAI's servers. Review OpenAI's data policies and remove sensitive entries before use. To keep data local, use the Python converter in `../dayone/scripts/` instead.

## Related guides
- `../docs/day-one-to-reflection.md`
- `../docs/ai-journal-migration-guide.md`
- `../docs/journal-csv-format.md`
