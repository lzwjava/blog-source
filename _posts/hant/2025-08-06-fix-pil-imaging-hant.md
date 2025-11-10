---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 修復PIL影像後端錯誤
translated: true
type: note
---

這個錯誤表示你的 PIL 安裝缺少二進制後端 (`_imaging`)，或者你不小心使用了舊版的「PIL」套件而非現代的「Pillow」。以下是解決方法：

1. **確認你使用 Python 3**
   如果 `python` 指向 Python 2，請切換到 Python 3：

   ```bash
   python3 --version
   python3 scripts/content/avatar.py
   ```

2. **解除安裝舊版 PIL 套件**

   ```bash
   # 如果舊版 PIL 是透過 pip 安裝的，此指令會將其移除
   python3 -m pip uninstall -y PIL
   ```

3. **（重新）安裝 Pillow**

   ```bash
   python3 -m pip install --upgrade --force-reinstall pillow
   ```

4. **安裝必要的系統函式庫**
   在 Ubuntu 上，你需要安裝影像標頭檔，這樣 Pillow 才能建置其 `_imaging` 擴充功能：

   ```bash
   sudo apt update
   sudo apt install -y libjpeg-dev zlib1g-dev
   # 然後重新安裝 Pillow，讓它針對這些函式庫重新編譯
   python3 -m pip install --upgrade --force-reinstall pillow
   ```

5. **使用虛擬環境（可選但建議）**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install pillow
   python scripts/content/avatar.py
   ```

完成後，`from PIL import Image` 應該就能正常運作，不會再出現 `_imaging` 匯入錯誤。