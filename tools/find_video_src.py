import requests
import json
import re

r = requests.get('https://www.dahlmarzin.com/', headers={'User-Agent': 'Mozilla/5.0'})
html = r.text

print("Searching for comp-kzfs4q8j in HTML...")
pos = 0
while True:
    pos = html.find('comp-kzfs4q8j', pos)
    if pos == -1:
        break
    start = max(0, pos - 200)
    end = min(len(html), pos + 500)
    print("--- MATCH ---")
    print(html[start:end])
    pos += len('comp-kzfs4q8j')

# Also search for 'video' in wix_viewer_model.json
with open('wix_viewer_model.json', 'r', encoding='utf-8') as f:
    vmodel = json.load(f)

vmodel_str = json.dumps(vmodel)
print("\nSearching in wix_viewer_model.json for video...")
for m in re.finditer(r'([^\"]*video[^\"]*)', vmodel_str, re.IGNORECASE):
    val = m.group(1)
    if any(ext in val for ext in ['.mp4', '.webm', 'wixstatic', 'media']):
        print("  Found in model:", val[:200])
