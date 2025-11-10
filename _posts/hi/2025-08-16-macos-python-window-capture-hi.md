---
audio: false
generated: true
image: false
lang: hi
layout: post
title: मैकओएस पायथन विंडो कैप्चर विधियाँ
translated: true
type: note
---

अच्छा सवाल है 👍 — `pygetwindow` एक lightweight wrapper है, लेकिन macOS पर स्क्रीनशॉट के लिए active window की ज्यामिति प्राप्त करने के लिए आप कई अन्य Python libraries का उपयोग कर सकते हैं:

---

## 1. **PyObjC + Quartz (native macOS API)**

यह macOS पर सबसे direct और reliable तरीका है, क्योंकि `Quartz` आपको system level पर window की जानकारी देता है। उदाहरण:

```bash
python3 -m pip install pyobjc
```

```python
import Quartz
from PIL import ImageGrab

# Get active window bounds
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

यह `pygetwindow` पर निर्भरता से बचता है और सीधे CoreGraphics से बात करता है।

---

## 2. **AppKit (via PyObjC)**

यह भी PyObjC से है, लेकिन AppKit के माध्यम से:

```python
from AppKit import NSWorkspace

ws = NSWorkspace.sharedWorkspace()
active_app = ws.frontmostApplication()
print("Active App:", active_app.localizedName())
```

आपको coordinates के लिए अभी भी `Quartz` की आवश्यकता होगी, लेकिन AppKit आपको foreground process अधिक साफ़ तरीके से देता है।

---

## 3. **PyWinCtl**

`pygetwindow` का cross-platform replacement (Windows, macOS, Linux):

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

यह शायद pygetwindow का सबसे करीबी "drop-in" विकल्प है, लेकिन अधिक सुसंगत macOS सपोर्ट के साथ।

---

## 4. **PyAutoGUI**

हालांकि PyAutoGUI स्वयं window हैंडल प्रदान नहीं करता है, एक बार जब आप coordinates (Quartz/AppKit से) जान जाते हैं, तो आप पूरी स्क्रीन कैप्चर कर सकते हैं या मैन्युअल रूप से एक region परिभाषित कर सकते हैं।

---

✅ यदि आप `pygetwindow` का **एक pure cross-platform replacement** चाहते हैं: **`pywinctl`** का उपयोग करें।
✅ यदि आप **native macOS precision और अधिक नियंत्रण** चाहते हैं: **PyObjC + Quartz** का उपयोग करें।

क्या आप चाहते हैं कि मैं आपको एक ready-to-use script दिखाऊं जो **केवल PyObjC (Quartz) पर निर्भर करती है** (कोई third-party wrappers नहीं), ताकि आप `pygetwindow` को पूरी तरह से छोड़ सकें?