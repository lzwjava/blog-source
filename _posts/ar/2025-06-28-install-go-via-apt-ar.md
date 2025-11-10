---
audio: false
generated: true
lang: ar
layout: post
title: تثبيت لغة Go عبر APT على دبيان
translated: true
type: note
---

لتثبيت Go باستخدام `apt` على نظام Linux مبني على Debian (مثل Ubuntu)، اتبع الخطوات التالية. لاحظ أن `apt` قد يثبت إصدارًا قديمًا من Go (مثل 1.18 على Ubuntu 22.04)، لذا يجب عليك التحقق مما إذا كان يلبي متطلبات مشروعك (تحقق من ملف `go.mod` في `~/Projects/clash-core` لمعرفة إصدار Go المطلوب).

### خطوات تثبيت Go باستخدام APT

1.  **تحديث فهرس الحزم**
    - تأكد من أن قوائم الحزم لديك محدثة:
      ```bash
      sudo apt update
      ```

2.  **تثبيت Go**
    - قم بتثبيت حزمة Go:
      ```bash
      sudo apt install golang-go
      ```
    - يقوم هذا بتثبيت مترجم Go والأدوات والمكتبة القياسية.

3.  **التحقق من التثبيت**
    - تحقق من إصدار Go المثبت:
      ```bash
      go version
      ```
    - يجب أن ترى ناتجًا مشابهًا لما يلي:
      ```
      go version go1.18.1 linux/amd64
      ```
      (يعتمد الإصدار على مستودع الحزم الخاص بتوزيعتك.)

4.  **إعداد GOPATH (اختياري)**
    - تستخدم الإصدارات الحديثة من Go (1.13+) الوحدات النمطية، لذا فإن `GOPATH` أصبح اختياريًا، ولكن إعداده يمكن أن يكون مفيدًا لبعض المشاريع.
    - قم بتحرير ملف التهيئة الخاص بالطرفية (Shell) الخاص بك (مثل `~/.bashrc` أو `~/.zshrc`):
      ```bash
      nano ~/.bashrc
      ```
    - أضف الأسطر التالية:
      ```bash
      export GOPATH=$HOME/go
      export PATH=$PATH:$GOPATH/bin
      ```
    - احفظ الملف وقم بإعادة تحميل إعدادات الطرفية:
      ```bash
      source ~/.bashrc
      ```

5.  **إعادة محاولة البناء**
    - انتقل إلى دليل مشروعك:
      ```bash
      cd ~/Projects/clash-core
      ```
    - شغل أمر `make` مرة أخرى:
      ```bash
      make
      ```

### ملاحظات
-   **التحقق من الإصدار**: إذا كان مشروعك يتطلب إصدارًا أحدث من Go (مثل 1.20 أو أحدث)، فقد يكون إصدار `apt` قديمًا. تحقق من الإصدار المطلوب في ملف `go.mod` أو وثائق المشروع. إذا لزم الأمر، قم بتثبيت إصدار أحدث يدويًا عن طريق تنزيل الأرشيف من [https://go.dev/dl/](https://go.dev/dl/) (كما هو موضح في الرد السابق).
-   **المستودعات البديلة**: للحصول على إصدار أحدث عبر `apt`، يمكنك إضافة مستودع تابع لطرف ثالث (مثل `ppa:longsleep/golang-backports` على Ubuntu). شغل:
    ```bash
    sudo add-apt-repository ppa:longsleep/golang-backports
    sudo apt update
    sudo apt install golang-go
    ```
-   **استكشاف الأخطاء وإصلاحها**:
    - إذا لم يتم العثور على `go`، تأكد من وجود `/usr/bin/go` (`ls /usr/bin/go`). إذا لم يكن موجودًا، أعد التثبيت باستخدام `sudo apt install --reinstall golang-go`.
    - إذا ظهرت أخطاء متعلقة بالتبعيات، شغل `sudo apt install -f` لإصلاحها.
    - لمشاكل الصلاحيات، تأكد من أن لديك صلاحيات `sudo`.

### المصادر
-   دليل تثبيت Go على Ubuntu: [https://ubuntu.com/server/docs/programming-go](https://ubuntu.com/server/docs/programming-go)
-   الاستخدام العام لـ apt: [https://help.ubuntu.com/community/AptGet/Howto](https://help.ubuntu.com/community/AptGet/Howto)

إذا كان الإصدار المثبت قديمًا جدًا أو واجهت مشاكل، أعلمني بتوزيعة Linux الخاصة بك (مثل Ubuntu 22.04) وإصدار Go المطلوب، وسأرشدك أكثر!