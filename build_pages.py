# -*- coding: utf-8 -*-
import re, glob
import pages1, pages2

TPL = open("anime-wallpaper-guide.html", encoding="utf-8").read()
HEAD = TPL[:TPL.index("<nav>")]
NAV  = TPL[TPL.index("<nav>"):TPL.index("<main")]
FOOT = TPL[TPL.index("<footer>"):]

# extra sections to lift the shorter pages above ~750 words
EXTRA = {
 "set-wallpaper-realme-oppo": """
<h2>Folder icons and the app drawer</h2>
<p>ColorOS draws folder icons as a translucent panel over the wallpaper. On a detailed image this panel is barely visible and the folder contents become hard to read. There is a setting to make the panel more opaque, and it is worth turning on if you insist on a busy wallpaper rather than switching to a calmer one.</p>
<h2>What happens when you change your screen resolution</h2>
<p>Some realme and OPPO phones let you switch between FHD+ and HD+ in display settings. If you set a wallpaper at FHD+ and then drop to HD+, the launcher keeps the old crop and the wallpaper is re-scaled. It usually looks fine, but if you notice softness after changing resolution, re-set the wallpaper to force a fresh crop.</p>
""",
 "set-wallpaper-iphone": """
<h2>Wallpaper pairs and focus modes</h2>
<p>iOS lets you tie a wallpaper pair to a Focus mode, so switching to Work or Sleep changes the lock screen along with the notifications. It is a genuinely useful feature and it is buried: you set it inside the Focus mode's settings, not in the wallpaper menu.</p>
<p>The catch is that each Focus mode needs its own wallpaper pair, and iOS will not let you reuse a pair you have already assigned. If a wallpaper seems to be "missing" after you set up a Focus mode, that is where it went.</p>
<h2>Do wallpapers sync between devices</h2>
<p>Wallpaper choices do not sync between an iPhone and an iPad, and they do not survive a restore from a backup that was taken before you set them. Keeping the original image in Files, or in an album that is set to download originals rather than optimise storage, is the only reliable way to get it back.</p>
""",
 "wallpaper-size-calculator": """
<h2>Why the same wallpaper looks different on two phones</h2>
<p>Two phones can both be described as "1080p" and still show the same image differently, because 1080p only fixes the width. A 1080 by 2400 phone and a 1080 by 1920 phone have different heights, and the taller one crops more from the top and bottom of a 16:9 image.</p>
<p>This is why a wallpaper that looks perfect on an older phone can look zoomed in on a new one, even though both are the same width. The aspect ratio moved, not the resolution.</p>
<h2>Screen density and why it matters</h2>
<p>Density is the number of physical pixels per inch. Two phones with the same pixel resolution but different physical sizes have different densities, so an image that is one-pixel-per-pixel on a small screen is stretched across more physical area on a large one.</p>
<p>In practice: if you are choosing between two files of the same image, take the larger one. Android will downscale a big image cleanly. It cannot invent detail when upscaling a small one.</p>
""",
 "live-wallpaper-not-working": """
<h2>How to check whether a clip is playable before setting it</h2>
<p>Most gallery apps will play an MP4 on tap. If the file plays smoothly there, it is playable and the problem is the wallpaper service, not the file. If the gallery refuses it or shows a black frame, the file is the problem &mdash; either the codec is unsupported or the download is incomplete.</p>
<p>Comparing file size against duration is a quick sanity check. A ten-second 720p clip should be well over a megabyte. A ten-second clip that is 40 kilobytes is a broken download.</p>
<h2>What to do if only the lock screen animates</h2>
<p>This is a manufacturer decision, not a fault. Several skins deliberately keep the home screen static to save power and only animate the lock screen. There is no permission or setting that changes it, and installing a different launcher usually will not either. If the animation works somewhere, the app is functioning correctly.</p>
""",
 "wallpaper-file-formats": """
<h2>How to check what format a file actually is</h2>
<p>Filenames lie. A file named wallpaper.jpg can be a WebP file that has been renamed, which is why it fails to open in an older gallery app. On Android, open the file's details from the gallery or a file manager and look at the MIME type rather than the extension. On a computer, most image viewers show the real format in their properties panel.</p>
<p>If the MIME type does not match the extension, renaming it back is usually enough to make it work.</p>
<h2>Re-saving without losing quality</h2>
<p>Every JPEG save loses a little quality. If you need to resize a wallpaper, resize the original once and keep that as your master copy. Repeatedly opening, resizing and saving the same file compounds the loss, and after several rounds the softness becomes visible on a phone screen.</p>
<p>For anything you plan to edit more than once, keep a PNG or a lossless copy as the master and export a JPEG only for the final version you actually set as a wallpaper.</p>
""",
 "anipix-changelog": """
<h2>Why there is no automatic update</h2>
<p>Apps installed from a store are updated by the store. An app distributed as a direct APK has no such channel, so a new build only reaches you when you install it. That is a deliberate trade: it means no store review delay and no store policy deciding what the app may contain, at the cost of you having to check occasionally.</p>
<p>Installing a newer build over an older one keeps your settings. You do not need to uninstall first, and you do not need to re-download wallpapers you have already saved &mdash; those live in your own storage.</p>
<h2>What is planned next</h2>
<p>The library keeps growing, and the work that matters most right now is coverage: making sure that every popular series has wallpapers rather than a handful of series having hundreds. Search quality is the other area &mdash; matching on partial names, alternate spellings and character names rather than exact strings.</p>
""",
}

