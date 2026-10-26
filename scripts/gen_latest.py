#!/usr/bin/env python3
"""
Generate latest.json for anipix.me from the AniPix Blog and Orbit (space) indexes.

Usage:
  python gen_latest.py            # read local clones in /scratch/work
  python gen_latest.py --remote   # fetch the live sites (for GitHub Actions)
  python gen_latest.py --remote --static   # also rewrite the static cards in index.html
"""
import re, json, html, os, sys, urllib.request

ROOT = "/scratch/work"
OUT = os.path.join(ROOT, "landing")
BLOG_BASE = "https://blog.anipix.me"
SPACE_BASE = "https://space.anipix.me"

def read(url, local):
    if "--remote" in sys.argv:
        req = urllib.request.Request(url, headers={"User-Agent": "AniPixBot/1.0"})
        return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
    with open(local, encoding="utf-8") as f:
        return f.read()

def pretty_date(d):
    """2026-10-20 -> 20 October 2026 (leave anything else alone)."""
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", (d or "").strip())
    if not m:
        return d or ""
    y, mo, da = m.groups()
    months = ["January","February","March","April","May","June",
              "July","August","September","October","November","December"]
    return f"{int(da)} {months[int(mo)-1]} {y}"

def clean(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()

def blog_latest(n=6):
    h = read(f"{BLOG_BASE}/index.html", os.path.join(ROOT, "blogrepo/index.html"))
    out = []
    for m in re.finditer(r'<div class="card">(.*?)</div>\s*</div>', h, re.S):
        c = m.group(1)
        u = re.search(r'<h3><a href="([^"]+)"', c)
        t = re.search(r'<h3><a href="[^"]+">(.*?)</a></h3>', c, re.S)
        img = re.search(r'<img src="([^"]+)"', c)
        ex = re.search(r"</h3>\s*<p>(.*?)</p>", c, re.S)
        dt = re.search(r'<div class="meta"><span>(.*?)</span>', c)
        if not (u and t):
            continue
        slug = u.group(1).split("/")[-1]
        out.append({
            "src": "blog",
            "url": f"{BLOG_BASE}/{u.group(1).lstrip('/')}",
            "img": f"{BLOG_BASE}/{img.group(1).lstrip('/')}" if img else "",
            "title": clean(t.group(1)),
            "excerpt": clean(ex.group(1)) if ex else "",
            "date": clean(dt.group(1)) if dt else "",
        })
        if len(out) >= n:
            break
    return out

def space_latest(n=6):
    h = read(f"{SPACE_BASE}/index.html", os.path.join(ROOT, "orbitrepo/index.html"))
    # slug -> lastmod from the sitemap
    dates = {}
    try:
        sm = read(f"{SPACE_BASE}/sitemap.xml", os.path.join(ROOT, "orbitrepo/sitemap.xml"))
        for m in re.finditer(r"<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>", sm):
            slug = m.group(1).rstrip("/").split("/")[-1].replace(".html", "")
            dates[slug] = m.group(2)
    except Exception:
        pass
    out = []
    for m in re.finditer(
        r'<a class="card" href="([^"]+)"><span class="k">(.*?)</span><h3>(.*?)</h3><p>(.*?)</p></a>',
        h, re.S):
        url, kicker, title, ex = m.groups()
        slug = url.split("/")[-1].replace(".html", "")
        out.append({
            "src": "space",
            "url": f"{SPACE_BASE}{url}",
            "img": f"{SPACE_BASE}/assets/img/{slug}-1.webp",
            "title": clean(title),
            "excerpt": clean(ex),
            "kicker": clean(kicker),
            "date": pretty_date(dates.get(slug, "")),
        })
        if len(out) >= n:
            break
    return out

def card_html(c):
    label = "Blog" if c["src"] == "blog" else "Orbit"
    date = c.get("date", "")
    date_html = f'<span class="dt">{date}</span>' if date else '<span class="dt">&nbsp;</span>'
    return (f'    <a class="lcard" href="{c["url"]}">\n'
            f'      <div class="th"><span class="src {c["src"]}">{label}</span>'
            f'<img src="{c["img"]}" alt="" loading="lazy"></div>\n'
            f'      <div class="bd"><h3>{html.escape(c["title"])}</h3>'
            f'<p>{html.escape(c["excerpt"])}</p>{date_html}</div>\n'
            f'    </a>')

def main():
    blog = blog_latest(6)
    space = space_latest(6)
    data = {"generated": __import__("datetime").date.today().isoformat(),
            "blog": blog, "space": space}
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "latest.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f"latest.json written — blog {len(blog)}, space {len(space)}")
    for c in blog + space:
        print(f"  [{c['src']:5}] {c['title'][:58]}  {c.get('date','')}")

    if "--static" in sys.argv and blog and space:
        p = os.path.join(OUT, "index.html")
        h = open(p, encoding="utf-8").read()
        blocks = re.findall(r'  <div class="latest">.*?\n  </div>', h, re.S)
        if len(blocks) == 2:
            new1 = '  <div class="latest">\n' + "\n".join(card_html(c) for c in blog) + "\n  </div>"
            new2 = '  <div class="latest">\n' + "\n".join(card_html(c) for c in space) + "\n  </div>"
            h = h.replace(blocks[0], new1, 1)
            h = h.replace(blocks[1], new2, 1)
            open(p, "w", encoding="utf-8").write(h)
            print("index.html static cards rewritten")
        else:
            print(f"WARNING: expected 2 .latest blocks, found {len(blocks)}")

if __name__ == "__main__":
    main()
