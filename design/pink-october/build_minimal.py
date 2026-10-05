"""Builds pink-october-minimal.html (self-contained post, 1080x1350).

Run: python3 build_minimal.py  ->  pink-october-minimal.html
Render: node render.js minimal  ->  pink-october-minimal.png and pink-october-minimal@2x.png
"""
import base64
from pathlib import Path

HERE = Path(__file__).parent
LOGO_PATH = (HERE / "logo_path.txt").read_text()

# Same ribbon geometry as the textured version (local 600x700 box), drawn flat.
STRAND_FULL = (
    "M 492 700 C 440 575 368 455 300 336 "
    "C 236 224 160 176 168 108 C 176 46 246 20 300 20 "
    "C 354 20 424 46 432 108 C 440 176 364 224 300 336 "
    "C 232 455 160 575 108 700"
)
STRAND_FRONT = "M 432 108 C 440 176 364 224 300 336 C 232 455 160 575 108 700"
W = 100   # ribbon width, local units
GAP = 16  # knockout gap where the front strand crosses


def font_b64(name):
    return base64.b64encode((HERE / "fonts" / name).read_bytes()).decode()


TEMPLATE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Pink October — ZAD</title>
<style>
@font-face{font-family:'Instrument Serif';font-style:normal;font-weight:400;src:url(data:font/woff2;base64,IS_REGULAR) format('woff2')}
@font-face{font-family:'Instrument Serif';font-style:italic;font-weight:400;src:url(data:font/woff2;base64,IS_ITALIC) format('woff2')}
@font-face{font-family:'Inter';font-style:normal;font-weight:100 900;src:url(data:font/woff2;base64,INTER_FONT) format('woff2')}
@font-face{font-family:'Geist Mono';font-style:normal;font-weight:100 900;src:url(data:font/woff2;base64,GEIST_MONO) format('woff2')}
:root{
  --canvas:#F7F5F2;      /* warm bone */
  --pastel:#FBE6EA;      /* pale pink disc behind the ribbon */
  --rule:#E4DFD8;        /* 1px structural lines */
  --ink:#1E2422;         /* off-black */
  --muted:#7A7672;       /* meta text */
  --zad-green:#044132;   /* logo + identity line 1 */
  --zad-pink:#E2468A;    /* ribbon, "Pink", identity line 2 */
}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;background:var(--canvas)}
.post{position:relative;width:1080px;height:1350px;overflow:hidden;background:var(--canvas);color:var(--ink)}
.layer{position:absolute;inset:0;width:1080px;height:1350px}
.grain{opacity:.05;mix-blend-mode:multiply;pointer-events:none}

.header{position:absolute;top:72px;left:72px;right:72px;height:56px;display:flex;align-items:center;justify-content:space-between}
.logo{width:132px;display:block}
.meta{font-family:'Geist Mono',monospace;font-size:20px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.rule{position:absolute;left:72px;right:72px;height:1px;background:var(--rule)}

h1{position:absolute;top:176px;left:64px;font-family:'Instrument Serif',serif;font-weight:400;
  font-size:268px;line-height:.86;letter-spacing:-.035em;color:var(--ink)}
h1 em{display:block;font-style:italic;color:var(--zad-pink)}
h1 span{display:block}

.tagline{position:absolute;left:72px;top:820px;width:430px;font-family:'Instrument Serif',serif;font-style:italic;
  font-size:50px;line-height:1.1;letter-spacing:-.015em;color:var(--ink)}
.index{position:absolute;left:72px;top:770px;font-family:'Geist Mono',monospace;font-size:18px;letter-spacing:.08em;
  text-transform:uppercase;color:var(--muted)}

.identity{position:absolute;left:72px;right:72px;bottom:70px;font-family:'Inter',sans-serif}
.identity .l1{font-weight:400;font-size:33px;letter-spacing:-.012em;color:var(--zad-green)}
.identity .l2{margin-top:12px;font-weight:700;font-size:28px;letter-spacing:-.005em;color:var(--zad-pink)}
</style></head>
<body><div class="post">

<svg class="layer" viewBox="0 0 1080 1350" aria-hidden="true">
  <defs>
    <path id="sFull" d="STRAND_FULL"/>
    <path id="sFront" d="STRAND_FRONT"/>
    <linearGradient id="fade" gradientUnits="userSpaceOnUse" x1="0" y1="150" x2="0" y2="235">
      <stop offset="0" stop-color="#000"/><stop offset="1" stop-color="#fff"/>
    </linearGradient>
    <mask id="mFade" maskUnits="userSpaceOnUse" x="-50" y="-50" width="700" height="800">
      <rect x="-50" y="-50" width="700" height="800" fill="url(#fade)"/></mask>
    <mask id="mNotch" maskUnits="userSpaceOnUse" x="-50" y="-50" width="700" height="800">
      <rect x="-50" y="-50" width="700" height="800" fill="#fff"/>
      <polygon fill="#000" points="40,676 132,606 222,664 222,780 40,780"/>
      <polygon fill="#000" points="378,664 468,606 560,676 560,780 378,780"/>
    </mask>
  </defs>

  <!-- single offset pastel disc: the only "depth" device -->
  <circle cx="790" cy="890" r="218" fill="#FBE6EA"/>

  <g transform="translate(582 702) scale(.66) rotate(-4 300 360)">
    <g mask="url(#mNotch)">
      <use href="#sFull" fill="none" stroke="#E2468A" stroke-width="W"/>
      <g mask="url(#mFade)">
        <use href="#sFront" fill="none" stroke="#FBE6EA" stroke-width="WG"/>
        <use href="#sFront" fill="none" stroke="#E2468A" stroke-width="W"/>
      </g>
    </g>
  </g>
</svg>

<svg class="layer grain" viewBox="0 0 1080 1350" aria-hidden="true">
  <filter id="noise"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="3" stitchTiles="stitch"/>
    <feColorMatrix type="saturate" values="0"/></filter>
  <rect width="1080" height="1350" filter="url(#noise)"/>
</svg>

<div class="header">
  <svg class="logo" viewBox="50 50 1110 400" role="img" aria-label="ZAD"><path fill="#044132" fill-rule="evenodd" d="LOGO"/></svg>
  <span class="meta">10 / 2026</span>
</div>
<div class="rule" style="top:162px"></div>

<h1><em>Pink</em><span>October</span></h1>

<p class="index">01 — 31 Oct</p>
<p class="tagline">Together for awareness. Together for hope.</p>

<div class="rule" style="bottom:184px"></div>
<div class="identity">
  <p class="l1">ZAD AI supports Breast Cancer Awareness Month</p>
  <p class="l2">Awareness • Support • Prevention</p>
</div>

</div></body></html>
"""

html = (
    TEMPLATE.replace("LOGO", LOGO_PATH)
    .replace("STRAND_FULL", STRAND_FULL)
    .replace("STRAND_FRONT", STRAND_FRONT)
    .replace('stroke-width="WG"', f'stroke-width="{W + GAP}"')
    .replace('stroke-width="W"', f'stroke-width="{W}"')
    .replace("IS_REGULAR", font_b64("InstrumentSerif-Regular-latin.woff2"))
    .replace("IS_ITALIC", font_b64("InstrumentSerif-Italic-latin.woff2"))
    .replace("INTER_FONT", font_b64("Inter-latin.woff2"))
    .replace("GEIST_MONO", font_b64("GeistMono-latin.woff2"))
)
(HERE / "pink-october-minimal.html").write_text(html)
print("wrote pink-october-minimal.html", len(html) // 1024, "KB")
