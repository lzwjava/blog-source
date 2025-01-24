---
audio: true
lang: ar
layout: post
title: تجربة llama.cpp
translated: true
---

عند محاولة تشغيل `llama.cpp` مع نموذج، قد تواجه خطأً مثل التالي:

```bash
(py311) lzwjava@Zhiweis-MacBook-Air llama.cpp % ./main -m models/7B/Phi-3-mini-4k-instruct-q4.gguf
main: build = 964 (f3c3b4b)
main: seed  = 1737736417
llama.cpp: loading model from models/7B/Phi-3-mini-4k-instruct-q4.gguf
error loading model: unknown (magic, version) combination: 46554747, 00000003; is this really a GGML file?
llama_load_model_from_file: failed to load model
llama_init_from_gpt_params: error: failed to load model 'models/7B/Phi-3-mini-4k-instruct-q4.gguf'
main: error: unable to load model
```

هذا الخطأ يشير عادةً إلى وجود مشكلة في تثبيت `llama.cpp` أو في ملف النموذج نفسه.

حل شائع هو تثبيت `llama.cpp` باستخدام Homebrew:

```bash
brew install llama.cpp
```

هذا يضمن أن لديك نسخة متوافقة من المكتبة.

إليك بعض المصادر المفيدة:

*   [نماذج Hugging Face GGML](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [مستودع llama.cpp على GitHub](https://github.com/ggerganov/llama.cpp)
*   [مستودع ggml على GitHub](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)