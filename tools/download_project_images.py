import requests
from bs4 import BeautifulSoup
import re
import os

r = requests.get('https://www.dahlmarzin.com/projects-8', headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(r.text, 'html.parser')

os.makedirs('assets/images/projects', exist_ok=True)

# Find all images on projects-8
imgs = soup.find_all('img')
print(f"Projects page img tags: {len(imgs)}")
downloaded = 0
for idx, i in enumerate(imgs):
    src = i.get('src') or i.get('data-src') or ''
    alt = i.get('alt', f'project_{idx}')
    if 'static.wixstatic.com/media/' in src:
        # Extract base media id
        match = re.search(r'static\.wixstatic\.com/media/([a-zA-Z0-9_~]+(?:\.jpg|\.png|\.jpeg)?)', src)
        if match:
            media_id = match.group(1)
            original_url = f"https://static.wixstatic.com/media/{media_id}"
            clean_name = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', alt.strip()) or f"project_{idx}"
            if not clean_name.lower().endswith(('.jpg', '.png', '.jpeg')):
                clean_name += '.jpg'
            target_path = f"assets/images/projects/{clean_name}"
            
            print(f"Downloading {original_url} -> {target_path}")
            res = requests.get(original_url, headers={'User-Agent': 'Mozilla/5.0'})
            if res.status_code == 200:
                with open(target_path, 'wb') as f:
                    f.write(res.content)
                print(f"  OK ({len(res.content)/1024:.1f} KB)")
                downloaded += 1

print(f"Downloaded {downloaded} project images!")
