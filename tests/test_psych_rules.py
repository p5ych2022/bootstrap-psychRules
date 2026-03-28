from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
INIT_SCRIPT = REPO_ROOT / "scripts" / "init_psych_rules.py"
MEMORY_SCRIPT = REPO_ROOT / "scripts" / "new_memory_entry.py"


class PsychRulesScriptsTest(unittest.TestCase):
    def run_script(self, script: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(script), *args],
            check=True,
            capture_output=True,
            text=True,
        )

    def test_init_scaffolds_session_and_index_protocol(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / ".gitignore").write_text("node_modules/\n", encoding="utf-8")

            self.run_script(INIT_SCRIPT, "--root", str(root))

            psych_dir = root / ".psychRules"
            self.assertTrue((psych_dir / "session.md").exists())
            self.assertTrue((psych_dir / "memory" / "index.md").exists())

            agents_text = (root / "AGENTS.md").read_text(encoding="utf-8")
            self.assertIn("session.md", agents_text)
            self.assertIn("memory/index.md", agents_text)
            self.assertIn("Do not read every file in `.psychRules/memory/` by default.", agents_text)

    def test_new_memory_entry_mentions_session_and_index_sync(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / ".gitignore").write_text(".venv/\n", encoding="utf-8")

            self.run_script(INIT_SCRIPT, "--root", str(root))
            self.run_script(
                MEMORY_SCRIPT,
                "--root",
                str(root),
                "--kind",
                "fix",
                "--title",
                "repair cache merge bug",
            )

            memory_files = sorted(
                path
                for path in (root / ".psychRules" / "memory").glob("fix*.md")
                if path.name != "index.md"
            )
            self.assertEqual(len(memory_files), 1)

            memory_text = memory_files[0].read_text(encoding="utf-8")
            self.assertIn("memory/index.md", memory_text)
            self.assertIn("session.md", memory_text)


if __name__ == "__main__":
    unittest.main()
