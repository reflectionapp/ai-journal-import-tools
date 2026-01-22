# ChatGPT Prompt: Day One to Reflection.App CSV

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

## Usage

1. Open ChatGPT
2. Copy the prompt above
3. Attach your Day One export file (JSON or ZIP)
4. ChatGPT will generate the CSV
5. Download the CSV and import to Reflection.App
