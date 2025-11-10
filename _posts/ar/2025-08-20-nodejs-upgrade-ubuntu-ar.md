---
audio: false
generated: true
image: false
lang: ar
layout: post
title: دليل ترقية Node.js على أوبونتو
translated: true
type: note
---

يمكن ترقية Node.js على أوبونتو بعدة طرق. أكثر الطرق موثوقية وموصى بها هي استخدام **`nvm` (مدير إصدارات Node)** أو **مستودع NodeSource**. فيما يلي تعليمات خطوة بخطوة لكلتا الطريقتين.

---

## **الطريقة 1: استخدام NVM (موصى بها)**
يتيح لك NVM تثبيت وإدارة إصدارات متعددة من Node.js بسهولة.

### 1. تثبيت NVM
افتح الطرفية وشغِّل:
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```
ثم، أعد تحميل shell الخاص بك:
```bash
source ~/.bashrc
```
أو
```bash
source ~/.zshrc
```
(اعتمادًا على shell الذي تستخدمه)

### 2. تثبيت أحدث إصدار من Node.js
اعرض الإصدارات المتاحة:
```bash
nvm ls-remote
```
ثبِّت أحدث إصدار LTS (موصى به لمعظم المستخدمين):
```bash
nvm install --lts
```
أو ثبِّت إصدارًا محددًا (مثل 20.x):
```bash
nvm install 20
```

### 3. تعيين الإصدار الافتراضي
```bash
nvm alias default 20
```

### 4. التحقق
```bash
node -v
npm -v
```

---

## **الطريقة 2: استخدام مستودع NodeSource**
تثبت هذه الطريقة Node.js على مستوى النظام بالكامل.

### 1. إزالة Node.js القديم (إذا كان مثبتًا عبر apt)
```bash
sudo apt remove --purge nodejs npm
sudo apt autoremove
```

### 2. إضافة مستودع NodeSource
لـ **Node.js 20.x** (LPS اعتبارًا من أغسطس 2025):
```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
```
لـ **Node.js 22.x** (إذا كان متاحًا):
```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
```

### 3. تثبيت Node.js
```bash
sudo apt install -y nodejs
```

### 4. التحقق
```bash
node -v
npm -v
```

---

## **الطريقة 3: استخدام المستودع الافتراضي لأوبونتو (غير موصى بها)**
يحتوي المستودع الافتراضي لأوبونتو غالبًا على إصدارات قديمة من Node.js. إذا كنت لا تزال ترغب في استخدامه:
```bash
sudo apt update
sudo apt install nodejs npm
```
لكن هذا **غير موصى به** للتطوير، حيث أن الإصدار عادة ما يكون قديمًا.

---

## **أي طريقة يجب أن تستخدم؟**
- **استخدم NVM** إذا كنت تريد التبديل بين إصدارات Node.js بسهولة أو إذا كنت بحاجة إلى أحدث الميزات.
- **استخدم NodeSource** إذا كنت تريد تثبيتًا مستقرًا على مستوى النظام بالكامل.