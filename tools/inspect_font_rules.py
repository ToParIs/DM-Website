import requests
from bs4 import BeautifulSoup
import re

r = requests.get('https://www.dahlmarzin.com/', headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(r.text, 'html.parser')

style_tags = soup.find_all('style')
print(f"Total style tags: {len(style_tags)}")

# Look for Maitree rules
for s in style_tags:
    content = s.string or ''
    if 'maitree' in content.lower():
        matches = re.findall(r'([^{}]*\{[^{}]*maitree[^{}]*\})', content, re.IGNORECASE)
        for m in matches[:10]:
            print("\n--- MAITREE RULE ---")
            print(m.strip())

    if 'lato' in content.lower():
        matches = re.findall(r'([^{}]*\{[^{}]*lato[^{}]*\})', content, re.IGNORECASE)
        for m in matches[:5]:
            print("\n--- LATO RULE ---")
            print(m.strip())
