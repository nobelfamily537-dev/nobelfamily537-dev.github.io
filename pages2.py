# -*- coding: utf-8 -*-
AMOLED = """
<p>An OLED phone screen switches individual pixels off to display black. That is not a marketing detail &mdash; it is a measurable difference in battery use, and it is the reason a dark wallpaper can genuinely extend your day.</p>

<h2>How OLED differs from LCD</h2>
<p>An LCD screen has a backlight that is always on, with liquid crystals in front of it blocking light to create dark areas. A black pixel on an LCD is a pixel with the backlight still burning behind it. The screen uses the same power whether it is showing white or black.</p>
<p>An OLED screen has no backlight. Each pixel emits its own light. A black pixel is simply switched off and draws no current. On a large dark area, the difference is real, not theoretical.</p>

<h2>How much does it actually save</h2>
<p>Independent measurements consistently put the saving at somewhere between 15 and 40 percent of screen power for a mostly-dark interface versus a mostly-white one, depending on brightness. Screen brightness matters more than anything else: at high brightness the saving is larger, because the light-emitting pixels are working harder.</p>
<p>Two things follow from that:</p>
<ul>
<li>A dark wallpaper saves the most at high brightness, which is exactly when you are outdoors and worried about battery.</li>
<li>At low brightness the saving is small, so if you keep your phone dim, a dark wallpaper is mostly an aesthetic choice.</li>
</ul>

<h2>What counts as a dark wallpaper</h2>
<p>Not all dark images are equal. An image that is black in the corners but has a bright subject in the middle will switch on a large block of pixels. For battery purposes, what matters is the total lit area, not the average brightness of the image.</p>
<p>If battery is the goal, the best wallpapers are ones with large genuine black regions: silhouettes against a black sky, minimal line art on pure black, night scenes where the darkness is actually black rather than dark blue.</p>
<p>A dark blue wallpaper looks dark to your eye but lights up all three colour channels. A pure black one lights up nothing.</p>

<h2>The always-on display is where it matters most</h2>
<p>On phones with an always-on display, a small part of the screen stays on constantly. On OLED that costs very little, because most pixels are off. But if your always-on clock sits over a bright wallpaper rather than a black background, the cost goes up.</p>
<p>This is why most always-on implementations default to black. If yours does not, changing it is one of the highest-value battery settings on the phone.</p>

<h2>Burn-in, and why dark wallpapers help there too</h2>
<p>OLED pixels dim unevenly over years of use. A bright static element in the same place every day &mdash; a status bar, a clock, a logo in a wallpaper &mdash; can leave a faint ghost.</p>
<p>A dark wallpaper reduces the overall pixel workload and lowers the risk. So does avoiding wallpapers with a bright high-contrast element in a fixed position. If you use the same wallpaper for years, prefer one without a bright object sitting in the middle of the screen.</p>

<h2>What about LCD phones</h2>
<p>If your phone has an LCD panel, a dark wallpaper saves nothing. You will still get the aesthetic benefit and slightly better icon contrast, but there is no battery argument. Most budget phones and a few mid-range models still use LCD, so it is worth checking before you optimise for it.</p>

<h2>How to tell which panel you have</h2>
<p>Look up your exact model and check whether the display is described as AMOLED, OLED, Super AMOLED, P-OLED or LTPO &mdash; all of these are OLED variants. If it says IPS, IPS LCD or TFT, it is LCD.</p>
<p>A quick practical test: display a full black image in a dark room at full brightness. On OLED the screen looks completely black and blends into the room. On LCD you can usually see a faint grey glow and some backlight bleed at the edges.</p>

<h2>Making a dark wallpaper readable</h2>
<p>The usual objection to dark wallpapers is that dark icons disappear into them. The fix is not to brighten the wallpaper but to brighten the icons: most launchers let you use a light icon pack, and both Android and iOS have per-appearance icon tinting. A black wallpaper with white icons is both the most battery-efficient and the most legible combination available.</p>
"""
LIVEFIX = """
<p>A live wallpaper that plays in the app's preview and then sits still on the home screen is the most common complaint about animated wallpapers on Android. It is almost never a broken file. Here is what is actually going wrong, in the order you should check.</p>

<h2>Cause 1: the system applied the preview image</h2>
<p>Most live wallpaper apps show a static thumbnail while they load the video. When you press the system's "Set wallpaper" option instead of the app's own button, some launchers pick up that thumbnail and apply it as an ordinary image.</p>
<p><strong>Fix:</strong> open the app, open the wallpaper, and use the button inside the app. Not the share sheet, not the gallery menu.</p>

<h2>Cause 2: missing overlay permission</h2>
<p>A live wallpaper draws behind your icons, which some Android skins treat as drawing over other apps. Without that permission the wallpaper service starts and immediately stops.</p>
<p><strong>Fix:</strong> Settings &rarr; Apps &rarr; [app] &rarr; Display over other apps &rarr; allow. On Xiaomi and OPPO this step is mandatory and the prompt is easy to miss.</p>

<h2>Cause 3: battery optimisation suspending the service</h2>
<p>Android suspends background services it considers idle. A live wallpaper is a background service. When it gets suspended, you see the last frame, frozen.</p>
<p><strong>Fix:</strong> set the app's battery setting to unrestricted, and if your phone has a "lock app in recents" feature, use it. This is the single most effective fix on Chinese Android skins.</p>

<h2>Cause 4: the video never downloaded properly</h2>
<p>Live wallpapers are video files, and video files fail in ways images do not. A partial download gives you a file that plays for two seconds and then freezes, or one that shows a single frame.</p>
<p>Check the file size. A short loop should be at least a few hundred kilobytes. If it is a few kilobytes, the download failed. Delete it and download again on a stable connection.</p>

<h2>Cause 5: the phone locked a static wallpaper over it</h2>
<p>Some manufacturers deliberately replace live wallpapers with a static frame on the home screen to save power, keeping the animation on the lock screen only. Samsung does this with its own live wallpapers. There is no setting that fully overrides it.</p>
<p>If the animation works on the lock screen but not the home screen, this is what is happening, and it is not a bug in the app.</p>

<h2>Cause 6: the launcher does not support it</h2>
<p>Third-party launchers sometimes do not pass the live wallpaper service through. If you recently changed launcher, switch back to the stock one and test. If it works there, the launcher is the problem.</p>

<h2>Battery cost, honestly</h2>
<p>A looping video on your home screen is a continuously running video decoder. It costs noticeably more than a static image &mdash; expect a real difference in screen-on time, more on high-resolution phones.</p>
<p>Practical mitigations: use a low-resolution loop (a 720p video stretched looks fine as a wallpaper), keep the loop short so the decoder does not seek constantly, and avoid live wallpapers on the lock screen if your phone has an always-on display, because both will be active at once.</p>

<h2>How to test whether it is the file or the phone</h2>
<p>Set a live wallpaper from a different app. If that one animates, the original file is the problem. If neither animates, the permission or battery setting is the problem. This takes two minutes and saves a lot of guessing.</p>
"""
FORMATS = """
<p>Wallpaper files come in several formats, and the differences matter more than most people expect &mdash; particularly when a file that looks fine on your computer turns soft or refuses to set on your phone.</p>

<h2>JPEG</h2>
<p>The default for photographs and for almost every wallpaper you will download. Small files, universal support, and quality that is excellent at high settings. The weakness is that JPEG is lossy: every time you edit and re-save, quality drops a little more.</p>
<p>For a wallpaper you are not editing, JPEG at high quality is the right choice. If you are resizing and re-saving repeatedly, work from the original each time rather than saving over the same file.</p>

<h2>PNG</h2>
<p>Lossless, supports transparency, and produces much larger files. For wallpapers, PNG matters in one specific case: artwork with flat colours, hard edges and text, where JPEG's compression produces visible smudging around edges.</p>
<p>If you are setting a logo, a poster, or line art as your wallpaper, PNG will look cleaner. For a photograph, PNG gives you a much larger file for no visible benefit.</p>

<h2>WebP</h2>
<p>Google's format, now supported by every current Android version and by iOS since 14. It typically produces files 25 to 35 percent smaller than JPEG at equivalent quality, which is why most wallpaper sites have moved to it.</p>
<p>The practical issue: older Android versions and some gallery apps do not recognise it. If a wallpaper downloads but will not appear in your gallery, this is usually why. Convert to JPEG or update the gallery app.</p>

<h2>AVIF and HEIC</h2>
<p>Both are newer, both compress better than JPEG, and both are inconsistent in support. HEIC is what iPhones shoot by default. AVIF is increasingly used on websites.</p>
<p>If you download an AVIF wallpaper and your phone will not set it, that is a support gap, not a corrupt file. Convert it. Most online converters handle both formats.</p>

<h2>GIF</h2>
<p>Avoid it for wallpapers. GIF is limited to 256 colours, produces banding on gradients, and the files are large for what you get. An animated GIF wallpaper will look worse than the same animation as a video, and it will be bigger.</p>

<h2>Video formats for live wallpapers</h2>
<p>Live wallpapers are usually MP4 with H.264 encoding. This is the most compatible combination by a wide margin. HEVC (H.265) produces smaller files and is supported on most recent phones, but older devices may refuse it.</p>
<p>If a live wallpaper file plays on your computer but not your phone, check the codec before assuming the file is broken.</p>

<h2>What format to use, in one line</h2>
<p>Photographic wallpaper: <strong>JPEG or WebP</strong>. Artwork with flat colour or text: <strong>PNG</strong>. Live wallpaper: <strong>MP4 with H.264</strong>. Everything else: convert it.</p>

<h2>A note on "HD" and "4K" labels</h2>
<p>These labels on wallpaper sites are unreliable. A file can be labelled 4K and be a 1080-pixel image that has been upscaled. The only number that matters is the actual pixel dimensions, which you can check in any gallery app's file details. If the width is smaller than your screen's width, it will be soft regardless of what the filename says.</p>
"""
FAQ = """
<p>Short, direct answers to the questions that come up most often about AniPix and about wallpapers in general. If your question is not here, the contact page is the fastest route.</p>

<h2>About the app</h2>
<h3>Is AniPix free?</h3>
<p>Yes. The app is free to download and use, and it is supported by advertising. There is no paywall on the wallpaper library.</p>

<h3>Where do I download it?</h3>
<p>From the download link on this site. The app is distributed as a direct APK rather than through the Play Store, so your phone will ask you to allow installation from your browser the first time. That prompt is normal for any app installed outside a store.</p>

<h3>Why is it not on the Play Store?</h3>
<p>Publishing on the Play Store requires a developer account, a review process and ongoing compliance work. The app is distributed directly so that updates can ship the same day they are finished.</p>

<h3>Is it safe to install?</h3>
<p>The APK is built from this project's own source and served from this project's own release page. You can verify the download URL before installing &mdash; it should point at the project's GitHub releases. Do not install a copy from a third-party APK mirror; those are repackaged by whoever runs the mirror and are not under our control.</p>

<h3>Does it work offline?</h3>
<p>Wallpapers you have already viewed are cached, and wallpapers you have downloaded are stored locally. Browsing new wallpapers needs a connection.</p>

<h3>How often are new wallpapers added?</h3>
<p>Several times a day. The library is updated on a schedule and the app picks up new additions automatically when it refreshes.</p>

<h2>Using wallpapers</h2>
<h3>Why does my wallpaper look blurry?</h3>
<p>Almost always because the source image is smaller than your screen. Check the actual pixel dimensions, not the filename. A 720-pixel-wide image on a 1080-pixel screen will look soft no matter how good it looked as a thumbnail.</p>

<h3>Why is my wallpaper cropped?</h3>
<p>Your screen is taller than most wallpaper images. A standard image is 9:16; most phones are close to 9:20. Something has to be cut. Cropping the image yourself before setting it gives you control over what is lost.</p>

<h3>Can I use the same wallpaper on both screens?</h3>
<p>Yes, but set them separately. On most Android phones, setting one image for both means the lock screen gets a crop of the home screen's crop, which often cuts the subject.</p>

<h3>Do dark wallpapers save battery?</h3>
<p>On OLED screens, yes &mdash; meaningfully, especially at high brightness. On LCD screens, no. The saving depends on how much of the image is genuinely black rather than merely dark.</p>

<h2>Live wallpapers</h2>
<h3>My live wallpaper does not animate. Why?</h3>
<p>Three common causes: the system applied the app's static preview instead of the live service, the app is missing the "display over other apps" permission, or battery optimisation suspended it. Setting the wallpaper from inside the app fixes the first; the other two are in system settings.</p>

<h3>Do live wallpapers drain battery?</h3>
<p>Yes, more than static ones. A looping video is a running video decoder. The cost is manageable if you keep the loop short and the resolution modest.</p>

<h2>Content and rights</h2>
<h3>Can I use these wallpapers anywhere I like?</h3>
<p>The app provides wallpapers for personal use on your own devices. Artwork depicting anime and game characters belongs to the studios and artists who made it, and is provided here for personal, non-commercial use. Do not resell it, and do not use it in commercial products.</p>

<h3>How do I request removal of an image?</h3>
<p>Use the contact page with the image description and a link. Rights requests are handled directly and the image is removed when a claim is valid.</p>

<h2>Technical</h2>
<h3>Which Android versions are supported?</h3>
<p>Android 8 and later. Live wallpapers need Android 8 or later as well; some animation features depend on the manufacturer's launcher.</p>

<h3>The app will not install. What now?</h3>
<p>Check that "install unknown apps" is enabled for the browser or file manager you are using to open the APK. On some phones this permission is per-app rather than global, so enabling it once for your browser is not enough if you then open the file from a file manager.</p>
"""
CHANGELOG = """
<p>A running record of what has changed in the AniPix app, so you can tell whether an update is worth installing. Entries are grouped by release and describe what actually changed for the person using the app, not the internal work behind it.</p>

<h2>How versioning works here</h2>
<p>Every build gets a new number. A build that changes only the wallpaper library keeps the same features and the same layout &mdash; the number moves because the library moved. Builds that change behaviour are called out explicitly in the entry.</p>
<p>Because the app is distributed directly rather than through a store, updates are not pushed to you. You install a new build when you want it, and your settings carry over.</p>

<h2>What the recent builds changed</h2>
<h3>Live wallpaper playback</h3>
<p>The most substantial fix in recent history. Live wallpapers that downloaded correctly were still showing as static images on some phones. The cause was that the video was being handed to the system as a remote stream rather than a local file, and the media player never received a ready callback, so it silently never started.</p>
<p>The fix downloads the clip to local storage first, then plays it from there. The preview now shows a poster frame while it loads, with a real progress indicator and a timeout, and error codes are surfaced instead of a silent failure.</p>

<h3>Static-frame locking on the home screen</h3>
<p>Some manufacturers lock a static bitmap over a live wallpaper on the home screen while leaving the lock screen animated. Earlier builds tried to work around this in a way that produced a frozen image on those devices. That approach was removed; the app now detects whether a clip is actually playable before offering it as a live wallpaper.</p>

<h3>Download validation</h3>
<p>Failed downloads previously left a partial file that looked like a wallpaper and behaved like a corrupt one. Downloads are now written to a temporary file, checked for a minimum size and a valid container header, and only then renamed into place. A failed download now reports as a failure.</p>

<h2>What is deliberately not in the app</h2>
<p>Worth stating, because people ask for these regularly:</p>
<ul>
<li><strong>No video downloading from other sites.</strong> The app is a wallpaper browser, not a media downloader.</li>
<li><strong>No account required.</strong> There is no sign-in, no profile and no cloud sync of your choices.</li>
<li><strong>No third-party analytics beyond crash reporting.</strong> The app does not build a profile of what you look at.</li>
</ul>

<h2>Reporting a problem</h2>
<p>If a build misbehaves, the useful information is: your phone model, your Android version, and what you did immediately before it went wrong. Send that through the contact page. Reports that include the phone model get fixed much faster than reports that do not, because half of these problems are manufacturer-specific.</p>

<h2>Requesting a feature</h2>
<p>Feature requests are read. The ones that get built are usually the ones that solve a problem many people have rather than one person's preference. Requests that describe the situation &mdash; "I cannot find wallpapers for a specific show because the search only matches exact names" &mdash; are far more actionable than a one-line wish.</p>

<h2>Keeping the library current</h2>
<p>The wallpaper library is the part of the app that changes most often, and it changes independently of the app build. New wallpapers are added on a schedule throughout the day, across categories. If a category feels thin, it is usually because it was recently cleared of low-quality entries rather than because nothing was added.</p>
"""
