---
audio: true
lang: ar
layout: post
title: تجربة llama.cpp
translated: true
---

## llama.cpp

عند محاولة تشغيل `llama.cpp` مع نموذج، قد تواجه خطأ مثل هذا:

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

هذا الخطأ يشير عادة إلى مشكلة في تثبيت `llama.cpp` أو في ملف النموذج نفسه.

حل شائع هو تثبيت `llama.cpp` باستخدام Homebrew:

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

إنها أداة رائعة للاستخدام. هناك بعض الأخطاء في Ollamac. على سبيل المثال، عندما تتلقى ردًا من API المحلي، يتم تحديث عدة مربعات نصية في التطبيق.

## LLM Farm

إنه تطبيق iOS رائع. في الإعدادات، هناك حوالي 20 نموذجًا. عند استيراد نموذج GGUF بأنفسنا، والتي يتم تنزيلها من Hugging Face، قد يؤدي ذلك إلى تعطل التطبيق.

## الفوائد

تشغيل نماذج LLM هذه محليًا يسمح لك بتشغيلها دون الحاجة إلى الوصول إلى الشبكة. على سبيل المثال، عند تنزيل ملفات كبيرة تعيق الشبكة، يمكن أن يكون تشغيل نموذج محلي مفيدًا.

## الموارد

*   [نماذج Hugging Face GGML](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [مستودع llama.cpp على GitHub](https://github.com/ggerganov/llama.cpp)
*   [مستودع ggml على GitHub](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)