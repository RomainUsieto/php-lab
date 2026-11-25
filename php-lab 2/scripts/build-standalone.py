"""Produit une version HTML autonome, ouvrable sans serveur ni réseau."""
from pathlib import Path
import json,re,base64
root=Path(__file__).resolve().parent.parent
modules=['quiz','exam','storage','statistics','code-editor','app']
parts=[]
for name in modules:
 s=(root/f'js/{name}.js').read_text()
 s=re.sub(r'^import .*?;\n','',s,flags=re.M)
 s=re.sub(r'^export ', '', s, flags=re.M)
 if name=='app':
  start=s.index("const data=await Promise.all(")
  end=s.index(';chapters=data[0]',start)
  s=s[:start]+'const data=PHP_LAB_EMBEDDED'+s[end:]
  s='const e=escapeHtml;\n'+s
 parts.append(s)
data=[json.loads((root/'data/chapters.json').read_text())]+[json.loads((root/f'data/chapitre-{c}.json').read_text()) for c in range(1,5)]
embedded=json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
js='const PHP_LAB_EMBEDDED='+embedded+';\n'+'\n'.join(parts)
js=re.sub(r'</script',r'<\\/script',js,flags=re.I)
html=(root/'index.html').read_text()
html=html.replace('<link rel="stylesheet" href="css/style.css">','<style>'+(root/'css/style.css').read_text()+'</style>')
html=html.replace('<script type="module" src="js/app.js"></script>','')
svg=base64.b64encode((root/'assets/favicon.svg').read_bytes()).decode()
html=html.replace('href="assets/favicon.svg"','href="data:image/svg+xml;base64,'+svg+'"')
html=html.replace('</body>', '<script type="module">\n'+js+'\n</script></body>')
(root/'PHP-Lab-autonome.html').write_text(html)
print('Version autonome produite : PHP-Lab-autonome.html')
