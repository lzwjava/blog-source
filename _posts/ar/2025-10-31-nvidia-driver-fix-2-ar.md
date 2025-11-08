---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: حل تعارض حزمة برامج تشغيل إنفيديا
translated: true
type: note
---

يبدو هذا كصراع كلاسيكي بين الحزم أثناء تحديث مشغل NVIDIA على أوبنتو (على الأرجح الإصدار 22.04 بناءً على إصدارات الحزم). تحاول حزمة `nvidia-kernel-common-535` استبدال ملف firmware (`gsp_ga10x.bin`) مملوك بالفعل من قبل `nvidia-firmware-535`، مما يتسبب في توقف dpkg. هذه مشكلة معروفة في مشغلات NVIDIA من السلسلة 535 من مستودعات أوبنتو.

لا داعي للذعر—يجب أن يظل نظامك قابلاً للإقلاع (على الرغم من أن الرسومات قد تعمل في وضع البرامج الوسيطة "software rendering" إذا كان المشغل تالفًا جزئيًا). إليك الحل خطوة بخطوة لحله بأمان. شغّل هذه الأوامر في الطرفية (استخدم TTY إذا كانت واجهة المستخدم غير مستقرة: Ctrl+Alt+F3 للتبديل).

### محاولة الإصلاح السريع (الأكثر أمانًا أولاً)
1. حاول إصلاح الحزم التالفة تلقائيًا:
   ```
   sudo apt --fix-broken install
   ```
   هذا غالبًا ما يحل مشاكل الاعتمادات/فك الحزم دون تدخل يدوي.

2. إذا فشل ذلك (أو نجح جزئيًا ولكن ترك أخطاء)، نظف التثبيت المتقطع:
   ```
   sudo dpkg --configure -a
   sudo apt update
   sudo apt upgrade
   ```

### إذا ما زلت عالقًا: فرض استبدال الملف المتعارض
الخطأ محدد في ملف حزمة `nvidia-kernel-common-535` deb. اجبر dpkg على استبدال الملف المكرر:
```
sudo dpkg -i --force-overwrite /var/cache/apt/archives/nvidia-kernel-common-535_535.274.02-0ubuntu1_amd64.deb
```
- هذا يثبت تلك الحزمة فقط، متجاهلاً تعارض الملفات.
- ثم شغّل:
  ```
  sudo apt --fix-broken install
  sudo apt autoremove
  sudo apt upgrade
  ```
- أعد التشغيل بعد ذلك: `sudo reboot`.

### الخيار الجذري: إزالة وإعادة تثبيت حزم NVIDIA
إذا لم تنجح الخطوات السابقة (على سبيل المثال، بسبب عدم تطابق أعمق في الإصدارات)، أزل أجزاء NVIDIA المتعارضة وأعد تثبيتها:
1. أزل الحزم المسببة للمشكلة (عدّل الإصدارات إذا لزم الأمر—تحقق منها باستخدام `dpkg -l | grep nvidia`):
   ```
   sudo dpkg --force-all -P nvidia-firmware-535-535.274.02 nvidia-kernel-common-535
   ```
2. نظف النظام:
   ```
   sudo apt autoremove --purge
   sudo apt autoclean
   ```
3. أعد تثبيت المشغل:
   ```
   sudo apt update
   sudo apt install nvidia-driver-535
   ```
4. أعد التشغيل.

### الوقاية/نصائح
- أضف PPA الخاص بـ graphics-drivers للحصول على تحديثات NVIDIA أكثر استقرارًا: `sudo add-apt-repository ppa:graphics-drivers/ppa && sudo apt update`.
- إذا كنت تستخدم حاسوبًا محمولًا، تأكد من تعطيل Secure Boot في BIOS قبل تثبيت المشغلات.
- اختبر بعد إعادة التشغيل باستخدام `nvidia-smi` (يجب أن يعرض بطاقتك الرسومية) أو `prime-select query` (إذا كان النظام يستخدم NVIDIA Optimus).
- إذا تسبب هذا في تعطيل شاشتك تمامًا، أقلع في وضع الاسترداد "recovery mode" وشغّل الإصلاحات من هناك.

إذا لم ينجح أي من هذا أو ظهر خطأ جديد، الصق الناتج الكامل هنا لمزيد من الحلول.

### المراجع
- [Unmet dependencies nvidia-dkms-535 - package conflict breaks Ubuntu 22.04 install](https://forums.developer.nvidia.com/t/unmet-dependencies-nvidia-dkms-535-package-conflict-breaks-ubuntu-22-04-install/265788)
- [Ubuntu and NVIDIA-provided packages conflict, breaking installation](https://forums.developer.nvidia.com/t/ubuntu-and-nvidia-provided-packages-conflict-breaking-installation/259150)
- [Problem with nvidia package dependencies](https://askubuntu.com/questions/1491916/problem-with-nvidia-package-dependencies)
- [nvidia-kernel-common-535 conflicts with nvidia-firmware-535](https://superuser.com/questions/1833427/nvidia-kernel-common-535-conflicts-with-nvidia-firmware-535-535-161-07-535-161-0)