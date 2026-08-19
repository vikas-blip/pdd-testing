import os
import re

root_dir = r"c:\Users\vikas\Downloads\ThermaScan"
dirs_to_update = [root_dir, os.path.join(root_dir, "pdd-testing")]

new_viewport_and_apple_tags = """  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no, shrink-to-fit=no, viewport-fit=cover">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="ThermaScan">
  <meta name="mobile-web-app-capable" content="yes">"""

ios_gesture_js = """
// --- Native Anti-Zoom & Touch Gesture Locks ---
(function() {
  if (window.__thermascan_touch_lock_initialized__) return;
  window.__thermascan_touch_lock_initialized__ = true;

  // 1. Prevent 2-finger pinch zoom on touch screens (touchstart & touchmove)
  document.addEventListener('touchstart', function (e) {
    if (e.touches && e.touches.length > 1) {
      e.preventDefault();
    }
  }, { passive: false });

  document.addEventListener('touchmove', function (e) {
    if (e.touches && e.touches.length > 1) {
      e.preventDefault();
    }
  }, { passive: false });

  // 2. Prevent WebKit iOS Safari gesture zooming
  ['gesturestart', 'gesturechange', 'gestureend'].forEach(function (eventName) {
    document.addEventListener(eventName, function (e) {
      e.preventDefault();
    }, { passive: false });
  });

  // 3. Prevent trackpad / mouse ctrl + wheel pinch zoom
  document.addEventListener('wheel', function (e) {
    if (e.ctrlKey) {
      e.preventDefault();
    }
  }, { passive: false });

  // 4. Trackpad / mouse ctrl + wheel pinch zoom
  document.addEventListener('wheel', function (e) {
    if (e.ctrlKey) {
      e.preventDefault();
    }
  }, { passive: false });
})();
"""

css_lockdown = """
/* Native App Touch & Anti-Zoom Constraints */
html, body {
  overflow-x: hidden;
  overflow-y: auto !important;
  -webkit-overflow-scrolling: touch !important;
  touch-action: manipulation !important;
  -webkit-text-size-adjust: 100%;
  -ms-text-size-adjust: 100%;
  text-size-adjust: 100%;
  -webkit-touch-callout: none;
  -webkit-tap-highlight-color: transparent;
}

input, textarea, select {
  -webkit-user-select: auto !important;
  user-select: auto !important;
  font-size: 16px !important;
}
"""

for d in dirs_to_update:
    # 1. Update index.html
    html_path = os.path.join(d, "index.html")
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        if '<meta name="viewport"' in html_content:
            html_content = re.sub(
                r'<meta name="viewport" content="[^"]*">',
                new_viewport_and_apple_tags,
                html_content
            )
        else:
            html_content = html_content.replace("<head>", "<head>\n" + new_viewport_and_apple_tags)

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Updated index.html in {d}")

    # 2. Update style.css
    css_path = os.path.join(d, "style.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            css_content = f.read()

        if "/* Native App Touch & Anti-Zoom Constraints */" in css_content:
            idx = css_content.find("/* Native App Touch & Anti-Zoom Constraints */")
            css_content = css_content[:idx].strip() + "\n\n" + css_lockdown
        else:
            css_content = css_content.strip() + "\n\n" + css_lockdown

        with open(css_path, "w", encoding="utf-8") as f:
            f.write(css_content)
        print(f"Updated style.css in {d}")

    # 3. Update app.js
    js_path = os.path.join(d, "app.js")
    if os.path.exists(js_path):
        with open(js_path, "r", encoding="utf-8") as f:
            js_content = f.read()

        if "// --- iOS Native App Anti-Zoom & Touch Gesture Locks ---" in js_content:
            idx = js_content.find("// --- iOS Native App Anti-Zoom & Touch Gesture Locks ---")
            js_content = js_content[:idx].strip() + "\n\n" + ios_gesture_js
        elif "// --- Native Anti-Zoom & Touch Gesture Locks ---" in js_content:
            idx = js_content.find("// --- Native Anti-Zoom & Touch Gesture Locks ---")
            js_content = js_content[:idx].strip() + "\n\n" + ios_gesture_js
        else:
            js_content = js_content.strip() + "\n\n" + ios_gesture_js

        with open(js_path, "w", encoding="utf-8") as f:
            f.write(js_content)
        print(f"Updated app.js in {d}")

print("Native Anti-Zoom & Touch Gesture Lockdowns applied successfully!")

