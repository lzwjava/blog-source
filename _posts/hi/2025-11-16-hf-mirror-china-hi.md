---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: चीन में hf-mirror.com का उपयोग
translated: true
type: note
---

### hf-mirror.com को समझना
hf-mirror.com आधिकारिक Hugging Face Hub (huggingface.co) का एक समुदाय-संचालित मिरर है, जो विशेष रूप से चीन (गुआंगज़ौ सहित) में उपयोगकर्ताओं को नेटवर्क प्रतिबंधों को बायपास करने और AI मॉडल/डेटासेट को तेजी से डाउनलोड करने में मदद के लिए डिज़ाइन किया गया है। यह पूरी रिपॉजिटरी संरचना को दोहराता है, इसलिए आप GPT-2 जैसे मॉडल या WikiText जैसे डेटासेट तक मूल साइट पर सीधे एक्सेस किए बिना पहुंच सकते हैं, जो अक्सर धीमी या ब्लॉक होती है। चूंकि आप अक्सर Clash प्रॉक्सी का उपयोग करते हैं, ध्यान दें कि hf-mirror.com घरेलू रूप से होस्ट किया गया है और आमतौर पर एक्सेस के लिए प्रॉक्सी की आवश्यकता नहीं होती है—यह चीन में सीधे उपयोग के लिए अनुकूलित है। यदि आप पहले से ही Clash के माध्यम से ट्रैफ़िक प्रॉक्सी कर रहे हैं, तो आप या तो hf-mirror.com ट्रैफ़िक को सीधे रूट कर सकते हैं (अनावश्यक हॉप्स से बचने के लिए) या इसे प्रॉक्सी किए रख सकते हैं यदि पसंद हो।

### बेसिक सेटअप: मिरर का उपयोग करना
मुख्य बात `HF_ENDPOINT` एनवायरनमेंट वेरिएबल को मिरर की ओर इशारा करने के लिए सेट करना है। यह Hugging Face टूल्स जैसे `transformers` लाइब्रेरी, `huggingface-cli`, या `hfd` (एक तेज़ डाउनलोडर) के लिए वैश्विक रूप से काम करता है। इसे लाइब्रेरीज़ इम्पोर्ट करने या डाउनलोड चलाने से **पहले** करें।

#### 1. एनवायरनमेंट वेरिएबल सेट करें
- **Linux/macOS पर (स्थायी)**: अपने `~/.bashrc` या `~/.zshrc` में जोड़ें:
  ```
  echo 'export HF_ENDPOINT=https://hf-mirror.com' >> ~/.bashrc
  source ~/.bashrc
  ```
- **Windows पर (PowerShell, स्थायी)**: एक बार चलाएं:
  ```
  [System.Environment]::SetEnvironmentVariable('HF_ENDPOINT', 'https://hf-mirror.com', 'User')
  ```
  फिर अपना टर्मिनल रीस्टार्ट करें।
- **अस्थायी (किसी भी OS पर)**: कमांड्स को इस प्रकार प्रीफ़िक्स करें:
  ```
  HF_ENDPOINT=https://hf-mirror.com your_command_here
  ```

यह आपका कोड बदले बिना सभी Hugging Face डाउनलोड को मिरर पर रीडायरेक्ट कर देता है।

#### 2. आवश्यक टूल्स इंस्टॉल करें
- Hugging Face Hub CLI इंस्टॉल करें (डाउनलोड के लिए):
  ```
  pip install -U huggingface_hub
  ```
- और भी तेज़ डाउनलोड के लिए, `hfd` (Hugging Face Downloader, मल्टी-थ्रेडेड स्पीड के लिए aria2 का उपयोग करता है) प्राप्त करें:
  ```
  wget https://hf-mirror.com/hfd/hfd.sh  # या ब्राउज़र के माध्यम से डाउनलोड करें
  chmod +x hfd.sh
  ```

#### 3. मॉडल या डेटासेट डाउनलोड करना
- **huggingface-cli का उपयोग करके** (इंटरप्ट पर रिज्यूम सपोर्ट करता है):
  ```
  # एक मॉडल डाउनलोड करें (उदाहरण के लिए, GPT-2)
  huggingface-cli download gpt2 --resume-download --local-dir ./gpt2

  # एक डेटासेट डाउनलोड करें (उदाहरण के लिए, WikiText)
  huggingface-cli download --repo-type dataset wikitext --resume-download --local-dir ./wikitext
  ```
- **hfd का उपयोग करके** (तेज़, विशेष रूप से बड़ी फ़ाइलों के लिए):
  ```
  # मॉडल
  ./hfd.sh gpt2

  # डेटासेट
  ./hfd.sh wikitext --dataset
  ```
- **Python कोड में** (उदाहरण के लिए, transformers लाइब्रेरी के साथ):
  ```python
  import os
  os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'  # इम्पोर्ट से पहले सेट करें

  from transformers import AutoModel, AutoTokenizer
  model = AutoModel.from_pretrained('gpt2')  # मिरर से स्वचालित रूप से डाउनलोड होता है
  tokenizer = AutoTokenizer.from_pretrained('gpt2')
  ```
  इसके साथ चलाएं: `HF_ENDPOINT=https://hf-mirror.com python your_script.py`

#### 4. गेटेड/लॉग्ड-इन मॉडल को हैंडल करना
कुछ मॉडल (उदाहरण के लिए, Llama-2) के लिए Hugging Face अकाउंट और टोकन की आवश्यकता होती है:
- huggingface.co पर लॉग इन करें (यदि साइट ब्लॉक है तो अपने Clash प्रॉक्सी का उपयोग करें)।
- https://huggingface.co/settings/tokens पर एक टोकन जनरेट करें।
- इसके साथ डाउनलोड करें:
  ```
  huggingface-cli download --token hf_YourTokenHere meta-llama/Llama-2-7b-hf --resume-download --local-dir ./Llama-2-7b-hf
  ```
  या hfd के लिए:
  ```
  ./hfd.sh meta-llama/Llama-2-7b-hf --hf_username your_username --hf_token hf_YourTokenHere
  ```

