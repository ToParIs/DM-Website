import urllib.request
import re
from bs4 import BeautifulSoup
import json

url = 'https://www.dahlmarzin.com/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')

# Check script tags
soup = BeautifulSoup(html, 'html.parser')
scripts = soup.find_all('script')
print(f"Total script tags: {len(scripts)}")
for idx, s in enumerate(scripts):
    s_id = s.get('id', '')
    s_type = s.get('type', '')
    src = s.get('src', '')
    text_sample = (s.string or '')[:100].replace('\n', ' ')
    if s_id or 'json' in s_type or 'warmup' in s_id.lower() or 'data' in s_id.lower():
        print(f"Script [{idx}] id='{s_id}' type='{s_type}' len={len(s.string or '')} sample: {text_sample}")

# Search for video URLs anywhere in HTML (including escaped)
video_matches = set(re.findall(r'(https?:\\?/\\?/[^"\'\s]+\.(?:mp4|webm|ogv))', html))
print("\nVideo extensions found in raw html:")
for vm in video_matches:
    print(" ", vm.replace(r'\/', '/'))

# Let's search for wix video ids or files
wix_mp4 = set(re.findall(r'([a-zA-Z0-9_\.]+\.mp4)', html))
print(f"\nMP4 references: {wix_mp4}")

# Search for french text or pages
print("\nSearching for FR links or language switch:")
fr_matches = set(re.findall(r'https://www\.dahlmarzin\.com/[a-zA-Z0-9_\-\?=/]+', html))
for m in sorted(fr_matches):
    print(" ", m)
