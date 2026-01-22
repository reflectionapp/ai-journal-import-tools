Move your Day One journal into Reflection, the AI journal, by converting your export to the Reflection CSV format. This folder includes a local Python converter, prompts, and sample files for Day One exports. Start with the migration guide: ../docs/day-one-to-reflection.md

---

# Day One to Reflection.App CSV Converter

Convert Day One journal exports (JSON or ZIP) to Reflection.App import format.

## Export from Day One

1. Open Day One app
2. Go to **File → Export → JSON** or **Export → ZIP**
3. Save the export file

## Conversion Options

### Option 1: AI-Assisted (Recommended)

Use AI prompts to guide the transformation:

- **ChatGPT**: `prompts/chatgpt.md`
- **Claude**: `prompts/claude.md`

Copy the prompt, attach your Day One export, and the AI will generate the CSV.

### Option 2: Python Script

```bash
python scripts/convert.py your_export.json
# Or with ZIP:
python scripts/convert.py your_export.zip

# Custom output path:
python scripts/convert.py your_export.json -o my_import.csv
```

**Requirements**: Python 3.7+ (uses stdlib only, no external dependencies)

## Output Schema

The converter produces a CSV with these columns:

| Column | Required | Description | Example |
|--------|----------|-------------|---------|
| `text` | ✅ | Entry content | "Today was a great day..." |
| `type` | ✅ | Entry type | "free write" |
| `date` | ✅ | ISO 8601 timestamp | "2024-01-15T14:30:00Z" |
| `platform` | ✅ | Platform identifier | "web" |
| `source_id` | ⬜ | Day One UUID | "A1B2C3D4..." |
| `tags` | ⬜ | Comma-separated | "reflection,gratitude" |
| `created_at` | ⬜ | Unix timestamp (seconds) | 1705331400 |

## Examples

See `examples/` for:
- `sample_input.json` - Day One JSON structure
- `sample_output.csv` - Expected output format

## Limitations

- **Images**: Not supported in Phase 1 (text-only import)
- **Location**: Not preserved
- **Weather**: Not preserved
- **Rich text formatting**: Converted to plain text

## Troubleshooting

**Error: "No entries found"**
- Check that your export contains `entries` array
- Try both `Journal.json` (ZIP) and standalone JSON formats

**Error: "Invalid date format"**
- Day One dates are parsed as ISO 8601
- Script handles both RFC3339 and unix timestamps

**Missing tags**
- Tags are optional; empty tags field is valid
- Multiple tags are joined with commas

---

## Privacy note

Privacy note: AI prompts may send your journal content to third-party AI services. Review those providers' data policies and remove sensitive entries before use. To keep data local, use the Python converter instead.

## Related guides

- [Day One to Reflection Migration Guide](../docs/day-one-to-reflection.md)
- [ChatGPT Journal Converter](../docs/chatgpt-journal-converter.md)
- [Reflection CSV Format](../docs/journal-csv-format.md)
