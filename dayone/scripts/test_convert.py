#!/usr/bin/env python3
"""
Tests for the Day One -> Reflection.App converter.

Stdlib only (unittest), matching the converter's no-dependency policy.
Run: python -m unittest test_convert -v   (or: python test_convert.py)
"""
import csv
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

import convert


def _journal(entries):
    return {"metadata": {"version": "1.0"}, "entries": entries}


def _entry(uuid, text="hello", date="2024-01-01T00:00:00Z", **extra):
    e = {"uuid": uuid, "text": text, "creationDate": date}
    e.update(extra)
    return e


class TagBuildingTest(unittest.TestCase):
    def _tags(self, entry, journal=None):
        if journal is not None:
            entry = {**entry, "__journal__": journal}
        return convert.convert_entry(entry)["tags"]

    def test_journal_name_first_source_last(self):
        tags = self._tags(_entry("1", tags=["wisdom"]), journal="Journal")
        self.assertEqual(tags, "Journal,wisdom,DayOne")

    def test_journal_named_journal_is_not_suppressed(self):
        # Regression: the old code dropped the tag when the journal was
        # literally named "Journal", leaving most entries untagged.
        tags = self._tags(_entry("1"), journal="Journal")
        self.assertEqual(tags, "Journal,DayOne")

    def test_source_tag_added_even_without_journal(self):
        # Standalone .json path injects no __journal__.
        self.assertEqual(self._tags(_entry("1")), "DayOne")

    def test_multiple_entry_tags_preserved_in_order(self):
        tags = self._tags(_entry("1", tags=["a", "b", "c"]), journal="Highlights")
        self.assertEqual(tags, "Highlights,a,b,c,DayOne")

    def test_comma_in_journal_name_does_not_split(self):
        tags = self._tags(_entry("1", tags=["cardio"]), journal="Health, Fitness")
        self.assertEqual(tags, "Health Fitness,cardio,DayOne")
        # Downstream comma-split yields clean tags (no stray fragments).
        self.assertEqual(tags.split(","), ["Health Fitness", "cardio", "DayOne"])

    def test_comma_in_entry_tag_does_not_split(self):
        tags = self._tags(_entry("1", tags=["a,b"]), journal="J")
        self.assertEqual(tags, "J,a b,DayOne")

    def test_string_tags_are_not_exploded_into_chars(self):
        # Regression: list("vacation") used to produce v,a,c,a,t,i,o,n.
        tags = self._tags(_entry("1", tags="vacation"), journal="Trips")
        self.assertEqual(tags, "Trips,vacation,DayOne")

    def test_duplicate_tags_deduped_case_insensitively(self):
        tags = self._tags(_entry("1", tags=["DayOne", "Travel"]), journal="Travel")
        self.assertEqual(tags, "Travel,DayOne")

    def test_capitalized_tags_key_supported(self):
        tags = self._tags({"uuid": "1", "text": "x", "CreationDate": "2024-01-01T00:00:00Z",
                            "Tags": ["foo"], "__journal__": "J"})
        self.assertEqual(tags, "J,foo,DayOne")


class ZipLoadingTest(unittest.TestCase):
    def _convert_zip(self, members):
        tmp = Path(tempfile.mkdtemp())
        zpath = tmp / "export.zip"
        with zipfile.ZipFile(zpath, "w") as z:
            for name, content in members.items():
                if isinstance(content, (dict, list)):
                    z.writestr(name, json.dumps(content))
                else:
                    z.writestr(name, content)
        out = tmp / "out.csv"
        convert.convert_dayone_to_csv(zpath, out)
        with open(out, newline='', encoding='utf-8') as f:
            return list(csv.DictReader(f))

    def test_all_journals_loaded_and_tagged(self):
        rows = self._convert_zip({
            "Daily.json": _journal([_entry("D1")]),
            "Highlights.json": _journal([_entry("H1", tags=["work"])]),
            "Journal.json": _journal([_entry("J1"), _entry("J2")]),
            "Lowlights.json": _journal([_entry("L1")]),
            "photos/img.jpg": b"\xff\xd8\xff\xe0not-json",
        })
        by_id = {r["source_id"]: r["tags"] for r in rows}
        self.assertEqual(len(rows), 5)
        self.assertEqual(by_id["D1"], "Daily,DayOne")
        self.assertEqual(by_id["H1"], "Highlights,work,DayOne")
        self.assertEqual(by_id["J1"], "Journal,DayOne")      # not suppressed
        self.assertEqual(by_id["J2"], "Journal,DayOne")
        self.assertEqual(by_id["L1"], "Lowlights,DayOne")

    def test_macosx_sidecars_skipped_without_phantom_journal(self):
        rows = self._convert_zip({
            "Highlights.json": _journal([_entry("H1")]),
            "__MACOSX/._Highlights.json": b"\x00\x05\x16\x07garbage",
        })
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["tags"], "Highlights,DayOne")
        # No "._Highlights" journal tag leaked in.
        self.assertNotIn("._Highlights", rows[0]["tags"])

    def test_one_bad_file_does_not_abort_whole_import(self):
        # Bad.json parses as JSON but its entries are not objects.
        rows = self._convert_zip({
            "Good.json": _journal([_entry("G1")]),
            "Bad.json": ["just", "strings", "not dicts"],
        })
        ids = {r["source_id"] for r in rows}
        self.assertIn("G1", ids)
        self.assertEqual(rows[0]["tags"], "Good,DayOne")

    def test_unparseable_file_skipped(self):
        rows = self._convert_zip({
            "Good.json": _journal([_entry("G1")]),
            "Broken.json": "{ not valid json ",
        })
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["source_id"], "G1")


class JsonPathTest(unittest.TestCase):
    def test_standalone_json_gets_source_tag_only(self):
        tmp = Path(tempfile.mkdtemp())
        jpath = tmp / "export.json"
        jpath.write_text(json.dumps(_journal([_entry("X1", tags=["mood"])])), encoding='utf-8')
        out = tmp / "out.csv"
        convert.convert_dayone_to_csv(jpath, out)
        with open(out, newline='', encoding='utf-8') as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(rows[0]["tags"], "mood,DayOne")


if __name__ == "__main__":
    unittest.main(verbosity=2)
