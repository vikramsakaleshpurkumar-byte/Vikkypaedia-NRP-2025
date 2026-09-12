import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULE_URL = "file:///" + os.path.join(ROOT, "index.html").replace("\\", "/").lstrip("/")
VERIFY_URL = "file:///" + os.path.join(ROOT, "verify.html").replace("\\", "/").lstrip("/")
from playwright.sync_api import sync_playwright
SKIP_ONB = "try{var K='vkp.nrp2025.v1';var r=localStorage.getItem(K);"\
    "var s=r?JSON.parse(r):{v:1,items:{},prefs:{pri:'all',lvl:'x',set:'both',fs:'m',theme:'system'},"\
    "placement:null,lastUnit:null,exam:{attempts:[],lockUntil:0},settings:null,started:null,"\
    "profile:null,plan:null,onboarded:false};"\
    "s.onboarded=true;localStorage.setItem(K,JSON.stringify(s));}catch(e){}"

with sync_playwright() as pw:
    b=pw.chromium.launch(); ctx=b.new_context(); ctx.add_init_script(SKIP_ONB); p=ctx.new_page()
    p.goto(MODULE_URL); p.wait_for_timeout(600)
    p.evaluate("""()=>{const K='vkp.nrp2025.v1';const s=JSON.parse(localStorage.getItem(K)||'{"v":1,"items":{}}');
      s.v=1; s.items=s.items||{}; s.exam={attempts:[{at:Date.now(),n:50,right:48,pct:96}],lockUntil:0};
      const past=Date.now()-3*86400000;
      document.querySelectorAll('.q').forEach(q=>{const id=q.getAttribute('data-q');
        s.items[id]={box:3,due:Date.now()+6e8,ok:true,firstPass:past,longest:2*86400000,retained:true,hint:0,tries:2};});
      localStorage.setItem(K,JSON.stringify(s));}""")
    p.reload(); p.wait_for_timeout(800)
    p.fill('#certName','Dr Ananya Raghavan'); p.click('#makeCert'); p.wait_for_timeout(600)
    p.emulate_media(media="print")
    vis = p.evaluate("""()=>{const g=s=>{const e=document.querySelector(s);return e?getComputedStyle(e).display:'missing'};
      return {printRoot:g('.printroot'), masthead:g('.masthead'), unit:g('.unit'), footer:g('footer'),
              sheetText:document.querySelector('.cert-sheet')?document.querySelector('.cert-sheet').textContent.length:0};}""")
    print("  print media:", vis)
    p.pdf(path=os.path.join(ROOT,"certificate-preview.pdf"), format="A4", landscape=True, print_background=True)
    p.emulate_media(media="screen")
    p.screenshot(path="shot-certificate.png", clip={"x":0,"y":0,"width":1280,"height":900})
    b.close()
