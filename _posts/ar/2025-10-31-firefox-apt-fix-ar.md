---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إصلاح خطأ مستودع APT في فَيَرفُكس
translated: true
type: note
---

الخطأ الذي تراه خاص بمستودع حزم موزيلا فايرفوكس (`https://packages.mozilla.org/apt`)، حيث تفشل عملية جلب ملف الفهرس `binary-all/Packages` مع خطأ 400 طلب خاطئ. هذه مشكلة متقطعة معروفة تم الإبلاغ عنها من قبل مستخدمي أوبنتو/ديبيان الآخرين، وغالبًا ما تكون مرتبطة بإعدادات الوكيل (الوكيل المحلي الخاص بك على `127.0.0.1:7890` يشير إلى أن أداة مثل Clash أو V2Ray أو أداة مشابهة قيد التشغيل، والتي يمكنها تشويش طلبات HTTPS الخاصة بـ APT). الخبر السار هو أن APT يتجاهل الفشل ويستخدم فهارسًا مخزنة/قديمة، لذا لا يتم حظر تحديثات النظام—ولكنه قد يمنعك من الحصول على أحدث حزم فايرفوكس.

### إصلاحات سريعة لتجربها (بالترتيب)
1.  **مسح ذاكرة التخزين المؤقت لـ APT** (هذا يحل مشكلة ملفات الفهرس التالفة أو القديمة، وهو ما أصلح المشكلة لعدة مستخدمين):
    ```
    sudo apt clean
    sudo apt update
    ```

2.  **تجاوز الوكيل الخاص بك مؤقتًا لـ APT** (بما أن الخطأ 400 غالبًا ما ينبع من تدخل الوكيل مع HTTPS الخاص بالمستودع):
    ```
    unset http_proxy https_proxy all_proxy
    sudo -E apt update
    ```
    *   قم بتشغيل هذا في نفس جلسة الطرفية. إذا نجح، يمكنك جعله دائمًا بإضافة أسطر `unset` إلى ملف `~/.bashrc` الخاص بك (أو قبل أوامر APT مباشرة) أو عن طريق تعطيل تطبيق الوكيل لفترة وجيزة.
    *   إذا كان الوكيل مضبوطًا على مستوى النظام بأكمله (مثلًا، في `/etc/environment`)، قم بتعديل ذلك الملف لاستثناء APT أو تعليق تلك الأسطر مؤقتًا.

3.  **تعطيل الوكيل globally لـ APT** (إذا نجح الحل أعلاه ولكنك تريد خيارًا دائمًا):
    ```
    echo 'Acquire::http::Proxy "";
    Acquire::https::Proxy "";' | sudo tee /etc/apt/apt.conf.d/99no-proxy
    sudo apt update
    ```
    *   هذا يخبر APT بتجاهل الوكلاء تمامًا. يمكنك التراجع عن هذا بحذف الملف `/etc/apt/apt.conf.d/99no-proxy` إذا لزم الأمر.

### إذا كنت بحاجة إلى أحدث إصدار من فايرفوكس بدون المستودع
إذا استمر فشل المستودع وأردت فقط فايرفوكس محدث:
*   **التبديل إلى Snap** (الإعداد الافتراضي لأوبنتو، تحديثات سهلة، بدون متاعب المستودعات):
    ```
    sudo snap install firefox
    ```
*   **أو Flatpak** (إذا كنت تفضل):
    ```
    sudo apt install flatpak
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
    flatpak install flathub org.mozilla.firefox
    ```

### الوقاية/ملاحظات
*   مستودع موزيلا غير رسمي للحصول على أحدث حزم فايرفوكس—فكر في البقاء على الإصدار snap الخاص بأوبنتو ما لم تكن بحاجة تحديدًا إلى حزمة deb.
*   إذا لم ينجح أي من هذا، تحقق من سجلات الوكيل الخاص بك (مثل لوحة تحكم Clash) للبحث عن الطلبات المرفوضة إلى `packages.mozilla.org`، أو اختبر بدون الوكيل تمامًا.
*   قم بتشغيل `sudo apt update` مرة أخرى بعد الإصلاحات للتحقق.

إذا لم تحل هذه الحلول المشكلة، شارك المزيد من التفاصيل مثل إعداد الوكيل الخاص بك أو محتويات ملف `/etc/apt/sources.list.d/mozilla.list` الكاملة لاستكشاف الأخطاء وإصلاحها بشكل أعمق.

[Ubuntu 23.10 - Update Problems](https://askubuntu.com/questions/1507571/ubuntu-23-10-update-problems-some-index-files-failed-to-download)  
[Firefox apt repository error](https://www.reddit.com/r/firefox/comments/1ois308/firefox_apt_repository_error/)