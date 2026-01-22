# Migrate to an AI Journal (Reflection) from Any App

A practical guide to move your journal into Reflection, the AI journal, from other apps or CSV exports in a few clear steps. Includes prompts and a schema link.

## Who This Guide Is For

This guide is for anyone switching journal apps and wanting to bring their history into Reflection. It works whether your current app is Day One, Journey, Diarium, Notion, or something else. If you can export your entries (CSV, JSON, or text), you can convert them into the Reflection CSV format and import.

If you're migrating from Day One specifically, use the detailed guide here:
- `./day-one-to-reflection.md`

## Step 1: Export from Your Current App

Most journaling apps include an export feature. Look for **Export**, **Backup**, or **Download** in settings.

Common export formats:
- **CSV** (best for direct mapping)
- **JSON** (structured, good for AI conversion)
- **TXT / Markdown** (possible but needs more conversion work)

If you can choose a "full" export, pick it. The more structured the export, the easier the conversion.

## Step 2: Convert to Reflection CSV

Reflection imports a CSV file with a specific column structure. You can create that file using AI prompts or a local script.

### Option A: AI Prompt Conversion

Use one of the prompt workflows in this repo:
- `../chatgpt/prompts/chatgpt-journal-converter.md`
- `../claude/prompts/claude-day-one-migration.md`

Best practices:
- Start with a small subset (5-10 entries) to validate output.
- Check dates, text, and any tags or metadata.
- Iterate until the format looks correct before converting all entries.

### Option B: Manual Mapping (CSV)

If you already have CSV:
1. Compare your export columns with the Reflection schema:
   - `./journal-csv-format.md`
2. Rename or map columns to match.
3. Ensure each row has a date and entry text.
4. Save as UTF-8 CSV.

### Option C: Local Script (Advanced)

If you have JSON or a complex export, you can write a small script to map fields to the Reflection CSV format. Keep it simple:
- Map `date` -> date column
- Map `text` -> entry body
- Map any tags or metadata to optional columns

## Step 3: Import into Reflection

Once you have a Reflection-formatted CSV:

1. Open Reflection and go to the import flow in the web app.
2. Upload the CSV.
3. Review the preview.
4. Confirm the import.

If you're unsure, start with a small CSV to test before importing everything.

## If You Already Have CSV

CSV exports are the easiest path:
- Map your columns to the Reflection CSV schema.
- Ensure date formatting is consistent.
- Validate with a quick spot-check.

If you need a reference schema:
- `./journal-csv-format.md`

## If You Have JSON or PDF

- **JSON**: Use AI prompts to map the structure to CSV.
- **PDF**: It's harder to convert; consider exporting again in CSV/JSON if possible.

## Privacy & Data Handling

Privacy note: AI prompts may send your journal content to third-party AI services. Review those providers' data policies and remove sensitive entries before use. To keep data local, use the Python converter instead.

## Related Guides

- `./day-one-to-reflection.md`
- `./chatgpt-journal-converter.md`
- `./journal-csv-format.md`
- `../chatgpt/prompts/chatgpt-journal-converter.md`
- `../claude/prompts/claude-day-one-migration.md`
