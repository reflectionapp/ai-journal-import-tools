# ChatGPT Journal Converter Prompt for Reflection

Use ChatGPT to convert a journal export into the Reflection CSV format so you can import entries into the AI journal. Start small, validate the output, then scale up.

## Before You Start

- Have a journal export ready (CSV, JSON, or text)
- Read the Reflection CSV schema:
  - `../../docs/journal-csv-format.md`
- Consider converting in small batches (5-10 entries) to validate output
- If you're migrating from Day One, start here:
  - `../../docs/day-one-to-reflection.md`

## Prompt

```
I have a Day One journal export (JSON or ZIP with Journal.json inside). Please convert it to a CSV file for importing into Reflection.App.

**Output CSV Schema (required columns):**
- text: Entry content in HTML format (see HTML rules below)
- type: Always "free write"
- date: ISO 8601 timestamp (RFC3339 format, e.g., "2024-01-15T14:30:00Z")
- platform: Always "web"

**Optional columns (include if available):**
- source_id: Day One entry UUID
- tags: Comma-separated tags (e.g., "reflection,gratitude")
- created_at: Unix timestamp in seconds

**HTML Formatting Rules:**
- Wrap body text in `<p>...</p>` tags
- Empty lines: `<p><br /></p>`
- Single newlines within paragraph: `<br />`
- Use only these tags: p, br, strong, em, h1-h6, ul, ol, li, blockquote, a, s
- Escape HTML entities (`<`, `>`, `&`, `"`) in plain text

**Instructions:**
1. Parse the JSON (handle both {"entries":[...]} and direct array formats)
2. For each entry:
   - Convert Day One text to HTML (wrap paragraphs in `<p>`, use `<br />` for line breaks)
   - Convert creationDate to RFC3339 format
   - Join tags with commas (if present)
   - Use Day One UUID as source_id
   - Convert creationDate to unix timestamp for created_at
3. Generate CSV with header row
4. Escape any quotes or commas in text content properly

**Notes:**
- Ignore images (not supported in Phase 1)
- Ignore location and weather data

Please process my export and provide the CSV file.
```

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

- `../../docs/chatgpt-journal-converter.md`
- `../../docs/journal-csv-format.md`
- `../../docs/day-one-to-reflection.md`
