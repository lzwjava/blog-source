---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إصلاح مشاكل تحميل برامج تشغيل إنفيديا
translated: true
type: note
---

### فهم الخطأ
يشير هذا الخطأ إلى أن مشغل نواة NVIDIA (الجزء منخفض المستوى الذي يتفاعل مع بطاقة الرسوميات) غير محمّل أو غير متوافق مع إعداداتك الحالية. يختلف هذا عن عدم تطابق الإصدارات—هنا، الأداة `nvidia-smi` (أداة في مساحة المستخدم) لا تستطيع حتى الوصول إلى المشغل. تشمل المحفزات الشائعة:
- عدم تثبيت المشغل.
- تحديث النواة دون إعادة بناء وحدات المشغل.
- تعارضات مع مشغل Nouveau مفتوح المصدر.
- منع Secure Boot للوحدات غير الموقعة.
- تثبيت غير مكتمل.

هذا شائع على أنظمة Linux (مثل Ubuntu, Mint) بعد التحديثات. سنقوم باستكشاف الأخطاء وإصلاحها خطوة بخطوة. قم بتشغيل الأوامر كمستخدم عادي ما لم يُذكر استخدام `sudo`. افترض أن التوزيعة مشابهة لـ Ubuntu/Debian (قم بالتعديل لتوزيعات أخرى مثل Fedora باستخدام `dnf`).

### الخطوة 1: التشخيص الأساسي
قم بتشغيل هذه الأوامر لتحديد المشكلة بدقة:

```
# التحقق مما إذا كانت وحدات نواة NVIDIA محملة
lsmod | grep nvidia

# التحقق من إصدار المشغل (إذا كان محملاً)
cat /proc/driver/nvidia/version

# البحث عن أخطاء في سجلات النواة
dmesg | grep -i nvidia
```

- **إذا لم يُظهر `lsmod` أي إخراج**: المشغل غير محمّل—تابع إلى التثبيت/إعادة البناء.
- **إذا ذكر `dmesg` "Nouveau" أو "failed to load"**: تعارض مع Nouveau—انتقل إلى الخطوة 3.
- **إذا أظهر الإصدار ولكن هناك عدم تطابق**: أعد التشغيل أولاً (`sudo reboot`)، ثم أعد تجربة `nvidia-smi`.

شارك المخرجات إذا كنت بحاجة إلى نصيحة أكثر تخصيصًا.

### الخطوة 2: إصلاحات سريعة (جرب هذه أولاً)
1. **إعادة التشغيل**: بسيط لكنه فعال بعد تغييرات النواة/المشغل.
   ```
   sudo reboot
   ```
   ثم: `nvidia-smi`.

2. **إعادة تحميل الوحدات** (إذا كانت محملة جزئيًا):
   ```
   sudo modprobe nvidia
   nvidia-smi  # اختبر
   ```
   إذا فشل مع رسالة "module not found"، قم بتثبيت المشغل (الخطوة 4).

3. **التحقق من عدم تطابق النواة**: إذا قمت مؤخرًا بتحديث نواتك، قم بالتمهيد باستخدام النواة السابقة عبر GRUB (اضغط على Shift أثناء التمهيد، واختر النواة الأقدم). أعد تثبيت المشغل بعد ذلك.

### الخطوة 3: تعطيل Nouveau (إذا كان هناك تعارض)
عادةً ما يقوم مشغل Nouveau (المشغل مفتوح المصدر الافتراضي) بحجب المشغل الاحتكاري من NVIDIA. قم بإدراجه في القائمة السوداء بشكل دائم:

1. إنشاء ملف القائمة السوداء:
   ```
   echo 'blacklist nouveau' | sudo tee /etc/modprobe.d/blacklist-nouveau.conf
   echo 'options nouveau modeset=0' | sudo tee -a /etc/modprobe.d/blacklist-nouveau.conf
   ```

2. تحديث initramfs:
   ```
   sudo update-initramfs -u
   ```

3. إعادة التشغيل:
   ```
   sudo reboot
   ```

