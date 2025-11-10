---
audio: false
generated: true
image: false
lang: hi
layout: post
title: होमब्रू के साथ ओल्लामा को अपग्रेड करें
translated: true
type: note
---

Ollama को नवीनतम संस्करण (वर्तमान में जुलाई 2025 तक v0.10.0) में अपग्रेड करने के लिए macOS पर Homebrew का उपयोग करते हुए, इन चरणों का पालन करें:

1. Homebrew के formulae को अपडेट करें ताकि यह नवीनतम उपलब्ध संस्करणों के बारे में जान सके:
   ```
   brew update
   ```

2. विशेष रूप से Ollama को अपग्रेड करें:
   ```
   brew upgrade ollama
   ```

3. संस्करण जांचकर अपग्रेड सत्यापित करें:
   ```
   ollama --version
   ```

यदि आप Ollama को एक पृष्ठभूमि सेवा के रूप में चला रहे हैं, तो अपग्रेड के बाद इसे पुनरारंभ करें:
```
brew services restart ollama
```

वैकल्पिक रूप से, यदि आप इसे मैन्युअली चलाते हैं, तो किसी भी मौजूदा प्रक्रिया को रोकें और इसे अपनी पसंदीदा कमांड के साथ फिर से शुरू करें (उदाहरण के लिए, आपके इंस्टॉल आउटपुट में दिए गए caveats से):
```
OLLAMA_FLASH_ATTENTION="1" OLLAMA_KV_CACHE_TYPE="q8_0" /opt/homebrew/opt/ollama/bin/ollama serve
```

इस मानक प्रक्रिया के अलावा किसी विशेष अपग्रेड निर्देशों की आवश्यकता नहीं है।

[Ollama Releases](https://github.com/ollama/ollama/releases)