from pathlib import Path
import tempfile
import unittest

from update_table import update_table


class UpdateTableTests(unittest.TestCase):
    def test_add_update_delete_and_repeat(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "codes").mkdir()
            (root / "explanations").mkdir()
            table = root / "table.md"
            table.write_text(
                "Intro\n\n| Problem Number | Title | Solved | Explained |\n|---|---|---|---|\n"
                "| [0002](codes/0001.py) | [Two](https://leetcode.com/problems/two/) | ⏱️ | ❌ |\n"
                "| [0003](codes/0003.py) | [Three](https://leetcode.com/problems/three/) | 💥 | ✅ |\n"
                "\nFooter\n", encoding="utf-8")
            one = root / "codes/0001.py"
            one.write_text("# https://leetcode.com/problems/one/description/\n# Alternative: TLE\n", encoding="utf-8")
            (root / "codes/0002.py").write_text("# https://leetcode.com/problems/two/", encoding="utf-8")
            explanation = root / "explanations/0001.md"
            explanation.write_text("# Solution 1 - One", encoding="utf-8")
            update_table(root)
            result = table.read_text(encoding="utf-8")
            self.assertIn("| [0001](codes/0001.py) | [One](https://leetcode.com/problems/one/) | ✅ | ✅ |", result)
            self.assertIn("| [0002](codes/0002.py) | [Two](https://leetcode.com/problems/two/) | ⏱️ | ❌ |", result)
            self.assertNotIn("0003", result)
            self.assertTrue(result.startswith("Intro\n"))
            self.assertTrue(result.endswith("\nFooter\n"))
            update_table(root)
            self.assertEqual(result, table.read_text(encoding="utf-8"))
            one.write_text("# https://leetcode.com/problems/new-one/\n# Status: MLE\n", encoding="utf-8")
            explanation.unlink()
            update_table(root)
            self.assertIn("[New One](https://leetcode.com/problems/new-one/) | 💥 | ❌", table.read_text(encoding="utf-8"))
            one.unlink()
            explanation.write_text("# Solution 1 - One", encoding="utf-8")
            update_table(root)
            self.assertIn("| 0001 | [New One](https://leetcode.com/problems/new-one/) | ❌ | ✅", table.read_text(encoding="utf-8"))
            (root / "explanations/0004.md").write_text("# Solution 4 - Four", encoding="utf-8")
            update_table(root)
            self.assertIn("| 0004 | Four | ❌ | ✅ |", table.read_text(encoding="utf-8"))

    def test_missing_url_does_not_overwrite_table(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "codes").mkdir()
            (root / "explanations").mkdir()
            (root / "codes/0001.py").write_text("class Solution: pass")
            table = root / "table.md"
            original = "| Problem Number | Title | Solved | Explained |\n|---|---|---|---|\n"
            table.write_text(original)
            with self.assertRaisesRegex(ValueError, "LeetCode problem URL"):
                update_table(root)
            self.assertEqual(original, table.read_text())


if __name__ == "__main__":
    unittest.main()
