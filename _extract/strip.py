#!/usr/bin/env python3
"""Strip HTML tags from xhtml files to plain text."""
import re, sys, html

for fn in sys.argv[1:]:
    with open(fn, 'r', encoding='utf-8') as f:
        s = f.read()
    # normalize line breaks
    s = re.sub(r'</p>|</div>|</h[1-6]>|</li>|</br\s*/?>', '\n', s)
    s = re.sub(r'<br\s*/?>', '\n', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s)
    s = re.sub(r'\n{3,}', '\n\n', s)
    s = s.strip()
    print(s)
    print('\n--- END ---\n')
