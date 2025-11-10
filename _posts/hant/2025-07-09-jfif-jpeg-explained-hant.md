---
audio: false
generated: true
image: false
lang: hant
layout: post
title: JFIF 只是 JPEG 解說
translated: true
type: note
---

JFIF 代表 **JPEG 檔案交換格式**。

### 什麼是 JFIF

* 它並非獨立於 JPEG 的圖像格式，而是一種 **在 JPEG 檔案內嵌入元數據和結構的標準化方式**。
* 副檔名為 `.jfif` 的檔案仍然是 **JPEG 圖像** — 它們僅在檔案頭中明確聲明採用 JFIF 規範。
* 許多工具（特別是較舊的軟體如 Windows 小畫家或部分相機/掃描器）會預設使用 `.jfif` 作為副檔名，而非 `.jpg` 或 `.jpeg`。

因此，當你遇到 `.jfif` 檔案時，完全可以將其視作與 `.jpg` 圖像相同的檔案。

---

### 如何將 JFIF 轉換為標準圖像格式

1. **重新命名副檔名**

   * 大多數情況下，只需將 `image.jfif` 重新命名為 `image.jpg` 即可。
   * 由於底層格式是 JPEG，多數程式都能正常開啟此類檔案。

2. **使用圖像編輯軟體**

   * 使用 Photoshop、GIMP、小畫家或 macOS 的 Preview 開啟 `.jfif` 檔案。
   * 另存為/匯出為 `.jpg` 或 `.png` 格式。

3. **使用 Python (Pillow)**

   ```python
   from PIL import Image

   img = Image.open("image.jfif")
   img.save("image.jpg")   # 儲存為 JPEG
   img.save("image.png")   # 或轉換為 PNG
   ```

4. **使用命令列工具 (ImageMagick)**

   ```bash
   magick image.jfif image.jpg
   ```

   或使用 FFmpeg（因其亦能解碼圖像）：

   ```bash
   ffmpeg -i image.jfif image.jpg
   ```

---

✅ 總結來說：**JFIF 本質上就是 JPEG**，因此你可以像開啟 `.jpg` 檔案一樣處理它。若遇到相容性問題，只需重新命名或使用 Pillow/ImageMagick 進行轉換。

需要我為你提供一個能批次將資料夾內所有 `.jfif` 檔案轉換為 `.jpg` 的 **Python 腳本**嗎？