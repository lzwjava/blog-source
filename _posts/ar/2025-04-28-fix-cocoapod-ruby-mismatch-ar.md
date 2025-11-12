---
audio: false
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: إصلاح عدم توافق كوكوا بود روبي على نظام ماك أو إس
translated: true
type: note
---

أرى ما يحدث: إعداد Ruby وGems في نظامك مختلط بعض الشيء، وبالتالي لا يمكن لأمر `pod deintegrate` العثور على CocoaPods. دعنا نتخطى الأمر خطوة بخطوة:

---

### المشكلة
- أنت تستخدم macOS (على الأرجح `arm64`، مثل M1/M2).
- قمت بتحديث Ruby (إلى الإصدار 3.4.1 عبر Homebrew).
- الملف التنفيذي `pod` الخاص بك تابع لإصدار Ruby الأقدم (المسار الخاص بحزمة 3.3.0: `/opt/homebrew/lib/ruby/gems/3.3.0/bin/pod`).
- لكن إصدار Ruby 3.4.1 هو النشط الآن، لذا لا يمكنه العثور على حزم `cocoapods` في المكان الصحيح.

هذا التباين هو سبب الفشل.

---

### الحلول

#### 1. إعادة تثبيت CocoaPods باستخدام إصدار Ruby الذي تستخدمه فعليًا
```bash
gem install cocoapods
```

ثم تحقق من العملية باستخدام:
```bash
which pod
pod --version
```

---

#### 2. إذا كنت تستخدم Ruby الخاص بـ `brew`، فمن الأفضل تثبيت CocoaPods عبر Homebrew أيضًا
```bash
brew install cocoapods
```

هذا يتجنب مشاكل التباين بين إصدارات Ruby تمامًا.

---

#### 3. إذا كنت تستخدم `rbenv` أو `rvm`، فتأكد من أنك في بيئة إصدار Ruby الصحيحة
على سبيل المثال، مع `rbenv`:
```bash
rbenv global 3.4.1
gem install cocoapods
```

---

#### 4. تنظيف روابط الملفات الثنائية القديمة لـ `pod`
تحقق من مصدر أمر `pod` المنعزل:
```bash
which pod
```
إذا كان يشير إلى `/opt/homebrew/lib/ruby/gems/3.3.0/bin/pod`، فقم بإزالته أو قم بتحديث `PATH` الخاص بك لاستخدام المسار الصحيح.

---

✅ موصى به (سهل ومستقر): ما عليك سوى تشغيل   
```bash
brew install cocoapods
```
ثم أعد المحاولة:
```bash
pod deintegrate
```

---

هل تريد مني مساعدتك في **إصلاح PATH بحيث يختار دائمًا الملف الثنائي `pod` الصحيح**، أم تفضل الحل السريع بإعادة التثبيت فحسب؟