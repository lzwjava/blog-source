---
audio: false
generated: true
image: false
lang: ar
layout: post
title: طرق التقاط نافذة بايثون في نظام ماك أو إس
translated: true
type: note
---

سؤال جيد 👍 — `pygetwindow` هو غلاف خفيف الوزن، ولكن هناك عدة مكتبات بايثون أخرى يمكنك استخدامها على نظام macOS للحصول على هندسة النافذة النشطة لالتقاط لقطات الشاشة:

---

## 1. **PyObjC + Quartz (واجهة برمجة تطبيقات macOS الأصلية)**

هذه هي الطريقة الأكثر مباشرة وموثوقية على نظام macOS، حيث يمنحك `Quartz` معلومات النافذة على مستوى النظام. مثال:

```bash
python3 -m pip install pyobjc
```

```python
import Quartz
from PIL import ImageGrab

# الحصول على حدود النافذة النشطة
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

هذا يتجنب الاعتماد على `pygetwindow` ويتواصل مباشرة مع CoreGraphics.

---

## 2. **AppKit (عبر PyObjC)**

أيضًا من PyObjC، ولكن من خلال AppKit:

```python
from AppKit import NSWorkspace

ws = NSWorkspace.sharedWorkspace()
active_app = ws.frontmostApplication()
print("Active App:", active_app.localizedName())
```

ستظل بحاجة إلى `Quartz` للإحداثيات، لكن AppKit يمنحك العملية الأمامية بطريقة أكثر نظافة.

---

## 3. **PyWinCtl**

بديل متعدد المنصات لـ `pygetwindow` (Windows، macOS، Linux):

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

هذا على الأرجح البديل الأقرب لـ pygetwindow من حيث كونه "جاهزًا للاستخدام"، ولكنه مع دعم أكثر اتساقًا لنظام macOS.

---

## 4. **PyAutoGUI**

بينما PyAutoGUI نفسه لا يوفر مقابض النوافذ، يمكنك التقاط الشاشة بالكامل أو تحديد منطقة يدويًا بمجرد معرفة الإحداثيات (من Quartz/AppKit).

---

✅ إذا كنت تريد **بديلاً متعدد المنصات بحتًا** لـ `pygetwindow`: استخدم **`pywinctl`**.
✅ إذا كنت تريد **دقة macOS أصلية ومزيدًا من التحكم**: استخدم **PyObjC + Quartz**.

هل تريد مني أن أريك نصًا برمجيًا جاهزًا للاستخدام **يعتمد فقط على PyObjC (Quartz)** (بدون أغلفة خارجية)، حتى تتمكن من التخلي عن `pygetwindow` تمامًا؟