---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: مشاكل تثبيت وتشغيل غوستي
translated: true
type: note
---

### تشخيص المشكلة

بناءً على السجلات التي شاركتها، فإن تثبيت Ghostty 1.1.3 عبر حزمة `.deb` قد نجح، لكن تشغيله يفشل لسببين رئيسيين:

1.  **خطأ في وسيطة سطر الأوامر (CLI)**: الأمر `ghostty .` يعامل النقطة `.` كحقل تكوين غير صالح (من المحتمل أنه كان المقصود استخدامها كدليل، لكن Ghostty لا يدعم هذا النحو). هذا يتسبب في الخروج الفوري مع رسالة "حقل غير صالح".

2.  **مشكلة توافق OpenGL/GTK**: عند تشغيل `ghostty` بدون وسيطات، يبدأ التطبيق في التهيئة ولكن يتعطل بسبب "إصدار OpenGL قديم جدًا. يتطلب Ghostty OpenGL 3.3" (نظامك يُبلغ Ghostty بالإصدار 3.2). هذه مشكلة معروفة على Ubuntu 22.04، خاصة مع برامج تشغيل NVIDIA تحت X11. على الرغم من أن `glxinfo` غالبًا ما يُظهر OpenGL 4.6+، فإن وقت تشغيل GTK 4.6 الخاص بـ Ghostty لا يمكنه الوصول بشكل صحيح إلى الإصدارات الأعلى مع NVIDIA GL. تحذير "GDK_DEBUG=vulkan-disable" هو محاولة لحل بديل لكنه لا يحل المشكلة الأساسية. خطأ Gtk-CRITICAL النهائي هو عرض من أعراض فشل تحقيق السطح.

هذا يؤثر على العديد من المستخدمين على Ubuntu 22.04 (والمشتقات مثل Pop!\_OS) بسبب إصدار GTK الأقدم (4.6 مقابل الإصدار الأحدث 4.12+ المطلوب لتوافق كامل مع NVIDIA).

### فحوصات سريعة
- تحقق من دعم OpenGL الفعلي على نظامك (قم بتثبيت `mesa-utils` إذا لزم الأمر: `sudo apt install mesa-utils`):
  ```
  glxinfo | grep "OpenGL version"
  ```
  إذا أظهرت النتيجة 3.3+، فإن المشكلة هي بالفعل خاصة بـ GTK/NVIDIA.
- تحقق من نوع جلسة العمل الخاصة بك: `echo $XDG_SESSION_TYPE`. إذا كانت `x11`، فمن المرجح أن هذا يساهم في المشكلة.

### الحلول
إليك الحلول خطوة بخطوة، بدءًا بالأبسط:

1.  **التبديل إلى Wayland (إذا كان لديك رسوميات هجينة، مثل Intel + NVIDIA)**:
    - سجل الخروج واختر جلسة Wayland عند تسجيل الدخول (أو أضف `WaylandEnable=true` إلى `/etc/gdm3/custom.conf` وأعد تشغيل GDM).
    - شغل Ghostty باستخدام الرسوميات المدمجة: `prime-run --gpu intel ghostty` (قم بتثبيت `nvidia-prime` إذا لزم الأمر).
    - يتخطى هذا حلولًا بديلة لمشاكل NVIDIA X11 لبعض المستخدمين.

2.  **التثبيت عبر Snap (حزمة بديلة أسهل)**:
    - حزمة `.deb` غير الرسمية التي استخدمتها يمكن أن ترث مشاكل النظام. جرب حزمة Snap الرسمية، والتي تضمّن التبعيات:
      ```
      sudo snap install ghostty --classic
      ```
    - شغل التطبيق باستخدام `snap run ghostty`. إذا استمر فشل OpenGL، فتابع إلى خيارات التحديث.

3.  **ترقية Ubuntu إلى الإصدار 24.04 (مُوصى به للحل طويل الأمد)**:
    - يتضمن Ubuntu 24.04 إصدار GTK 4.14+، مما يحل مشكلة التوافق مع NVIDIA.
    - اتبع دليل الترقية الرسمي: `sudo do-release-upgrade`.
    - بعد الترقية، أعد تثبيت Ghostty عبر نفس حزمة `.deb` أو Snap. أفاد المستخدمون بأنه يعمل بشكل لا تشوبه شائبة بعد الترقية.

4.  **البناء من المصدر باستخدام واجهة GLFW الخلفية (حل بديل مؤقت)**:
    - يستخدم هذا وقت تشغيل غير GTK لتجنب مشكلة OpenGL (ملاحظة: يفتقر إلى علامات التبويب، وهو مخصص للاختبار فقط).
      ```
      sudo apt install git zig libgtk-4-dev libadwaita-1-dev libharfbuzz-dev libpango1.0-dev libcairo2-dev libgdk-pixbuf-2.0-dev libglib2.0-dev libwayland-dev libxkbcommon-dev libinput-dev libudev-dev libseat-dev libpipewire-0.3-dev libsystemd-dev libx11-dev libxext-dev libxfixes-dev libxi-dev libxrandr-dev libxtst-dev libxdamage-dev libxcomposite-dev libxrender-dev libxcursor-dev libxinerama-dev libxss-dev libxv-dev libxxf86vm-dev libgl1-mesa-dev libegl1-mesa-dev libgles2-mesa-dev libgbm-dev libdrm-dev libvulkan-dev libclang-dev
      git clone https://github.com/ghostty-org/ghostty.git
      cd ghostty
      zig build -Doptimize=ReleaseFast -Dapp-runtime=glfw
      sudo cp zig-out/bin/ghostty /usr/local/bin/
      ```
    - شغل `ghostty`. للحصول على جميع الميزات، ارجع إلى استخدام GTK بمجرد الترقية.

### نصائح إضافية
- حدّث برامج تشغيل NVIDIA: `sudo ubuntu-drivers autoinstall` (أو استخدم السلسلة 550+ يدويًا).
- إذا كنت تستخدم AMD/Intel فقط، تأكد من تحديث Mesa: `sudo apt update && sudo apt upgrade mesa-vulkan-drivers`.
- لتحذير التكوين في ملف القالب الخاص بك (`~/.config/ghostty/config`)، قم بتحريره لإزالة أي أسطر غير صالحة (مثل النقطة `.` الضالة).

إذا لم ينجح أي من هذه الحلول، شارك ناتج أمر `glxinfo` أو تفاصيل بطاقة الرسوميات الخاصة بك (`lspci | grep VGA`) للحصول على نصائح أكثر تخصيصًا.

[مناقشة إصدار OpenGL قديم جدًا](https://github.com/ghostty-org/ghostty/discussions/3159)  
[إصدارات Ghostty لـ Ubuntu](https://github.com/mkasberg/ghostty-ubuntu)  
[Ghostty على Snap](https://snapcraft.io/ghostty)