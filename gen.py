import os, re
files=sorted([f for f in os.listdir('.') if f.startswith('AImyAdvance-') and f.endswith('.mp4')])
# newest first by mtime
files.sort(key=lambda f: os.path.getmtime(f), reverse=True)
def title(f):
    t=f.replace('AImyAdvance-','').replace('.mp4','').replace('-',' ')
    return t
cards="".join(f'''
  <div class="card"><h2>{title(f)}</h2>
    <video src="{f}" controls preload="none" playsinline></video>
    <a href="{f}">Open direct link ↗</a></div>''' for f in files)
html=f'''<!doctype html><html><head><meta charset="utf-8"><title>AI My Advance — Demo Videos</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>body{{margin:0;font-family:system-ui,Segoe UI,Arial,sans-serif;background:#0f2038;color:#eaf0f7}}
header{{padding:32px 20px;text-align:center;border-bottom:2px solid #14b8a6}} header h1{{margin:0;font-size:28px}}
header p{{color:#9fb0c7;margin:8px 0 0}}
.grid{{max-width:1100px;margin:24px auto;padding:0 16px;display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:20px}}
.card{{background:#16304f;border-radius:14px;padding:16px}} .card h2{{font-size:16px;margin:0 0 10px;text-transform:capitalize}}
video{{width:100%;border-radius:8px;background:#000}}
a{{display:inline-block;margin-top:8px;color:#14b8a6;text-decoration:none;font-size:13px}}</style></head><body>
<header><h1>AI My Advance — Demo Videos</h1><p>{len(files)} demos. Click any to play.</p></header>
<div class="grid">{cards}</div></body></html>'''
open("index.html","w",encoding="utf-8").write(html)
print("gallery regenerated:", len(files), "videos")
