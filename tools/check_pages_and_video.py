import requests
import re
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

urls = [
    'https://www.dahlmarzin.com/',
    'https://www.dahlmarzin.com/?lang=fr',
    'https://www.dahlmarzin.com/projects-8',
    'https://www.dahlmarzin.com/your-job',
]

for u in urls:
    r = requests.get(u, headers=headers)
    print(f"\n=== URL: {u} (Status: {r.status_code}, Length: {len(r.text)}) ===")
    soup = BeautifulSoup(r.text, 'html.parser')
    print(f"Title: {soup.title.string if soup.title else 'None'}")
    
    # Check for videos in HTML
    videos = soup.find_all('video')
    for v in videos:
        print("  <video> tag:", v.attrs)
        for s in v.find_all('source'):
            print("    <source>:", s.attrs)
            
    # Search for video URLs in scripts/data
    v_urls = set(re.findall(r'(https?://[^"\'\s]+\.(?:mp4|webm))', r.text))
    wix_video_ids = set(re.findall(r'video\.wixstatic\.com/video/([a-zA-Z0-9_\.]+\.mp4)', r.text))
    print(f"  Direct video URLs found: {v_urls}")
    print(f"  Wix video IDs found: {wix_video_ids}")
