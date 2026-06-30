#!/usr/bin/env python3
"""
Day One to Reflection.App CSV Converter

Converts Day One JSON/ZIP exports to Reflection.App import format.
Supports multi-journal ZIP exports — each entry is tagged with its journal
name and the import source ("DayOne").
Requires Python 3.7+ (stdlib only, no external dependencies).

Usage:
    python convert.py input.json [-o output.csv]
    python convert.py input.zip [-o output.csv]
"""

import argparse
import csv
import json
import sys
import zipfile
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

# Tag added to every converted entry to record where it was imported from.
SOURCE_TAG = 'DayOne'


def _sanitize_tag(tag: str) -> str:
    """Normalise a value for the comma-separated ``tags`` CSV column.

    Commas are the tag delimiter, so they are replaced with spaces to stop a
    single value (e.g. a journal named ``"Health, Fitness"``) from splitting
    into multiple tags downstream. Surrounding/duplicate whitespace is
    collapsed.
    """
    return ' '.join(str(tag).replace(',', ' ').split())


def parse_dayone_date(date_str: str) -> tuple[str, int]:
    """
    Parse Day One date to RFC3339 and unix timestamp.

    Args:
        date_str: ISO 8601 date string

    Returns:
        Tuple of (RFC3339 string, unix timestamp)
    """
    try:
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        rfc3339 = dt.strftime('%Y-%m-%dT%H:%M:%SZ')
        unix_ts = int(dt.timestamp())
        return rfc3339, unix_ts
    except Exception as e:
        print(
            f"Warning: Failed to parse date '{date_str}': {e}", file=sys.stderr)
        now = datetime.utcnow()
        return now.strftime('%Y-%m-%dT%H:%M:%SZ'), int(now.timestamp())


def extract_entries_from_json(data: Any) -> List[Dict[str, Any]]:
    """
    Extract entries array from JSON data.

    Handles both {"entries":[...]} and direct array formats.

    Args:
        data: Parsed JSON data

    Returns:
        List of entry dictionaries
    """
    if isinstance(data, list):
        return data
    elif isinstance(data, dict):
        for key in ['entries', 'Entries', 'items', 'Items']:
            if key in data and isinstance(data[key], list):
                return data[key]

    print("Error: Could not find entries array in JSON", file=sys.stderr)
    return []


def convert_entry(entry: Dict[str, Any]) -> Dict[str, str]:
    """
    Convert a Day One entry to Reflection.App CSV row.

    Tags are emitted as: journal name, the entry's own tags, then the import
    source — e.g. "Highlights,work,DayOne". Values are de-duplicated and
    comma-sanitised so the tag contract stays valid.

    Args:
        entry: Day One entry dictionary

    Returns:
        CSV row dictionary
    """
    text = entry.get('text', entry.get('Text', ''))
    entry_type = 'free write'
    platform = 'web'

    creation_date = entry.get('creationDate', entry.get('CreationDate', ''))
    if not creation_date:
        print("Warning: Entry missing creationDate, using current time",
              file=sys.stderr)
        creation_date = datetime.utcnow().isoformat()

    date_rfc3339, created_at = parse_dayone_date(creation_date)
    source_id = entry.get('uuid', entry.get('UUID', ''))

    # Build tags: journal name first, then the entry's own tags, then the
    # import source. Day One stores tags as a list, but tolerate a bare string.
    raw_tags = entry.get('tags', entry.get('Tags', [])) or []
    if isinstance(raw_tags, str):
        raw_tags = [raw_tags]

    ordered_tags: List[str] = []
    journal_name = entry.get('__journal__', '')
    if journal_name:
        ordered_tags.append(journal_name)
    ordered_tags.extend(raw_tags)
    ordered_tags.append(SOURCE_TAG)

    seen = set()
    tags: List[str] = []
    for tag in ordered_tags:
        tag = _sanitize_tag(tag)
        if tag and tag.lower() not in seen:
            seen.add(tag.lower())
            tags.append(tag)

    tags_str = ','.join(tags)

    return {
        'text': text,
        'type': entry_type,
        'date': date_rfc3339,
        'platform': platform,
        'source_id': source_id,
        'tags': tags_str,
        'created_at': str(created_at),
    }


def load_all_entries_from_zip(zip_path: Path) -> List[Dict[str, Any]]:
    """
    Extract and parse ALL journal JSON files from a Day One ZIP export.
    Injects a '__journal__' key into each entry with the source journal name.

    macOS metadata (``__MACOSX/`` and ``._*`` AppleDouble sidecars) is skipped,
    and a single unreadable or malformed file is skipped rather than aborting
    the whole import.

    Args:
        zip_path: Path to ZIP file

    Returns:
        Combined list of all entries across all journals
    """
    all_entries: List[Dict[str, Any]] = []

    with zipfile.ZipFile(zip_path, 'r') as zf:
        json_files = [
            name for name in zf.namelist()
            if name.endswith('.json')
            and not name.startswith('__MACOSX/')
            and not Path(name).name.startswith('._')
        ]

        if not json_files:
            raise FileNotFoundError("No JSON files found in ZIP")

        for filename in json_files:
            # e.g. "Journal", "Travel", "Work"
            journal_name = Path(filename).stem
            print(f"  Processing journal: {journal_name} ({filename})")

            try:
                with zf.open(filename) as f:
                    data = json.load(f)
            except (json.JSONDecodeError, UnicodeDecodeError, OSError) as e:
                print(
                    f"  Warning: Skipping {filename} — could not read JSON: {e}",
                    file=sys.stderr)
                continue

            entries = extract_entries_from_json(data)

            # Day One entries are objects; ignore anything else so one
            # malformed file can't abort the whole import.
            dict_entries = [e for e in entries if isinstance(e, dict)]
            skipped = len(entries) - len(dict_entries)
            if skipped:
                print(
                    f"  Warning: Skipped {skipped} non-object entries in {filename}",
                    file=sys.stderr)

            print(f"    Found {len(dict_entries)} entries")

            for entry in dict_entries:
                entry['__journal__'] = journal_name

            all_entries.extend(dict_entries)

    return all_entries


def convert_dayone_to_csv(input_path: Path, output_path: Path) -> None:
    """
    Convert Day One export to Reflection.App CSV.

    Args:
        input_path: Path to JSON or ZIP file
        output_path: Path to output CSV file
    """
    if input_path.suffix.lower() == '.zip':
        print(f"Extracting all journals from {input_path.name}...")
        entries = load_all_entries_from_zip(input_path)
    elif input_path.suffix.lower() == '.json':
        print(f"Loading {input_path.name}...")
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        entries = extract_entries_from_json(data)
    else:
        raise ValueError(f"Unsupported file type: {input_path.suffix}")

    if not entries:
        print("Error: No entries found in export", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(entries)} entries total")

    rows = [convert_entry(entry) for entry in entries]

    fieldnames = ['text', 'type', 'date', 'platform',
                  'source_id', 'tags', 'created_at']
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✓ Converted {len(rows)} entries to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description='Convert Day One export to Reflection.App CSV format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python convert.py export.json
  python convert.py export.zip -o my_import.csv
        """
    )
    parser.add_argument('input', type=Path,
                        help='Day One export (JSON or ZIP)')
    parser.add_argument('-o', '--output', type=Path, default=Path('reflection_import.csv'),
                        help='Output CSV path (default: reflection_import.csv)')

    args = parser.parse_args()

    if not args.input.exists():
        print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    try:
        convert_dayone_to_csv(args.input, args.output)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
