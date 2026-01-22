# Reflection Journal CSV Format (Schema)

Reflection's journal CSV format documents the fields required for import, including dates, text, and metadata. Use it to map exports or validate conversions.

## Overview

The Reflection CSV format is the documented schema used for importing journal entries into Reflection. Each row represents a single entry. Required columns capture the entry text and date; optional columns let you preserve tags and other metadata.

Use this doc to:
- Map another app's export to the Reflection schema
- Validate AI prompt output
- Build or test import scripts

## Required Columns

At minimum, your CSV should include:

- `date` - the entry's date (YYYY-MM-DD recommended)
- `text` - the entry body

Example:
```
date,text
2024-04-12,"Today I went for a long walk and felt lighter."
```

## Optional Columns

Optional fields allow you to preserve more context:
- `title` - entry title or summary
- `tags` - comma-separated tags
- `mood` - a short label (if your source app supports it)
- `source` - the original app name

If you include optional columns, keep them consistent across rows.

## Date and Time Rules

- Prefer ISO format: `YYYY-MM-DD` or `YYYY-MM-DD HH:MM`
- If you include times, keep them in a single timezone
- Avoid ambiguous formats like `04/05/24`

## Text and Metadata Guidelines

- Keep text in a single CSV cell with proper quoting
- Escape line breaks using standard CSV quoting
- If your export includes rich text or HTML, convert to plain text

## Example Rows

```
date,text,title,tags
2024-01-01,"New year reflections","New Year","reflection,goals"
2024-01-15,"First week back at work felt steady.","","work"
```

## Validation Checklist

Before importing:
- Dates are valid and consistent
- Entry text is present in every row
- Commas and line breaks are properly escaped
- Optional columns are spelled consistently

## Versioning

This schema may evolve as Reflection adds import features. When changes occur, we'll update this document and note compatibility guidance.

## Privacy Note

If you use AI prompts to map your CSV, review third-party data policies and remove sensitive entries before use. For offline conversion, use local scripts.
