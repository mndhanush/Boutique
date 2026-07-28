import os
import glob
import re

directory = r'd:\GrowwPark projects\Bloom'
html_files = glob.glob(os.path.join(directory, '*.html'))

def replace_root(match):
    root_content = match.group(0)
    root_content = root_content.replace('--bg-color: #050505;', '--bg-color: #FFFFFF;')
    root_content = root_content.replace('--bg-alt: #0A0A0A;', '--bg-alt: #F9F6F0;')
    root_content = root_content.replace('--card-bg: #111111;', '--card-bg: #FFFFFF;')
    root_content = root_content.replace('--text-main: #CCCCCC;', '--text-main: #333333;')
    root_content = root_content.replace('--text-heading: #FFFFFF;', '--text-heading: #000000;')
    root_content = root_content.replace('--navbar-bg: #000000;', '--navbar-bg: #FFFFFF;')
    root_content = root_content.replace('--border-color: #333333;', '--border-color: #E5E5E5;')
    return root_content

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # regex to find :root { ... }
    content = re.sub(r':root\s*\{[^}]*\}', replace_root, content, count=1)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f'Updated {len(html_files)} HTML files.')
