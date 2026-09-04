import json

# Let's inspect the main text sections
with open('data/en_content.json', 'r', encoding='utf-8') as f:
    en = json.load(f)

with open('data/fr_content.json', 'r', encoding='utf-8') as f:
    fr = json.load(f)

print("=== SAMPLE EN HEADINGS & PARAGRAPHS ===")
for item in en:
    if item['tag'] in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p'] and len(item['text']) > 15:
        print(f"[{item['tag'].upper()}] {item['text']}")

print("\n=== SAMPLE FR HEADINGS & PARAGRAPHS ===")
for item in fr:
    if item['tag'] in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p'] and len(item['text']) > 15:
        print(f"[{item['tag'].upper()}] {item['text']}")
