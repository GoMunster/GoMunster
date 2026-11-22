#!/usr/bin/env python3
"""Regenerates every SVG in ../assets. Edit the CONFIG block, then run:  python3 tools/generate.py"""
import math, os

# ============================ CONFIG (edit me) ============================
NAME      = "YOUR NAME"
TAGLINE   = "dev / maker / artist-in-progress"
MARQUEE   = "<3 game dev   <3 web projects   <3 microcontrollers   <3 art (loading...)   "
BREADCRUMB= "me / projects / github"
# (title, stack) for each card. Keep 3 per row for a tidy grid.
PROJECTS = {
  "game":  [("game name","godot"), ("another game","unity"), ("next game","wip")],
  "web":   [("my website","html/css"), ("web project","react"), ("web toy","js")],
  "micro": [("blinky thing","esp32"), ("pocket gadget","arduino"), ("sensor pal","pico")],
  "art":   [("sketchbook","soon"), ("pixel art","soon"), ("illustrations","soon")],
}
# ==========================================================================

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets')
os.makedirs(OUT, exist_ok=True)
FONT = "font-family=\"'Trebuchet MS','Comic Sans MS','Segoe UI',Verdana,sans-serif\""
OL='#2b2352'; BG='#17122b'; PINK='#ff9bd0'; HOT='#f06bb0'; LIL='#b9a0ff'; YEL='#ffd36b'; MINT='#7fdba0'
SKY='#bfe6ff'; CREAM='#fff1dc'; PEACH='#ffd9b8'; SCR='#3d3d70'; DIMD='#2a2350'
esc=lambda t:t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def G(inner,x=0,y=0,s=1,sw=3,extra=''):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="{OL}" stroke-width="{sw/s:.2f}" '
            f'stroke-linejoin="round" stroke-linecap="round" {extra}>{inner}</g>')
def star5(r,fill):
    pts=[]
    for i in range(10):
        a=-math.pi/2+i*math.pi/5; rr=r if i%2==0 else r*0.52
        pts.append(f'{rr*math.cos(a):.1f},{rr*math.sin(a):.1f}')
    return f'<polygon points="{" ".join(pts)}" fill="{fill}"/>'
def heart_s(r,fill):
    return (f'<path d="M0 {r*.95:.1f} C{-r*1.7:.1f} {-r*.1:.1f} {-r*.75:.1f} {-r*1.15:.1f} 0 {-r*.4:.1f} '
            f'C{r*.75:.1f} {-r*1.15:.1f} {r*1.7:.1f} {-r*.1:.1f} 0 {r*.95:.1f}Z" fill="{fill}"/>')
def twinkle(x,y,r,i,fill='#ffe9a8'):
    return (f'<path d="M{x} {y-r} Q{x} {y} {x+r} {y} Q{x} {y} {x} {y+r} Q{x} {y} {x-r} {y} Q{x} {y} {x} {y-r}Z" fill="{fill}">'
            f'<animate attributeName="opacity" values="0.2;1;0.2" dur="{2+i*0.3:.1f}s" begin="{i*0.4:.1f}s" repeatCount="indefinite"/></path>')
def check(x,y,s=1):
    return G(f'<rect x="-10" y="-10" width="20" height="20" rx="6" fill="{MINT}"/><path d="M-5 0 L-1.5 4 L5.5 -4" fill="none" stroke="#fff" stroke-width="3.2"/>',x,y,s,2.5)

# ---- critters / stickers (drawn around 0,0) ----
def bunny(): return (f'<ellipse cx="-9" cy="-24" rx="6.5" ry="15" fill="#fff"/><ellipse cx="-9" cy="-23" rx="3" ry="9" fill="{PINK}" stroke="none"/>'
    f'<ellipse cx="9" cy="-24" rx="6.5" ry="15" fill="#fff"/><ellipse cx="9" cy="-23" rx="3" ry="9" fill="{PINK}" stroke="none"/>'
    f'<ellipse cx="0" cy="0" rx="19" ry="15" fill="#fff"/><circle cx="-7" cy="-1" r="2.2" fill="{OL}" stroke="none"/><circle cx="7" cy="-1" r="2.2" fill="{OL}" stroke="none"/>'
    f'<circle cx="-12" cy="4" r="3" fill="{PINK}" stroke="none"/><circle cx="12" cy="4" r="3" fill="{PINK}" stroke="none"/><path d="M-2 4 L2 4 L0 7Z" fill="{HOT}" stroke-width="1.5"/>')
