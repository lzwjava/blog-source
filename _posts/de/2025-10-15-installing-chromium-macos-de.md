---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Installation von Chromium auf macOS
translated: true
type: note
---

Ja, macOS kann Chromium definitiv als Alternative zu Google Chrome installieren. Chromium ist die Open-Source-Grundlage, auf der Chrome aufbaut, daher ist es in der Funktionalität sehr ähnlich, es fehlen jedoch einige proprietäre Google-Funktionen wie automatische Updates und bestimmte Codecs.

### So installieren Sie es
Es gibt einige einfache Methoden:

1. **Über Homebrew (am einfachsten für die meisten Benutzer)**:
   - Installieren Sie Homebrew, falls noch nicht geschehen: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`.
   - Führen Sie dann aus: `brew install --cask chromium`.
   - Dies funktioniert sowohl auf Intel- als auch auf Apple Silicon (M1/M2/M3) Macs.

2. **Direkter Download**:
   - Gehen Sie auf die offizielle Chromium-Website und laden Sie den neuesten Build für Mac herunter.
   - Entpacken Sie die Datei und ziehen Sie die App in Ihren Programme-Ordner.

3. **Für Entwickler oder benutzerdefinierte Builds**:
   - Verwenden Sie Tools wie Woolyss für vorgefertigte Releases oder bauen Sie es bei Bedarf aus dem Quellcode (erfordert Xcode).

Sobald es installiert ist, können Sie Chromium in den Systemeinstellungen > Schreibtisch & Dock > Standard-Webbrowser als Ihren Standardbrowser festlegen.

[Chromium herunterladen](https://www.chromium.org/getting-involved/download-chromium/)  
[Homebrew Formula](https://formulae.brew.sh/cask/chromium)  
[Installation auf Apple Silicon](https://dev.to/pixelrena/installing-chromium-on-mac-apple-m2-pro-tutorial-4i4i)  
[MacUpdate Download](https://chromium.macupdate.com/)  
[Aktuelle Releases](https://chromium.woolyss.com/download/en/)