---
audio: false
generated: true
lang: ar
layout: post
title: تجربة llama.cpp
translated: true
---

## llama.cpp

عند محاولة تشغيل `llama.cpp` مع نموذج، قد تواجه خطأً مثل هذا:

```bash
% ./main -m models/7B/Phi-3-mini-4k-instruct-q4.gguf
main: build = 964 (f3c3b4b)
main: seed  = 1737736417
llama.cpp: loading model from models/7B/Phi-3-mini-4k-instruct-q4.gguf
error loading model: unknown (magic, version) combination: 46554747, 00000003; is this really a GGML file?
llama_load_model_from_file: failed to load model
llama_init_from_gpt_params: error: failed to load model 'models/7B/Phi-3-mini-4k-instruct-q4.gguf'
main: error: unable to load model
```

يحدث هذا الخطأ لأنك تقوم بتشغيل برنامج `main`.  يجب أن يؤدي تشغيل برامج `llama-cli` أو `llama-server` الموجودة ضمن `build/bin` إلى حل المشكلة.

تم إنشاء برنامج `main` في ٨ أغسطس ٢٠٢٣، مما يعني أنه ليس الإصدار الحالي.

حل آخر هو تثبيت `llama.cpp` باستخدام Homebrew:

```bash
brew install llama.cpp
```

هذا يضمن أن لديك إصدارًا متوافقًا من المكتبة.

## LLM Farm

إنه تطبيق رائع لنظام iOS. في الإعدادات، يوجد حوالي ٢٠ نموذجًا. عند استيراد نموذج GGUF بأنفسنا، والذي يتم تنزيله من Hugging Face، فقد يؤدي ذلك إلى تعطل التطبيق.

## الفوائد

يسمح استضافة نماذج LLM هذه بنفسك بتشغيلها محليًا دون الحاجة إلى الوصول إلى الشبكة. على سبيل المثال، عند تنزيل ملفات كبيرة تُعيق الشبكة، قد يكون تشغيل نموذج محلي مفيدًا.

## الموارد

*   [نماذج Hugging Face GGML](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [مستودع GitHub لـ llama.cpp](https://github.com/ggerganov/llama.cpp)
*   [مستودع GitHub لـ ggml](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)
