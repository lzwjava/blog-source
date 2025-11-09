---
audio: false
generated: true
image: false
lang: ar
layout: post
model: anthropic/claude-sonnet-4
title: دليل تصحيح أخطاء أداة xdotool لنظام X11
translated: true
type: note
---

الخطأ الذي تراه يشير إلى أن `xdotool` يواجه مشكلة في الحصول على معلومات النافذة النشطة من خادم X الخاص بك. إليك عدة طرق لتشخيص المشكلة والحصول على معلومات تفصيلية أكثر عن الخطأ:

## 1. التحقق من بيئة X11
أولاً، تحقق من بيئة العرض الخاصة بك:
```bash
echo $DISPLAY
echo $XDG_SESSION_TYPE
```

إذا كنت تستخدم Wayland بدلاً من X11، فإن `xdotool` لن يعمل بشكل صحيح لأنه مصمم لـ X11.

## 2. استخدام الوضع التفصيلي
جرب تشغيل xdotool مع إخراج أكثر تفصيلاً:
```bash
xdotool --help  # التحقق من الخيارات المتاحة
```

## 3. أوامر التصحيح البديلة
جرب هذه الأوامر لجمع المزيد من المعلومات:

```bash
# التحقق من إمكانية الوصول إلى خادم X
xwininfo -root -tree

# تجربة أمر xdotool أبسط
xdotool search --name ".*" | head -5

# التحقق من مدير النوافذ
wmctrl -l  # عرض جميع النوافذ
wmctrl -d  # عرض مساحات العمل

# التحقق من خصائص X11 مباشرة
xprop -root _NET_ACTIVE_WINDOW
```

## 4. التحقق من إضافات X11
قد يكون الخطأ متعلقاً بغياب إضافات X11 المطلوبة:
```bash
# التحقق من الإضافات المتاحة
xdpyinfo | grep -i extension

# البحث تحديداً عن الإضافات المطلوبة
xdpyinfo | grep -E "(XTEST|Extended-Visual-Information)"
```

## 5. مشاكل الصلاحيات
تحقق مما إذا كنت تملك الصلاحيات المناسبة:
```bash
# التحقق من إمكانية الوصول إلى العرض
xhost +local:
```

## 6. أدوات بديلة
إذا استمر فشل xdotool، جرب هذه البدائل:

```bash
# لـ Wayland
if [ "$XDG_SESSION_TYPE" = "wayland" ]; then
    # استخدام wlr-activewindow إذا كان متاحاً (لـ Wayland)
    swaymsg -t get_tree | jq '.. | select(.focused?) | .name'
fi

# بدائل X11
xtitle  # إذا كان مثبتاً
xprop -root | grep "_NET_ACTIVE_WINDOW(WINDOW)"
```

## 7. معلومات النظام
تحقق من إعدادات نظامك:
```bash
# التحقق من بيئة سطح المكتب
echo $DESKTOP_SESSION
ps aux | grep -E "(gnome|kde|xfce|i3|sway)"

# التحقق إذا كنت تعمل في حاوية أو آلة افتراضية
systemd-detect-virt
```

أكثر الأسباب احتمالاً هي:
1. **جلسة Wayland**: xdotool لا يعمل مع Wayland
2. **غياب الصلاحيات**: قيود الوصول إلى خادم X
3. **عدم توافق مدير النوافذ**: بعض مديري النوافذ لا يدعمون `_NET_ACTIVE_WINDOW`
4. **غياب إضافات X11**: الإضافات المطلوبة غير محملة

جرب أوامر التشخيص أعلاه وأخبرني بالمخرجات التي تحصل عليها - هذا سيساعد في تحديد المشكلة الدقيقة.