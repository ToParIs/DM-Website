import requests
from bs4 import BeautifulSoup
import re
import json

# Let's inspect the entire HTML of the homepage
r = requests.get('https://www.dahlmarzin.com/', headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(r.text, 'html.parser')

# Find all images
imgs = soup.find_all('img')
print(f"Total img tags: {len(imgs)}")
for i in imgs:
    src = i.get('src') or i.get('data-src')
    alt = i.get('alt', '')
    print(f"  img alt='{alt}' src='{src[:120] if src else 'None'}'")

# Also let's extract all wix media URLs
all_media = set(re.findall(r'https?://static\.wixstatic\.com/media/[a-zA-Z0-9_\.]+', r.text))
print(f"\nUnique static.wixstatic.com/media URLs found: {len(all_media)}")
for m in sorted(all_media):
    print(" ", m)
