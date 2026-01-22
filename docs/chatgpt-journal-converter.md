# Use ChatGPT to Convert a Journal Export for Reflection

Use ChatGPT to convert a journal export into the Reflection CSV format so you can import entries into the AI journal. Includes a ready-to-use prompt and checks.

## Before You Start

You'll need:
- A journal export file (CSV, JSON, or text)
- A place to store your converted CSV
- The Reflection CSV schema:
  - `./journal-csv-format.md`

If you're migrating from Day One, use the full guide here:
- `./day-one-to-reflection.md`

## Prompt

Use the prompt in this file:
- `../chatgpt/prompts/chatgpt-journal-converter.md`

Tip: start with a small sample of entries (5-10) before converting everything.

## How to Run the Prompt

1. Open ChatGPT.
2. Paste the prompt from `../chatgpt/prompts/chatgpt-journal-converter.md`.
3. Provide a small sample of your export.
4. Ask for CSV output in the Reflection format.
5. Review the output and validate it.

Once the small sample looks correct, repeat with larger batches.

## Validate the Output

Before import, check:
- **Dates** are present and correct
- **Entry text** is intact (no missing paragraphs)
- **Commas and line breaks** are correctly escaped
- **Columns** match the Reflection schema

If the output is inconsistent, re-run with fewer entries or clarify formatting in your prompt.

## Import into Reflection

When your CSV looks correct:

1. Open Reflection's import flow.
2. Upload the CSV.
3. Review the preview.
4. Confirm import.

## Privacy Note

Privacy note: AI prompts may send your journal content to third-party AI services. Review those providers' data policies and remove sensitive entries before use. To keep data local, use the Python converter instead.

## Related Guides

- `./day-one-to-reflection.md`
- `./journal-csv-format.md`
- `../chatgpt/prompts/chatgpt-journal-converter.md`
