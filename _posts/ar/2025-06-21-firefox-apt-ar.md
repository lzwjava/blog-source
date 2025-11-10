---
audio: false
generated: true
lang: ar
layout: post
title: تثبيت فايرفوكس عبر APT على أوبونتو
translated: true
type: note
---

يُفصّل هذا الدليل كيفية تثبيت Firefox من مستودع Mozilla APT على أوبونتو، ليحل محل حزمة Snap الافتراضية.

**لماذا استخدام إصدار APT؟**

بينما يُعد إصدار Snap مريحًا، يفضل بعض المستخدمين إصدار APT لتحسين التكامل والأداء.

**الخطوات:**

1.  **إزالة حزمة Firefox من Snap:**

    ```bash
    sudo snap remove firefox
    ```

2.  **إنشاء دليل keyring لـ APT (إذا لم يكن موجودًا):**

    ```bash
    sudo install -d -m 0755 /etc/apt/keyrings
    ```

3.  **استيراد مفتاح توقيع مستودع Mozilla APT:**

    ```bash
    wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | sudo tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null
    ```
    *إذا كان `wget` غير مثبت، قم بتثبيته أولاً: `sudo apt install wget`*

4.  **إضافة مستودع Mozilla إلى قائمة المصادر (sources list):**

    ```bash
    echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | sudo tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null
    ```

5.  **تعيين أولوية الحزمة لتُفضّل DEB من Mozilla:**

    هذا يمنع حزمة الانتقال (transition package) في أوبونتو من إعادة تثبيت Snap.

    ```bash
    echo '
    Package: *
    Pin: origin packages.mozilla.org
    Pin-Priority: 1000

    Package: firefox*
    Pin: release o=Ubuntu
    Pin-Priority: -1' | sudo tee /etc/apt/preferences.d/mozilla
    ```

6.  **إزالة حزمة Firefox DEB الخاصة بأوبونتو (إذا كانت موجودة) وتثبيت إصدار Mozilla:**

    ```bash
    sudo apt update && sudo apt remove firefox
    sudo apt install firefox
    ```

الآن لديك Firefox مثبتًا من مستودع Mozilla APT الرسمي!