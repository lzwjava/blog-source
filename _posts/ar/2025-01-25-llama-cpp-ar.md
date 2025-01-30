---
audio: false
lang: ar
layout: post
title: تجربة لاما دوت سي بي بي
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

يحدث هذا الخطأ لأنك تقوم بتشغيل برنامج `main`. يجب أن يحل تشغيل برامج `llama-cli` أو `llama-server` الموجودة في `build/bin` المشكلة.

تم إنشاء برنامج `main` في 8 أغسطس 2023، مما يعني أنه ليس الإصدار الحالي.

حل آخر هو تثبيت `llama.cpp` باستخدام Homebrew:

```bash
brew install llama.cpp
```

هذا يضمن أن لديك نسخة متوافقة من المكتبة.

## Ollama

```bash
% ollama list
NAME                   ID              SIZE      MODIFIED
deepseek-coder:6.7b    ce298d984115    3.8 GB    14 hours ago
mistral:7b             f974a74358d6    4.1 GB    15 hours ago
```

```bash
ollama remove model
```

إنها أداة رائعة للاستخدام. هناك بعض الأخطاء في Ollamac. على سبيل المثال، عندما يتلقى استجابة من واجهة برمجة التطبيقات المحلية، يتم تحديث عدة مربعات نصية في التطبيق.

## LLM Farm

إنه تطبيق iOS رائع. في الإعدادات، هناك حوالي 20 نموذجًا. عند استيراد نموذج GGUF بواسطتنا، والتي تم تنزيلها من Hugging Face، قد يؤدي إلى تعطل.

## الفوائد

يتيح استضافة هذه النماذج LLM بنفسك تشغيلها محليًا دون الحاجة إلى وصول إلى الشبكة. على سبيل المثال، عند تنزيل ملفات كبيرة تزدحم الشبكة، يمكن أن يكون تشغيل نموذج محلي مفيدًا.

## الموارد

*   [Hugging Face GGML Models](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [llama.cpp GitHub Repository](https://github.com/ggerganov/llama.cpp)
*   [ggml GitHub Repository](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)