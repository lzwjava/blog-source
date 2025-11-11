---
audio: false
generated: true
image: false
lang: hant
layout: post
title: PIL 與 PyAutoGUI 截圖比較
translated: true
type: note
---

**PIL 的 `ImageGrab`** 與 **PyAutoGUI 的截圖工具** 都能擷取螢幕畫面，但它們在用法、功能和跨平台支援方面有所不同。

---

## 1. PIL (Pillow) – `ImageGrab`

`ImageGrab` 是 **Pillow（現代 PIL 分支）** 的一部分，可讓您擷取整個螢幕或部分區域。

### 運作原理

* 在 **Windows 和 macOS** 上，它使用原生 API（Windows 使用 GDI，macOS 使用 Quartz）來擷取像素。
* 在 **Linux** 上，預設不支援（需要額外套件庫如 `xwd`）。

### 使用範例

```python
from PIL import ImageGrab

# 擷取整個螢幕
screenshot = ImageGrab.grab()
screenshot.save("screenshot.png")

# 擷取指定區域（左、上、右、下）
region = (100, 100, 500, 500)
cropped_screenshot = ImageGrab.grab(bbox=region)
cropped_screenshot.show()
```

### 優點

* 簡單易用，屬於 Pillow 套件的一部分（無需額外依賴）。
* 若已使用 Pillow 進行影像處理，整合性佳。

### 缺點

* 預設不支援 Linux。
* 靈活性較低（不支援多螢幕辨識）。

---

## 2. PyAutoGUI – `screenshot()`

PyAutoGUI 是更通用的自動化工具（包含滑鼠/鍵盤控制與螢幕擷取功能）。

### 運作原理

* 內部封裝 **Pillow**。
* 使用作業系統 API（跨平台支援：Windows、macOS、Linux）。
* 可直接返回 Pillow `Image` 物件或儲存為檔案。

### 使用範例

```python
import pyautogui

# 擷取整個螢幕
screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

# 擷取指定區域（左、上、寬度、高度）
region_screenshot = pyautogui.screenshot(region=(100, 100, 400, 400))
region_screenshot.show()
```

### 優點

* 跨平台支援（Windows、macOS、Linux）。
* 易與自動化腳本整合（滑鼠/鍵盤控制）。
* 可直接擷取特定區域。

### 缺點

* 因抽象層較多，速度略慢於 `ImageGrab`。
* 需要額外安裝依賴項（`pip install pyautogui`）。

---

## 該如何選擇？

* **若只需截圖功能且使用 Windows/macOS** → `ImageGrab` 輕量且快速。
* **若需自動化功能或 Linux 支援** → `pyautogui` 更適合。

---

👉 是否需要我進一步示範如何用 Python 程式碼 **對 `ImageGrab` 與 `pyautogui.screenshot()` 進行效能評測**？