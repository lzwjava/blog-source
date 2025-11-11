---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: ओपनराउटर के लिए कोडेक्स सीएलआई कॉन्फ़िगर करना
translated: true
type: note
---

### OpenRouter के लिए Codex CLI कॉन्फ़िगरेशन सेट अप करना

Codex CLI (OpenAI से) एक टर्मिनल-आधारित कोडिंग एजेंट है जो अपनी कॉन्फ़िगरेशन फ़ाइल के माध्यम से OpenRouter जैसे कस्टम मॉडल प्रदाताओं को सपोर्ट करता है। OpenRouter एक OpenAI-संगत API प्रदान करता है, इसलिए आप उचित बेस URL परिभाषित करके इसके माध्यम से अनुरोधों को रूट कर सकते हैं। यह Codex का उपयोग करते हुए मॉडलों की एक विस्तृत श्रृंखला (जैसे, Anthropic, Google, या ओपन-सोर्स प्रदाताओं से) तक पहुंच की अनुमति देता है।

कॉन्फ़िगरेशन `~/.codex/config.toml` पर एक TOML फ़ाइल में संग्रहीत होता है (यदि यह मौजूद नहीं है तो इसे बनाएं)। आप OpenRouter के लिए एक **मॉडल प्रदाता** सेक्शन परिभाषित करेंगे और फिर विशिष्ट मॉडलों के लिए एक **प्रोफाइल** में इसका संदर्भ देंगे।

#### चरण 1: अपनी OpenRouter API कुंजी प्राप्त करें
- यदि आपने पहले से नहीं किया है, तो [openrouter.ai](https://openrouter.ai) पर साइन अप करें।
- अपने अकाउंट डैशबोर्ड से एक API कुंजी जनरेट करें।
- इसे एक पर्यावरण चर के रूप में सेट करें:  
  ```
  export OPENROUTER_API_KEY=your_api_key_here
  ```
  इसे अपने शेल प्रोफाइल (जैसे, `~/.bashrc` या `~/.zshrc`) में दृढ़ता के लिए जोड़ें।

#### चरण 2: कॉन्फ़िग फ़ाइल संपादित करें
अपने एडिटर में `~/.codex/config.toml` खोलें और निम्नलिखित सेक्शन जोड़ें। यह बेस URL को OpenRouter के एंडपॉइंट (`https://openrouter.ai/api/v1`) पर सेट करता है, जो OpenAI-संगत है (Codex स्वचालित रूप से `/chat/completions` जोड़ता है)।

```toml
# OpenRouter प्रदाता को परिभाषित करें
[model_providers.openrouter]
name = "OpenRouter"
base_url = "https://openrouter.ai/api/v1"
env_key = "OPENROUTER_API_KEY"  # प्रमाणीकरण के लिए आपके env var से पढ़ता है

# इस प्रदाता का उपयोग करते हुए एक प्रोफाइल परिभाषित करें (उदाहरण: GPT-जैसे मॉडल का उपयोग करना)
[profiles.openrouter-gpt]
model_provider = "openrouter"
model = "openai/gpt-4o-mini"  # किसी भी OpenRouter मॉडल ID से बदलें, जैसे "anthropic/claude-3.5-sonnet"
```

- **मुख्य फ़ील्ड्स समझाई गईं**:
  - `base_url`: OpenRouter के API एंडपॉइंट की ओर इशारा करता है। यह डिफ़ॉल्ट OpenAI बेस URL को ओवरराइड करता है।
  - `env_key`: Bearer टोकन ऑथ हेडर के लिए env var निर्दिष्ट करता है।
  - `model`: [OpenRouter के मॉडल सूची](https://openrouter.ai/models) से सटीक मॉडल ID का उपयोग करें। कोडिंग टास्क के लिए, "openai/codex-mini-latest" या "meta-llama/llama-3.1-405b-instruct" आज़माएं।
  - आप विभिन्न मॉडलों के लिए कई प्रोफाइल जोड़ सकते हैं (जैसे, `[profiles.openrouter-claude]` के साथ `model = "anthropic/claude-3.5-sonnet"`)।

#### चरण 3: कॉन्फ़िगरेशन का उपयोग करें
- यदि आवश्यक हो तो Codex CLI इंस्टॉल करें: `npm install -g @openai/codex` (या Homebrew के माध्यम से: `brew install codex`)।
- अपनी प्रोफाइल के साथ Codex चलाएं:  
  ```
  codex --profile openrouter-gpt
  ```
  या कॉन्फ़िग में एक डिफ़ॉल्ट प्रोफाइल सेट करें:  
  ```toml
  [default_profile]
  name = "openrouter-gpt"
  ```
- इसका परीक्षण करें: `codex` चलाएं और इसे एक साधारण कोडिंग प्रॉम्प्ट दें। उपयोग के लिए OpenRouter के डैशबोर्ड की जांच करें।

#### समस्या निवारण
- **प्रमाणीकरण त्रुटियाँ**: सुनिश्चित करें कि `OPENROUTER_API_KEY` सेट और एक्सपोर्टेड है।
- **मॉडल नहीं मिला**: OpenRouter पर मॉडल ID सत्यापित करें—यह केस-सेंसिटिव और उपसर्गित है (जैसे, "provider/model-name")।
- **संस्करण जांच**: पूर्ण प्रदाता समर्थन के लिए Codex CLI v0.13+ का उपयोग करें। `npm update -g @openai/codex` के साथ अपडेट करें।
- **उन्नत रूटिंग**: OpenRouter-विशिष्ट सुविधाओं जैसे लागत-अनुकूलित रूटिंग के लिए, प्रोफाइल के तहत वैकल्पिक पैरामीटर जोड़ें जैसे `provider = { sort = "price" }` (नए संस्करणों में समर्थित)।

यह सेटअप आपके अनुरोधों को Codex के OpenAI-शैली API के साथ संगत रखते हुए OpenRouter के इकोसिस्टम का लाभ उठाता है। अधिक जानकारी के लिए, [Codex CLI डॉक्स npm पर](https://www.npmjs.com/package/@openai/codex) या OpenRouter का [API गाइड](https://openrouter.ai/docs) देखें। यदि आप Open Codex जैसे फोर्क का उपयोग कर रहे हैं, तो कॉन्फ़िग समान है लेकिन इसमें अतिरिक्त Gemini सपोर्ट हो सकता है।