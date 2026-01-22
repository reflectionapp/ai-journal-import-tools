#!/usr/bin/env python3
"""
Day One to Reflection.App CSV Converter

Converts Day One JSON/ZIP exports to Reflection.App import format.
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


def parse_dayone_date(date_str: str) -> tuple[str, int]:
    """
    Parse Day One date to RFC3339 and unix timestamp.

    Args:
        date_str: ISO 8601 date string

    Returns:
        Tuple of (RFC3339 string, unix timestamp)
    """
    try:
        # Parse ISO 8601 (Day One format)
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        rfc3339 = dt.strftime('%Y-%m-%dT%H:%M:%SZ')
        unix_ts = int(dt.timestamp())
        return rfc3339, unix_ts
    except Exception as e:
        print(f"Warning: Failed to parse date '{date_str}': {e}", file=sys.stderr)
        # Return current time as fallback
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
        # Try common keys
        for key in ['entries', 'Entries', 'items', 'Items']:
            if key in data and isinstance(data[key], list):
                return data[key]

    print("Error: Could not find entries array in JSON", file=sys.stderr)
    return []


def convert_entry(entry: Dict[str, Any]) -> Dict[str, str]:
    """
    Convert a Day One entry to Reflection.App CSV row.

    Args:
        entry: Day One entry dictionary

    Returns:
        CSV row dictionary
    """
    # Required fields with defaults
    text = entry.get('text', entry.get('Text', ''))
    entry_type = 'free write'
    platform = 'web'

    # Date conversion
    creation_date = entry.get('creationDate', entry.get('CreationDate', ''))
    if not creation_date:
        print(f"Warning: Entry missing creationDate, using current time", file=sys.stderr)
        creation_date = datetime.utcnow().isoformat()

    date_rfc3339, created_at = parse_dayone_date(creation_date)

    # Optional fields
    source_id = entry.get('uuid', entry.get('UUID', ''))
    tags = entry.get('tags', entry.get('Tags', []))
    tags_str = ','.join(tags) if tags else ''

    return {
        'text': text,
        'type': entry_type,
        'date': date_rfc3339,
        'platform': platform,
        'source_id': source_id,
        'tags': tags_str,
        'created_at': str(created_at),
    }


def load_json_from_zip(zip_path: Path) -> Any:
    """
    Extract and parse Journal.json from Day One ZIP export.

    Args:
        zip_path: Path to ZIP file

    Returns:
        Parsed JSON data
    """
    with zipfile.ZipFile(zip_path, 'r') as zf:
        # Try common filenames
        for filename in ['Journal.json', 'journal.json']:
            try:
                with zf.open(filename) as f:
                    return json.load(f)
            except KeyError:
                continue

        # Fallback: find any .json file
        json_files = [name for name in zf.namelist() if name.endswith('.json')]
        if json_files:
            with zf.open(json_files[0]) as f:
                return json.load(f)

        raise FileNotFoundError("No JSON file found in ZIP")


def convert_dayone_to_csv(input_path: Path, output_path: Path) -> None:
    """
    Convert Day One export to Reflection.App CSV.

    Args:
        input_path: Path to JSON or ZIP file
        output_path: Path to output CSV file
    """
    # Load JSON data
    if input_path.suffix.lower() == '.zip':
        print(f"Extracting Journal.json from {input_path.name}...")
        data = load_json_from_zip(input_path)
    elif input_path.suffix.lower() == '.json':
        print(f"Loading {input_path.name}...")
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        raise ValueError(f"Unsupported file type: {input_path.suffix}")

    # Extract entries
    entries = extract_entries_from_json(data)
    if not entries:
        print("Error: No entries found in export", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(entries)} entries")

    # Convert entries
    rows = [convert_entry(entry) for entry in entries]

    # Write CSV
    fieldnames = ['text', 'type', 'date', 'platform', 'source_id', 'tags', 'created_at']
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
    parser.add_argument('input', type=Path, help='Day One export (JSON or ZIP)')
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
