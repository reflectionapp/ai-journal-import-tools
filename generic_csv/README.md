Use this CSV schema to import entries into Reflection, the AI journal. If your current app exports CSV, map its columns to the Reflection format described in ../docs/journal-csv-format.md

---

# Generic CSV Import Schema

Canonical CSV schema for importing journal entries into Reflection.App.

## Schema Definition

### Required Columns

| Column | Type | Format | Description |
|--------|------|--------|-------------|
| `text` | string | HTML | Entry content in HTML format (see HTML requirements below) |
| `type` | string | Enumeration | Entry type (default: "free write") |
| `date` | string | ISO 8601 (RFC3339) | Entry timestamp (e.g., "2024-01-15T14:30:00Z") |
| `platform` | string | Identifier | Platform/source (default: "web") |

### Optional Columns

| Column | Type | Format | Description |
|--------|------|--------|-------------|
| `source_id` | string | Free text | Original entry ID from source system |
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

### `type` (required)
- **Format**: String identifier
- **Default**: "free write"
- **Case**: Lowercase recommended
- **Valid values**: "free write" (others reserved for future use)

### `date` (required)
- **Format**: ISO 8601 / RFC3339
- **Timezone**: Must include timezone (use `Z` for UTC or `+HH:MM` offset)
- **Examples**:
  - `2024-01-15T14:30:00Z` (UTC)
  - `2024-01-15T09:30:00-05:00` (EST)

### `platform` (required)
- **Format**: String identifier
- **Default**: "web"
- **Case**: Lowercase
- **Purpose**: Track entry source for analytics

### `source_id` (optional)
- **Format**: Free text (typically UUID or numeric ID)
- **Purpose**: Idempotency and deduplication
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
- **Encoding**: UTF-8
- **Line endings**: LF (`\n`) or CRLF (`\r\n`)
- **Quoting**: Per RFC 4180 (quote fields containing commas, quotes, or newlines)
- **Delimiter**: Comma (`,`)

## Validation

Imports will fail if:
- Required columns are missing
- `date` is not valid ISO 8601
- `text` is empty
- CSV is malformed (unclosed quotes, invalid encoding)

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

Reserved for Phase 2:
- `images` - Image attachment support
- `location` - Geolocation data
- `mood` - Mood/sentiment tracking
- `weather` - Weather conditions

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