def duck(): return (f'<ellipse cx="0" cy="8" rx="15" ry="10" fill="{YEL}"/><circle cx="6" cy="-6" r="9" fill="{YEL}"/>'
    f'<ellipse cx="15" cy="-4" rx="6" ry="3.2" fill="#ffa94d"/><circle cx="8" cy="-8" r="1.9" fill="{OL}" stroke="none"/><path d="M-12 6 Q-4 14 4 8" fill="none" stroke-width="2"/>')
def frog(): return (f'<ellipse cx="0" cy="6" rx="17" ry="10" fill="{MINT}"/><circle cx="-8" cy="-3" r="6.5" fill="{MINT}"/><circle cx="8" cy="-3" r="6.5" fill="{MINT}"/>'
    f'<circle cx="-8" cy="-3" r="3.2" fill="#fff" stroke="none"/><circle cx="8" cy="-3" r="3.2" fill="#fff" stroke="none"/>'
    f'<circle cx="-8" cy="-3" r="1.6" fill="{OL}" stroke="none"/><circle cx="8" cy="-3" r="1.6" fill="{OL}" stroke="none"/><path d="M-5 8 Q0 12 5 8" fill="none" stroke-width="2"/>')
def cat(): return (f'<polygon points="-21,-8 -19,-28 -4,-17" fill="{LIL}"/><polygon points="21,-8 19,-28 4,-17" fill="{LIL}"/><ellipse cx="0" cy="0" rx="23" ry="19" fill="{LIL}"/>'
    f'<ellipse cx="-9" cy="-2" rx="5.5" ry="6" fill="#ffe27a" stroke-width="1.8"/><ellipse cx="9" cy="-2" rx="5.5" ry="6" fill="#ffe27a" stroke-width="1.8"/>'
    f'<ellipse cx="-9" cy="-2" rx="1.7" ry="4.2" fill="{OL}" stroke="none"/><ellipse cx="9" cy="-2" rx="1.7" ry="4.2" fill="{OL}" stroke="none"/>'
    f'<path d="M-2.5 6 L2.5 6 L0 9Z" fill="{PINK}" stroke-width="1.5"/><path d="M-15 8 L-27 6 M-15 11 L-26 14 M15 8 L27 6 M15 11 L26 14" fill="none" stroke-width="1.6"/>')
def tea(): return (f'<path d="M5 -28 L12 -52" stroke="{LIL}" stroke-width="7" fill="none"/><path d="M5 -28 L12 -52" stroke-width="1" fill="none" stroke="{OL}" opacity="0"/>'
    f'<path d="M-18 -20 L18 -20 L14 32 Q0 37 -14 32 Z" fill="#ffe0f0"/><path d="M-16.4 0 L16.4 0 L14 32 Q0 37 -14 32 Z" fill="{PINK}" stroke="none"/>'
    f'<path d="M-18 -20 L18 -20 L14 32 Q0 37 -14 32 Z" fill="none"/><rect x="-21" y="-28" width="42" height="9" rx="4.5" fill="{LIL}"/>'
    + ''.join(f'<circle cx="{x}" cy="{y}" r="4.2" fill="#7a3d86" stroke-width="1.8"/>' for x,y in ((-8,25),(0,27),(8,25),(-4,18),(5,18)))
    + f'<path d="M-10 -10 L-8 6" stroke="#fff" stroke-width="2.5" opacity="0.7" fill="none"/>')
def strawberry(): return (f'<path d="M-15 -8 C-15 -18 15 -18 15 -8 C15 6 7 17 0 20 C-7 17 -15 6 -15 -8Z" fill="#ff6f91"/>'
    f'<path d="M-11 -11 L-5 -18 L0 -12 L5 -18 L11 -11 L0 -6Z" fill="{MINT}"/>'
    + ''.join(f'<ellipse cx="{x}" cy="{y}" rx="1.4" ry="2" fill="#ffe2ea" stroke="none"/>' for x,y in ((-7,-1),(1,1),(-3,8),(7,-4),(-9,5),(5,9),(0,-4))))
