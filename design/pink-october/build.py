"""Builds pink-october.html (self-contained post, 1080x1350) from the template below.

Run: python3 build.py  ->  pink-october.html
Render: node render.js  ->  pink-october.png (1080x1350) and pink-october@2x.png
"""
import base64
from pathlib import Path

HERE = Path(__file__).parent
LOGO_PATH = (HERE / "logo_path.txt").read_text()


def font_b64(name):
    return base64.b64encode((HERE / "fonts" / name).read_bytes()).decode()


# Ribbon geometry in a local 600x700 box. One continuous strand (back pass),
# plus the segment that crosses on top (front pass) faded in above the crossing.
STRAND_FULL = (
    "M 492 700 C 440 575 368 455 300 336 "
    "C 236 224 160 176 168 108 C 176 46 246 20 300 20 "
    "C 354 20 424 46 432 108 C 440 176 364 224 300 336 "
    "C 232 455 160 575 108 700"
)
STRAND_FRONT = "M 432 108 C 440 176 364 224 300 336 C 232 455 160 575 108 700"
W = 100  # ribbon width in local units


def satin(href):
    """Flat satin strip: dark selvedge edges, body gradient, one soft sheen band, a specular thread."""
    return f"""
      <use href="#{href}" fill="none" stroke="#C12A69" stroke-width="{W}"/>
      <use href="#{href}" fill="none" stroke="url(#rib)" stroke-width="{W - 6}"/>
      <use href="#{href}" fill="none" stroke="#8A0F45" stroke-opacity=".26" stroke-width="{W}" transform="translate(18 8)" filter="url(#b10)"/>
      <use href="#{href}" fill="none" stroke="#FFF0F5" stroke-opacity=".5" stroke-width="30" transform="translate(-22 -6)" filter="url(#b6)"/>
      <use href="#{href}" fill="none" stroke="#FFFFFF" stroke-opacity=".85" stroke-width="2.5" transform="translate(-38 -10)" filter="url(#b1)"/>
      <use href="#{href}" fill="none" stroke="#FFFFFF" stroke-opacity=".35" stroke-width="1.5" transform="translate(44 6)" filter="url(#b1)"/>
      <rect x="0" y="0" width="600" height="720" filter="url(#weave)" opacity=".45" style="mix-blend-mode:soft-light"/>"""


