---
audio: false
lang: hi
layout: post
title: llama.cpp को आज़मा रहे हैं
translated: true
---

## llama.cpp

जब आप `llama.cpp` को एक मॉडल के साथ चलाने का प्रयास करते हैं, तो आपको इस तरह की त्रुटि का सामना करना पड़ सकता है:

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

यह त्रुटि इसलिए होती है क्योंकि मैं `main` प्रोग्राम चला रहा हूँ। `build/bin` के अंतर्गत स्थित `llama-cli` या `llama-server` प्रोग्राम चलाने से यह समस्या हल हो जाएगी।

एक और समाधान यह है कि `llama.cpp` को Homebrew का उपयोग करके इंस्टॉल करें:

```bash
brew install llama.cpp
```

यह सुनिश्चित करता है कि आपके पास लाइब्रेरी का एक संगत संस्करण है।

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

यह एक बहुत ही उपयोगी टूल है। Ollamac में कुछ बग हैं। उदाहरण के लिए, जब यह स्थानीय API से प्रतिक्रिया प्राप्त करता है, तो ऐप में कई टेक्स्ट बॉक्स अपडेट हो जाते हैं।

## LLM Farm

यह एक बेहतरीन iOS ऐप है। सेटिंग्स में लगभग 20 मॉडल हैं। जब हम Hugging Face से डाउनलोड किए गए GGUF मॉडल को स्वयं आयात करते हैं, तो इससे ऐप क्रैश हो सकता है।

## लाभ

इन LLM मॉडल्स को स्वयं होस्ट करने से आप उन्हें नेटवर्क एक्सेस की आवश्यकता के बिना स्थानीय रूप से चला सकते हैं। उदाहरण के लिए, जब बड़ी फाइलें डाउनलोड करने से नेटवर्क भर जाता है, तो स्थानीय मॉडल चलाना फायदेमंद हो सकता है।

## संसाधन

*   [Hugging Face GGML Models](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [llama.cpp GitHub Repository](https://github.com/ggerganov/llama.cpp)
*   [ggml GitHub Repository](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)