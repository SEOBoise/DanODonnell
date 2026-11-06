from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
import json
import re

root=Path(__file__).resolve().parent/'dist'
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.assets=[]; self.ids=[]; self.h1=0; self.images=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag=='h1': self.h1+=1
        if tag=='a': self.links.append(a.get('href',''))
        if tag=='img': self.images.append(a); self.assets.append(a.get('src',''))
        if tag=='script' and 'src' in a: self.assets.append(a['src'])

failures=[]; pages={}
for f in root.rglob('*.html'):
    text=f.read_text(encoding='utf-8'); p=Page(); p.feed(text); pages[f]=p
    if p.h1!=1: failures.append(str(f)+': H1 count')
    if len(p.ids)!=len(set(p.ids)): failures.append(str(f)+': duplicate IDs')
    for data in re.findall(r'<script type="application/ld\+json">(.*?)</script>',text,re.S): json.loads(data)
    for im in p.images:
        if not all(k in im for k in ['alt','width','height']): failures.append('Image accessibility/dimensions: '+str(im))
    for a in p.assets:
        target=root/a.lstrip('/')
        if not target.exists() or target.stat().st_size==0: failures.append('Missing asset '+a)
for f,p in pages.items():
    for href in p.links:
        u=urlparse(href)
        if u.scheme or u.netloc: continue
        target=(root/u.path.lstrip('/')) if u.path else f
        if target.is_dir(): target=target/'index.html'
        if not target.exists(): failures.append('Missing link '+href)
        if u.fragment and target in pages and u.fragment not in pages[target].ids: failures.append('Missing anchor '+href)
print(json.dumps({'pages':len(pages),'home_links':len(pages[root/'index.html'].links),'asset_bytes':sum(f.stat().st_size for f in (root/'assets').iterdir()),'failures':failures},indent=2))
assert not failures
