---
audio: false
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

يحدث هذا الخطأ لأنك تقوم بتشغيل برنامج `main`.  يجب أن يؤدي تشغيل برامج `llama-cli` أو `llama-server` الموجودة أسفل `build/bin` إلى حل المشكلة.

تم إنشاء برنامج `main` في 8 أغسطس 2023، مما يعني أنه ليس الإصدار الحالي.

حل آخر هو تثبيت `llama.cpp` باستخدام Homebrew:

```bash
brew install llama.cpp
```

هذا يضمن أن لديك إصدارًا متوافقًا من المكتبة.

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

إنها أداة رائعة للاستخدام. هناك بعض الأخطاء في Ollamac. على سبيل المثال، عندما يتلقى استجابة من واجهة برمجة التطبيقات المحلية، يتم تحديث العديد من مربعات النص في التطبيق.

ومع ذلك، في لينكس، يعمل Ollama كخدمة نظام. فيما يلي ملف تكوين الخدمة:

`/etc/systemd/system/ollama.service`:

```bash
[Unit]
Description=Ollama Service
After=network-online.target

[Service]
ExecStart=/usr/local/bin/ollama serve
User=ollama
Group=ollama
Restart=always
RestartSec=3
Environment="PATH=/home/lzw/.local/bin:/home/lzw/bin:/usr/local/cuda-12.2/bin:/home/lzw/.local/share/gem/ruby/3.0.0/bin:/home/lzw/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin"

[Install]
WantedBy=default.target
```

استخدم الأوامر التالية للتحكم في خدمة Ollama:

```bash
sudo systemctl stop ollama.service
sudo systemctl disable ollama.service
sudo systemctl status ollama.service
```

## LLM Farm

إنه تطبيق iOS رائع. في الإعدادات، يوجد حوالي 20 نموذجًا. عند استيراد نموذج GGUF بأنفسنا، والذي يتم تنزيله من Hugging Face، فقد يؤدي ذلك إلى تعطل.

## الفوائد

يسمح استضافة نماذج LLM هذه بنفسك بتشغيلها محليًا دون الحاجة إلى الوصول إلى الشبكة. على سبيل المثال، عند تنزيل ملفات كبيرة تُعيق الشبكة، يمكن أن يكون تشغيل نموذج محلي مفيدًا.

## الموارد

*   [نماذج Hugging Face GGML](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [مستودع GitHub لـ llama.cpp](https://github.com/ggerganov/llama.cpp)
*   [مستودع GitHub لـ ggml](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)
