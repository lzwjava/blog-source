---
audio: false
generated: true
image: false
lang: hant
layout: post
title: macOS Python 視窗擷取方法
translated: true
type: note
---

好問題 👍 — `pygetwindow` 是個輕量級的封裝程式庫，但在 macOS 上還有其他幾個 Python 程式庫可以用來取得作用中視窗的幾何資訊以進行螢幕截圖：

---

## 1. **PyObjC + Quartz (原生 macOS API)**

這是在 macOS 上最直接可靠的方法，因為 `Quartz` 能在系統層級提供視窗資訊。範例：

```bash
python3 -m pip install pyobjc
```

```python
import Quartz
from PIL import ImageGrab

# 取得作用中視窗邊界
window_info = Quartz.CGWindowListCopyWindowInfo(
    Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID
)

active_app = Quartz.CGWindowListCopyWindowInfo(
    Quartz.kCGWindowListOptionOnScreenOnly | Quartz.kCGWindowListOptionOnScreenAbove,
    Quartz.kCGNullWindowID,
)

if active_app:
    bounds = active_app[0]['kCGWindowBounds']
    x, y = int(bounds['X']), int(bounds['Y'])
    w, h = int(bounds['Width']), int(bounds['Height'])
    img = ImageGrab.grab(bbox=(x, y, x + w, y + h))
    img.save("active-window.png")
    print(f"已儲存 active-window.png 尺寸={img.size}")
```

這樣就無需依賴 `pygetwindow`，直接與 CoreGraphics 溝通。

---

## 2. **AppKit (透過 PyObjC)**

同樣來自 PyObjC，但透過 AppKit 實現：

```python
from AppKit import NSWorkspace

ws = NSWorkspace.sharedWorkspace()
active_app = ws.frontmostApplication()
print("作用中應用程式：", active_app.localizedName())
```

你仍然需要 `Quartz` 來取得座標，但 AppKit 能更簡潔地取得前景處理程序。

---

## 3. **PyWinCtl**

`pygetwindow` 的跨平台替代方案（Windows、macOS、Linux）：

```bash
python3 -m pip install pywinctl
```

```python
import pywinctl
from PIL import ImageGrab

active = pywinctl.getActiveWindow()
if active:
    x, y, w, h = active.left, active.top, active.width, active.height
    img = ImageGrab.grab(bbox=(x, y, x + w, y + h))
    img.save("active-window.png")
    print("已儲存 active-window.png")
```

這可能是最接近 pygetwindow 的「即插即用」替代方案，並提供更一致的 macOS 支援。

---

## 4. **PyAutoGUI**

雖然 PyAutoGUI 本身不提供視窗控制代碼，但一旦你從 Quartz/AppKit 取得座標後，可以手動擷取整個螢幕或定義區域。

---

✅ 如果你想要 **純粹的跨平台替代方案** 來取代 `pygetwindow`：使用 **`pywinctl`**。
✅ 如果你想要 **原生 macOS 精確度和更多控制權**：使用 **PyObjC + Quartz**。

需要我展示一個 **僅依賴 PyObjC (Quartz)**（無需第三方封裝）的即用腳本，讓你可以完全棄用 `pygetwindow` 嗎？