def bolt(): return f'<polygon points="2,-20 -12,3 -2,3 -6,20 12,-6 2,-6" fill="{YEL}"/>'
def squig(): return f'<path d="M-24 6 L-16 -6 L-8 6 L0 -6 L8 6 L16 -6 L24 6" fill="none" stroke-width="7" stroke="{OL}"/><path d="M-24 6 L-16 -6 L-8 6 L0 -6 L8 6 L16 -6 L24 6" fill="none" stroke-width="3" stroke="{LIL}"/>'
def lock(): return (f'<path d="M-7 -2 V-9 a7 7 0 0 1 14 0 V-2" fill="none" stroke-width="3.4"/><rect x="-12" y="-2" width="24" height="19" rx="5" fill="{LIL}"/>'
    f'<circle cx="0" cy="6" r="2.4" fill="{OL}" stroke="none"/><rect x="-1" y="6" width="2" height="6" fill="{OL}" stroke="none"/>')
def controller(): return (f'<rect x="-22" y="-13" width="44" height="26" rx="13" fill="{PINK}"/><rect x="-16" y="-2" width="10" height="4" rx="1" fill="{OL}" stroke="none"/>'
    f'<rect x="-13" y="-5" width="4" height="10" rx="1" fill="{OL}" stroke="none"/><circle cx="9" cy="-3" r="3.2" fill="{YEL}" stroke-width="1.6"/><circle cx="15" cy="2" r="3.2" fill="{YEL}" stroke-width="1.6"/>')
def browser(): return (f'<rect x="-22" y="-16" width="44" height="32" rx="6" fill="{CREAM}"/><path d="M-22 -7 H22" fill="none" stroke-width="2"/>'
    + ''.join(f'<circle cx="{x}" cy="-11.5" r="1.7" fill="{c}" stroke="none"/>' for x,c in ((-16,HOT),(-10,YEL),(-4,MINT)))
    + f'<g transform="translate(0 4)" stroke-width="2">{heart_s(6.5,PINK)}</g>')
def chip(): return (''.join(f'<path d="M-18 {k} H-14 M14 {k} H18 M{k} -18 V-14 M{k} 14 V18" fill="none"/>' for k in (-8,0,8))
    + f'<rect x="-14" y="-14" width="28" height="28" rx="5" fill="{MINT}"/><rect x="-6" y="-6" width="12" height="12" rx="2" fill="{LIL}" stroke-width="2"/>')
ICON={'game':controller,'web':browser,'micro':chip,'art':lock}
def icon(k,x,y,s): return G(ICON[k](),x,y,s)
def wrap(w,h,body,defs=''):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" {FONT}>'
            f'<defs>{defs}</defs>{body}</svg>')
def save(n,s): open(os.path.join(OUT,n),'w').write(s)
def spiral(cx,cy,R,turns=2.6):
    pts=[]; n=90
    for i in range(n+1):
        t=i/n*turns*2*math.pi; r=R*t/(turns*2*math.pi)
        pts.append(f'{cx+r*math.cos(t):.1f},{cy+r*math.sin(t):.1f}')
    return ('<polyline points="'+' '.join(pts)+f'" fill="none" stroke="#dcd6ff" stroke-width="2" stroke-linecap="round">'
            f'<animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="360 {cx} {cy}" dur="24s" repeatCount="indefinite"/></polyline>')

# ============================ BANNER ============================
W,H=960,384
defs=f'<pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="11" cy="11" r="1.4" fill="{DIMD}"/></pattern><clipPath id="mq"><rect x="692" y="240" width="206" height="24"/></clipPath>'
b=f'<rect width="{W}" height="{H}" rx="28" fill="{BG}"/><rect width="{W}" height="{H}" rx="28" fill="url(#dots)"/>'
b+=f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="27" fill="none" stroke="{PINK}" stroke-width="3"/>'
for i,(x,y,r) in enumerate([(30,40,9),(500,34,7),(520,170,6),(930,360,8),(480,372,6),(24,350,7),(930,30,7)]): b+=twinkle(x,y,r,i)
# console
b+=G(f'<rect x="34" y="332" width="372" height="30" rx="14" fill="{LIL}"/>')
b+=G(f'<rect x="40" y="56" width="360" height="168" rx="24" fill="{PINK}"/><rect x="58" y="72" width="324" height="134" rx="12" fill="#ffc9e6" stroke-width="2.5"/>'
     f'<rect x="76" y="84" width="288" height="94" rx="6" fill="{SCR}" stroke-width="2.5"/>')
