---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تثبيت كروميوم على أوبونتو ٢٤.٠٤
translated: true
type: note
---

لتثبيت **Chromium** على **Ubuntu 24.04**، لديك عدة خيارات جيدة — اعتمادًا على ما إذا كنت تريد **الإصدار الرسمي عبر Snap**، أو إصدار **APT (حزمة Debian)**، أو **التنزيل اليدوي**. إليك دليل واضح لكل منها:

---

### 🧩 الخيار 1: التثبيت عبر Snap (الطريقة الرسمية لأوبونتو)

هذه هي الطريقة **الافتراضية** والأكثر استقرارًا.

```bash
sudo snap install chromium
```

ثم شغله باستخدام:

```bash
chromium
```

✅ *المزايا:*

* تُدار بشكل رسمي من قبل Canonical.
* يتم التحديث تلقائيًا.

⚠️ *العيوب:*

* وقت البدء قد يكون أبطأ.
* الحماية Sandbox الخاصة بـ Snap قد تسبب مشاكل في الوصول إلى وكيل النظام System Proxy أو الملفات.

---

### ⚙️ الخيار 2: التثبيت عبر APT (حزمة Debian، بدون Snap)

إذا كنت **لا تفضل Snap**، يمكنك تثبيت Chromium من **مستودع تابع لطرف ثالث** مثل إصدار Debian الرسمي المقدم من **ungoogled-chromium** أو **OBS**.

1.  أضف مستودع OBS:

    ```bash
    sudo apt install wget gnupg
    wget -qO - https://download.opensuse.org/repositories/home:/ungoogled_chromium/Ubuntu_24.04/Release.key | sudo gpg --dearmor -o /usr/share/keyrings/ungoogled-chromium.gpg
    ```

2.  أضف المستودع:

    ```bash
    echo "deb [signed-by=/usr/share/keyrings/ungoogled-chromium.gpg] https://download.opensuse.org/repositories/home:/ungoogled_chromium/Ubuntu_24.04/ /" | sudo tee /etc/apt/sources.list.d/ungoogled-chromium.list
    ```

3.  قم بتثبيت Chromium:

    ```bash
    sudo apt update
    sudo apt install ungoogled-chromium
    ```

ثم شغله باستخدام:

```bash
ungoogled-chromium
```

✅ *المزايا:*

* لا توجد تبعية لـ Snap.
* إصدار معزز الخصوصية متاح.

⚠️ *العيوب:*

* التحديثات تأتي بشكل أبطأ من Snap.
* بعض الميزات (مثل Google Sync) معطلة.

---

### 🧰 الخيار 3: التثبيت من الإصدار الرسمي لـ Chromium (يدويًا)

إذا كنت تريد **أحدث إصدار للمطورين**:

```bash
sudo apt install chromium-browser
```

إذا تم تحويلك إلى Snap وأردت تجنب ذلك:

```bash
sudo apt purge chromium-browser
sudo apt install chromium
```

أو، حمل ملف `.deb` يدويًا:

```bash
wget https://commondatastorage.googleapis.com/chromium-browser-snapshots/Linux_x64/LAST_CHANGE -O /tmp/LAST_CHANGE
LATEST=$(cat /tmp/LAST_CHANGE)
wget "https://commondatastorage.googleapis.com/chromium-browser-snapshots/Linux_x64/${LATEST}/chrome-linux.zip"
unzip chrome-linux.zip
./chrome-linux/chrome
```

---

### 🌍 ملاحظة حول إعدادات الوكيل Proxy

بما أن نظامك يستخدم:

```
HTTP_PROXY=http://127.0.0.1:7890
HTTPS_PROXY=http://127.0.0.1:7890
```

تأكد من أن Snap وAPT يحترمان إعدادات الوكيل الخاص بك عن طريق تصدير هذه المتغيرات في `/etc/environment` أو ملف تعريف shell الخاص بك:

```bash
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
```

---

هل تريد مني أن أوضح كيفية جعل Chromium يستخدم ذلك الوكيل تلقائيًا (حتى يتم الاتصال دائمًا من خلاله)؟