TEMPLATE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Pink October — ZAD</title>
<style>
@font-face{font-family:'Fraunces';font-style:italic;font-weight:300 700;src:url(data:font/woff2;base64,FRAUNCES) format('woff2')}
@font-face{font-family:'Inter';font-style:normal;font-weight:100 900;src:url(data:font/woff2;base64,INTER) format('woff2')}
:root{
  --zad-green:#044132;   /* logo + identity line 1 */
  --zad-pink:#E2468A;    /* identity line 2 */
  --rose-ink:#A3164F;    /* title */
  --blush-0:#FFF8FA; --blush-1:#FBE4EB; --blush-2:#F3C2D2; --blush-3:#E596B2;
}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;background:var(--blush-1)}
.post{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:'Inter',sans-serif;
  background:
    radial-gradient(110% 55% at 50% -5%, #FFFFFF 0%, var(--blush-0) 35%, transparent 70%),
    radial-gradient(80% 45% at 50% 108%, var(--blush-3) 0%, transparent 75%),
    linear-gradient(180deg, var(--blush-0) 0%, var(--blush-1) 40%, var(--blush-2) 100%)}
.layer{position:absolute;inset:0;width:1080px;height:1350px}
.grain{mix-blend-mode:multiply;pointer-events:none}

.logo{position:absolute;top:72px;left:50%;width:176px;transform:translateX(-50%);
  filter:drop-shadow(0 1px 0 rgba(255,255,255,.9))}

h1{position:absolute;top:146px;left:0;right:0;text-align:center;
  font-family:'Fraunces',serif;font-style:italic;font-weight:600;
  font-variation-settings:"opsz" 144,"SOFT" 100,"WONK" 1;
  font-size:162px;line-height:.9;letter-spacing:-.03em;color:var(--rose-ink);
  text-shadow:
    0 -1px 0 rgba(255,255,255,.7),
    0 1px 0 #B42A62, 0 2px 0 #AA2259, 0 3px 0 #9E1B50, 0 4px 0 #921548,
    0 8px 4px rgba(110,10,48,.22), 0 22px 34px rgba(150,20,70,.24)}
h1 span{display:block}
h1 .l1{transform:translateX(-118px)}
h1 .l2{transform:translateX(64px)}

.tagline{position:absolute;top:1046px;left:0;right:0;text-align:center;
  font-family:'Fraunces',serif;font-style:italic;font-weight:400;
  font-variation-settings:"opsz" 48,"SOFT" 100,"WONK" 0;
  font-size:35px;letter-spacing:-.005em;color:var(--zad-green)}
.tagline i{font-style:normal;color:var(--zad-pink);padding:0 .4em}

.card{position:absolute;left:56px;right:56px;bottom:56px;padding:34px 28px 38px;border-radius:40px;text-align:center;
  background:linear-gradient(180deg,rgba(255,255,255,.80),rgba(255,255,255,.56));
  border:1px solid rgba(255,255,255,.95);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.95), inset 0 -2px 0 rgba(214,110,150,.16),
             0 34px 60px -30px rgba(140,20,72,.55), 0 12px 24px -14px rgba(140,20,72,.30);
  backdrop-filter:blur(18px) saturate(1.25);-webkit-backdrop-filter:blur(18px) saturate(1.25)}
.card .l1{font-weight:400;font-size:35px;letter-spacing:-.012em;color:var(--zad-green)}
.card .l2{margin-top:16px;font-weight:700;font-size:32px;letter-spacing:-.008em;color:var(--zad-pink);
  text-shadow:0 1px 0 rgba(255,255,255,.85),0 4px 10px rgba(226,70,138,.28)}
</style></head>
<body><div class="post">

