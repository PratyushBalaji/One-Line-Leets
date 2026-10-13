"""Sync CSV from filenames and render Markdown with no dependencies."""
import csv
import io
from pathlib import Path
import re

FIELDS = ['number', 'title', 'url', 'solved', 'explained']
EMOJI = {'SOLVED': '✅', 'UNSOLVED': '❌', 'TLE': '⏱️', 'MLE': '💥',
         'EXPLAINED': '✅', 'UNEXPLAINED': '❌'}
MINOR = set('a an the and but or nor for as at by from in into of on onto per to via with'.split())
ACRONYMS = {'xor': 'XOR', '1d': '1D', '2d': '2D', 'i': 'I', 'ii': 'II', 'iii': 'III', 'iv': 'IV'}
INTRO = '''# What You'll Find in this Repository :

Below is a table indicating problems I've solved and explained in one line out of all the files I've uploaded to this repository. The problem title is a link to the problem for you to try it out yourself.

My solutions can be found under `codes/` named `<problem-number>.py` or by clicking on each "Problem Number" below. Explanations if present are under `explanations/` named `<problem-number>.md`.

(Note : the problem numbers are 0-padded to be 4 digits long)

**Legend :**
- ✅ Complete
- ❌ Incomplete
- ⏱️ Time Limit Exceeded
- 💥 Memory Limit Exceeded

'''


def title_case(text):
    words = text.split()
    return ' '.join(ACRONYMS.get(word.lower(), word.lower() if 0 < i < len(words) - 1
                                and word.lower() in MINOR else word.title())
                    for i, word in enumerate(words))


def markdown_cells(row, codes):
    number = row['number']
    title = row['title'].replace('|', r'\|')
    return [f'[{number}](codes/{number}.py)' if number in codes else number,
            f"[{title}]({row['url']})", EMOJI[row['solved']], EMOJI[row['explained']]]


def update_table(root):
    codes = {p.stem: p for p in (root / 'codes').glob('*.py') if re.fullmatch(r'\d{4}', p.stem)}
    explanations = {p.stem for p in (root / 'explanations').glob('*.md') if re.fullmatch(r'\d{4}', p.stem)}
    missing = explanations - codes.keys()
    if missing:
        raise ValueError('Explanations need matching code: ' + ', '.join(sorted(missing)))

    csv_path, md_path = root / 'table.csv', root / 'table.md'
    original_csv = csv_path.read_text(encoding='utf-8')
    reader = csv.DictReader(io.StringIO(original_csv))
    rows = {}
    for row in reader:
        number = row['number']
        if not re.fullmatch(r'\d{4}', number) or number in rows:
            raise ValueError(f'Invalid or duplicate problem number: {number}')
        rows[number] = row
    before = {number: row.copy() for number, row in rows.items()}

    for number, path in codes.items():
        url = re.search(r'^\s*#.*?(https://leetcode\.com/problems/([a-z0-9-]+))(?:/|\s|$)',
                        path.read_text(encoding='utf-8'), re.MULTILINE)
        if url is None:
            raise ValueError(f'codes/{number}.py needs a commented LeetCode problem URL')
        if number not in rows:
            rows[number] = dict(zip(FIELDS, [number, title_case(url.group(2).replace('-', ' ')),
                                           url.group(1) + '/', 'SOLVED', 'UNEXPLAINED']))
        rows[number]['url'] = url.group(1) + '/'
    for number, row in rows.items():
        if number not in codes:
            row['solved'] = 'UNSOLVED'
        elif row['solved'] not in {'MLE', 'TLE'}:
            row['solved'] = 'SOLVED'
        row['explained'] = 'EXPLAINED' if number in explanations else 'UNEXPLAINED'

    rows = dict(sorted(rows.items(), key=lambda item: int(item[0])))
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=FIELDS, lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows.values())
    result_csv = buffer.getvalue()
    rendered = {number: markdown_cells(row, codes) for number, row in rows.items()}
    table = [['Problem Number', 'Problem Title (Leetcode Redirect)', 'Solved', 'Explained'], *rendered.values()]
    widths = [max(len(row[i]) for row in table) for i in range(4)]
    lines = ['| ' + ' | '.join(cell.ljust(width) for cell, width in zip(row, widths)) + ' |'
             for row in table]
    lines.insert(1, '| ' + ' | '.join('-' * width for width in widths) + ' |')
    result_md = INTRO + '\n'.join(lines) + '\n'
    original_md = md_path.read_text(encoding='utf-8')
    if original_csv == result_csv and original_md == result_md:
        return []

    old_rendered = {}
    for line in original_md.splitlines():
        if not line.startswith('|'):
            continue
        cells = [cell.strip() for cell in re.split(r'(?<!\\)\|', line)[1:-1]]
        if len(cells) == 4:
            number = re.match(r'(?:\[)?(\d{4})', cells[0])
            if number:
                old_rendered[number.group(1)] = cells
    changed = sorted(number for number in rows.keys() | old_rendered.keys()
                     if before.get(number) != rows.get(number)
                     or old_rendered.get(number) != rendered.get(number))
    # Finish validation and rendering before writing either file.
    if original_csv != result_csv:
        csv_path.write_text(result_csv, encoding='utf-8', newline='\n')
    if original_md != result_md:
        md_path.write_text(result_md, encoding='utf-8', newline='\n')
    return changed or list(rows)


if __name__ == '__main__':
    changed = update_table(Path(__file__).resolve().parents[1])
    if changed:
        print('table: update ' + ', '.join(changed))
