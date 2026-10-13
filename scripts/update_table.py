"""Synchronize table.md with solution and explanation files, without running them."""

from pathlib import Path
import re


PROBLEM_URL = re.compile(r"https://leetcode\.com/problems/([a-z0-9-]+)")
STATUSES = {"AC": "✅", "WA": "❌", "TLE": "⏱️", "MLE": "💥"}


def update_table(root):
    table = root / "table.md"
    original = table.read_text(encoding="utf-8")
    lines = original.splitlines(keepends=True)
    start = next(i for i, line in enumerate(lines) if line.startswith("| Problem Number")) + 2
    end = start
    existing = {}
    while end < len(lines) and lines[end].startswith("|"):
        cells = [cell.strip() for cell in lines[end].strip().strip("|").split("|")]
        if len(cells) != 4:
            raise ValueError(f"Invalid table row: {lines[end]}")
        number = re.fullmatch(r"\[(\d{4})\]\(codes/\d{4}\.py\)|\d{4}", cells[0])
        if number is None:
            raise ValueError(f"Invalid table row: {lines[end]}")
        existing[number.group(1) or number.group(0)] = (cells, lines[end])
        end += 1

    codes = {p.stem: p for p in (root / "codes").glob("*.py") if re.fullmatch(r"\d{4}", p.stem)}
    explanations = {p.stem: p for p in (root / "explanations").glob("*.md") if re.fullmatch(r"\d{4}", p.stem)}
    rows = []
    for number in sorted(codes.keys() | explanations.keys()):
        previous, raw = existing.get(number, ([number, "", "❌", "❌"], ""))
        title = previous[1]
        solved = "❌"
        if number in codes:
            content = codes[number].read_text(encoding="utf-8")
            url = PROBLEM_URL.search(content)
            if url is None:
                raise ValueError(f"codes/{number}.py needs a LeetCode problem URL")
            slug = url.group(1)
            old_url = PROBLEM_URL.search(title)
            if old_url is None or old_url.group(1) != slug:
                title = f"[{slug.replace('-', ' ').title()}](https://leetcode.com/problems/{slug}/)"
            solved = previous[2] if previous[0].startswith("[") else "✅"
            status = re.search(r"^#\s*Status:\s*(\w+)\s*$", content, re.MULTILINE)
            if status:
                solved = STATUSES[status.group(1)]
        if not title:
            heading = explanations[number].read_text(encoding="utf-8").splitlines()[0]
            match = re.fullmatch(r"# Solution \d+ - (.+)", heading)
            if match is None:
                raise ValueError(f"explanations/{number}.md needs a '# Solution N - Title' heading")
            title = match.group(1)
        cells = [f"[{number}](codes/{number}.py)" if number in codes else number,
                 title, solved, "✅" if number in explanations else "❌"]
        rows.append(raw if cells == previous else "| " + " | ".join(cells) + " |\n")

    result = "".join(lines[:start] + rows + lines[end:])
    if result != original:
        table.write_text(result, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    update_table(Path(__file__).resolve().parents[1])
