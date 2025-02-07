---
audio: false
lang: hi
layout: post
title: llama.cpp को आजमाते हुए
translated: true
---

## llama.cpp

जब आप किसी मॉडल के साथ `llama.cpp` चलाने का प्रयास करते हैं, तो आपको इस तरह की त्रुटि का सामना हो सकता है:

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

यह त्रुटि इसलिए होती है क्योंकि आप `main` प्रोग्राम चला रहे हैं। `build/bin` के अंतर्गत स्थित `llama-cli` या `llama-server` प्रोग्राम चलाने से यह समस्या हल हो जानी चाहिए।

`main` प्रोग्राम 8 अगस्त 2023 को बनाया गया था, जिसका अर्थ है कि यह वर्तमान बिल्ड नहीं है।

एक और समाधान Homebrew का उपयोग करके `llama.cpp` स्थापित करना है:

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

यह उपयोग करने के लिए एक बेहतरीन उपकरण है। Ollamac में कुछ बग हैं। उदाहरण के लिए, जब इसे स्थानीय API से प्रतिक्रिया मिलती है, तो ऐप में कई टेक्स्ट बॉक्स अपडेट हो जाते हैं।

हालांकि, Linux में, Ollama एक सिस्टम सेवा के रूप में चलता है। यहाँ सेवा कॉन्फ़िगरेशन फ़ाइल है:

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

Ollama सेवा को नियंत्रित करने के लिए निम्न आदेशों का उपयोग करें:

```bash
sudo systemctl stop ollama.service
sudo systemctl disable ollama.service
sudo systemctl status ollama.service
```

## LLM Farm

यह एक बेहतरीन iOS ऐप है। सेटिंग्स में, लगभग 20 मॉडल हैं। स्वयं द्वारा GGUF मॉडल आयात करते समय, जो Hugging Face से डाउनलोड किए जाते हैं, इससे क्रैश हो सकता है।

## लाभ

इन LLM मॉडल को स्वयं होस्ट करने से आप उन्हें नेटवर्क एक्सेस की आवश्यकता के बिना स्थानीय रूप से चला सकते हैं। उदाहरण के लिए, बड़ी फ़ाइलों को डाउनलोड करते समय जो नेटवर्क को भीड़भाड़ करते हैं, एक स्थानीय मॉडल चलाना फायदेमंद हो सकता है।

## संसाधन

*   [Hugging Face GGML Models](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [llama.cpp GitHub Repository](https://github.com/ggerganov/llama.cpp)
*   [ggml GitHub Repository](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)
