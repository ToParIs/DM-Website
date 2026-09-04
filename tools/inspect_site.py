import urllib.request
import re
from bs4 import BeautifulSoup
import json

url = 'https://www.dahlmarzin.com/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')

soup = BeautifulSoup(html, 'html.parser')
title = soup.title.string if soup.title else 'No Title'
print(f"Title: {title}")

# Links
links = sorted(list(set([a.get('href') for a in soup.find_all('a') if a.get('href')])))
print(f"Total links: {len(links)}")
for l in links:
    if any(k in l for k in ['dahlmarzin', 'en', 'fr', '#', '/']):
        print(f"  Link: {l}")

# Wix videos
wix_videos = sorted(list(set(re.findall(r'video\.wixstatic\.com/video/[^"\'\s>]+', html))))
print(f"\nWix Videos ({len(wix_videos)}):")
for v in wix_videos:
    print(f"  https://{v}")

# Images
wix_images = sorted(list(set(re.findall(r'static\.wixstatic\.com/media/[a-zA-Z0-9_\.]+', html))))
print(f"\nWix Images ({len(wix_images)}):")
for img in wix_images[:10]:
    print(f"  https://{img}")

# Check languages
print("\nLanguage indicators or switcher:")
lang_elements = soup.find_all(attrs={"data-testid": re.compile(r'lang|switch', re.I)})
for el in lang_elements:
    print(el)

# Check text navigation items
nav = soup.find_all('nav')
print(f"\nNav tags: {len(nav)}")
for n in nav:
    print(n.get_text(strip=True, separator=' | '))

# Check all text headers
headers = [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
print(f"\nHeadings ({len(headers)}):")
for h in headers[:15]:
    print(f"  - {h}")
