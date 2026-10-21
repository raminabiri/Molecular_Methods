#!/usr/bin/env python3
"""Insert a '> راهنمایی: …' line under each numbered question of an assessment file.

Questions start with **N.** (Persian or Latin digits). The hint goes after the
question's paragraph (before the next blank line). Existing hints are replaced.
Usage: python3 _tools/add_hints.py 04_Assessment.md hints.json
hints.json: {"1": "…", "2": "…"}
"""
import json, re, sys

FA = str.maketrans('۰۱۲۳۴۵۶۷۸۹', '0123456789')
path, hints = sys.argv[1], json.load(open(sys.argv[2], encoding='utf-8'))
lines = open(path, encoding='utf-8').read().split('\n')
out, i, used = [], 0, set()
while i < len(lines):
    line = lines[i]
    m = re.match(r'^\*\*([۰-۹0-9]+)\.\*\*', line)
    if not m:
        out.append(line); i += 1; continue
    n = m.group(1).translate(FA)
    while i < len(lines) and lines[i].strip() != '':
        out.append(lines[i]); i += 1
    # drop an old hint block
    j = i
    while j < len(lines) and lines[j].strip() == '':
        j += 1
    if j < len(lines) and lines[j].startswith('> راهنمایی'):
        i = j + 1
    if n in hints:
        out += ['', '> راهنمایی: ' + hints[n]]
        used.add(n)
missing = set(hints) - used
if missing:
    sys.exit(f'hints with no question: {sorted(missing)}')
open(path, 'w', encoding='utf-8').write('\n'.join(out))
