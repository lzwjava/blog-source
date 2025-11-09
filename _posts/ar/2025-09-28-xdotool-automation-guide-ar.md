---
audio: false
generated: true
image: false
lang: ar
layout: post
model: anthropic/claude-sonnet-4
title: دليل الأتمتة عبر سطر الأوامر باستخدام xdotool
translated: true
type: note
---

## ما هو xdotool؟

xdotool هو أداة أتمتة سطر الأوامر لـ X11 (بيئات سطح مكتب Linux) تتيح لك:
- التحكم في حركات الفأرة والنقرات
- إرسال ضغطات المفاتيح إلى التطبيقات
- معالجة النوافذ (نقل، تغيير الحجم، التركيز)
- البحث عن النوافذ بناءً على معايير مختلفة
- أتمتة تفاعلات سطح المكتب برمجيًا

## التثبيت

```bash
# Ubuntu/Debian
sudo apt install xdotool

# Fedora/RHEL/CentOS
sudo dnf install xdotool

# Arch Linux
sudo pacman -S xdotool

# من المصدر
git clone https://github.com/jordansissel/xdotool
cd xdotool
make
sudo make install
```

## الأوامر الأساسية

### أوامر معلومات النافذة

#### `getactivewindow`
يحصل على معرف النافذة النشطة/المحددة حاليًا.
```bash
xdotool getactivewindow
# الإخراج: 52428807 (معرف النافذة)

# الحصول على عنوان النافذة النشطة
xdotool getactivewindow getwindowname
```

#### `getwindowfocus`
مشابه لـ getactivewindow ولكن قد يتصرف بشكل مختلف في بعض مديري النوافذ.
```bash
xdotool getwindowfocus
```

#### `getwindowname`
يحصل على عنوان/اسم النافذة.
```bash
# الحصول على اسم النافذة النشطة
xdotool getactivewindow getwindowname

# الحصول على اسم معرف نافذة محدد
xdotool getwindowname 52428807
```

#### `getwindowpid`
يحصل على معرف العملية (PID) المرتبط بالنافذة.
```bash
xdotool getactivewindow getwindowpid
```

#### `getwindowgeometry`
يحصل على معلومات موقع وحجم النافذة.
```bash
xdotool getactivewindow getwindowgeometry
# الإخراج: Window 52428807
#   Position: 100,50 (screen: 0)
#   Geometry: 800x600
```

#### `getdisplaygeometry`
يحصل على أبعاد الشاشة/العرض.
```bash
xdotool getdisplaygeometry
# الإخراج: 1920x1080
```

### البحث عن النوافذ واختيارها

#### `search`
البحث عن النوافذ بناءً على معايير مختلفة.
```bash
# البحث حسب اسم/عنوان النافذة
xdotool search --name "Firefox"
xdotool search --name "Terminal"

# البحث حسب اسم الفئة
xdotool search --class "firefox"

# بحث غير حساس لحالة الأحرف
xdotool search --name --onlyvisible --maxdepth 1 "terminal"

# خيارات البحث الشائعة:
# --name: البحث في عناوين النوافذ
# --class: البحث في أسماء فئات النوافذ
# --classname: البحث في أسماء مثيلات فئة النافذة
# --onlyvisible: النوافذ المرئية فقط
# --maxdepth N: تحديد عمق البحث
# --limit N: تحديد عدد النتائج
# --desktop N: البحث في سطح مكتب/مساحة عمل محددة
```

#### `selectwindow`
اختيار النافذة تفاعليًا (انقر لتحديد).
```bash
xdotool selectwindow
# انقر على أي نافذة للحصول على معرفها
```

### التحكم في الفأرة

#### `click`
محاكاة نقرات الفأرة.
```bash
# نقر يساري في الموضع الحالي
xdotool click 1

# نقر يميني
xdotool click 3

# نقر وسطي
xdotool click 2

# نقر مزدوج
xdotool click --repeat 2 1

# النقر في إحداثيات محددة
xdotool mousemove 500 300 click 1

# النقر مع تأخير
xdotool click --delay 500 1
```

#### `getmouselocation`
الحصول على موضع مؤشر الفأرة الحالي.
```bash
xdotool getmouselocation
# الإخراج: x:500 y:300 screen:0 window:52428807

# الحصول على الإحداثيات فقط
xdotool getmouselocation --shell
# الإخراج: X=500 Y=300 SCREEN=0 WINDOW=52428807
```

#### حركة الفأرة
```bash
# تحريك الفأرة إلى موضع مطلق
xdotool mousemove 500 300

# تحريك الفأرة نسبيًا للموضع الحالي
xdotool mousemove_relative 10 -20

# التحريك والنقر في أمر واحد
xdotool mousemove 500 300 click 1
```