### الخطوة 4: تثبيت/إعادة تثبيت أحدث مشغل NVIDIA
اعتبارًا من أكتوبر 2025، أحدث إصدار مستقر لمشغل Linux هو الإصدار 580.95 (موصى به لمعظم بطاقات الرسوميات؛ تحقق من [موقع NVIDIA](https://www.nvidia.com/Download/index.aspx) لطراز بطاقتك). استخدم أدوات Ubuntu لسهولة تكامل DKMS (يعيد البناء تلقائيًا عند تحديثات النواة).

#### بالنسبة لـ Ubuntu 22.04+ / Debian:
1. **إضافة PPA لمشغلي الرسوميات** (للحصول على أحدث الإصدارات):
   ```
   sudo add-apt-repository ppa:graphics-drivers/ppa
   sudo apt update
   ```

2. **الكشف التلقائي والتثبيت**:
   ```
   sudo ubuntu-drivers autoinstall  # يثبت الإصدار الموصى به (على الأرجح 580.x)
   ```
   أو حدد يدويًا: `sudo apt install nvidia-driver-580` (يتضمن DKMS للاستقرار).

3. **إذا كان Secure Boot مفعلًا** (تحقق من الـ BIOS):
   - عطله مؤقتًا (أسهل)، أو سجل مفتاح NVIDIA's MOK أثناء التثبيت (سيطلب منك ذلك عند إعادة التشغيل).

4. **إعادة التشغيل والتحقق**:
   ```
   sudo reboot
   nvidia-smi  # يجب أن تظهر جدول بطاقة الرسوميات
   ```

#### بديل: التثبيت اليدوي (إذا فشل PPA)
1. قم بتنزيل ملف التشغيل من [NVIDIA](https://www.nvidia.com/Download/driverResults.aspx/227xxx/en-us/?driverType=linux) (اختر Linux 64-bit, 580.95).
2. أوقف مدير العرض: `sudo systemctl stop gdm` (أو lightdm/sddm)، ثم `sudo telinit 3`.
3. قم بالتثبيت: `sudo bash NVIDIA-Linux-x86_64-580.95.xx.run` (اقبل المطالبات).
4. أعد التشغيل.

#### لتوزيعات أخرى:
- **Fedora/RHEL**: `sudo dnf install akmod-nvidia` (يستخدم 580.x).
- **Arch**: `sudo pacman -S nvidia nvidia-dkms`.

### الخطوة 5: فحوصات ما بعد التثبيت
- **إعداد CUDA** (لـ nanoGPT/التعلم الآلي): بعد تثبيت المشغل، قم بتثبيت أدوات CUDA: `sudo apt install nvidia-cuda-toolkit`.
- **اختبار**: شغل `nvidia-smi`—توقع ظهور جدول يوضح استخدام بطاقة الرسوميات، الذاكرة، إلخ.
- **إذا ما زال فاشلًا**:
  - احذف كل شيء: `sudo apt purge 'nvidia*'; sudo apt autoremove; reboot; reinstall`.
  - تحقق من السجلات: `journalctl -b -u gdm | grep nvidia` (لمشاكل العرض).

هذا يجب أن يجعلك تعمل. إذا كنت تستخدم توزيعة/بطاقة رسوميات محددة أو ترى أخطاء في التشخيص، قم بالرد بالتفاصيل!

### المراجع
- [منتديات مطوري NVIDIA: إصلاحات شائعة](https://forums.developer.nvidia.com/t/nvidia-smi-has-failed-because-it-couldnt-communicate-with-the-nvidia-driver-make-sure-that-the-latest-nvidia-driver-is-installed-and-running/197141)
- [AskUbuntu: تبديل المشغل](https://askubuntu.com/questions/927199/nvidia-smi-has-failed-because-it-couldnt-communicate-with-the-nvidia-driver-ma)
- [GamingOnLinux: إصدار أحدث مشغل](https://www.gamingonlinux.com/2025/09/nvidia-driver-580-95-05-released-as-the-latest-recommended-for-linux/)