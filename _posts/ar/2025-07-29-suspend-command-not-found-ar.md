---
audio: false
generated: true
image: false
lang: ar
layout: post
title: حل خطأ أمر التعليق
translated: true
type: note
---

يشير الخطأ `sudo: suspend: command not found` إلى أن أمر `suspend` غير متاح على نظامك أو غير مثبت. يُستخدم أمر `suspend` عادةً لوضع نظام Linux في حالة تعليق (إسبات)، ولكن قد لا يكون موجودًا افتراضيًا أو قد يكون له اسم مختلف اعتمادًا على توزيعتك.

إليك كيفية حل هذه المشكلة:

### 1. **استخدم الأمر الصحيح**
في العديد من توزيعات Linux، الأمر المستخدم لتعليق النظام ليس `suspend` بل أحد الأوامر التالية:

- **`systemctl suspend`**:
  هذا هو الأمر القياسي على الأنظمة التي تستخدم `systemd` (مثل Ubuntu، Debian، Fedora، إلخ).
  ```bash
  sudo systemctl suspend
  ```

- **`pm-suspend`**:
  إذا كان نظامك يستخدم حزمة `pm-utils`، يمكنك استخدام:
  ```bash
  sudo pm-suspend
  ```
  ملاحظة: قد تحتاج إلى تثبيت `pm-utils` إذا لم يكن مثبتًا مسبقًا:
  ```bash
  sudo apt-get install pm-utils  # لنظام Debian/Ubuntu
  sudo dnf install pm-utils      # لنظام Fedora
  ```

- **`echo mem > /sys/power/state`**:
  للوصول لمستوى منخفض، يمكنك الكتابة مباشرة في حالة طاقة النظام:
  ```bash
  echo mem | sudo tee /sys/power/state
  ```
  هذا يتطلب صلاحيات مدير نظام وقد لا يعمل على جميع الأنظمة اعتمادًا على تهيئة النواة.

### 2. **تحقق من توفر `systemd`**
بما أن `systemctl suspend` هو الطريقة الأكثر شيوعًا على توزيعات Linux الحديثة، تحقق مما إذا كان `systemd` يعمل:
```bash
pidof systemd
```
إذا أرجع هذا الأمر معرف عملية (PID)، فإن نظامك يستخدم `systemd`، ويجب أن يعمل `systemctl suspend`. إذا لم يكن الأمر كذلك، قد تحتاج إلى استخدام `pm-suspend` أو طريقة أخرى.

### 3. **ثبت الأدوات المفقودة**
إذا لم يكن `systemctl` أو `pm-suspend` متاحًا، قد تحتاج إلى تثبيت الحزمة المناسبة:
- لنظام Ubuntu/Debian:
  ```bash
  sudo apt-get update
  sudo apt-get install pm-utils
  ```
- لنظام Fedora:
  ```bash
  sudo dnf install pm-utils
  ```

### 4. **تحقق من الصلاحيات**
تأكد من أن لديك الصلاحيات الكافية. يشير الأمر `sudo` إلى أنك تحاول تشغيله كمسؤول، ولكن راجع مرة أخرى أن مستخدمك موجود في ملف `sudoers`:
```bash
sudo -l
```
إذا كنت تفتقر إلى الصلاحيات، قد تحتاج إلى الاتصال بمسؤول النظام.

### 5. **بديل: استخدم بيئة سطح المكتب**
إذا كنت تشغل بيئة سطح مكتب رسومية (مثل GNOME، KDE)، يمكنك تعليق النظام عبر واجهة المستخدم الرسومية (مثل النقر على قائمة الطاقة واختيار "تعليق"). بدلاً من ذلك، استخدم:
- لنظام GNOME:
  ```bash
  gnome-session-quit --power-off
  ```
- لنظام KDE:
  ```bash
  qdbus org.kde.ksmserver /KSMServer org.kde.KSMServerInterface.logout 0 1 0
  ```

### 6. **تحقق من دعم العتاد**
قد لا تدعم بعض الأنظمة التعليق بسبب مشاكل في العتاد أو النواة. تحقق مما إذا كان التعليق مدعومًا:
```bash
cat /sys/power/state
```
إذا كانت `mem` مدرجة في الناتج، فإن التعليق مدعوم. إذا لم تكن موجودة، قد تحتاج إلى استكشاف أخطاء إعدادات العتاد أو النواة وإصلاحها.

### 7. **إذا كنت تحتاج تحديدًا لأمر `suspend`**
إذا كنت تبحث عن أمر `suspend` محدد (مثل كونه جزءًا من سكريبت مخصص أو حزمة)، فقد لا يكون مثبتًا. ابحث عنه:
```bash
sudo apt-cache search suspend
```
أو تحقق مما إذا كان جزءًا من حزمة أخرى. إذا كنت تقصد سكريبت مخصص أو اسم مستعار، فتحقق من موقعه وتأكد من أنه قابل للتنفيذ:
```bash
which suspend
```

### مثال على سير العمل
لتعليق نظامك على إعدادات Ubuntu النموذجية:
```bash
sudo systemctl suspend
```
يجب أن يضع هذا النظام في حالة إسباط منخفضة الطاقة. عند الاستئناف، قد تحتاج إلى فتح قفل جلستك.

إذا كنت لا تزال تواجه مشاكل، فأعلمني بتوزيعة Linux التي تستخدمها وأي تفاصيل إضافية عن إعداداتك، وسأقدم لك نصائح أكثر تخصيصًا.

[Ubuntu Documentation on Power Management](https://help.ubuntu.com/stable/ubuntu-help/power-suspend.html)
[systemd suspend man page](https://www.freedesktop.org/software/systemd/man/systemctl.html)