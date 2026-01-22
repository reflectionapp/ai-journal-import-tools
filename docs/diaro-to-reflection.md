# Diaro to Reflection: Migrate to an AI Journal

Move your Diaro journal into Reflection, the AI journal, using exports and a simple conversion workflow.

## Overview

If you're switching from Diaro, you don't need to start fresh. This guide shows how to export your entries, convert them to Reflection's CSV format, and import into Reflection so your journal history comes with you.

## What You'll Need

- A Diaro export file (CSV, JSON, or text)
- A local folder for your conversion files
- One of the following:
  - An AI prompt workflow (ChatGPT, Claude, Gemini, or Grok)
  - Manual CSV mapping

## Step 1: Export from Diaro

1. Open Diaro and access **Menu** > **Export**
2. Choose export format: **CSV** (recommended) or **XML**
3. Save the export file to a local folder

Tips:
- Choose the most complete export format available
- If multiple journals exist, export the one you want to migrate
- Keep the original export file as a backup

## Step 2: Convert to Reflection CSV

Reflection imports a CSV file with a specific column structure. You have several options:

### Option A: AI Prompt Conversion

Use one of the AI prompt workflows:
- [ChatGPT](../chatgpt/README.md)
- [Claude](../claude/README.md)
- [Gemini](../gemini/README.md)
- [Grok](../xai/README.md)

Best practices:
- Start with a small subset (5-10 entries) to validate
- Check dates, text, and any metadata
- Scale up once output looks correct

### Option B: Manual CSV Mapping

If your export is already CSV:
1. Compare columns with the [Reflection CSV schema](./journal-csv-format.md)
2. Rename or map columns to match
3. Ensure each row has a date and entry text
4. Save as UTF-8 CSV

## Step 3: Import into Reflection

Once you have a Reflection-formatted CSV:

1. Open Reflection and go to the import flow in the web app
2. Upload the CSV file
3. Review the import preview
4. Confirm and complete the import

If unsure, start with a small test import (10-20 entries) first.

## Troubleshooting

**Dates are missing or wrong**
- Check date column format matches Reflection's expected format
- Ensure timezone information is preserved if present

**Entries are in the wrong order**
- Reflection sorts by date - verify each row has a valid date

**Text is split across rows**
- Usually caused by unescaped line breaks or commas
- Re-run conversion with proper CSV quoting

**Import fails**
- Validate against the [CSV schema](./journal-csv-format.md)
- Remove empty rows and retry

## Privacy & Data Handling

Privacy note: AI prompts may send your journal content to third-party AI services. Review those providers' data policies and remove sensitive entries before use. To keep data local, use manual CSV mapping or the Python converter.

## Related Guides

- [AI Journal Migration Guide](./ai-journal-migration-guide.md)
- [Reflection CSV Format](./journal-csv-format.md)
- [ChatGPT Converter](../chatgpt/README.md)
- [Claude Converter](../claude/README.md)