b+=f'<text x="90" y="101" font-size="11" fill="#e8e2ff">{esc(BREADCRUMB)}</text>'
b+=spiral(150,138,24)+spiral(290,136,22)
b+=f'<text x="150" y="172" font-size="9" fill="#b9b3e6" text-anchor="middle">games &amp; web</text><text x="290" y="172" font-size="9" fill="#b9b3e6" text-anchor="middle">chips &amp; art</text>'
b+=f'<circle cx="215" cy="136" r="1.6" fill="#fff"/><circle cx="330" cy="104" r="1.4" fill="#fff"/><circle cx="108" cy="112" r="1.4" fill="#fff"/>'
for x in (196,220,244): b+=G(heart_s(6,HOT),x,193,1,2)
b+=G(f'<rect x="76" y="218" width="22" height="30" rx="9" fill="{LIL}"/><rect x="342" y="218" width="22" height="30" rx="9" fill="{LIL}"/><rect x="92" y="222" width="256" height="22" rx="8" fill="#f58cc4"/>')
b+=G(f'<rect x="24" y="240" width="392" height="104" rx="30" fill="{PINK}"/>')
b+=G(f'<rect x="76" y="282" width="48" height="20" rx="6" fill="{YEL}"/><rect x="90" y="268" width="20" height="48" rx="6" fill="{YEL}"/><rect x="91.5" y="283.5" width="17" height="17" fill="{YEL}" stroke="none"/><circle cx="100" cy="292" r="3" fill="#f0b840" stroke="none"/>')
b+=''.join(f'<circle cx="{176+i*10}" cy="{272+j*10}" r="1.8" fill="#e86ba8"/>' for i in range(4) for j in range(4))
b+=G(f'<rect x="296" y="274" width="104" height="40" rx="20" fill="#ffc9e6" transform="rotate(-16 348 294)"/><circle cx="324" cy="302" r="11" fill="{YEL}"/><circle cx="372" cy="288" r="11" fill="{YEL}"/>')
b+=f'<text x="324" y="306" font-size="11" font-weight="bold" fill="{OL}" text-anchor="middle">B</text><text x="372" y="292" font-size="11" font-weight="bold" fill="{OL}" text-anchor="middle">A</text>'
b+=G(f'<ellipse cx="132" cy="330" rx="12" ry="7" fill="{YEL}"/><ellipse cx="162" cy="330" rx="12" ry="7" fill="{YEL}"/>',sw=2.5)
b+=G(strawberry(),62,322,1,2.5)+G(bolt(),214,308,1,2.5)+G(squig(),284,326,0.9,2.5)+G(star5(10,YEL),256,264,1,2.5)+G(star5(8,YEL),50,262,1,2.5)
# critters on lid
b+=G(frog(),110,40,1,2.5)+G(duck(),160,38,1,2.5)+G(bunny(),338,41,1,2.5)
# charms (sway)
beads=''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="{c}" stroke="{OL}" stroke-width="2"/>' for x,y,c in ((420,243,PINK),(431,247,YEL),(441,251,LIL),(449,257,PINK)))
beads+=''.join(f'<circle cx="{x}" cy="{y}" r="3" fill="{c}" stroke="{OL}" stroke-width="1.8"/>' for x,y,c in ((456,320,YEL),(454,328,PINK)))
ch=f'<path d="M410 238 Q440 244 456 262" fill="none" stroke="{OL}" stroke-width="2"/>'+beads+G(tea(),458,286,1,2.5)+G(cat(),452,358,0.9,2.5)
b+=f'<g><animateTransform attributeName="transform" type="rotate" values="-2.5 410 238;2.5 410 238;-2.5 410 238" keyTimes="0;0.5;1" dur="4s" repeatCount="indefinite"/>{ch}</g>'
# HUD
hx=540
b+=f'<rect x="{hx}" y="44" width="380" height="56" rx="14" fill="{CREAM}" stroke="{OL}" stroke-width="3"/>'
b+=f'<text x="{hx+20}" y="83" font-size="28" font-weight="bold" fill="{OL}" letter-spacing="1">{esc(NAME)}</text>'
b+=G(f'<polygon points="0,-13 10,-3 0,13 -10,-3" fill="{LIL}"/><path d="M-10 -3 H10" fill="none" stroke-width="1.5"/>',890,72,1,2.5)
b+=f'<rect x="{hx}" y="114" width="300" height="40" rx="12" fill="{SKY}" stroke="{OL}" stroke-width="3"/><text x="{hx+16}" y="140" font-size="14" fill="{OL}">{esc(TAGLINE)}</text>'
b+=f'<rect x="{hx}" y="168" width="300" height="38" rx="12" fill="{CREAM}" stroke="{OL}" stroke-width="3"/>'
b+=f'<rect x="{hx+4}" y="172" width="180" height="30" rx="9" fill="{YEL}"><animate attributeName="width" values="150;220;150" dur="6s" repeatCount="indefinite"/></rect>'
b+=f'<text x="{hx+16}" y="193" font-size="14" font-weight="bold" fill="{OL}">loading portfolio...</text>'
b+=G(star5(15,YEL),872,188,1,2.8)+G(heart_s(9,PINK),872,134,1,2.5)
# mp3 pill
b+=f'<rect x="{hx}" y="224" width="380" height="64" rx="32" fill="#cdbfff" stroke="{OL}" stroke-width="3"/>'
b+=G(f'<rect x="-10" y="-9" width="3" height="18" fill="{OL}"/><path d="M8 -9 L-6 0 L8 9Z" fill="{OL}"/>',574,256,1,2)
b+=G(f'<circle r="18" fill="{PINK}"><animate attributeName="r" values="18;19.5;18" dur="1.6s" repeatCount="indefinite"/></circle><path d="M-5 -8 L9 0 L-5 8Z" fill="{OL}"/>',612,256,1,3)
b+=G(f'<path d="M-8 -9 L6 0 L-8 9Z" fill="{OL}"/><rect x="7" y="-9" width="3" height="18" fill="{OL}"/>',650,256,1,2)
b+=f'<rect x="684" y="234" width="222" height="44" rx="12" fill="{SCR}" stroke="{OL}" stroke-width="2.5"/>'
L=round(len(MARQUEE)*7.4); mq=esc(MARQUEE)
b+=(f'<g clip-path="url(#mq)" fill="#fde6f4" font-size="13"><g><animateTransform attributeName="transform" type="translate" from="0 0" to="-{L} 0" dur="14s" repeatCount="indefinite"/>'
    f'<text x="696" y="256" textLength="{L}" lengthAdjust="spacing">{mq}</text><text x="{696+L}" y="256" textLength="{L}" lengthAdjust="spacing">{mq}</text></g></g>')
