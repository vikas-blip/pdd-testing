import os
import shutil

src_dir = r"c:\Users\vikas\Downloads\ThermaScan\pdd-testing"
dst_dir = r"c:\Users\vikas\Downloads\ThermaScan"

pwa_files = [
    "index.html",
    "style.css",
    "app.js",
    "manifest.json",
    "serviceWorker.js",
    "backend_user_logs.json",
    "index_restored.html",
    "generate_test_cases.py",
    "export_backend_data.js",
    "deploy.ps1",
    "build_excel_findings.py"
]

for f in pwa_files:
    sf = os.path.join(src_dir, f)
    df = os.path.join(dst_dir, f)
    if os.path.exists(sf):
        shutil.copy2(sf, df)
        print(f"Copied {f} to root directory.")

print("PWA web app files successfully copied to root workspace!")
