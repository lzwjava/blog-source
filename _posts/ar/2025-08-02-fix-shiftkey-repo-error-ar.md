---
audio: false
generated: true
image: false
lang: ar
layout: post
title: إصلاح خطأ توقيع APT GPG
translated: true
type: note
---

الخطأ الذي تراه يعني أن APT يرفض التحديث من مستودع ShiftKey لأنه لا يمكنه التحقق من توقيع GPG الخاص به. لديك طريقتان بسيطتان لإصلاح هذا:

---

## 1. **إزالة أو تعطيل المستودع المعطّل**

إذا كنت لا تحتاج فعليًا إلى `https://apt.packages.shiftkey.dev/ubuntu`، فعطّله فقط:

```bash
# ابحث عن الملف الذي يعرّف ذلك المستودع (سيكون موجودًا في /etc/apt/sources.list.d/)
ls /etc/apt/sources.list.d/shiftkey*

# أزله (استبدل باسم الملف الفعلي)
sudo rm /etc/apt/sources.list.d/shiftkey.packages.shiftkey.dev.list

# ثم قم بالتحديث والتثبيت
sudo apt update
sudo apt install pkg-config libssl-dev
```

---

## 2. **استيراد مفتاح التوقيع الخاص بالمستودع**

إذا كنت تريد الاستمرار في استخدام حزم ShiftKey، فأنت بحاجة إلى جلب وتثبيت مفتاحها العام:

```bash
# حمّل وفك تشفير مفتاح GPG الخاص بهم إلى سجل مفاتيح APT
curl -fsSL https://apt.packages.shiftkey.dev/ubuntu/pubkey.gpg \
  | gpg --dearmor \
  | sudo tee /usr/share/keyrings/shiftkey-archive-keyring.gpg > /dev/null

# حرّر ملف المستودع ليشار إلى سجل المفاتيح هذا.
# افتح /etc/apt/sources.list.d/shiftkey*.list في محررك، وغير سطر deb إلى:
#   deb [signed-by=/usr/share/keyrings/shiftkey-archive-keyring.gpg] https://apt.packages.shiftkey.dev/ubuntu any main

# ثم قم بالتحديث والتثبيت
sudo apt update
sudo apt install pkg-config libssl-dev
```

---

بمجرد أن يتمكن APT من التحديث دون أخطاء GPG، ستكون حرًا في تثبيت `pkg-config` و `libssl-dev`، ثم إعادة البناء:

```bash
cargo clean
cargo run
```