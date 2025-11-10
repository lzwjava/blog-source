---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: دليل البداية السريعة لـ PyGetWindow
translated: true
type: note
---

### التثبيت
PyGetWindow هي مكتبة بايثون للتحكم في النوافذ والاستعلام عنها على منصات متعددة (Windows وmacOS وLinux). قم بتثبيتها عبر pip:

```bash
pip install pygetwindow
```

### استيراد الوحدة
ابدأ باستيراد الوحدة في سكريبت البايثون الخاص بك:

```python
import pygetwindow as gw
```

### الحصول على كائنات النوافذ
تمثل PyGetWindow النوافذ ككائنات `Window`. يمكنك استرداد النوافذ حسب العنوان، أو العملية، أو السمات الأخرى.

- **الحصول على جميع كائنات النوافذ**:  
  استخدم `gw.getAllWindows()` لإرجاع قائمة بجميع النوافذ المفتوحة.

- **الحصول على النوافذ حسب العنوان**:  
  استخدم `gw.getWindowsWithTitle(title)` أو `gw.getFirstWindowWithTitle(title)` للمطابقات الجزئية أو التامة.

- **الحصول على النافذة النشطة**:  
  استخدم `gw.getActiveWindow()` للحصول على النافذة المحددة حاليًا.

مثال:
```python
windows = gw.getAllWindows()
active = gw.getActiveWindow()
notepad = gw.getWindowsWithTitle('Notepad')  # قائمة النوافذ التي تحتوي على 'Notepad' في العنوان
```

### الطرق الشائعة على كائنات النوافذ
بمجرد حصولك على كائن `Window`، يمكنك الوصول إلى الخصائص والطرق مثل:

- **الخصائص**: `title`, `left`, `top`, `width`, `height`, `isMinimized`, `isMaximized`, `isActive`.
- **الطرق**: 
  - `activate()`: إحضار النافذة إلى الأمام وجعلها نشطة.
  - `maximize()` / `minimize()` / `restore()` / `close()`: التحكم في حالة النافذة.
  - `resize() / move()`: ضبط الحجم والموضع.

مثال:
```python
if notepad:
    win = notepad[0]
    print(win.title)  # الإخراج: على سبيل المثال، 'Untitled - Notepad'
    win.activate()
    win.maximize()
    win.move(100, 100)  # الانتقال إلى الموضع (100, 100)
    win.resize(800, 600)  # تغيير الحجم إلى 800x600
```

### التعامل مع المنصات المتعددة
- على Windows وmacOS، تستخدم واجهات برمجة التطبيقات (APIs) الأصلية.
- على Linux، تعتمد على دعم X11 أو Wayland؛ تأكد من تثبيته على نظامك (مثل `x11-utils` على Ubuntu).
- إذا لم تكن الطريقة مدعومة على نظام التشغيل الخاص بك، فقد ترفع استثناءً `NotImplementedError`.

### أمثلة
إليك بعض مقاطع التعليمات البرمجية العملية:

1. **طباعة جميع عناوين النوافذ**:
   ```python
   for win in gw.getAllWindows():
       print(win.title)
   ```

2. **إغلاق نافذة محددة**:
   ```python
   firefox_wins = gw.getWindowsWithTitle('Mozilla Firefox')
   if firefox_wins:
       firefox_wins[0].close()
   ```

3. **تحريك وتغيير حجم نوافذ متعددة**:
   ```python
   windows = gw.getAllWindows()
   for i, win in enumerate(windows[:3]):  # أول 3 نوافذ
       win.move(50 * i, 50 * i)
       win.resize(400, 400)
   ```

للحصول على استخدام متقدم، راجع [الوثائق الرسمية](https://pygetwindow.readthedocs.io/). إذا واجهت مشاكل خاصة بمنصة معينة، فتحقق من أذونات النظام أو التبعيات مثل `xdotool` على Linux.