### Clash प्रॉक्सी के साथ इंटीग्रेशन
चूंकि hf-mirror.com एक चीनी मिरर है, इसे Clash के बिना एक्सेस किया जाना चाहिए (डायरेक्ट कनेक्शन तेज़ है)। हालाँकि, यदि आप इसे प्रॉक्सी करना चाहते हैं (उदाहरण के लिए, स्थिरता के लिए या यदि आप कोई समस्या आती है), तो Clash को कॉन्फ़िगर करें कि वह hf-mirror.com के ट्रैफ़िक को आपके पसंदीदा प्रॉक्सी ग्रुप के माध्यम से रूट करे। Clash को विशेष "HF" कॉन्फ़िग की आवश्यकता नहीं है—यह सिस्टम-वाइड है।

#### क्विक Clash सेटअप टिप्स
- सुनिश्चित करें कि Clash चल रहा है और आपके सिस्टम प्रॉक्सी के रूप में सेट है (Clash में: "General" > "System Proxy" को सक्षम करें)।
- **hf-mirror.com को सीधे रूट करें (स्पीड के लिए अनुशंसित)**: अपनी Clash कॉन्फ़िग YAML (आमतौर पर Clash के फ़ोल्डर में `config.yaml`) एडिट करें। मिरर के लिए प्रॉक्सी को बायपास करने के लिए एक नियम जोड़ें:
  ```
  rules:
    # ... आपके मौजूदा नियम ...
    - DOMAIN-SUFFIX,hf-mirror.com,DIRECT  # प्रॉक्सी को बायपास करता है, सीधे जाता है
    # ... बाकी नियम ...
  ```
  Clash में कॉन्फ़िग को रीलोड करें (Profiles > Reload)।
- **यदि आवश्यक हो तो इसे प्रॉक्सी करें**: यदि आप Clash के माध्यम से रूट करना पसंद करते हैं, तो कोई विशेष नियम न जोड़ें—यह आपके डिफ़ॉल्ट (उदाहरण के लिए, `MATCH,Proxy`) का पालन करेगा। Clash चालू/बंद करके ब्राउज़र में hf-mirror.com को पिंग करके टेस्ट करें।
- डाउनलोड के लिए: एक टर्मिनल में कमांड्स चलाएं जहाँ सिस्टम प्रॉक्सी सक्रिय हो (Clash इसे हैंडल करता है)। यदि Python का उपयोग कर रहे हैं, तो `requests` जैसी लाइब्रेरीज़ (जिनका उपयोग transformers द्वारा किया जाता है) Clash द्वारा सेट किए गए `HTTP_PROXY`/`HTTPS_PROXY` एनवायरनमेंट वेरिएबल्स का सम्मान करती हैं (उदाहरण के लिए, HTTP पोर्ट के लिए `http://127.0.0.1:7890`)।
- टेस्ट: एक छोटे मॉडल जैसे `distilbert-base-uncased` को डाउनलोड करने का प्रयास करें। यदि धीमा है, तो hf-mirror.com ट्रैफ़िक के लिए Clash को बंद करें।

### समस्या निवारण
- **डाउनलोड अभी भी huggingface.co पर हिट हो रहे हैं?** सुनिश्चित करें कि `HF_ENDPOINT` किसी भी HF लाइब्रेरी को इम्पोर्ट करने से **पहले** सेट है (अपना नोटबुक/टर्मिनल रीस्टार्ट करें)।
- **धीमी स्पीड?** aria2 के साथ `hfd` का उपयोग करें (यह मल्टी-कनेक्शन्स को सपोर्ट करता है)। या अपने नेटवर्क की जाँच करें—गुआंगज़ौ उपयोगकर्ताओं को अक्सर hf-mirror.com पर 10-50MB/s मिलते हैं।
- **डेटासेट के साथ एरर्स?** कुछ में कस्टम स्क्रिप्ट्स होती हैं; बेस URL के रूप में `https://hf-mirror.com` का उपयोग करने के लिए उन्हें एडिट करें।
- **Windows-विशिष्ट**: यदि Anaconda का उपयोग कर रहे हैं, तो बेस एनवायरनमेंट में एनवायरनमेंट वेरिएबल सेट करें।
- उन्नत सेल्फ-होस्टिंग के लिए एक लोकल मिरर (यदि आप पूर्ण नियंत्रण चाहते हैं), GitHub पर Olah या hf-mirror-site जैसे ओपन-सोर्स टूल्स चेक करें, लेकिन पब्लिक मिरर से शुरुआत करें।

यह सेटअप आपको विश्वसनीय रूप से डाउनलोड करने में सक्षम करना चाहिए। यदि आपको कोई विशिष्ट त्रुटि आती है, तो अधिक मदद के लिए आउटपुट साझा करें!

### संदर्भ
- [HF-Mirror आधिकारिक गाइड](https://hf-mirror.com/)
- [Hugging Face Hub डॉक्स एंडपॉइंट्स पर](https://huggingface.co/docs/huggingface_hub/en/package_reference/environment_variables#huggingface_hub_constants.HF_ENDPOINT)
- [hfd डाउनलोडर](https://hf-mirror.com/hfd/hfd.sh)
- [Clash कॉन्फ़िग रूल्स](https://github.com/Dreamacro/clash/wiki/Configuration#rules)
- [Stack Overflow: चीन में डाउनलोड करना](https://stackoverflow.com/questions/77388822/how-to-download-huggingface-bert-base-uncased-in-china)