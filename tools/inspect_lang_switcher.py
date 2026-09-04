import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.dahlmarzin.com/', headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(r.text, 'html.parser')

# Look for language switcher elements or links containing lang=
lang_elements = soup.find_all(lambda tag: tag.get('href') and ('lang=' in tag.get('href') or 'dahlmarzin.com' in tag.get('href') and ('fr' in tag.text.lower() or 'en' in tag.text.lower())))
print("Lang elements found:")
for el in lang_elements:
    print(el)
    print("Parent:", el.parent)

# Check all elements with text 'EN' or 'FR'
for el in soup.find_all(text=lambda t: t and t.strip() in ['EN', 'FR', 'English', 'Français']):
    print(f"Text match: '{el.strip()}' in tag <{el.parent.name}> id='{el.parent.get('id')}' class='{el.parent.get('class')}'")
    print("  Parent HTML:", el.parent)
