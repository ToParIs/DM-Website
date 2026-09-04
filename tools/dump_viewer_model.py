import urllib.request
from bs4 import BeautifulSoup
import json

url = 'https://www.dahlmarzin.com/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
soup = BeautifulSoup(html, 'html.parser')

vm_script = soup.find('script', id='wix-viewer-model')
if vm_script:
    data = json.loads(vm_script.string)
    with open('wix_viewer_model.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Saved wix_viewer_model.json successfully!")
    print("Top keys in model:", list(data.keys()))
    
    # Check sitePages or router or multilingual
    if 'siteFeaturesConfigs' in data:
        print("Site features:", list(data['siteFeaturesConfigs'].keys()))
        if 'multilingual' in data['siteFeaturesConfigs']:
            print("Multilingual:", json.dumps(data['siteFeaturesConfigs']['multilingual'], indent=2))
        if 'router' in data['siteFeaturesConfigs']:
            print("Router:", json.dumps(data['siteFeaturesConfigs']['router'], indent=2)[:500])
else:
    print("wix-viewer-model not found")
