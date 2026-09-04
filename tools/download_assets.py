import os
import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urlparse

os.makedirs('assets/images', exist_ok=True)
os.makedirs('assets/videos', exist_ok=True)
os.makedirs('data', exist_ok=True)

# Media to download
media_map = {
    'assets/images/logo-white.png': 'https://static.wixstatic.com/media/14e118_4bf7379891324d5b958fc95e6f706967~mv2.png',
    'assets/images/logo-footer.png': 'https://static.wixstatic.com/media/14e118_cf382f8f9e5b44cd9a9084c78f9a24ff~mv2.png',
    'assets/images/about-bg.jpg': 'https://static.wixstatic.com/media/14e118_7dccd812a3af43a886ed3669e43263d8~mv2.jpg',
    'assets/images/portfolio-banner.jpg': 'https://static.wixstatic.com/media/14e118_7cfb2596ba78440585ef5b8a6e09add6~mv2.jpg',
    'assets/images/team.jpg': 'https://static.wixstatic.com/media/14e118_943ecf4b0db94611a6baff1f6e69c3d3~mv2.jpg',
    'assets/images/silverio-marzin.jpg': 'https://static.wixstatic.com/media/14e118_00f969ab64cf45e290fc0c24a78bfbab~mv2.jpg',
    'assets/images/icon-blueprint.png': 'https://static.wixstatic.com/media/14e118_f44b0ddb3c9a4bec8f52cc7de4606798~mv2.png',
    'assets/images/icon-house.png': 'https://static.wixstatic.com/media/11062b_bf349604256e48abaf8a452aefe9436d~mv2.png',
    'assets/images/icon-contract.png': 'https://static.wixstatic.com/media/14e118_ed96042c89b3400a93ed20f56c58c7e7~mv2.png',
    'assets/images/hero-poster.jpg': 'https://static.wixstatic.com/media/11062b_4f14b356c1df4854968cf1cc94ca98c5f000.jpg',
    'assets/videos/hero-video-720p.mp4': 'https://video.wixstatic.com/video/11062b_4f14b356c1df4854968cf1cc94ca98c5/720p/mp4/file.mp4',
    'assets/videos/hero-video-480p.mp4': 'https://video.wixstatic.com/video/11062b_4f14b356c1df4854968cf1cc94ca98c5/480p/mp4/file.mp4'
}

print("Starting download of assets...")
for local_path, url in media_map.items():
    print(f"Downloading {url} -> {local_path} ...")
    r = requests.get(url, stream=True, headers={'User-Agent': 'Mozilla/5.0'})
    if r.status_code == 200:
        with open(local_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        size_kb = os.path.getsize(local_path) / 1024
        print(f"  OK ({size_kb:.1f} KB)")
    else:
        print(f"  FAILED ({r.status_code})")

print("All asset downloads complete!")