### إدخال لوحة المفاتيح

#### `key`
إرسال ضغطات المفاتيح إلى النافذة النشطة.
```bash
# إرسال مفتاح واحد
xdotool key Return
xdotool key Escape
xdotool key Tab

# إرسال تركيبات المفاتيح
xdotool key ctrl+c
xdotool key ctrl+alt+t
xdotool key shift+F10

# إرسال مفاتيح متعددة بالتسلسل
xdotool key ctrl+l type "https://google.com" key Return

# أسماء المفاتيح الشائعة:
# - الأحرف: a, b, c, ... (أحرف صغيرة)
# - الأرقام: 1, 2, 3, ...
# - الخاصة: Return, Escape, Tab, space, BackSpace, Delete
# - الوظائف: F1, F2, ... F12
# - المعدلات: ctrl, alt, shift, super (مفتاح Windows)
# - الأسهم: Up, Down, Left, Right
```

#### إدخال النص
```bash
# كتابة نص (يحاكي كتابة كل حرف)
xdotool type "Hello World"

# الكتابة مع تأخير بين الأحرف
xdotool type --delay 100 "Slow typing"

# مسح التأخير للكتابة السريعة
xdotool type --clearmodifiers --delay 0 "Fast text"
```

### معالجة النوافذ

```bash
# تركيز/تفعيل نافذة
xdotool windowactivate WINDOW_ID

# تصغير النافذة
xdotool windowminimize WINDOW_ID

# تكبير النافذة
xdotool windowmaximize WINDOW_ID

# إغلاق النافذة
xdotool windowclose WINDOW_ID

# نقل النافذة إلى موضع
xdotool windowmove WINDOW_ID 100 50

# تغيير حجم النافذة
xdotool windowsize WINDOW_ID 800 600

# نقل النافذة إلى سطح مكتب محدد
xdotool set_desktop_for_window WINDOW_ID 2

# رفع النافذة إلى الأعلى
xdotool windowraise WINDOW_ID

# عرض النافذة
xdotool windowmap WINDOW_ID

# إخفاء النافذة
xdotool windowunmap WINDOW_ID
```

### الميزات المتقدمة

#### `behave`
إعداد سلوكيات أحداث النافذة (المشغلات).
```bash
# تنفيذ أمر عندما تكتسب النافذة التركيز
xdotool behave WINDOW_ID focus exec echo "Window focused"

# التنفيذ عند إنشاء النافذة
xdotool behave WINDOW_ID create exec "notify-send 'New window'"

# الأحداث المتاحة: focus, unfocus, mouse-enter, mouse-leave, create, destroy
```

#### `behave_screen_edge`
تشغيل الإجراءات عندما تصل الفأرة إلى حواف الشاشة.
```bash
# تنفيذ أمر عندما تصل الفأرة إلى الحافة اليسرى
xdotool behave_screen_edge left exec "echo 'Left edge hit'"

# الحواف المتاحة: left, right, top, bottom
```

## أمثلة عملية

### نصوص الأتمتة الأساسية

#### فتح Terminal وتنفيذ أمر
```bash
#!/bin/bash
# فتح Terminal وتنفيذ أمر ls
xdotool key ctrl+alt+t
sleep 1
xdotool type "ls -la"
xdotool key Return
```

#### لقطة شاشة للنافذة النشطة
```bash
#!/bin/bash
WINDOW=$(xdotool getactivewindow)
NAME=$(xdotool getwindowname $WINDOW | sed 's/[^a-zA-Z0-9]/_/g')
import -window $WINDOW "screenshot_${NAME}.png"
```

#### التركيز على تطبيق محدد
```bash
#!/bin/bash
# التركيز على Firefox أو فتحه إذا لم يكن يعمل
WINDOW=$(xdotool search --onlyvisible --class "firefox" | head -1)
if [ -n "$WINDOW" ]; then
    xdotool windowactivate $WINDOW
else
    firefox &
fi
```

### نصوص إدارة النوافذ

#### ترتيب النوافذ جنبًا إلى جنب
```bash
#!/bin/bash
# الحصول على أبعاد الشاشة
eval $(xdotool getdisplaygeometry --shell)
HALF_WIDTH=$((WIDTH / 2))

# الحصول على أحدث نافذتين
WINDOWS=($(xdotool search --onlyvisible --maxdepth 1 "" | tail -2))

# وضع النافذة الأولى على اليسار
xdotool windowsize ${WINDOWS[0]} $HALF_WIDTH $HEIGHT
xdotool windowmove ${WINDOWS[0]} 0 0

# وضع النافذة الثانية على اليمين
xdotool windowsize ${WINDOWS[1]} $HALF_WIDTH $HEIGHT
xdotool windowmove ${WINDOWS[1]} $HALF_WIDTH 0
```

