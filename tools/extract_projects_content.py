import requests
from bs4 import BeautifulSoup
import json

def get_project_items(url):
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.text, 'html.parser')
    # Find all text blocks
    text_blocks = []
    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']):
        t = tag.get_text(strip=True)
        if t and len(t) > 2:
            text_blocks.append(t)
    return text_blocks

en_p = get_project_items('https://www.dahlmarzin.com/projects-8')
fr_p = get_project_items('https://www.dahlmarzin.com/projects-8?lang=fr')

print(f"EN project lines: {len(en_p)}")
print(f"FR project lines: {len(fr_p)}")

with open('data/en_projects.json', 'w', encoding='utf-8') as f:
    json.dump(en_p, f, indent=2, ensure_ascii=False)

with open('data/fr_projects.json', 'w', encoding='utf-8') as f:
    json.dump(fr_p, f, indent=2, ensure_ascii=False)

print("Saved data/en_projects.json and data/fr_projects.json")
