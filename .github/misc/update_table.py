"""Update problem statuses, the Markdown table, and the stats card."""
import csv
import io
import json
import math
from html import escape
from pathlib import Path
import re
from urllib.request import Request, urlopen

FIELDS = ['number', 'solved', 'explained']
EMOJI = {'SOLVED': '✅', 'UNSOLVED': '❌', 'TLE': '⏱️', 'MLE': '💥',
         'EXPLAINED': '✅', 'UNEXPLAINED': '❌'}
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


def stats_svg(rows, problems):
    catalog = sorted(problems.items(), key=lambda item: int(item[0]))
    columns, pitch, size = 114, 5, 4
    section_height = math.ceil(len(catalog) / columns) * pitch - (pitch - size)
    map_width = columns * pitch - (pitch - size)
    width, circle_width, cats_width = 1000, 176, 108
    gap = (width - circle_width - cats_width - map_width) / 4
    height = section_height + 2 * gap
    cx = cy = gap + circle_width / 2
    cats_x = 2 * gap + circle_width
    map_x = 3 * gap + circle_width + cats_width
    totals = [sum(p['difficulty']['level'] == level for p in problems.values()) for level in (1, 2, 3)]
    solved = [sum(row['solved'] == 'SOLVED' and problems[number]['difficulty']['level'] == level
                  for number, row in rows.items()) for level in (1, 2, 3)]
    explained = sum(row['explained'] == 'EXPLAINED' for row in rows.values())
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height:g}" viewBox="0 0 {width} {height:g}" role="img" aria-labelledby="title desc">',
             '<title id="title">One-line LeetCode solutions</title>',
             f'<desc id="desc">{sum(solved)} of {sum(totals)} solved. Easy {solved[0]}/{totals[0]}, Medium {solved[1]}/{totals[1]}, Hard {solved[2]}/{totals[2]}. {explained} explained.</desc>',
             f'<rect width="{width}" height="{height:g}" rx="14" fill="#262626"/>',
             '<g font-family="Helvetica, Arial, sans-serif" text-anchor="middle">']
    cat_gap = 10
    cat_height = (section_height - 2 * cat_gap) / 3
    colors = {1: ('#1cbaba', '#283737'), 2: ('#ffb800', '#3a3426'), 3: ('#f63737', '#3a2929')}
    for i, (label, background) in enumerate([('Easy', '#234747'), ('Medium', '#58491f'), ('Hard', '#572b2b')]):
        color = colors[i + 1][0]
        start, end = math.radians(135 + i * 90), math.radians(219 + i * 90)
        radius = 85
        x1, y1 = cx + radius * math.cos(start), cy + radius * math.sin(start)
        x2, y2 = cx + radius * math.cos(end), cy + radius * math.sin(end)
        path = f'M {x1:.3f} {y1:.3f} A {radius} {radius} 0 0 1 {x2:.3f} {y2:.3f}'
        parts.append(f'<path d="{path}" fill="none" stroke="{background}" stroke-width="6" stroke-linecap="round"/>')
        length = radius * (end - start)
        if solved[i]:
            progress = length * solved[i] / totals[i]
            parts.append(f'<path d="{path}" fill="none" stroke="{color}" stroke-width="6" stroke-linecap="round" stroke-dasharray="{progress:.4f} {length:.4f}"/>')
        y = gap + i * (cat_height + cat_gap)
        parts.extend([f'<rect x="{cats_x:g}" y="{y:g}" width="{cats_width}" height="{cat_height:g}" rx="7" fill="#333333"/>',
                      f'<text x="{cats_x + cats_width / 2:g}" y="{y + cat_height / 2 - 5:g}" fill="{color}" font-size="14.5">{label}</text>',
                      f'<text x="{cats_x + cats_width / 2:g}" y="{y + cat_height / 2 + 16:g}" fill="#f2f2f2" font-size="15.3">{solved[i]}/{totals[i]}</text>'])
    parts.extend([f'<text x="{cx:g}" y="{cy - 8:g}" fill="#f5f5f5"><tspan font-size="36.5">{sum(solved)}</tspan><tspan font-size="17">/{sum(totals)}</tspan></text>',
                  f'<text x="{cx:g}" y="{cy + 18:g}" fill="#f5f5f5" font-size="17.8"><tspan fill="#00b333">✓ </tspan>one-liners</text>',
                  f'<text x="{cx:g}" y="{gap + section_height - 4:g}" fill="#a6a6a6" font-size="15.3">{explained} Explained</text>',
                  '</g>', '<g id="problem-map">'])
    for i, (number, problem) in enumerate(catalog):
        level = problem['difficulty']['level']
        status = rows.get(number, {}).get('solved', 'UNSOLVED')
        color = colors[level][0 if status == 'SOLVED' else 1]
        x, y = map_x + (i % columns) * pitch, gap + (i // columns) * pitch
        label = escape(f"{number}: {problem['stat']['question__title']} — {('Easy', 'Medium', 'Hard')[level - 1]} — {status}")
        parts.append(f'<rect x="{x:g}" y="{y:g}" width="{size}" height="{size}" fill="{color}"><title>{label}</title></rect>')
    parts.append('</g></svg>')
    return '\n'.join(parts) + '\n'


def update_table(root, data):
    misc = root / '.github/misc'
    codes = {p.stem: p for p in (root / 'codes').glob('*.py') if re.fullmatch(r'\d{4}', p.stem)}
    explanations = {p.stem for p in (root / 'explanations').glob('*.md') if re.fullmatch(r'\d{4}', p.stem)}
    if missing := explanations - codes.keys():
        raise ValueError('Explanations need matching code: ' + ', '.join(sorted(missing)))
    problems = {str(p['stat']['frontend_question_id']).zfill(4): p
                for p in data['stat_status_pairs'] if not p['stat']['question__hide']}
    if not problems or any(p['difficulty']['level'] not in (1, 2, 3) for p in problems.values()):
        raise ValueError('Invalid API problem list')
    csv_path = misc / 'table.csv'
    with csv_path.open(encoding='utf-8') as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != FIELDS:
            raise ValueError(f'CSV columns must be {FIELDS}')
        rows = {}
        for row in reader:
            number = row['number']
            if (not re.fullmatch(r'\d{4}', number) or number in rows
                    or row['solved'] not in {'SOLVED', 'UNSOLVED', 'TLE', 'MLE'}
                    or row['explained'] not in {'EXPLAINED', 'UNEXPLAINED'}):
                raise ValueError(f'Invalid or duplicate CSV row: {row}')
            rows[number] = row
    before = {number: row.copy() for number, row in rows.items()}
    for number, path in codes.items():
        if number not in rows:
            slug = problems[number]['stat']['question__title_slug']
            if not re.search(r'https://leetcode\.com/problems/' + re.escape(slug) + r'(?:/|\s|$)',
                             path.read_text(encoding='utf-8')):
                raise ValueError(f'codes/{number}.py does not contain the expected problem URL: {slug}')
            rows[number] = dict(number=number, solved='SOLVED', explained='UNEXPLAINED')
    for number, row in rows.items():
        if number not in codes:
            row['solved'] = 'UNSOLVED'
        elif row['solved'] not in {'TLE', 'MLE'}:
            row['solved'] = 'SOLVED'
        row['explained'] = 'EXPLAINED' if number in explanations else 'UNEXPLAINED'
    rows = dict(sorted(rows.items(), key=lambda item: int(item[0])))
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=FIELDS, lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows.values())
    rendered = {}
    for number, row in rows.items():
        metadata = problems[number]
        problem = metadata['stat']
        title = problem['question__title'].replace('|', r'\|')
        url = 'https://leetcode.com/problems/' + problem['question__title_slug'] + '/'
        rendered[number] = [f'[{number}](codes/{number}.py)' if number in codes else number,
                            f'[{title}]({url})', ('Easy', 'Medium', 'Hard')[metadata['difficulty']['level'] - 1],
                            EMOJI[row['solved']], EMOJI[row['explained']]]
    table = [['Problem Number', 'Problem Title (Leetcode Redirect)', 'Difficulty', 'Solved', 'Explained'], *rendered.values()]
    widths = [max(len(row[i]) for row in table) for i in range(len(table[0]))]
    lines = ['| ' + ' | '.join(cell.ljust(width) for cell, width in zip(row, widths)) + ' |' for row in table]
    lines.insert(1, '| ' + ' | '.join('-' * width for width in widths) + ' |')
    md_path = root / 'table.md'
    old_rendered = {}
    for line in md_path.read_text(encoding='utf-8').splitlines():
        if line.startswith('|'):
            cells = [cell.strip() for cell in re.split(r'(?<!\\)\|', line)[1:-1]]
            if len(cells) in (4, 5) and (match := re.match(r'(?:\[)?(\d{4})', cells[0])):
                old_rendered[match.group(1)] = cells
    changed = sorted(number for number in rows.keys() | old_rendered.keys()
                     if rows.get(number) != before.get(number) or rendered.get(number) != old_rendered.get(number))
    outputs = {csv_path: buffer.getvalue(), md_path: INTRO + '\n'.join(lines) + '\n',
               misc / 'stats.svg': stats_svg(rows, problems)}
    # Validate and render everything before changing any files.
    dirty = {path: text for path, text in outputs.items()
             if not path.exists() or path.read_text(encoding='utf-8') != text}
    for path, text in dirty.items():
        path.write_text(text, encoding='utf-8', newline='\n')
    return changed or (list(rows) if dirty else [])


if __name__ == '__main__':
    request = Request('https://leetcode.com/api/problems/all/', headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(request, timeout=30) as response:
        data = json.load(response)
    changed = update_table(Path(__file__).resolve().parents[2], data)
    if changed:
        print('table: update ' + ', '.join(changed))