b+=f'<rect x="696" y="266" width="196" height="4" rx="2" fill="#5a5a96"/><rect x="696" y="266" width="8" height="4" rx="2" fill="{PINK}"><animate attributeName="width" values="8;196" dur="24s" repeatCount="indefinite"/></rect>'
# category stickers
for i,(k,lab) in enumerate((('game','games'),('web','web'),('micro','chips'),('art','art'))):
    x=hx+i*100
    b+=f'<rect x="{x}" y="304" width="80" height="68" rx="14" fill="{CREAM if k!="art" else "#e6dcff"}" stroke="{OL}" stroke-width="3"{" stroke-dasharray=\"6 5\"" if k=="art" else ""}/>'
    b+=f'<g><animateTransform attributeName="transform" type="translate" values="0 0;0 -3;0 0" dur="{2+i*0.3:.1f}s" repeatCount="indefinite"/>{icon(k,x+40,331,0.85)}</g>'
    b+=f'<text x="{x+40}" y="363" font-size="12" font-weight="bold" fill="{OL}" text-anchor="middle">{lab}</text>'
    if k!='art': b+=check(x+70,310,0.75)
save('banner.svg',wrap(W,H,b,defs))

# ============================ TAB HEADERS ============================
def tab(fn,k,title,state,ok=True):
    w,h=830,76
    s=f'<rect x="2" y="2" width="{w-4}" height="{h-4}" rx="22" fill="{PEACH}" stroke="{OL}" stroke-width="3"/>'
    s+=f'<rect x="14" y="10" width="56" height="56" rx="16" fill="{CREAM}" stroke="{OL}" stroke-width="3"/>'+icon(k,42,38,0.78)
    s+=f'<text x="90" y="48" font-size="27" font-weight="bold" fill="{OL}">{title}</text>'
    s+=twinkle(560,26,8,1,'#fff')+twinkle(600,50,6,2,'#fff')+twinkle(520,48,5,3,'#fff')
    s+=f'<rect x="690" y="22" width="126" height="32" rx="16" fill="{MINT if ok else LIL}" stroke="{OL}" stroke-width="2.5"/>'
    s+=f'<text x="753" y="44" font-size="14" font-weight="bold" fill="{OL}" text-anchor="middle">{state}</text>'
    save(fn,wrap(w,h,s))
