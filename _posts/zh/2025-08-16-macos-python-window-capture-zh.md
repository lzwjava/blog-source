---
audio: false
generated: true
image: false
lang: zh
layout: post
title: MacOS Python 窗口捕获方法
translated: true
type: note
---

好问题 👍 — `pygetwindow` 确实是个轻量级封装，不过在 macOS 上还有其他几种获取活动窗口坐标以进行屏幕截图的 Python 库方案：

---

## 1. **PyObjC + Quartz（原生 macOS API）**

这是最直接可靠的方式，因为 `Quartz` 能在系统层级提供窗口信息。示例：

```bash
python3 -m pip install pyobjc
```

```python
import Quartz
from PIL import ImageGrab

# 获取活动窗口边界
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
    print(f"已保存 active-window.png 尺寸={img.size}")
```

这种方法无需依赖 `pygetwindow`，直接与 CoreGraphics 交互。

---

## 2. **AppKit（通过 PyObjC）**

同样基于 PyObjC，但通过 AppKit 实现：

```python
from AppKit import NSWorkspace

ws = NSWorkspace.sharedWorkspace()
active_app = ws.frontmostApplication()
print("当前应用:", active_app.localizedName())
```

虽然坐标获取仍需依赖 `Quartz`，但 AppKit 能更清晰地获取前台进程信息。

---

## 3. **PyWinCtl**

跨平台的 `pygetwindow` 替代方案（支持 Windows、macOS、Linux）：

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
    print("已保存 active-window.png")
```

这可能是最接近 pygetwindow 的“开箱即用”替代方案，且对 macOS 支持更稳定。

---

## 4. **PyAutoGUI**

虽然 PyAutoGUI 本身不提供窗口句柄，但在获取坐标后（通过 Quartz/AppKit）可以手动截取全屏或指定区域。

---

✅ 若需要 **纯跨平台的 `pygetwindow` 替代品**：推荐 **`pywinctl`**  
✅ 若需要 **原生 macOS 精准控制和更高自由度**：推荐 **PyObjC + Quartz**

需要我为您展示一个 **仅依赖 PyObjC (Quartz)**（无需第三方封装）的完整脚本吗？这样就能彻底摆脱 `pygetwindow` 了。