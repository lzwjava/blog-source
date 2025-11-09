---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تثبيت كروميوم على نظام ماك أو إس
translated: true
type: note
---

نعم، يمكن لنظام macOS تثبيت Chromium كبديل لمتصفح Google Chrome. Chromium هو الأساس مفتوح المصدر الذي تم بناء Chrome عليه، لذا فهو مشابه جدًا من حيث الوظائف ولكنه يفتقر إلى بعض ميزات Google الاحتكارية مثل التحديثات التلقائية وبعض برامج الترميز.

### كيفية تثبيته
هناك عدة طرق مباشرة:

1. **عبر Homebrew (الأسهل لمعظم المستخدمين)**:
   - قم بتثبيت Homebrew إذا لم يكن لديك بالفعل: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`.
   - ثم شغّل: `brew install --cask chromium`.
   - تعمل هذه الطريقة على أجهزة Mac ذات معالجات Intel و Apple Silicon (M1/M2/M3).

2. **التنزيل المباشر**:
   - انتقل إلى موقع Chromium الرسمي وقم بتنزيل أحدث إصدار لـ Mac.
   - قم بفك الضغط عن الملف واسحب التطبيق إلى مجلد التطبيقات Applications.

3. **للمطورين أو الإصدارات المخصصة**:
   - استخدم أدوات مثل Woolyss للحصول على إصدارات مجمعة مسبقًا، أو قم بالبناء من المصدر إذا لزم الأمر (يتطلب Xcode).

بمجرد التثبيت، يمكنك تعيين Chromium كمتصفحك الافتراضي من خلال System Settings > Desktop & Dock > Default web browser.

[تنزيل Chromium](https://www.chromium.org/getting-involved/download-chromium/)  
[صيغة Homebrew](https://formulae.brew.sh/cask/chromium)  
[التثبيت على أجهزة Apple Silicon](https://dev.to/pixelrena/installing-chromium-on-mac-apple-m2-pro-tutorial-4i4i)  
[تنزيل من MacUpdate](https://chromium.macupdate.com/)  
[أحدث الإصدارات](https://chromium.woolyss.com/download/en/)