#### توسيط النافذة النشطة
```bash
#!/bin/bash
WINDOW=$(xdotool getactivewindow)
eval $(xdotool getdisplaygeometry --shell)
eval $(xdotool getwindowgeometry --shell $WINDOW)

NEW_X=$(((WIDTH - WINDOW_WIDTH) / 2))
NEW_Y=$(((HEIGHT - WINDOW_HEIGHT) / 2))

xdotool windowmove $WINDOW $NEW_X $NEW_Y
```

### أتمتة محددة للتطبيقات

#### أتمتة المتصفح
```bash
#!/bin/bash
# فتح علامة تبويب جديدة والتنقل
xdotool key ctrl+t
sleep 0.5
xdotool type "github.com"
xdotool key Return
```

#### أتمتة محرر النصوص
```bash
#!/bin/bash
# تحديد الكل ونسخ إلى الحافظة
xdotool key ctrl+a
sleep 0.1
xdotool key ctrl+c
```

## النصائح وأفضل الممارسات

### التوقيت والتأخيرات
```bash
# إضافة تأخيرات للتطبيقات البطيئة
xdotool key ctrl+alt+t
sleep 2  # الانتظار حتى يفتح Terminal
xdotool type "echo hello"

# استخدام التأخيرات المدمجة في xdotool
xdotool key --delay 100 ctrl+alt+t
```

### معالجة الأخطاء
```bash
#!/bin/bash
# التحقق من وجود النافذة قبل التصرف بناءً عليها
WINDOW=$(xdotool search --name "MyApp" 2>/dev/null)
if [ -n "$WINDOW" ]; then
    xdotool windowactivate $WINDOW
else
    echo "Window not found"
    exit 1
fi
```

### العمل مع نوافذ متعددة
```bash
#!/bin/bash
# التصرف على جميع نوافذ تطبيق محدد
xdotool search --name "Firefox" | while read WINDOW; do
    xdotool windowactivate $WINDOW
    xdotool key F5  # تحديث
    sleep 0.5
done
```

### التصحيح
```bash
# تمكين الإخراج المفصل
xdotool --verbose key Return

# الحصول على معلومات مفصلة عن النافذة
xdotool search --name "Terminal" getwindowgeometry getwindowname getwindowpid
```

## حالات الاستخدام الشائعة

1. **إدارة النوافذ**: التركيز، نقل، تغيير حجم النوافذ برمجيًا
2. **اختبار التطبيقات**: أتمتة سيناريوهات اختبار واجهة المستخدم الرسومية
3. **أدوات العروض التقديمية**: أتمتة التنقل بين الشرائح وتبديل النوافذ
4. **ماكروات الألعاب**: أتمتة مهام الألعاب المتكررة
5. **إمكانية الوصول**: إنشاء طرق إدخال مخصصة للمستخدمين ذوي الإعاقات
6. **إدارة النظام**: أتمتة مهام الإدارة القائمة على واجهة المستخدم الرسومية
7. **أدوات التطوير**: التكامل مع بيئات التطوير المتكاملة وسير عمل التطوير

## استكشاف الأخطاء وإصلاحها

### المشكلات الشائعة

- **الأوامر لا تعمل**: تأكد من أن X11 يعمل (وليس Wayland)
- **مشكلات الصلاحيات**: بعض العمليات قد تتطلب صلاحيات مستخدم مناسبة
- **النافذة غير موجودة**: استخدم `xdotool search` للتحقق من وجود النافذة وكونها مرئية
- **مشكلات التوقيت**: أضف تأخيرات مناسبة بين الأوامر
- **الأحرف الخاصة**: استخدم الهروب المناسب للأحرف الخاصة في إدخال النص

### الاعتبارات الأمنية

- xdotool يمكنه التحكم في أي تطبيق، استخدمه بحذر
- تجنب تشغيل نصوص xdotool غير الموثوقة
- كن حذرًا مع الأتمتة التي تتعامل مع البيانات الحساسة
- فكر في استخدام `xdotool` في بيئات خاضعة للرقابة فقط

يغطي هذا الدليل الميزات الأساسية والمتقدمة لـ xdotool. جرب هذه الأوامر لإنشاء نصوص أتمتة سطح مكتب قوية مصممة خصيصًا لاحتياجاتك المحددة.