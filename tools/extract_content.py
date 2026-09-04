import requests
from bs4 import BeautifulSoup
import json
import re

def extract_texts(url):
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Let's find all text blocks in DOM order
    content_blocks = []
    
    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'a']):
        text = tag.get_text(strip=True)
        if text and len(text) > 1 and not text.startswith(('function', 'var ', 'window.')):
            # Avoid duplicate children if parent already has it
            parent_text = tag.parent.get_text(strip=True) if tag.parent else ''
            # Check if this exact text is identical to parent
            is_redundant = False
            if tag.parent and tag.parent.name in ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a'] and parent_text == text:
                is_redundant = True
            if not is_redundant:
                content_blocks.append({
                    'tag': tag.name,
                    'text': text,
                    'id': tag.get('id', '')
                })
    return content_blocks

en_blocks = extract_texts('https://www.dahlmarzin.com/')
fr_blocks = extract_texts('https://www.dahlmarzin.com/?lang=fr')

print(f"EN blocks: {len(en_blocks)}")
print(f"FR blocks: {len(fr_blocks)}")

with open('data/en_content.json', 'w', encoding='utf-8') as f:
    json.dump(en_blocks, f, indent=2, ensure_ascii=False)

with open('data/fr_content.json', 'w', encoding='utf-8') as f:
    json.dump(fr_blocks, f, indent=2, ensure_ascii=False)

print("Saved data/en_content.json and data/fr_content.json")
