Use this CSV schema to import entries into Reflection, the AI journal. If your current app exports CSV, map its columns to the Reflection format described in ../docs/journal-csv-format.md

---

# Generic CSV Import Schema

Canonical CSV schema for importing journal entries into Reflection.App.

## Schema Definition

### Required Columns

| Column | Type | Format | Description |
|--------|------|--------|-------------|
| `text` | string | HTML or plain text | Entry content (see HTML requirements below) |
| `date` | string | `YYYY-MM-DD`, `YYYY-MM-DD HH:MM[:SS]` or RFC3339 | When the entry was written |

Header names are matched case- and spacing-insensitively (`Text`, `Source ID`). Columns not listed here are ignored.

### Optional Columns

| Column | Type | Format | Description |
|--------|------|--------|-------------|
| `type` | string | Enumeration | `free write` (default), `highlight` or `lowlight`; case-insensitive |
| `platform` | string | Identifier | Platform/source (default: "mobile") |
| `source_id` | string | Free text | Original entry ID from source system; used to recognize a re-import |
| `tags` | string | Comma-separated | Tag list (e.g., "reflection,gratitude") |
| `created_at` | integer | Unix timestamp (seconds) | Creation time in source system |

## Field Specifications

### `text` (required)
- **Format**: HTML (UTF-8)
- **Multi-line**: Supported via CSV quoting (wrap in double quotes)
- **Max length**: No hard limit (recommended < 50,000 characters)
- **Special characters**: CSV quotes must be escaped as `""` per RFC 4180; HTML entities (`<`, `>`, `&`) must be properly escaped in plain text content

**HTML Requirements**:
- Body text (non-list) must be wrapped in `<p>...</p>` tags
- Empty lines: `<p><br /></p>`
- Single newlines within paragraph: `<br />`
- **Allowed tags**: `p`, `br`, `strong`, `em`, `b`, `i`, `h1`-`h6`, `ul`, `ol`, `li`, `blockquote`, `a`, `s`, `hr`, `figure`, `div`, `span`
- Invalid tags will be escaped automatically
- Plain text entries (no HTML tags) will be auto-wrapped in `<p>` tags on import

**Example**:
```csv
text,type,date,platform
"<p>This is a multi-line entry.</p><p><br /></p><p>It has multiple paragraphs.</p>",free write,2024-01-15T14:30:00Z,web
```

### `type` (optional)
- **Format**: String identifier, case-insensitive
- **Default**: "free write"
- **Valid values**: "free write", "highlight", "lowlight". A row with any other type is skipped.

### `date` (required)
- **Formats**:
  - `2024-01-15` (stored as that day in the importing device's time zone)
  - `2024-01-15 14:30` or `2024-01-15 14:30:00` (that wall-clock time in the importing device's time zone)
  - `2024-01-15T14:30:00Z` or `2024-01-15T09:30:00-05:00` (that exact moment)
- A row with a missing, unreadable or future date is skipped.

### `platform` (optional)
- **Format**: String identifier
- **Default**: "mobile"
- **Case**: Lowercase
- **Purpose**: Track entry source for analytics

### `source_id` (optional)
- **Format**: Free text (typically UUID or numeric ID)
- **Purpose**: Idempotency. Importing a row whose `source_id` was imported before replaces that entry, including edits
  made in Reflection since. Without it, rows are matched by date and text.
- **Example**: Day One UUID, Evernote note ID

### `tags` (optional)
- **Format**: Comma-separated list (no spaces)
- **Case**: Lowercase recommended
- **Empty value**: Allowed (omit column or leave blank)
- **Examples**:
  - `reflection,gratitude`
  - `morning-pages`

### `created_at` (optional)
- **Format**: Unix timestamp (seconds since epoch)
- **Purpose**: Preserve original creation time from source system
- **Example**: `1705331400` (2024-01-15 14:30:00 UTC)

## CSV Format Rules

- **Header row**: Required
- **Encoding**: UTF-8 (a byte-order mark is fine; other encodings are refused)
- **Line endings**: LF (`\n`) or CRLF (`\r\n`)
- **Quoting**: Per RFC 4180 (quote fields containing commas, quotes, or newlines)
- **Delimiter**: Comma (`,`)

## Validation

The whole import fails, and the app says why, if:
- The `text` or `date` column is missing
- The file isn't UTF-8
- The CSV is malformed (for example an unclosed quote; the app names the line)
- No row could be imported

A single bad row is skipped instead, and the app lists it by row number with the reason: missing text, missing,
unreadable or future date, unsupported type, or a value too large to store.

## Examples

### Minimal CSV
```csv
text,type,date,platform
"<p>First entry</p>",free write,2024-01-15T14:30:00Z,web
"<p>Second entry</p>",free write,2024-01-16T08:15:00Z,web
```

### Full CSV (all columns)
```csv
text,type,date,platform,source_id,tags,created_at
"<p>First entry with <strong>bold</strong> text.</p>",free write,2024-01-15T14:30:00Z,web,abc-123,reflection,1705331400
"<p>Second entry.</p><p><br /></p><p>With multiple paragraphs.</p>",free write,2024-01-16T08:15:00Z,web,def-456,"morning,gratitude",1705396500
```

## Future Extensions

Not supported yet:
- Photos and other images. Email help@reflection.app to hear when photo import arrives.
- `location`, `mood`, `weather` columns are ignored; put anything you want to keep in the text.

## Migration from Other Services

Adapters for popular journal apps:
- **Day One**: See `../dayone/` directory
- **Other services**: Coming soon

If you're building a custom adapter, follow this schema and see existing adapters for reference.

---

## Privacy note

Privacy note: If you use AI prompts to map your CSV, review third-party data policies and remove sensitive entries before use. For offline conversion, use local scripts.

## Related guides

- [AI Journal Migration Guide](../docs/ai-journal-migration-guide.md)
- [Reflection CSV Format](../docs/journal-csv-format.md)
