import json

with open('wix_viewer_model.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

router = data.get('siteFeaturesConfigs', {}).get('router', {})
pages = router.get('pagesMap', {})
print(f"Total pages in router: {len(pages)}")
for pid, pinfo in pages.items():
    print(f"Page ID: {pid}")
    print(f"  Title: {pinfo.get('title')}")
    print(f"  pageUriSEO: {pinfo.get('pageUriSEO')}")
    print(f"  pageFullPath: {pinfo.get('pageFullPath')}")
    print(f"  pageJsonFileName: {pinfo.get('pageJsonFileName')}")

# Also check siteFeaturesConfigs for masterPage, pageList, siteStructure, etc.
sfc = data.get('siteFeaturesConfigs', {})
for k in sfc.keys():
    if any(term in k.lower() for term in ['page', 'menu', 'nav', 'seo', 'structure']):
        print(f"Feature '{k}':", str(sfc[k])[:200])
