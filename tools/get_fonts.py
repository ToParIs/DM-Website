import json
import re

with open('tools/wix_viewer_model.json', 'r', encoding='utf-8') as f:
    text = f.read()

# Search for font keywords
fonts = set(re.findall(r'font-family[:=][^;,\"\']+', text, re.IGNORECASE))
print("Font families found in wix_viewer_model.json:")
for fn in sorted(fonts):
    print(" ", fn)

# Check if there are font links in the original HTML
with open('tools/dump_viewer_model.py', 'r') as f:
    pass

import requests
r = requests.get('https://www.dahlmarzin.com/', headers={'User-Agent': 'Mozilla/5.0'})
html = r.text

fonts_html = set(re.findall(r'font-family:[^;\"\}]+', html, re.IGNORECASE))
print("\nFont families found in HTML:")
for fn in sorted(fonts_html)[:20]:
    print(" ", fn)

wix_fonts = set(re.findall(r'fonts\.googleapis\.com/css\?family=([^\"\'&]+)', html))
print("\nGoogle fonts loaded in HTML:", wix_fonts)

wix_font_css = set(re.findall(r'https://static\.parastorage\.com/services/wix-bolt/[^\"\'\s]+\.css', html))
print("\nBolt CSS links:", len(wix_font_css))
