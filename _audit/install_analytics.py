# -*- coding: utf-8 -*-
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP_DIRS = ('.vercel', '_staging', '_audit')
SKIP_NAMES = {'index-v2.html', 'index.previous-pre-v03.html', 'index.v03-draft.html'}

def is_prod(p):
    parts = p.parts
    if any(s in parts for s in SKIP_DIRS): return False
    if any(part.startswith('_backup') for part in parts): return False
    return p.name not in SKIP_NAMES

HEAD = """
    <!-- Aventario analytics: consent-gated GA4 / Google Ads (Consent Mode v2) -->
    <script>
      window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}
      gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied'});
      window.AV_GA_ID='G-WV4NNK7FSV';
      window.avLoadGA=function(){if(window.__avGA)return;window.__avGA=true;gtag('consent','update',{ad_storage:'granted',ad_user_data:'granted',ad_personalization:'granted',analytics_storage:'granted'});var s=document.createElement('script');s.async=true;s.src='https://www.googletagmanager.com/gtag/js?id='+AV_GA_ID;document.head.appendChild(s);gtag('js',new Date());gtag('config',AV_GA_ID);};
      try{if(localStorage.getItem('av-consent')==='granted')window.avLoadGA();}catch(e){}
    </script>"""

BANNER = """
    <!-- Aventario cookie consent banner -->
    <style>
    #av-consent{position:fixed;left:1rem;right:1rem;bottom:1rem;max-width:30rem;margin-left:auto;z-index:9999;background:#334b60;color:#fff;border-radius:12px;padding:1.2rem;box-shadow:0 18px 50px -20px rgba(0,0,0,.55);font-family:'Lato',system-ui,sans-serif;font-size:14px;line-height:1.55}
    #av-consent p{margin:0 0 .9rem}
    #av-consent a{color:#8dccc0;text-decoration:underline}
    #av-consent .av-row{display:flex;gap:.6rem;flex-wrap:wrap}
    #av-consent button{font:inherit;font-weight:700;border-radius:999px;padding:.55rem 1.15rem;cursor:pointer;border:1px solid transparent}
    #av-accept{background:#8dccc0;color:#16323f}
    #av-decline{background:transparent;color:#fff;border-color:rgba(255,255,255,.55)}
    #av-consent[hidden]{display:none}
    </style>
    <div id="av-consent" role="dialog" aria-label="Cookie consent" hidden>
      <p id="av-consent-text"></p>
      <div class="av-row">
        <button id="av-accept" type="button"></button>
        <button id="av-decline" type="button"></button>
      </div>
    </div>
    <script>
    (function(){var el=document.getElementById('av-consent');if(!el)return;
     try{if(localStorage.getItem('av-consent'))return;}catch(e){}
     var de=(document.documentElement.lang||'en').slice(0,2)==='de';
     var txt=de?'Wir nutzen Cookies für Analyse und Werbung, um die Leistung unserer Website zu verstehen. Diese werden erst nach Ihrer Zustimmung geladen. Mehr in unserer <a href="/datenschutz">Datenschutzerklärung</a>.':'We use analytics and advertising cookies to understand how our site performs. They load only after you accept. See our <a href="/datenschutz">Privacy Policy</a>.';
     document.getElementById('av-consent-text').innerHTML=txt;
     document.getElementById('av-accept').textContent=de?'Zustimmen':'Accept';
     document.getElementById('av-decline').textContent=de?'Ablehnen':'Decline';
     el.hidden=false;
     document.getElementById('av-accept').addEventListener('click',function(){try{localStorage.setItem('av-consent','granted');}catch(e){}if(window.avLoadGA)window.avLoadGA();el.hidden=true;});
     document.getElementById('av-decline').addEventListener('click',function(){try{localStorage.setItem('av-consent','denied');}catch(e){}el.hidden=true;});
    })();
    </script>"""

files = [p for p in ROOT.rglob('*.html') if is_prod(p)]
done = 0
for p in files:
    h = p.read_text(encoding='utf-8')
    if 'AV_GA_ID' in h or 'av-consent' in h:
        continue  # idempotent
    if '<head>' not in h or '</body>' not in h:
        continue
    h = h.replace('<head>', '<head>' + HEAD, 1)
    idx = h.rfind('</body>')
    h = h[:idx] + BANNER + '\n  ' + h[idx:]
    p.write_text(h, encoding='utf-8')
    done += 1
print(f"scanned {len(files)} files, injected GA4 + consent banner into {done}")
