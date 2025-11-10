---
audio: false
generated: true
image: false
lang: ja
layout: post
title: macOS Python ウィンドウキャプチャ方法
translated: true
type: note
---

良い質問です 👍 — `pygetwindow`は軽量なラッパーですが、macOSでスクリーンショット用にアクティブウィンドウのジオメトリを取得するために使用できる他のPythonライブラリがいくつかあります：

---

## 1. **PyObjC + Quartz (ネイティブmacOS API)**

これはmacOS上で最も直接的で信頼性の高い方法です。`Quartz`はシステムレベルでウィンドウ情報を提供するためです。例：

```bash
python3 -m pip install pyobjc
```

```python
import Quartz
from PIL import ImageGrab

# アクティブウィンドウの境界を取得
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
    print(f"Saved active-window.png size={img.size}")
```

これにより`pygetwindow`への依存を避け、CoreGraphicsと直接通信します。

---

## 2. **AppKit (PyObjC経由)**

これもPyObjCからですが、AppKitを通じて：

```python
from AppKit import NSWorkspace

ws = NSWorkspace.sharedWorkspace()
active_app = ws.frontmostApplication()
print("Active App:", active_app.localizedName())
```

座標にはまだ`Quartz`が必要ですが、AppKitはフォアグラウンドプロセスをよりクリーンに取得します。

---

## 3. **PyWinCtl**

`pygetwindow`のクロスプラットフォーム代替（Windows、macOS、Linux）：

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
    print("Saved active-window.png")
```

これはおそらく`pygetwindow`に最も近い「ドロップイン」代替であり、より一貫したmacOSサポートを提供します。

---

## 4. **PyAutoGUI**

PyAutoGUI自体はウィンドウハンドルを提供しませんが、座標が分かれば（Quartz/AppKitから）、全画面をキャプチャしたり、領域を手動で定義したりできます。

---

✅ **純粋なクロスプラットフォーム代替**を求める場合：**`pywinctl`**を使用してください。
✅ **ネイティブなmacOSの精度とより多くの制御**を求める場合：**PyObjC + Quartz**を使用してください。

`pygetwindow`を完全に排除できる、**PyObjC (Quartz)のみに依存する**すぐに使用できるスクリプトをお見せしましょうか？