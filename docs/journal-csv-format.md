# Reflection Journal CSV Format (Schema)

This is the exact format Reflection's CSV import reads. Use it to map another app's export, check what an AI tool
produced, or build a file by hand in a spreadsheet.

Each row is one journal entry.

> **Easiest route for most journals:** if you have Reflection Premium, connect an AI assistant (ChatGPT, Claude,
> or any tool that supports MCP) to Reflection under **Settings → Advanced → MCP Keys**, hand it your export, and
> ask it to create the entries. It writes them straight into your journal, with no CSV in between. A CSV is the
> right choice when you want to check every row yourself before importing.

## Required columns

| Column | What goes in it                                                                                      |
| ------ | ---------------------------------------------------------------------------------------------------- |
| `date` | When the entry was written. See [Dates](#dates).                                                      |
| `text` | The entry itself. Plain text, or simple HTML (`<p>`, `<h1>`–`<h6>`, `<ul>`/`<ol>`/`<li>`, `<strong>`, `<em>`). |

Column names are matched without regard to case or spacing: `Date`, `TEXT` and `Source ID` all work.

```csv
date,text
2024-04-12,"Today I went for a long walk and felt lighter."
```

## Optional columns

| Column      | What goes in it                                                                                     |
| ----------- | --------------------------------------------------------------------------------------------------- |
| `tags`      | Comma-separated tags, in one quoted cell: `"work,gratitude"`.                                       |
| `type`      | `free write` (the default), `highlight` or `lowlight`. Case doesn't matter.                         |
| `source_id` | Any ID that's unique per entry, such as the ID from the app you're leaving. Strongly recommended. See [Importing again](#importing-again). |

Any other column (`title`, `mood`, `weather` and so on) is ignored, not imported. If you want that information
in Reflection, put it in the text, for example `<p><strong>Mood:</strong> calm</p>` at the top.

## Dates

Any of these work:

| Format                        | Example                | Stored as                                 |
| ----------------------------- | ---------------------- | ----------------------------------------- |
| `YYYY-MM-DD`                  | `2024-04-12`           | That day                                  |
| `YYYY-MM-DD HH:MM`            | `2024-04-12 21:30`     | That time, in your device's time zone     |
| `YYYY-MM-DD HH:MM:SS`         | `2024-04-12 21:30:05`  | That time, in your device's time zone     |
| ISO 8601 with a time zone     | `2024-04-12T21:30:00Z` | That exact moment                         |

Formats like `04/12/24` or `12 April 2024` aren't read, because they're ambiguous. Convert them first: in most
spreadsheet apps, format the column as `yyyy-mm-dd`.

A row with no date, an unreadable date or a date in the future is skipped, not imported as today.

## Text

- Keep each entry's text in one cell. Wrap it in double quotes if it contains commas, quotes or line breaks, and
  double any quotes inside it (`"She said ""hi"""`). Spreadsheet apps do this for you when you save as CSV.
- Plain text keeps its line breaks. A blank line starts a new paragraph.
- Markdown isn't converted: `# Title` arrives as the characters `# Title`. Convert it to the HTML above, or use the
  Day One converter in `dayone/scripts/`, which does this for Day One exports.
- A row with no text is skipped.

## Photos

Photos can't be imported yet. Image links in the text arrive as plain text, so remove them. To hear when photo
import arrives, email [help@reflection.app](mailto:help@reflection.app?subject=Notify%20me%20about%20photo%20import).

## Saving the file

- Save as **CSV UTF-8** (Excel: *File → Save As → CSV UTF-8*; Google Sheets: *File → Download → CSV*; Numbers:
  *File → Export To → CSV*, Text Encoding *Unicode (UTF-8)*). A file in another encoding is refused rather than
  imported with garbled characters.
- One file can hold up to 25,000 entries.

## What happens when you import

Import from **Settings → Advanced → Import & Export** in the Reflection app. You can leave the screen while it runs. When you
come back, the same screen shows how it went:

- how many entries were added,
- how many replaced entries from an earlier import,
- which rows were skipped, by row number (the header is row 1, as in your spreadsheet), and why.

If the whole file can't be read, for example because the `date` or `text` column is missing or the file isn't
UTF-8, the screen says what to fix.

## Importing again

Reflection recognizes a row it has imported before and **replaces** that entry, including any edits you've made to
it in Reflection since. It matches rows by `source_id`. Without a `source_id`, it matches by the row's date and text,
so if you change a row's text and import again, you get a second entry instead of an updated one.

So: give every row a `source_id`, and if you've edited imported entries in Reflection, leave those rows out of a
re-import.

## Example

```csv
date,text,tags,type,source_id
2024-01-01,"<h2>New year</h2><p>Three things I want more of this year.</p>","reflection,goals",free write,old-app-0001
2024-01-15 07:45,"First week back at work felt steady.",work,highlight,old-app-0002
2024-01-20T22:10:00Z,"Rough day.
Slept badly, snapped at a friend.",,lowlight,old-app-0003
```

## Checklist

- [ ] `date` and `text` columns, every row filled
- [ ] Dates in one of the formats above, none in the future
- [ ] A unique `source_id` on every row
- [ ] Saved as CSV UTF-8
- [ ] Image links and other app-specific markup removed from the text

## Privacy note

If you use an AI assistant to convert your export, your journal passes through that provider. Review its data
policy and remove anything you don't want to share first. To keep everything on your computer, convert with a
local script, such as the Day One converter in this repo.
