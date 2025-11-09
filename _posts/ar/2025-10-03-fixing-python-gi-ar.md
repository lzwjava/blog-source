---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast:free
title: إصلاح روابط بايثون GI المعطلة
translated: true
type: note
---

### التشخيص المحدث
استناداً إلى التفاصيل الجديدة، فإن تثبيت Python 3.13.7 الخاص بك (على الأرجح تم يدوياً أو عبر PPA/المصدر) قد تسبب في تلف ربط GObject Introspection (GI) في النظام. تم تجميع امتداد C `_gi` الخاص بالوحدة النمطية `gi` لإصدار Python الافتراضي في توزيعتك (على الأرجح 3.10 أو 3.11، نظراً للأدلة الموجودة في `/usr/lib/python`)، وليس الإصدار 3.13. هذا يسبب خطأ الاستيراد الدائري عندما تحاول النصية البرمجية `gnome-terminal` (وهي نصية Python) تحميله. يؤكد الإعداد متعدد الإصدارات في `/usr/lib/python` وجود هذا التباين—حزم النظام مثل `python3-gi` لم يتم بناؤها للإصدار 3.13 بعد (فهو جديد جداً على معظم التوزيعات اعتباراً من 2025).

سجلات UFW تبقى ضوضاء غير ذات صلة.

### الإصلاح الموصى به: العودة إلى Python الافتراضي للنظام
الحل الأكثر نظافة هو تبديل `/usr/bin/python3` مرة أخرى إلى الإصدار الافتراضي لتوزيعتك (مثلاً، 3.10)، ثم إعادة تثبيت ربط GI. هذا يتجنب الحلول غير السليمة مثل نسخ ملفات .so، والتي يمكن أن تسبب عدم اتساق.

1. **تحديد الإصدار الافتراضي لـ Python والتبديل إليه** (استخدم `update-alternatives` إذا كان مضبوطاً؛ وإلا، فاستخدم رابطاً رمزياً يدوياً):
   ```
   # تحقق مما إذا كانت بدائل update-alternatives مضبوطة
   sudo update-alternatives --config python3
   ```
   - إذا عرض خيارات، اختر الخيار ذا الأولوية الأدنى (عادة الإصدار الافتراضي للتوزيعة، مثل 3.10).
   - إذا لم تكن هناك بدائل (شائع في Ubuntu الأساسي)، ارجع يدوياً:
     ```
     # بافتراض أن الإصدار الافتراضي هو 3.10 (شائع في Ubuntu 22.04؛ استبدله بـ 3.11 إذا كان هذا هو إصدارك الأساسي)
     sudo rm /usr/bin/python3
     sudo ln -s /usr/bin/python3.10 /usr/bin/python3
     ```
   - تحقق: `python3 --version` يجب أن يعرض الآن 3.10.x (أو الإصدار الافتراضي الخاص بك).

2. **إعادة تثبيت حزم GI و GNOME Terminal**:
   ```
   sudo apt update
   sudo apt install --reinstall python3-gi gir1.2-glib-2.0 gnome-terminal
   ```

3. **اختبار**:
   ```
   python3 -c "from gi.repository import GLib, Gio; print('GI OK')"
   gnome-terminal
   ```
   - إذا نجح اختبار Python ولكن terminal لا يزال يفشل، أعِد ضبط إعداداته: `dconf reset -f /org/gnome/terminal/`.

### إذا كنت ترغب في الإبقاء على Python 3.13
- هذا أصعب، لأن الحزمة الرسمية `python3-gi` لن تكون موجودة للإصدار 3.13 بعد. ستحتاج إلى تجميع PyGObject من المصدر:
  1. قم بتثبيت تبعيات البناء: `sudo apt install libgirepository1.0-dev libcairo2-dev pkg-config python3.13-dev`.
  2. نزّل وقم ببناء PyGObject: اتبع [الدليل الرسمي](https://pygobject.gnome.org/install.html) مع `--prefix=/usr/local`.
  3. لكن هذا يُخاطر بتعطيل أدوات نظام أخرى—ارجع إذا ظهرت مشاكل.
- أو، بطريقة غير سليمة، انسخ امتداد `_gi` (غير موصى به على المدى الطويل):
  ```
  cd /usr/lib/python3/dist-packages/gi/
  sudo cp _gi.cpython-3[01]m*.so _gi.cpython-313m-x86_64-linux-gnu.so  # عدل '3[01]' ليناسب إصدارك الافتراضي (3.10 أو 3.11)
  ```
  ثم أعد تثبيت `python3-gi` كما ورد أعلاه.

### الوقاية
- لا تتجاوز `/usr/bin/python3` يدوياً—استخدم virtualenvs (`python3 -m venv myenv`) للمشاريع التي تحتاج الإصدار 3.13.
- إذا قمت بتثبيت الإصدار 3.13 عبر PPA خاص بـ deadsnakes، فقم بإزالته والتزم باستخدام Python الخاص بالتوزيعة.

إذا لم يُصلح هذا المشكلة، قم بتشغيل `ls -l /usr/bin/python*` و `dpkg -l | grep python3 | grep -E 'gi|default'` وشارك الناتج.

[gnome-terminal will not start after trying to install newer version of Python 3](https://askubuntu.com/questions/880188/gnome-terminal-will-not-start-after-trying-to-install-newer-version-of-python-3)  
[ImportError: cannot import name '_gi' from partially initialized module 'gi'](https://stackoverflow.com/questions/59838238/importerror-cannot-import-name-gi-from-partially-initialized-module-gi-mo)  
[Why won't terminal open?](https://www.reddit.com/r/Ubuntu/comments/1f9qh0a/why_wont_terminal_open/)