PAGES = [
 dict(slug="set-wallpaper-samsung", body=pages1.SAMSUNG,
      title="How to Set a Wallpaper on a Samsung Phone (One UI)",
      desc="Step-by-step for One UI: separate home and lock screen wallpapers, where the crop happens, colour palettes, live wallpapers and why a wallpaper looks blurry after setting it.",
      kind="Device guide"),
 dict(slug="set-wallpaper-xiaomi", body=pages1.XIAOMI,
      title="How to Set a Wallpaper on Xiaomi, Redmi and POCO (HyperOS)",
      desc="HyperOS wallpaper steps, the scrolling home screen crop problem, carousel wallpapers, super wallpapers, live wallpaper permissions and battery optimisation.",
      kind="Device guide"),
 dict(slug="set-wallpaper-realme-oppo", body=pages1.REALME,
      title="How to Set a Wallpaper on realme and OPPO (ColorOS)",
      desc="ColorOS wallpaper steps, the lock-screen-first crop problem, live wallpaper overlay permission, battery settings and why a wallpaper reverts after reboot.",
      kind="Device guide"),
 dict(slug="set-wallpaper-iphone", body=pages1.IPHONE,
      title="How to Set a Wallpaper on iPhone Without Losing Quality",
      desc="iOS wallpaper steps, the depth effect, photo library compression, getting the crop right for a 9:19.5 screen, and how wallpaper pairs work with Focus modes.",
      kind="Device guide"),
 dict(slug="wallpaper-size-calculator", body=pages1.CALC,
      title="Wallpaper Size Calculator: What Resolution Your Phone Needs",
      desc="Enter your screen resolution and get the wallpaper size you actually need, plus why a 16:9 image gets cropped on a 9:20 phone and when to use a larger file.",
      kind="Tool"),
 dict(slug="amoled-dark-wallpapers", body=pages2.AMOLED,
      title="Dark Wallpapers on OLED: How Much Battery They Actually Save",
      desc="Why black pixels cost nothing on OLED, how much a dark wallpaper really saves, which images count as dark, and the burn-in argument for using one.",
      kind="Guide"),
 dict(slug="live-wallpaper-not-working", body=pages2.LIVEFIX,
      title="Live Wallpaper Not Working? Six Causes and Their Fixes",
      desc="Why a live wallpaper plays in the preview then sits still on the home screen: preview image applied, missing overlay permission, battery optimisation, broken download, manufacturer locking, launcher support.",
      kind="Troubleshooting"),
 dict(slug="wallpaper-file-formats", body=pages2.FORMATS,
      title="JPEG, PNG, WebP or AVIF: Which Wallpaper Format to Use",
      desc="What each image format is actually good for on a phone wallpaper, why a WebP file will not open in some galleries, and how to check what a file really is.",
      kind="Guide"),
 dict(slug="anipix-faq", body=pages2.FAQ,
      title="AniPix FAQ: Downloading, Installing and Using the App",
      desc="Direct answers about the app: is it free, where to download it, whether it is safe, why it is not on the Play Store, how wallpapers are licensed and what to do when it will not install.",
      kind="FAQ"),
 dict(slug="anipix-changelog", body=pages2.CHANGELOG,
      title="AniPix Changelog: What Each Update Actually Changed",
      desc="A record of what changed in the AniPix app, including the live wallpaper playback fix, download validation, and what is deliberately left out of the app.",
      kind="Changelog"),
]