<!-- BACKDROP: embossed rings, halo, silk drapes -->
<svg class="layer" viewBox="0 0 1080 1350" aria-hidden="true">
  <defs>
    <radialGradient id="halo" cx="540" cy="740" r="420" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#FFFFFF" stop-opacity=".95"/>
      <stop offset=".5" stop-color="#FFF1F5" stop-opacity=".55"/>
      <stop offset="1" stop-color="#FFF1F5" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="silkA" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#FFFFFF" stop-opacity=".9"/>
      <stop offset=".3" stop-color="#F8D2DE" stop-opacity=".6"/>
      <stop offset="1" stop-color="#DF84A6" stop-opacity=".6"/>
    </linearGradient>
    <linearGradient id="silkB" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#FFFFFF" stop-opacity=".75"/>
      <stop offset=".45" stop-color="#F1AFC5" stop-opacity=".55"/>
      <stop offset="1" stop-color="#C95E88" stop-opacity=".7"/>
    </linearGradient>
    <filter id="s3" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="3"/></filter>
    <filter id="s16" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="16"/></filter>
  </defs>
  <g fill="none" transform="translate(540 740)">
    <g stroke="#FFFFFF" stroke-opacity=".95" stroke-width="2" transform="translate(0 -1.5)">
      <circle r="290"/><circle r="380"/><circle r="470"/><circle r="560"/><circle r="650"/></g>
    <g stroke="#B9466F" stroke-opacity=".17" stroke-width="2" transform="translate(0 1.5)">
      <circle r="290"/><circle r="380"/><circle r="470"/><circle r="560"/><circle r="650"/></g>
  </g>
  <circle cx="540" cy="740" r="420" fill="url(#halo)"/>

  <!-- soft light orbs: depth on the flanks -->
  <g fill="#FFFFFF">
    <circle cx="150" cy="620" r="46" opacity=".55" filter="url(#s16)"/>
    <circle cx="210" cy="820" r="14" opacity=".7" filter="url(#s3)"/>
    <circle cx="92" cy="900" r="26" opacity=".45" filter="url(#s3)"/>
    <circle cx="250" cy="560" r="7" opacity=".85"/>
    <circle cx="930" cy="610" r="56" opacity=".5" filter="url(#s16)"/>
    <circle cx="870" cy="790" r="18" opacity=".7" filter="url(#s3)"/>
    <circle cx="985" cy="870" r="10" opacity=".8" filter="url(#s3)"/>
    <circle cx="820" cy="530" r="6" opacity=".85"/>
  </g>
  <g fill="#E2468A">
    <circle cx="300" cy="700" r="9" opacity=".22" filter="url(#s3)"/>
    <circle cx="790" cy="900" r="12" opacity=".2" filter="url(#s3)"/>
  </g>

  <!-- upper wisps: fill the shoulders beside the title -->
  <path filter="url(#s16)" fill="#F4C1D2" fill-opacity=".42" d="M-80 330 C 120 270 250 400 400 360 C 290 460 110 470 -80 520Z"/>
  <path filter="url(#s16)" fill="#F4C1D2" fill-opacity=".42" d="M1160 280 C 950 230 840 370 690 340 C 800 440 980 450 1160 480Z"/>

  <!-- lower silk: folds rising behind the card -->
  <path filter="url(#s16)" fill="#B23A69" fill-opacity=".22" d="M-60 1000 C 200 900 380 1050 620 970 S 990 860 1160 930 L1160 1420 L-60 1420Z"/>
  <path filter="url(#s3)" fill="url(#silkA)" d="M-60 975 C 180 880 400 1020 640 945 S 990 830 1160 900 L1160 1420 L-60 1420Z"/>
  <path filter="url(#s3)" fill="url(#silkB)" d="M-60 1110 C 240 1020 430 1160 700 1080 S 1000 1010 1160 1060 L1160 1420 L-60 1420Z"/>
  <path filter="url(#s3)" fill="none" stroke="#FFFFFF" stroke-opacity=".8" stroke-width="3" d="M-60 977 C 180 882 400 1022 640 947 S 990 832 1160 902"/>
  <path filter="url(#s3)" fill="none" stroke="#FFFFFF" stroke-opacity=".55" stroke-width="2" d="M-60 1112 C 240 1022 430 1162 700 1082 S 1000 1012 1160 1062"/>
</svg>

