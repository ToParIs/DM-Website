import requests
from bs4 import BeautifulSoup
import json

for lang_url, name in [('https://www.dahlmarzin.com/', 'EN'), ('https://www.dahlmarzin.com/?lang=fr', 'FR')]:
    r = requests.get(lang_url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.text, 'html.parser')
    
    print(f"\n=================== {name} Navigation & Anchors ===================")
    for a in soup.find_all('a'):
        href = a.get('href', '')
        text = a.get_text(strip=True)
        if text or href:
            print(f"  [{text}] -> {href}")
