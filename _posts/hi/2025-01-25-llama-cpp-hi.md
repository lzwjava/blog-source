---
audio: false
generated: false
image: false
lang: hi
layout: post
title: llama.cpp को आजमा रहे हैं
translated: true
type: post
---

## llama.cpp

जब आप किसी मॉडल के साथ `llama.cpp` चलाने का प्रयास करते हैं, तो आपको इस तरह की त्रुटि का सामना करना पड़ सकता है:

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

यह त्रुटि इसलिए होती है क्योंकि आप `main` प्रोग्राम चला रहे हैं। `build/bin` के अंतर्गत स्थित `llama-cli` या `llama-server` प्रोग्राम चलाने से समस्या हल हो जानी चाहिए।

`main` प्रोग्राम 8 अगस्त 2023 को बनाया गया था, जिसका अर्थ है कि यह वर्तमान बिल्ड नहीं है।

एक अन्य समाधान Homebrew का उपयोग करके `llama.cpp` स्थापित करना है:

```bash
brew install llama.cpp
```

यह सुनिश्चित करता है कि आपके पास पुस्तकालय का एक संगत संस्करण है।

## LLM Farm

यह एक बेहतरीन iOS ऐप है। सेटिंग्स में, लगभग 20 मॉडल हैं। स्वयं द्वारा GGUF मॉडल आयात करते समय, जिन्हें Hugging Face से डाउनलोड किया जाता है, क्रैश हो सकता है।

## लाभ

इन LLM मॉडल को स्व-होस्ट करने से आप उन्हें नेटवर्क एक्सेस की आवश्यकता के बिना स्थानीय रूप से चला सकते हैं। उदाहरण के लिए, बड़ी फ़ाइलों को डाउनलोड करते समय जो नेटवर्क को जाम करते हैं, एक स्थानीय मॉडल चलाना फायदेमंद हो सकता है।

## संसाधन

*   [Hugging Face GGML Models](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [llama.cpp GitHub Repository](https://github.com/ggerganov/llama.cpp)
*   [ggml GitHub Repository](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)