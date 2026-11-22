# -*- coding: utf-8 -*-
SAMSUNG = """
<p>Setting a wallpaper on a Samsung phone should take ten seconds. On One UI it can take longer, because the same image ends up in three different places depending on where you tap. This page is the version that actually works, including the parts Samsung's own help pages skip.</p>

<h2>The short version</h2>
<p>Open <strong>Gallery</strong>, open the picture, tap the <strong>three dots</strong> in the top right, choose <strong>Set as wallpaper</strong>. You then get a choice between Lock screen, Home screen, or both. That is the whole flow. Everything below is about the cases where it does not behave the way you expect.</p>

<h2>Home screen and lock screen are separate images</h2>
<p>Most people do not realise this until they notice their lock screen looks different from their home screen. Samsung lets you set two entirely different wallpapers. If you choose "Home screen" only, the lock screen keeps whatever it had before.</p>
<p>There is also a third setting that catches people out: <strong>Apply to Always On Display</strong>. If your lock screen wallpaper seems to bleed into the clock screen at a strange brightness, that is why. Turn it off unless you want it.</p>

<h2>Where the crop actually happens</h2>
<p>When you set a wallpaper from the Gallery, Samsung shows a crop frame. The frame is wider than it is tall, because the home screen scrolls sideways between pages. If you are setting the same image on both screens, the frame represents the home screen, and the lock screen will use the centre of that crop.</p>
<p>This is why a portrait wallpaper that looks perfect in the preview can look zoomed in on the lock screen. Two ways around it:</p>
<ul>
<li>Set the lock screen and home screen separately, choosing a different crop for each.</li>
<li>Use an image that already has empty space around the subject, so any crop still works.</li>
</ul>
<p>A 1080 by 1920 image is the safe size for most Samsung phones. Taller phones like the S23 Ultra and S24 Ultra are 1440 by 3088, so a 1080 by 1920 file gets scaled up slightly. It is usually not visible, but if you are picky, use a file at or above your screen's native resolution.</p>

<h2>Wallpaper services and the "Dynamic" lock screen</h2>
<p>In <strong>Settings &rarr; Wallpaper and style</strong> Samsung offers a few things the Gallery route does not: wallpaper services, colour palettes pulled from the image, and a dynamic lock screen that rotates pictures automatically.</p>
<p>The colour palette feature is worth knowing about. When you set a wallpaper there, One UI can recolour your icons and quick settings to match. It is the fastest way to make a phone look intentional rather than assembled.</p>
<p>Dynamic lock screen pulls from Samsung's own categories, not your gallery. If you want your own images to rotate, you cannot use it &mdash; you would need a live wallpaper app instead.</p>

<h2>Live wallpapers on One UI</h2>
<p>Samsung's own "live wallpaper" in the Wallpaper and style menu is a short video that plays on the lock screen only, not the home screen. Third-party live wallpaper apps behave differently: they run as a background service and animate on both screens, which costs battery.</p>
<p>If you install a live wallpaper app and the animation does not start, the usual cause is that One UI applied the app's static preview image instead of the video. The fix is to go back into the app, open the wallpaper, and use the app's own "Set wallpaper" button rather than setting it from the Gallery or the system picker.</p>

<h2>Why a wallpaper can look blurry after setting it</h2>
<p>Three causes, in order of likelihood:</p>
<ul>
<li><strong>The source file is small.</strong> A 720 by 1280 image stretched to a 1440-wide screen will look soft. Check the file's actual dimensions, not how it looks in the gallery thumbnail.</li>
<li><strong>Battery saver is compressing it.</strong> Some One UI builds reduce wallpaper quality when battery saver is on. Turn it off and set the wallpaper again.</li>
<li><strong>You set it through a theme.</strong> Samsung themes can override the wallpaper with their own asset. Remove the theme, set the wallpaper, then decide whether you still want the theme.</li>
</ul>

<h2>Home screen grid and icon contrast</h2>
<p>A wallpaper is only half the job. If your icons are unreadable over a busy image, the wallpaper is wrong for that screen, no matter how good it looks on its own.</p>
<p>Two fixes that take seconds: change the home screen grid to 5 by 6 so icons sit further apart, and enable <strong>dark mode for icons</strong> if your wallpaper is bright. Samsung also has a setting that dims the wallpaper behind the app drawer, which helps more than people expect.</p>

<h2>If the button is missing entirely</h2>
<p>On a few carrier-locked Samsung builds and on some work profiles, "Set as wallpaper" is greyed out or absent in the Gallery. That is a device management restriction, not a bug. The workaround is <strong>Settings &rarr; Wallpaper and style &rarr; More wallpapers &rarr; Gallery</strong>, which goes through the system picker instead of the Gallery app and usually bypasses the restriction.</p>
<p>If that also fails, the image may be in a cloud-only state. Download it to the device first, then try again.</p>
"""
XIAOMI = """
<p>Xiaomi phones &mdash; Redmi, POCO and Mi models &mdash; run HyperOS now, which replaced MIUI. The wallpaper flow is similar but the menu names changed, and a few behaviours are specific to Xiaomi. Here is what actually happens on a current HyperOS build.</p>

<h2>The basic flow</h2>
<p>Open <strong>Gallery</strong>, open the image, tap <strong>More</strong> at the bottom, then <strong>Set as wallpaper</strong>. You will be asked whether you want it on the lock screen, the home screen, or both. Choosing both lets you adjust the crop separately for each, which most people skip and then regret.</p>
<p>The alternate route is <strong>Settings &rarr; Wallpaper &rarr; Gallery</strong>. This is the one to use if the Gallery option is missing or the crop behaves strangely.</p>

<h2>The scrolling home screen problem</h2>
<p>MIUI and HyperOS scroll the home screen wallpaper horizontally as you swipe between pages. When you set one image for both screens, the launcher crops it wider than the screen to give itself room to scroll.</p>
<p>Two consequences:</p>
<ul>
<li>A portrait wallpaper gets zoomed in, cutting the top and bottom.</li>
<li>The lock screen shows only the centre of that wider crop, so it looks different from what you set.</li>
</ul>
<p>The fix is either to set the two screens separately with different crops, or to turn off wallpaper scrolling. On HyperOS the scrolling toggle lives in the launcher settings rather than the wallpaper menu, which is why people cannot find it.</p>

<h2>Carousel wallpaper &mdash; Xiaomi's best-kept feature</h2>
<p>In <strong>Settings &rarr; Wallpaper &rarr; Carousel wallpaper</strong>, HyperOS can rotate through a set of images on the lock screen, changing each time you unlock. You choose the folder or album. This is genuinely useful and almost nobody uses it.</p>
<p>One caveat: carousel wallpapers work on the lock screen, not the home screen. If you want rotation on both, you need a live wallpaper app.</p>

<h2>Super wallpapers</h2>
<p>Xiaomi ships a set of animated 3D "super wallpapers" (the Earth and Mars ones are the well-known pair). They are beautiful and they are also among the heaviest wallpapers you can run &mdash; expect a measurable battery cost, especially on the always-on display.</p>
<p>If your phone runs warm or the battery drops faster after you set one, that is the cause. Switching to a static wallpaper is the fastest test.</p>

<h2>Live wallpapers that will not animate</h2>
<p>Third-party live wallpaper apps on HyperOS have one recurring failure: the animation plays in the app preview, then the home screen shows a still image. This is almost always the system picker applying the app's static preview instead of the live service.</p>
<p>Fix it from inside the app, not from Settings. Open the app, open the wallpaper, and press the app's own "Set wallpaper" button. Grant the "display over other apps" permission when asked &mdash; MIUI blocks live wallpapers without it, and the prompt is easy to dismiss by accident.</p>

<h2>Battery saver kills live wallpapers</h2>
<p>HyperOS has aggressive battery management. When battery saver turns on, live wallpapers are usually suspended and you get a frozen image. There is no setting that fully prevents this; the only reliable workaround is to exclude the wallpaper app from battery optimisation in <strong>Settings &rarr; Apps &rarr; Manage apps &rarr; [app] &rarr; Battery saver &rarr; No restrictions</strong>.</p>

<h2>Wallpaper resolution on Xiaomi screens</h2>
<p>Most current Redmi and POCO phones are 1080 by 2400 or 1220 by 2712. A 1080 by 1920 wallpaper will be scaled and cropped. It usually looks acceptable, but if you want it sharp, match or exceed the screen's native height.</p>
<p>To check your exact resolution: <strong>Settings &rarr; About phone &rarr; All specs &rarr; Resolution</strong>.</p>

<h2>Two things that silently override your wallpaper</h2>
<ul>
<li><strong>Themes.</strong> Applying a theme replaces the wallpaper with the theme's own asset. If your wallpaper keeps reverting, a theme is the reason.</li>
<li><strong>Second space / dual apps.</strong> A separate space has its own wallpaper. Setting it in the main space does nothing there.</li>
</ul>
<p>Both are quick to check and both waste a lot of people's time before they are found.</p>
"""
REALME = """
<p>realme UI and ColorOS are the same codebase with different branding, so everything here applies to realme, OPPO and OnePlus phones running ColorOS 13 or later. The wallpaper flow is straightforward; the quirks are not.</p>

<h2>Setting a wallpaper</h2>
<p>From <strong>Gallery</strong>: open the image, tap the <strong>three dots</strong>, choose <strong>Set as wallpaper</strong>, then pick lock screen, home screen, or both.</p>
<p>From <strong>Settings &rarr; Wallpaper &amp; style</strong>: this route gives you more control, including separate crops and the option to apply a matching colour palette to your icons.</p>

<h2>The crop that fights you</h2>
<p>ColorOS crops for the lock screen first and then reuses that crop for the home screen. If your image has a subject near the top or bottom edge, it will get cut. The reliable workaround is to set the home screen wallpaper first, adjust the crop you want, then set the lock screen separately.</p>
<p>Also note that ColorOS adds a slight parallax effect by default, which shifts the wallpaper as you tilt the phone. Some people find it distracting. It can be turned off in the launcher settings, not in the wallpaper menu.</p>

<h2>Wallpaper scrolling is off by default</h2>
<p>Unlike Xiaomi, ColorOS does not scroll the home screen wallpaper between pages by default. That is why a portrait wallpaper tends to fit better here. If you turn scrolling on, expect the same zoom-in problem other launchers have.</p>

<h2>Live wallpapers and the "display over other apps" permission</h2>
<p>This is the single most common reason a live wallpaper fails on realme and OPPO phones. The app needs permission to draw over other apps, and ColorOS does not always prompt for it clearly.</p>
<p>Go to <strong>Settings &rarr; Apps &rarr; App management &rarr; [your wallpaper app] &rarr; Display over other apps</strong> and enable it. Then set the wallpaper again from inside the app. If you skip this step, the wallpaper usually appears as a static image or not at all.</p>

<h2>Battery optimisation will stop the animation</h2>
<p>ColorOS suspends background services aggressively. A live wallpaper is a background service. When the phone decides the app is idle, the animation freezes.</p>
<p>Set the wallpaper app to <strong>Allow background activity</strong> in its battery settings, and if the problem persists, lock the app in the recent-apps view (the small padlock icon) so the system stops clearing it.</p>

<h2>Resolution on realme and OPPO screens</h2>
<p>Most current models are 1080 by 2400 or 1240 by 2772. A 1080 by 1920 file will be upscaled and cropped. For a sharp result, use an image at least as tall as your screen.</p>
<p>Check yours at <strong>Settings &rarr; About device &rarr; Screen</strong>.</p>

<h2>What to do when the wallpaper reverts by itself</h2>
<p>If your wallpaper changes back to a default image after a reboot or after charging overnight, the cause is almost always one of these:</p>
<ul>
<li>A <strong>theme</strong> is applied and is reasserting its own wallpaper on boot.</li>
<li>The wallpaper lives on <strong>cloud storage only</strong> and the local copy was cleared, so the system fell back to default.</li>
<li>The image was in a folder the system cleaned as <strong>cache</strong>.</li>
</ul>
<p>The fix for all three is the same: copy the image into a permanent local folder such as Pictures, set it from there, and remove any theme.</p>

<h2>Icon contrast on busy wallpapers</h2>
<p>ColorOS lets you add a translucent panel behind the app drawer and behind folder icons. On a detailed wallpaper this makes a bigger difference than changing the wallpaper itself. It is in <strong>Settings &rarr; Home screen &amp; Lock screen</strong>.</p>
"""
IPHONE = """
<p>iOS handles wallpapers differently from Android in ways that matter: there is no separate home screen wallpaper crop on older versions, there is a depth effect that changes how the clock sits, and the photo picker will happily hand you a compressed copy. Here is how it works on a current iOS release.</p>

<h2>The current flow</h2>
<p>Open <strong>Settings &rarr; Wallpaper &rarr; Add New Wallpaper</strong>, or long-press the lock screen and tap <strong>+</strong>. Choose Photos, pick your image, adjust the crop, then tap <strong>Add</strong>. You will be asked whether to set it as a pair (lock and home together) or customise the home screen separately.</p>

<h2>Depth effect &mdash; the feature that ruins crops</h2>
<p>iOS can push the clock behind your subject so the subject overlaps it. It looks excellent when it works. It also moves the image around to achieve it, which can push your subject off-centre.</p>
<p>If your wallpaper looks wrong after setting it, the depth effect is the first thing to turn off. There is a small toggle on the preview screen. Turning it off restores the image exactly as you cropped it.</p>

<h2>Photo Library compresses what you give it</h2>
<p>When you pick an image through the Photos app, iOS may hand over an optimised copy rather than the original file. If your wallpaper looks softer than the source, this is why.</p>
<p>The workaround is to set the wallpaper from a file stored in the <strong>Files</strong> app instead, using the same Settings route. Files are passed through without the photo library's optimisation.</p>

<h2>Getting the crop right</h2>
<p>An iPhone lock screen is tall and narrow. Current models are roughly 1179 by 2556 pixels, which is close to a 9:19.5 ratio. A standard 1080 by 1920 image is 9:16, so it is too wide &mdash; iOS will crop the sides or the top and bottom.</p>
<p>Two practical options:</p>
<ul>
<li>Use an image that already has space around the subject, so any crop is safe.</li>
<li>Crop the image yourself to roughly 9:19.5 before setting it, so you control exactly what is lost.</li>
</ul>

<h2>Home screen wallpaper on iOS</h2>
<p>Since iOS 16 the home screen can have its own wallpaper, with a blur option. The blur is worth knowing about: it makes icons far more readable over a busy image without changing the image. If your home screen looks cluttered, try the blur before changing the wallpaper.</p>

<h2>Live Photos as wallpapers</h2>
<p>A Live Photo can animate on the lock screen when you press and hold. It is not a looping animation like an Android live wallpaper, and it does not play on the home screen at all.</p>
<p>If the animation does not trigger, the Live Photo has usually been converted to a still somewhere along the way &mdash; editing it in Photos, or transferring it through a service that strips the motion data, will do that.</p>

<h2>Why a wallpaper can revert after an update</h2>
<p>iOS occasionally resets wallpaper pairs after a major update, particularly if the image was stored in an iCloud-optimised state and the local copy had been evicted. Keeping the original file in Files, or in an album set to download originals, prevents it.</p>

<h2>Reducing battery cost on OLED iPhones</h2>
<p>OLED screens use no power for black pixels. A wallpaper that is mostly black genuinely saves battery on an iPhone with an OLED panel &mdash; and on the always-on display it saves considerably more, because the screen stays on. Dark wallpapers are not just an aesthetic choice on these devices.</p>
"""
CALC = """
<p>Phone screens are not all the same shape, and a wallpaper that looks sharp on one phone can look soft or badly cropped on another. This page explains the numbers and includes a calculator that tells you exactly what size to use for your device.</p>

<h2>Why resolution is not the whole story</h2>
<p>A wallpaper has to satisfy two separate requirements: it needs to be at least as many pixels as the screen, and it needs to match the screen's aspect ratio. Miss the first and it looks soft. Miss the second and it gets cropped or stretched.</p>
<p>Most phones now are close to a 9:20 ratio, which is much taller than the 9:16 that most wallpaper images are made in. That gap is why so many wallpapers get cut.</p>

<h2>The calculator</h2>
<div class="calc" style="background:#fff;border:1px solid #e4e9f2;border-radius:16px;padding:22px;margin:26px 0">
  <label style="display:block;font-weight:600;margin-bottom:8px">Your screen resolution</label>
  <div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:16px">
    <input id="cw" type="number" value="1080" placeholder="width" style="flex:1;min-width:110px;padding:11px 13px;border:1px solid #d3dbeb;border-radius:10px;font-size:15px">
    <input id="ch" type="number" value="2400" placeholder="height" style="flex:1;min-width:110px;padding:11px 13px;border:1px solid #d3dbeb;border-radius:10px;font-size:15px">
  </div>
  <button onclick="calcWall()" style="background:linear-gradient(135deg,#3b82f6,#8b5cf6);color:#fff;border:0;padding:12px 22px;border-radius:10px;font-size:15px;font-weight:600;cursor:pointer">Calculate</button>
  <div id="cres" style="margin-top:18px;font-size:15px;line-height:1.8"></div>
</div>
<script>
function calcWall(){
  var w=parseInt(document.getElementById('cw').value,10);
  var h=parseInt(document.getElementById('ch').value,10);
  var out=document.getElementById('cres');
  if(!w||!h||w<200||h<200){ out.innerHTML='<span style="color:#dc2626">Enter a valid resolution.</span>'; return; }
  var r=h/w, pct=(r/ (16/9))*100;
  var rec16=Math.round(h*9/16);
  var megapix=((w*h)/1000000).toFixed(1);
  out.innerHTML =
    '<strong>Your screen ratio:</strong> 1 : '+r.toFixed(2)+' (roughly 9 : '+Math.round(r*9)+')<br>'+
    '<strong>Screen size:</strong> '+w+' &times; '+h+' pixels, '+megapix+' megapixels<br>'+
    '<strong>Best wallpaper size:</strong> at least '+w+' &times; '+h+', ideally '+(w*2)+' &times; '+(h*2)+' for high-density displays<br>'+
    '<strong>If you use a 16:9 image:</strong> it needs to be at least '+rec16+' &times; '+h+' to avoid upscaling, and it will still be cropped top and bottom.<br>'+
    '<strong>Recommendation:</strong> '+(pct>105 ? 'Your screen is much taller than 16:9. Use an image made for phones, or crop it yourself to 9:'+Math.round(r*9)+' before setting.' : 'Your screen is close to 16:9, so standard wallpaper images will fit with minimal cropping.');
}
calcWall();
</script>

<h2>Reading the result</h2>
<p><strong>"At least width by height"</strong> is the minimum. Below that, the phone scales the image up and you lose sharpness. Matching it exactly is fine for most people.</p>
<p><strong>"Ideally double"</strong> matters on high-density screens. A 1080-wide image on a 1080-wide screen is one image pixel per physical pixel, which is sharp. But when you set it as a scrolling home screen wallpaper, the launcher needs extra width to scroll, so it stretches the image horizontally &mdash; and that is where softness appears.</p>
<p><strong>The 16:9 note</strong> is the important one for most people. If you download a wallpaper made for a desktop monitor, it is 16:9. On a phone that is 9:20, you either crop the sides heavily or accept a squashed image. Neither is good.</p>

<h2>How to find your phone's resolution</h2>
<p>On Android: <strong>Settings &rarr; About phone &rarr; All specs &rarr; Resolution</strong>. Some phones show a different "HD+" or "FHD+" label instead of the raw number &mdash; those mean 720p and 1080p respectively.</p>
<p>On iPhone: the numbers are fixed per model. Search your model name plus "resolution" and you will get the exact figures, or use the calculator above with the values for your device.</p>

<h2>The one setting that changes everything</h2>
<p>If your launcher scrolls the wallpaper between pages, it needs roughly 1.5 to 2 times the screen width. A portrait image will be stretched or cropped to fill that. Turning wallpaper scrolling off is the single biggest improvement most people can make to how a wallpaper looks.</p>
"""
