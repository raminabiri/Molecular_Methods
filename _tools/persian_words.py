#!/usr/bin/env python3
"""Apply the safe word replacements of STYLE_GUIDE §6 and list the ones that need a human.

Only replaces outside code (fenced blocks and `inline code`) and outside URLs.
Usage: python3 _tools/persian_words.py FILE.md [...]
"""
import re
import sys

SAFE = [
    (r'نمی[‌ ]?باشند', 'نیستند'),
    (r'نمی[‌ ]?باشد', 'نیست'),
    (r'(?<![\w‌])می[‌ ]?باشند', 'هستند'),
    (r'(?<![\w‌])می[‌ ]?باشد', 'است'),
    (r'مثلاً|مثلا(?![\w])', 'برای نمونه'),
    (r'معمولاً|معمولا(?![\w])', 'در بسیاری از موارد'),
    (r'علناً|علنا(?![\w])', 'آشکارا'),
    (r'(?<![\w‌])مختلف(?![\w])', 'گوناگون'),
    (r'(?<![\w‌])سؤال|(?<![\w‌])سوال', 'پرسش'),
    (r'(?<![\w‌])جواب', 'پاسخ'),
    (r'(?<![\w‌])فقط(?![\w])', 'تنها'),
    (r'(?<![\w‌])مثل(?![\w‌])', 'مانند'),
    (r'دستور[ ‌]?العمل‌?ها', 'روش‌های کار'),
    (r'دستور[ ‌]?العمل', 'روش کار'),
]
MANUAL = (r'مثال|استفاده|حتماً|حتما(?![\w])|عملیات|عملی(?![\w])|عملاً|(?<![\w‌])عمل(?![\w])|'
          r'تقریباً|(?<![\w‌])مشخص')
PROTECT = re.compile(r'(```.*?```|~~~.*?~~~|`[^`\n]*`|https?://\S+|\]\([^)]*\))', re.S)

report = '--report' in sys.argv
for path in [a for a in sys.argv[1:] if not a.startswith('--')]:
    src = open(path, encoding='utf-8').read()
    parts = PROTECT.split(src)
    for i in range(0, len(parts), 2):  # even indexes = prose
        for pat, rep in SAFE:
            parts[i] = re.sub(pat, rep, parts[i])
    new = ''.join(parts)
    if new != src:
        open(path, 'w', encoding='utf-8').write(new)
    if report:
        prose = PROTECT.sub('', new)
        for line in prose.split('\n'):
            for m in re.finditer(MANUAL, line):
                print(f'{path}: manual: …{line[max(0, m.start()-25):m.end()+25]}…')
