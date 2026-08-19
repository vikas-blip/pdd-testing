# ThermaScan Android Application Section (`/android`)

This directory contains all **Android Native, PWA & TWA (Trusted Web Activity)** code files:

## 📁 Directory Files
- 📲 manifest.json — Web App Manifest for Android home screen installation, launcher icons, standalone display mode.
- 🔑 .well-known/assetlinks.json — Digital Asset Links file verifying package SHA-256 fingerprint for Android TWA / Google Play Store association.
- ⚙️ serviceWorker.js — Android offline caching & background service worker logic.
- 🐍 upload_assetlinks.py — Python script for deploying and validating Android AssetLinks.
- 🔒 apply_native_ios_lockdown.py — Touch gesture and anti-zoom mobile lock controller.
