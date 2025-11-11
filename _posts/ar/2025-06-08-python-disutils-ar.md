---
audio: false
generated: true
lang: ar
layout: post
title: إصلاح خطأ وحدة Python distutils غير موجودة
translated: true
type: note
---

يحدث هذا الخطأ لأن وحدة `distutils`، وهي جزء من المكتبة القياسية لـ Python، مفقودة في بيئتك. هذا شائع في تثبيتات Python الحد الأدنى. إليك كيفية إصلاحه:

### الحل:
1. **تثبيت أدوات تطوير Python** (تشمل `distutils`):
   ```bash
   sudo apt update && sudo apt install python3-distutils python3-dev
   ```

2. **إعادة تثبيت `setuptools`** (لضمان العملية السليمة):
   ```bash
   pip install --upgrade --force-reinstall setuptools
   ```

3. **إعادة محاولة تثبيت المتطلبات**:
   ```bash
   pip install -r requirements.local.txt
   ```

### سبب نجاح هذا الحل:
- `python3-distutils` توفر وحدة `distutils` المفقودة.
- `python3-dev` تشمل رؤوس/أدوات البناء الضرورية.
- إعادة تثبيت `setuptools` تحل أي مشاكل إعداد متبقية.

إذا كنت تستخدم بيئة افتراضية، أعد إنشائها بعد تثبيت الحزم النظامية لضمان وصول البيئة إلى الوحدات النمطية المطلوبة.