<!-- RIBBON -->
<svg class="layer" viewBox="0 0 1080 1350" aria-hidden="true">
  <defs>
    <path id="sFull" d="STRAND_FULL"/>
    <path id="sFront" d="STRAND_FRONT"/>
    <linearGradient id="rib" gradientUnits="userSpaceOnUse" x1="150" y1="20" x2="470" y2="700">
      <stop offset="0" stop-color="#F9AFCB"/>
      <stop offset=".32" stop-color="#EF74A2"/>
      <stop offset=".62" stop-color="#E2468A"/>
      <stop offset="1" stop-color="#C42B6E"/>
    </linearGradient>
    <linearGradient id="fade" gradientUnits="userSpaceOnUse" x1="0" y1="150" x2="0" y2="235">
      <stop offset="0" stop-color="#000"/><stop offset="1" stop-color="#fff"/>
    </linearGradient>
    <filter id="b6" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="6"/></filter>
    <filter id="b1"><feGaussianBlur stdDeviation="1.2"/></filter>
    <filter id="b10" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="10"/></filter>
    <filter id="cast" x="-40%" y="-20%" width="180%" height="160%">
      <feDropShadow dx="6" dy="34" stdDeviation="26" flood-color="#86103F" flood-opacity=".38"/></filter>
    <filter id="cross" x="-40%" y="-40%" width="180%" height="180%">
      <feDropShadow dx="10" dy="12" stdDeviation="10" flood-color="#6E0B35" flood-opacity=".5"/></filter>
    <!-- fine diagonal weave so the satin reads as fabric, not plastic -->
    <filter id="weave" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="1.8 .09" numOctaves="2" seed="11"/>
      <feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .9 -.32"/>
    </filter>
    <mask id="mFull" maskUnits="userSpaceOnUse" x="-50" y="-50" width="700" height="800">
      <use href="#sFull" fill="none" stroke="#fff" stroke-width="W"/></mask>
    <mask id="mFront" maskUnits="userSpaceOnUse" x="-50" y="-50" width="700" height="800">
      <use href="#sFront" fill="none" stroke="#fff" stroke-width="W"/></mask>
    <mask id="mFade" maskUnits="userSpaceOnUse" x="-50" y="-50" width="700" height="800">
      <rect x="-50" y="-50" width="700" height="800" fill="url(#fade)"/></mask>
    <!-- V-notch cuts at the tail ends -->
    <mask id="mNotch" maskUnits="userSpaceOnUse" x="-50" y="-50" width="700" height="800">
      <rect x="-50" y="-50" width="700" height="800" fill="#fff"/>
      <polygon fill="#000" points="40,676 132,606 222,664 222,780 40,780"/>
      <polygon fill="#000" points="378,664 468,606 560,676 560,780 378,780"/>
    </mask>
  </defs>

  <g transform="translate(300 476) scale(.8) rotate(-4 300 360)">
    <g filter="url(#cast)"><g mask="url(#mNotch)"><use href="#sFull" fill="none" stroke="#D63A7E" stroke-width="W"/></g></g>
    <g mask="url(#mNotch)">
      <g mask="url(#mFull)">SATIN_FULL
        <!-- inside of the loop's crown sits in shade -->
        <path d="M168 108 C 176 46 246 20 300 20 C 354 20 424 46 432 108" fill="none" stroke="#7A0D3C" stroke-opacity=".18" stroke-width="40" transform="translate(0 46)" filter="url(#b10)"/>
      </g>
      <g mask="url(#mFade)"><g filter="url(#cross)"><g mask="url(#mFront)">SATIN_FRONT</g></g></g>
    </g>
  </g>
</svg>

<!-- GRAIN over everything except type -->
<svg class="layer grain" viewBox="0 0 1080 1350" aria-hidden="true">
  <filter id="noise"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="3" stitchTiles="stitch"/>
    <feColorMatrix values="0 0 0 0 .52  0 0 0 0 .22  0 0 0 0 .32  0 0 0 .26 0"/></filter>
  <rect width="1080" height="1350" filter="url(#noise)"/>
</svg>

<svg class="logo" viewBox="50 50 1110 400" role="img" aria-label="ZAD"><path fill="#044132" fill-rule="evenodd" d="LOGO"/></svg>
<h1><span class="l1">Pink</span><span class="l2">October</span></h1>
<p class="tagline">Together for awareness<i>·</i>Together for hope</p>
<div class="card">
  <p class="l1">ZAD AI supports Breast Cancer Awareness Month</p>
  <p class="l2">Awareness • Support • Prevention</p>
</div>

</div></body></html>
"""

html = (
    TEMPLATE.replace("SATIN_FULL", satin("sFull"))
    .replace("SATIN_FRONT", satin("sFront"))
    .replace("STRAND_FULL", STRAND_FULL)
    .replace("STRAND_FRONT", STRAND_FRONT)
    .replace('stroke-width="W"', f'stroke-width="{W}"')
    .replace("FRAUNCES", font_b64("Fraunces-Italic-latin.woff2"))
    .replace("INTER", font_b64("Inter-latin.woff2"))
    .replace("LOGO", LOGO_PATH)
)
(HERE / "pink-october.html").write_text(html)
print("wrote pink-october.html", len(html) // 1024, "KB")
