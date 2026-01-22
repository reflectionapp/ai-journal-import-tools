# Day One to Reflection: Migrate Your Journal to the AI Journal

Move your Day One journal into Reflection, the AI journal, using exports plus AI prompts or a local script to build the import CSV. No retyping required.

## Overview

If you're switching from Day One, you don't need to start fresh. This guide walks you through a simple migration flow: export your Day One data, convert it into the Reflection CSV format, then import it into Reflection. You can choose an AI-prompt workflow (ChatGPT or Claude) or use the local Python converter included in this repo.

The goal is to keep your writing intact - dates, text, and metadata - so your journal history comes with you.

## What You'll Need

- A Day One export file (ZIP, JSON, or text-based export)
- A local folder to store your export and conversion files
- One of the following:
  - An AI prompt workflow (ChatGPT or Claude)
  - The local Python converter in `dayone/scripts/`
- A way to open and review CSV files (Excel, Numbers, Google Sheets, or a text editor)

Optional but recommended:
- A backup copy of your original export
- A small test import (10-20 entries) before doing the full import

## Step 1: Export from Day One

Day One provides a built-in export tool. The exact menu labels may vary by device and version, but the general flow is:

1. Open Day One and go to **Settings** or **Journal settings**.
2. Look for **Export**, **Backup**, or **Export Journal**.
3. Choose a format that includes entry text and dates (JSON or full export ZIP are ideal).
4. Save the export to a local folder you can access.

Tips:
- If you have multiple journals, export the one you want to migrate.
- If Day One offers "Full" vs "Text only," choose the full export.
- Keep the export file intact; do not edit it yet.

If you're unsure which export format to pick, start with the full export ZIP. Most conversion workflows can work from that.

## Step 2: Convert to Reflection CSV

Reflection imports a CSV file with a specific set of columns. This step converts your Day One export into that format. You have two options:

- **Option A: AI prompts** (faster to start, uses a hosted AI tool)
- **Option B: Local Python script** (keeps data offline)

Both options produce the same Reflection CSV output.

### Option A: AI Prompts

This option uses the prompts in `prompts/` to map your Day One export to the Reflection CSV format.

**Recommended flow:**
1. Open the prompt file:
   - `../chatgpt/prompts/chatgpt-journal-converter.md`
   - or `../claude/prompts/claude-day-one-migration.md`
2. Paste a small subset of your Day One export to test (5-10 entries).
3. Run the prompt and inspect the output CSV.
4. Once the output looks correct, repeat with larger batches until complete.

**Tips for accuracy:**
- Keep the export data in small batches to reduce formatting errors.
- Always validate dates and entry text after conversion.
- If the output looks inconsistent, rerun the prompt with fewer entries.

### Option B: Python Script (Local)

If you prefer to keep data offline, use the Python converter in `dayone/scripts/`.

**General flow:**
1. Navigate to the script folder: `dayone/scripts/`
2. Follow the instructions in that folder's README.
3. Run the script against your export file.
4. The script outputs a Reflection-formatted CSV.

This method keeps data local and avoids sending your journal content to any external AI service.

## Step 3: Import into Reflection

Once you have your Reflection CSV:

1. Open Reflection and go to the import tool in the web app.
2. Upload the CSV file.
3. Review the import preview.
4. Confirm and complete the import.

If you're unsure about the import, start with a small CSV (10-20 entries), check the results, and then import the full file.

## Troubleshooting

**Dates are missing or wrong**
- Check that your CSV has a date column in the format expected by Reflection.
- If your export includes time zones, ensure they're preserved.

**Entries are in the wrong order**
- Reflection sorts by date. Confirm that each row has a valid date.

**Text is split across rows**
- This usually happens when line breaks or commas weren't escaped.
- Re-run conversion with smaller batches or ensure proper CSV quoting.

**Import fails**
- Validate the CSV against the schema: `./journal-csv-format.md`
- Remove empty rows and re-import.

## Privacy & Data Handling

Privacy note: AI prompts may send your journal content to third-party AI services. Review those providers' data policies and remove sensitive entries before use. To keep data local, use the Python converter instead.

## Related Guides

- `./ai-journal-migration-guide.md`
- `./chatgpt-journal-converter.md`
- `./journal-csv-format.md`
- `../chatgpt/README.md`
- `../claude/README.md`
- `../gemini/README.md`
- `../xai/README.md`
- `../chatgpt/prompts/chatgpt-journal-converter.md`
- `../claude/prompts/claude-day-one-migration.md`
