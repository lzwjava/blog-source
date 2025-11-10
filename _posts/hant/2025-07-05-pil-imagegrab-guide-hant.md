---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: PIL ImageGrab 截圖指南
translated: true
type: note
---

### 前置準備
要使用 PIL (Pillow) 函式庫中的 `ImageGrab`，請確保已安裝 Pillow。在 Windows 系統上，可透過 pip 安裝：
```
pip install Pillow
```
Windows 通常無需額外設定，因為 `ImageGrab` 使用原生 Windows API。

### 基礎用法
`ImageGrab.grab()` 會擷取整個螢幕（所有顯示器）作為 PIL Image 物件。以下為擷取螢幕截圖並儲存為 PNG 檔案的簡單範例：

```python
from PIL import ImageGrab

# 擷取整個螢幕
screenshot = ImageGrab.grab()

# 將影像儲存至檔案
screenshot.save("screenshot.png")
```

這會將名為 `screenshot.png` 的檔案儲存至當前工作目錄。

### 進階選項
- **擷取特定區域**：指定邊界框（左、上、右、下）作為像素座標的元組。
  ```python
  # 擷取從 (100, 100) 開始的 300x300 像素區域
  region = (100, 100, 400, 400)  # 請根據需要調整座標
  screenshot = ImageGrab.grab(bbox=region)
  screenshot.save("region_screenshot.png")
  ```
- **包含滑鼠游標**（若支援；請查閱 Pillow 文件以確認版本細節）：
  ```python
  # 注意：在某些系統上可能需要設定 include_layered_windows=True
  screenshot = ImageGrab.grab(include_layered_windows=True)
  ```
- **顯示影像**：使用 `screenshot.show()` 在預設圖片檢視器中開啟（用於測試）。

### 注意事項
- 座標單位為像素，主顯示器的左上角為 (0, 0)
- 在多顯示器設定中，`grab()` 會將所有螢幕擷取為單一合成影像
- 若遇到問題（例如新版 Windows 的權限錯誤），請確保腳本具有螢幕擷取權限，或嘗試以管理員權限執行
- 完整文件：[Pillow ImageGrab 文件](https://pillow.readthedocs.io/en/stable/reference/ImageGrab.html)。若需 Windows 特定疑難排解，可查閱 GitHub 相關議題