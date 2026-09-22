"""Exercise the preview guardrails using a disposable Git repository (no network)."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

PHP = sys.argv.pop(1) if len(sys.argv) > 1 else "php"
SCRIPT = Path(__file__).with_name("preview.php")
SOURCE = b"""<?php
// oldName and $oldVar in prose are not symbol tokens.
class Example {
    public static function oldName($oldVar) { return $oldVar; }
}
Example::oldName('oldName');
$data = ['oldName' => '$oldVar'];
"""


class PreviewTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / "demo"
        self.repo.mkdir()
        self.git("init", "-q")
        (self.repo / "example.php").write_bytes(SOURCE)
        self.git("add", "example.php")
        self.git("-c", "user.name=Preview Fixture", "-c", "user.email=fixture@example.invalid",
                 "-c", "commit.gpgsign=false", "commit", "-qm", "fixture")
        revision = self.git("rev-parse", "HEAD").strip()
        self.manifest = {
            "version": 1, "repositories": {"demo": revision}, "guards": [],
            "files": [{"repository": "demo", "path": "example.php",
                       "sha256": hashlib.sha256(SOURCE).hexdigest(), "tokens": [
                           {"kind": "T_STRING", "from": "oldName", "to": "old_name", "count": 2},
                           {"kind": "T_VARIABLE", "from": "$oldVar", "to": "$old_var", "count": 2}]}]}

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.repo), *args], text=True)

    def run_preview(self, manifest=None, output=None):
        path = self.root / "manifest.json"
        path.write_text(json.dumps(self.manifest if manifest is None else manifest))
        return subprocess.run([PHP, str(SCRIPT), str(path), str(self.root),
                               str(output or self.root / "output")], text=True, capture_output=True)

    def test_exact_tokens_preserve_data_comments_and_worktree(self):
        # The worktree is intentionally different: preview reads the recorded commit.
        (self.repo / "example.php").write_text("uncommitted work\n")
        result = self.run_preview()
        self.assertEqual(0, result.returncode, result.stderr)
        expected = SOURCE.replace(b"function oldName($oldVar) { return $oldVar; }",
                                  b"function old_name($old_var) { return $old_var; }")
        expected = expected.replace(b"Example::oldName(", b"Example::old_name(")
        self.assertEqual(expected, (self.root / "output/demo/example.php").read_bytes())
        self.assertEqual("uncommitted work\n", (self.repo / "example.php").read_text())

    def test_bad_hash_and_counts_fail_before_output(self):
        for field, value in [("sha256", "0" * 64), ("count", 99)]:
            with self.subTest(field=field):
                manifest = copy.deepcopy(self.manifest)
                target = manifest["files"][0]
                if field == "count":
                    target = target["tokens"][0]
                target[field] = value
                self.assertNotEqual(0, self.run_preview(manifest).returncode)
                self.assertFalse((self.root / "output").exists())

    def test_existing_output_is_never_overwritten(self):
        output = self.root / "output"
        output.mkdir()
        (output / "marker").write_text("keep")
        self.assertNotEqual(0, self.run_preview().returncode)
        self.assertEqual("keep", (output / "marker").read_text())

    def test_output_inside_input_repository_is_rejected(self):
        self.assertNotEqual(0, self.run_preview(output=self.repo / "output").returncode)
        self.assertFalse((self.repo / "output").exists())

    def test_path_traversal_is_rejected(self):
        self.manifest["files"][0]["path"] = "../escape.php"
        self.assertNotEqual(0, self.run_preview().returncode)
        self.assertFalse((self.root / "output").exists())

    def test_destination_collision_is_rejected(self):
        self.manifest["files"][0]["tokens"][1]["to"] = "$data"
        self.assertNotEqual(0, self.run_preview().returncode)
        self.assertFalse((self.root / "output").exists())

    def test_reviewed_embedded_code_literal_only(self):
        # Explicit literal edits are separate from token renames and require a reason/count.
        self.manifest["files"][0]["literals"] = [
            {"from": "['oldName' => '$oldVar']", "to": "['oldName' => 'kept-data']",
             "count": 1, "reason": "Synthetic literal-path test, not an API rename."}]
        self.assertEqual(0, self.run_preview().returncode)
        self.assertIn("['oldName' => 'kept-data']", (self.root / "output/demo/example.php").read_text())


if __name__ == "__main__":
    unittest.main()
