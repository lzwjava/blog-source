---
audio: false
generated: true
image: false
lang: ar
layout: post
title: ترقية أولاما باستخدام هومبرو
translated: true
type: note
---

لترقية Ollama إلى أحدث إصدار (حاليًا v0.10.0 اعتبارًا من يوليو 2025) باستخدام Homebrew على نظام macOS، اتبع هذه الخطوات:

1. قم بتحديث صيغ Homebrew لضمان معرفتها بأحدث الإصدارات المتاحة:
   ```
   brew update
   ```

2. قم بترقية Ollama على وجه التحديد:
   ```
   brew upgrade ollama
   ```

3. تحقق من الترقية عن طريق التحقق من الإصدار:
   ```
   ollama --version
   ```

إذا كنت تشغل Ollama كخدمة في الخلفية، أعد تشغيلها بعد الترقية:
```
brew services restart ollama
```

بدلاً من ذلك، إذا كنت تشغلها يدويًا، أوقف أي عملية قائمة وابدأها مرة أخرى باستخدام الأمر الذي تفضله (على سبيل المثال، من الملاحظات في ناتج التثبيت الخاص بك):
```
OLLAMA_FLASH_ATTENTION="1" OLLAMA_KV_CACHE_TYPE="q8_0" /opt/homebrew/opt/ollama/bin/ollama serve
```

لا توجد حاجة لتعليمات ترقية خاصة تتجاوز هذه العملية القياسية.

[إصدارات Ollama](https://github.com/ollama/ollama/releases)