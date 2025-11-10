---
audio: false
generated: true
image: false
lang: de
layout: post
title: Behebung des PIL-Imaging-Backend-Fehlers
translated: true
type: note
---

Dieser Fehler bedeutet, dass Ihrer PIL-Installation entweder das binäre Backend (`_imaging`) fehlt oder Sie versehentlich das alte „PIL“-Paket anstelle des modernen „Pillow“ verwenden. So beheben Sie das Problem:

1. **Stellen Sie sicher, dass Sie Python 3 verwenden**
   Wenn `python` auf Python 2 verweist, wechseln Sie zu Python 3:

   ```bash
   python3 --version
   python3 scripts/content/avatar.py
   ```

2. **Deinstallieren Sie veraltete PIL-Pakete**

   ```bash
   # Dies entfernt das alte PIL, falls es über pip installiert wurde
   python3 -m pip uninstall -y PIL
   ```

3. **(Erneut) Installieren Sie Pillow**

   ```bash
   python3 -m pip install --upgrade --force-reinstall pillow
   ```

4. **Installieren Sie die erforderlichen Systembibliotheken**
   Unter Ubuntu benötigen Sie die Imaging-Header, damit Pillow seine `_imaging`-Erweiterung bauen kann:

   ```bash
   sudo apt update
   sudo apt install -y libjpeg-dev zlib1g-dev
   # Installieren Sie Pillow dann neu, damit es gegen diese Bibliotheken neu kompiliert wird
   python3 -m pip install --upgrade --force-reinstall pillow
   ```

5. **Verwenden Sie eine Virtual Environment (optional, aber empfohlen)**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install pillow
   python scripts/content/avatar.py
   ```

Danach sollte `from PIL import Image` ohne den `_imaging`-Importfehler funktionieren.