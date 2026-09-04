import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}

for path in ['projects-8', 'your-job']:
    r = requests.get(f'https://www.dahlmarzin.com/{path}', headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    text = soup.get_text(separator='\n', strip=True)
    lines = [l for l in text.split('\n') if len(l) > 3]
    print(f"\n=================== {path} ===================")
    print(f"Title: {soup.title.string if soup.title else ''}")
    print("Sample lines:")
    for line in lines[:25]:
        print(" ", line)