def build(p):
    body = p["body"] + EXTRA.get(p["slug"], "")
    head = HEAD
    head = re.sub(r"<title>.*?</title>", f"<title>{p['title']} | AniPix</title>", head, count=1, flags=re.S)
    head = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{p["desc"]}">', head, count=1, flags=re.S)
    head = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="https://anipix.me/{p["slug"]}.html">', head, count=1)
    head = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{p["title"]}">', head, count=1, flags=re.S)
    head = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{p["desc"]}">', head, count=1, flags=re.S)
    head = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="https://anipix.me/{p["slug"]}.html">', head, count=1, flags=re.S)
    main = (f'<main class="wrap prose" style="padding:46px 20px 64px">\n'
            f'<p class="eyebrow" style="color:#5a6785;font-size:13px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;margin-bottom:10px">{p["kind"]}</p>\n'
            f'<h1>{p["title"]}</h1>\n'
            f'<p class="updated" style="color:#8a94ab;font-size:14px;margin:10px 0 26px">Last updated: 22 November 2026</p>\n'
            f'{body}\n'
            f'<div style="margin:38px 0 0;padding:18px 20px;border:1px solid #e4e9f2;border-radius:14px;background:#fff">'
            f'<strong>Written by Lavkush Kumar</strong>, who builds and uses the AniPix wallpaper app. '
            f'<a href="about.html">About</a> &middot; <a href="contact.html">Contact</a></div>\n'
            f'</main>\n')
    open(f'{p["slug"]}.html', 'w', encoding="utf-8").write(head + NAV + main + FOOT)

for p in PAGES:
    build(p)

# ---- guides index ----
cards = "\n".join(
    f'<a class="card" href="{p["slug"]}.html" style="display:block;background:#fff;border:1px solid #e4e9f2;border-radius:16px;padding:20px;text-decoration:none;color:inherit">'
    f'<span style="color:#5a6785;font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase">{p["kind"]}</span>'
    f'<h3 style="margin:8px 0 8px;font-size:18px">{p["title"]}</h3>'
    f'<p style="color:#5a6785;font-size:14.5px;line-height:1.6">{p["desc"]}</p></a>'
    for p in PAGES)
ghead = HEAD
ghead = re.sub(r"<title>.*?</title>", "<title>Guides, Tools and Help | AniPix</title>", ghead, count=1, flags=re.S)
ghead = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Every AniPix guide in one place: setting wallpapers on Samsung, Xiaomi, realme and iPhone, a wallpaper size calculator, live wallpaper fixes and format advice.">', ghead, count=1, flags=re.S)
ghead = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="https://anipix.me/guides.html">', ghead, count=1)
gmain = (f'<main class="wrap prose" style="padding:46px 20px 64px">\n'
         f'<h1>Guides, tools and help</h1>\n'
         f'<p class="updated" style="color:#8a94ab;font-size:14px;margin:10px 0 26px">Last updated: 22 November 2026</p>\n'
         f'<p>Everything here is written from actually using these phones rather than from a spec sheet. If a guide says a setting is in a particular menu, it is there on a current build &mdash; and where a manufacturer has changed it, the guide says what changed.</p>\n'
         f'<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px;margin:28px 0">\n{cards}\n</div>\n'
         f'<h2>Longer reading</h2>\n'
         f'<p>The blog covers anime and gaming wallpapers in more depth: character art breakdowns, episode guides and honest game write-ups. '
         f'<a href="https://blog.anipix.me/">AniPix Blog</a>. Space and science imagery lives at <a href="https://space.anipix.me/">Orbit</a>.</p>\n'
         f'</main>\n')
open("guides.html", "w", encoding="utf-8").write(ghead + NAV + gmain + FOOT)

# ---- nav + footer links on ALL pages ----
files = [f for f in glob.glob("*.html")]
added_nav = added_foot = 0
for f in files:
    s = open(f, encoding="utf-8").read(); o = s
    if '<a href="guides.html">Guides</a>' not in s:
        s = s.replace('<a href="about.html">About</a>',
                      '<a href="guides.html">Guides</a>\n      <a href="about.html">About</a>', 1)
        if s != o: added_nav += 1
    if 'href="guides.html">Guides</a>' not in s.split("<footer>")[-1]:
        s = s.replace('<a href="about.html">About</a>',
                      '<a href="guides.html">Guides</a>\n      <a href="about.html">About</a>', 1)
        if s != o: added_foot += 1
    if s != o: open(f, "w", encoding="utf-8").write(s)
print(f"pages built: {len(PAGES)+1} | nav updated: {added_nav}")

# ---- sitemap ----
sm = open("sitemap.xml", encoding="utf-8").read()
for p in PAGES + [dict(slug="guides")]:
    u = f"https://anipix.me/{p['slug']}.html"
    if u not in sm:
        pr = "0.8" if p["slug"] != "guides" else "0.7"
        sm = sm.replace("</urlset>", f'  <url><loc>{u}</loc><lastmod>2026-11-22</lastmod><changefreq>monthly</changefreq><priority>{pr}</priority></url>\n</urlset>')
open("sitemap.xml", "w", encoding="utf-8").write(sm)
print("sitemap urls:", sm.count("<url>"))