tab('tab_game.svg','game','game dev','unlocked'); tab('tab_web.svg','web','websites','unlocked')
tab('tab_micro.svg','micro','microcontrollers','unlocked'); tab('tab_art.svg','art','art','coming soon',False)

# ============================ CARDS ============================
BGC={'game':'#ffc2e0','web':SKY,'micro':'#c4f2dc','art':'#d9ccff'}
for k,items in PROJECTS.items():
    for n,(title,stack) in enumerate(items,1):
        locked=(k=='art'); w,h=230,250
        s=f'<rect x="3" y="3" width="{w-6}" height="{h-6}" rx="22" fill="{"#e6dcff" if locked else CREAM}" stroke="{OL}" stroke-width="3"{" stroke-dasharray=\"8 6\"" if locked else ""}/>'
        s+=f'<rect x="22" y="20" width="186" height="116" rx="16" fill="{BGC[k]}" stroke="{OL}" stroke-width="2.5"/>'
        s+=twinkle(40,38,6,n,'#fff')+twinkle(190,44,5,n+1,'#fff')
        s+=f'<g><animateTransform attributeName="transform" type="translate" values="0 0;0 -4;0 0" dur="{2+n*0.35:.2f}s" repeatCount="indefinite"/>{icon(k,115,78,2.3)}</g>'
        if not locked: s+=check(194,122,1.2)
        s+=f'<text x="115" y="166" font-size="20" font-weight="bold" fill="{OL}" text-anchor="middle">{esc(title)}</text>'
        s+=f'<rect x="45" y="184" width="140" height="34" rx="17" fill="{SKY if not locked else "#cdbfff"}" stroke="{OL}" stroke-width="2.5"/>'
        s+=f'<text x="115" y="207" font-size="15" fill="{OL}" text-anchor="middle">{esc(stack)}</text>'
        save(f'card_{k}_{n}.svg',wrap(w,h,s))

# ============================ PET SCENE ============================
PETG=[".XX.....XX.",".Xi.....iX.",".XXXXXXXXX.","XXXXXXXXXXX","XXXXXXXXXXX","XXcXXmXXcXX","XXXXXXXXXXX",".XXXXXXXXX.","..XX...XX.."]
def pet(x,y,s):
    cm={'X':'#ffc9e6','i':HOT,'c':HOT,'m':SCR}
    r=''.join(f'<rect x="{x+c*s}" y="{y+r_*s}" width="{s}" height="{s}" fill="{cm[ch]}"/>' for r_,row in enumerate(PETG) for c,ch in enumerate(row) if ch in cm)
    def eye(cx): return (f'<rect x="{x+cx*s}" y="{y+3*s}" width="{s}" height="{2*s}" fill="{SCR}"><animate attributeName="y" values="{y+3*s};{y+3*s};{y+4*s+s//2};{y+3*s}" keyTimes="0;0.9;0.95;1" dur="4s" repeatCount="indefinite"/>'
        f'<animate attributeName="height" values="{2*s};{2*s};{s//2};{2*s}" keyTimes="0;0.9;0.95;1" dur="4s" repeatCount="indefinite"/></rect>')
    return f'<g shape-rendering="crispEdges">{r}{eye(3)}{eye(7)}</g>'
