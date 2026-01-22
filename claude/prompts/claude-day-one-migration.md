# Claude Prompt for Day One to Reflection Migration

Use Claude to convert a Day One export into the Reflection CSV format so you can import entries into the AI journal. Start with a small sample, validate, then scale.

## Before You Start

- Export your Day One journal (full export preferred)
- Review the Reflection CSV schema:
  - `../../docs/journal-csv-format.md`
- Use small batches first to reduce formatting errors
- Follow the full migration guide:
  - `../../docs/day-one-to-reflection.md`

## Prompt

```
I have a Day One journal export (JSON or ZIP containing Journal.json). Convert it to a CSV file for Reflection.App import.

**Required CSV columns:**
- text: Entry content in HTML format (see HTML formatting rules below)
- type: Set to "free write"
- date: ISO 8601 timestamp (RFC3339, e.g., "2024-01-15T14:30:00Z")
- platform: Set to "web"

**Optional CSV columns (include if data available):**
- source_id: Day One entry UUID
- tags: Comma-separated tag list (e.g., "reflection,gratitude")
- created_at: Unix timestamp (seconds)

**HTML Formatting Rules:**
- Wrap body text (non-list content) in `<p>...</p>` tags
- Empty lines: `<p><br /></p>`
- Single newlines within a paragraph: `<br />`
- Allowed tags only: p, br, strong, em, h1-h6, ul, ol, li, blockquote, a, s
- Escape HTML entities (`<`, `>`, `&`, `"`) in plain text content

**Conversion steps:**
1. Extract Journal.json from ZIP (if needed) or parse JSON directly
2. Handle both {"entries":[...]} and direct array formats
3. For each entry:
   - Convert Day One rich text to HTML using formatting rules above
   - Wrap plain paragraphs in `<p>` tags, separate with empty `<p><br /></p>` for blank lines
   - Convert `creationDate` to RFC3339 format for `date`
   - Join `tags` array with commas
   - Use `uuid` as `source_id`
   - Convert `creationDate` to unix seconds for `created_at`
4. Generate CSV with proper escaping (quotes, commas, newlines)
5. Include header row

**Data to exclude:**
- Images (Phase 1 limitation)
- Location metadata
- Weather data

Process the attached file and provide the CSV output.
```

## Output Checklist

Before importing, verify:
- Dates are correct and consistent
- Entry text matches the Day One export
- CSV columns match the Reflection schema
- No rows are split incorrectly

If output looks inconsistent, try smaller batches.

## Privacy Note

Privacy note: AI prompts may send your journal content to third-party AI services. Review those providers' data policies and remove sensitive entries before use. To keep data local, use the Python converter instead.

## Related Guides

- `../../docs/day-one-to-reflection.md`
- `../../docs/journal-csv-format.md`
- `../../docs/chatgpt-journal-converter.md`
