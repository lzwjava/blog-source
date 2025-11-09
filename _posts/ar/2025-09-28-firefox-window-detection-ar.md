---
audio: false
generated: true
image: false
lang: ar
layout: post
model: anthropic/claude-sonnet-4
title: أدوات كشف نوافذ فايرفوكس لنظام لينكس
translated: true
type: note
---

بالإضافة إلى `xdotool`، هناك عدة أدوات وطرق بديلة للحصول على معلومات عن نافذة فايرفوكس النشطة على لينكس:

## أدوات بديلة

### 1. **wmctrl**
بديل أكثر متانة لـ xdotool:
```bash
# الحصول على النافذة النشطة
wmctrl -a

# سرد جميع النوافذ بالتفاصيل
wmctrl -l -x

# الحصول على نوافذ فايرفوكس تحديدًا
wmctrl -l | grep -i firefox
```

### 2. **qdbus** (لتطبيقات KDE/Qt)
```bash
# الحصول على معلومات النافذة النشطة
qdbus org.kde.KWin /KWin activeWindow

# الحصول على قائمة النوافذ
qdbus org.kde.KWin /KWin windows
```

### 3. **xwininfo**
أداة X11 المدمجة:
```bash
# اختيار النافذة بشكل تفاعلي
xwininfo

# الحصول على معلومات نافذة الجذر
xwininfo -root -tree | grep -i firefox

# الحصول على النافذة النشطة (يتطلب معرفة معرف النافذة)
xwininfo -id $(xprop -root _NET_ACTIVE_WINDOW | cut -d' ' -f5)
```

### 4. **xprop**
أداة X11 أخرى:
```bash
# الحصول على خصائص النافذة النشطة
xprop -root _NET_ACTIVE_WINDOW

# الحصول على صنف النافذة وعنوانها
xprop -root | grep "_NET_ACTIVE_WINDOW(WINDOW)"
```

## لأنظمة Wayland

إذا كنت تستخدم Wayland، فإن أدوات X11 لن تعمل. جرب هذه البدائل:

### 5. **swaymsg** (لـ Sway)
```bash
swaymsg -t get_tree | jq -r '.. | select(.focused? == true)'
```

### 6. **hyprctl** (لـ Hyprland)
```bash
hyprctl activewindow
```

### 7. **gdbus** (GNOME/GTK)
```bash
gdbus call --session --dest org.gnome.Shell --object-path /org/gnome/Shell --method org.gnome.Shell.Eval "global.get_window_actors()"
```

## حلول بايثون

### 8. **بايثون مع Xlib**
```python
from Xlib import X, display
from Xlib.error import XError

def get_active_window():
    try:
        d = display.Display()
        root = d.screen().root
        
        # الحصول على النافذة النشطة
        active_window = root.get_full_property(
            d.intern_atom('_NET_ACTIVE_WINDOW'), X.AnyPropertyType
        )
        
        if active_window:
            window_id = active_window.value[0]
            window = d.create_resource_object('window', window_id)
            window_name = window.get_wm_name()
            return window_name
    except XError:
        return None

print(get_active_window())
```

### 9. **بايثون مع subprocess**
```python
import subprocess

def get_firefox_windows():
    try:
        # استخدام wmctrl
        result = subprocess.run(['wmctrl', '-l'], 
                              capture_output=True, text=True)
        firefox_windows = [line for line in result.stdout.split('\n') 
                          if 'firefox' in line.lower()]
        return firefox_windows
    except FileNotFoundError:
        return "wmctrl not installed"

print(get_firefox_windows())
```

## استكشاف أخطاء مشكلة xdotool الخاصة بك

خطأ "BadWindow" يعني عادة:

1. **مشاكل في الأذونات**: حاول التشغيل بأذونات مختلفة
2. **مشاكل في العرض**: تحقق مما إذا كان `$DISPLAY` مضبوطًا بشكل صحيح
3. **تعارض مع Wayland**: قد تكون على Wayland بدلاً من X11

للتحقق من خادم العرض الخاص بك:
```bash
echo $XDG_SESSION_TYPE
loginctl show-session $(loginctl | grep $(whoami) | awk '{print $1}') -p Type
```

## النهج الموصى به

لتحقيق أقصى قدر من التوافق، أوصي بهذا الترتيب:

1. **wmctrl** - الأكثر موثوقية عبر مدير النوافذ المختلفة
2. **مزيج xwininfo + xprop** - مضمن في معظم تثبيتات X11
3. **حل بايثون** - الأكثر مرونة وقابلية للبرمجة
4. **أدوات بيئة سطح المكتب المحددة** (swaymsg, hyprctl، إلخ)

جرب `wmctrl -l | grep -i firefox` أولاً - فهو عادةً البديل الأكثر مباشرة لوظيفة اكتشاف النوافذ في xdotool.