PH=[".XX.XX.","XXXXXXX","XXXXXXX",".XXXXX.","..XXX..","...X..."]
def phe(x,y,s,c): return '<g shape-rendering="crispEdges">'+''.join(f'<rect x="{x+i*s}" y="{y+j*s}" width="{s}" height="{s}" fill="{c}"/>' for j,row in enumerate(PH) for i,ch in enumerate(row) if ch=='X')+'</g>'
w,h=830,230
s=f'<rect x="2" y="2" width="{w-4}" height="{h-4}" rx="34" fill="{PINK}" stroke="{OL}" stroke-width="3"/>'
s+=f'<rect x="22" y="22" width="{w-44}" height="{h-44}" rx="18" fill="{SCR}" stroke="{OL}" stroke-width="3"/>'
s+=f'<rect x="40" y="176" width="{w-80}" height="3" rx="1.5" fill="#5a5a96"/>'
s+=f'<g fill="#55558f"><animateTransform attributeName="transform" type="translate" from="-120 0" to="840 0" dur="40s" repeatCount="indefinite"/><rect x="0" y="46" width="60" height="12" rx="6"/><rect x="12" y="36" width="36" height="12" rx="6"/></g>'
s+=(f'<g><animateTransform attributeName="transform" type="translate" values="60 0;340 0;340 0;60 0;60 0" keyTimes="0;0.4;0.5;0.9;1" dur="14s" repeatCount="indefinite"/>'
    f'<rect x="-8" y="46" width="116" height="30" rx="10" fill="{CREAM}" stroke="{OL}" stroke-width="2.5"/><path d="M30 76 L42 76 L37 84Z" fill="{CREAM}" stroke="{OL}" stroke-width="2.5"/><rect x="31" y="74" width="10" height="4" fill="{CREAM}"/>'
    f'<text x="50" y="67" font-size="15" font-weight="bold" fill="{OL}" text-anchor="middle">welcome!!</text>'
    f'<g><animateTransform attributeName="transform" type="translate" values="0 0;0 -8;0 0" keyTimes="0;0.5;1" calcMode="discrete" dur="0.6s" repeatCount="indefinite"/>{pet(6,104,8)}</g></g>')
sx=530
s+=f'<rect x="{sx-22}" y="40" width="3" height="146" rx="1.5" fill="#5a5a96"/><text x="{sx}" y="62" font-size="14" font-weight="bold" letter-spacing="2" fill="{YEL}">STATUS</text>'
for i,(lab,n) in enumerate((('happy',5),('snacks',4),('sleep',2))):
    y=84+i*32
    s+=f'<text x="{sx}" y="{y+12}" font-size="14" fill="#e8e2ff">{lab}</text>'
    for k in range(5): s+=phe(sx+90+k*34,y,3,PINK if k<n else '#5a5a96')
s+=f'<text x="{sx}" y="{84+3*32+12}" font-size="14" fill="#e8e2ff">code lv</text><text x="{sx+90}" y="{84+3*32+12}" font-size="15" font-weight="bold" fill="#fde6f4">99 (leveling up)</text>'
s+=G(star5(11,YEL),w-34,34,1,2.5)+G(heart_s(8,HOT),34,h-34,1,2.5)
save('pet.svg',wrap(w,h,s))

# ============================ DIVIDER ============================
w,h=830,34; s=''
for i in range(11):
    x=40+i*75
    st=(star5(7,YEL) if i%2 else heart_s(7,PINK))
    s+=f'<g><animateTransform attributeName="transform" type="translate" values="0 0;0 -3;0 0" dur="{1.6+i*0.15:.2f}s" repeatCount="indefinite"/>{G(st,x,17,1,2)}</g>'
save('divider.svg',wrap(w,h,s))

# ============================ FOOTER ============================
w,h=830,170
s=f'<rect x="2" y="2" width="{w-4}" height="{h-4}" rx="26" fill="{PEACH}" stroke="{OL}" stroke-width="3"/>'
s+=f'<text x="415" y="70" font-size="30" font-weight="bold" fill="{OL}" text-anchor="middle">thanks for visiting!</text>'
s+=f'<text x="415" y="102" font-size="15" fill="{OL}" text-anchor="middle">star a repo to feed the pet</text>'
for i in range(5): s+=G(heart_s(8,PINK if i<4 else '#e6dcff'),363+i*26,134,1,2.5)
s+=G(bunny(),90,112,1.1,2.5)+G(frog(),170,128,1.1,2.5)+G(duck(),660,126,1.1,2.5)+G(cat(),748,118,1,2.5)
s+=twinkle(300,40,7,1,'#fff')+twinkle(540,38,6,2,'#fff')
save('footer.svg',wrap(w,h,s))
print('generated',len(os.listdir(OUT)),'svgs')
