---
audio: false
generated: true
lang: hi
layout: post
title: ओपनराउटर के माध्यम से क्लॉड तक पहुँच
translated: true
type: note
---

### OpenRouter के माध्यम से Claude मॉडल का उपयोग कैसे करें (एक चीनी उपयोगकर्ता के रूप में Anthropic API एक्सेस के बिना)

एक चीनी उपयोगकर्ता के रूप में, आपको क्षेत्रीय ब्लॉक के कारण सीधे Anthropic की Claude API तक पहुंचने में प्रतिबंधों का सामना करना पड़ सकता है। हालांकि, OpenRouter एक विश्वसनीय विकल्प है जो कई AI प्रदाताओं, जिनमें Anthropic के Claude मॉडल शामिल हैं, के लिए एक एकीकृत API गेटवे के रूप में कार्य करता है। OpenRouter चीन में सुलभ है (वेबसाइट और API एंडपॉइंट दोनों ब्लॉक नहीं हैं), जिससे आप बिना सीधे Anthropic अकाउंट या API कुंजी की आवश्यकता के Claude को रिक्वेस्ट भेज सकते हैं। यह पे-पर-यूज़ (आपको एक भुगतान विधि जोड़नी होगी) है, लेकिन साइन अप करना मुफ्त है, और यह सीमित उपयोग के लिए एक फ्री टियर को सपोर्ट करता है।

OpenRouter का API OpenAI के फॉर्मेट के साथ संगत है, इसलिए आप OpenAI Python SDK जैसी परिचित लाइब्रेरीज़ का उपयोग कर सकते हैं। नीचे, मैं शुरुआत करने के चरणों को रेखांकित करूंगा और Python में Claude का उपयोग करने के लिए कोड उदाहरण प्रदान करूंगा।

#### चरण 1: OpenRouter के लिए साइन अप करें
1. OpenRouter वेबसाइट पर जाएं: https://openrouter.ai।
2. "Sign Up" या "Get Started" पर क्लिक करें (आमतौर पर शीर्ष दाएं कोने में)।
3. अपने ईमेल का उपयोग करके एक अकाउंट बनाएं (या यदि उपलब्ध हो तो GitHub/Google लॉगिन का उपयोग करें)। VPN की आवश्यकता नहीं है, क्योंकि साइट चीन में काम करती है।
4. साइन अप करने के बाद, यदि आवश्यक हो तो अपना ईमेल वेरीफाई करें।
5. डैशबोर्ड पर जाएं और एक भुगतान विधि (जैसे, क्रेडिट कार्ड) जोड़ें। OpenRouter टोकन उपयोग के आधार पर शुल्क लेता है, लेकिन आप एक छोटे डिपॉजिट के साथ शुरुआत कर सकते हैं। Claude मॉडल पर विवरण के लिए उनके प्राइसिंग पेज की जांच करें।

#### चरण 2: एक API कुंजी जनरेट करें
1. अपने OpenRouter डैशबोर्ड में, "API Keys" या "Keys" सेक्शन पर नेविगेट करें।
2. एक नई API कुंजी बनाएं (यह एक लंबी स्ट्रिंग जैसी दिखेगी, जैसे `sk-or-v1-...`)।
3. इसे कॉपी करें और सुरक्षित रूप से सहेजें—इसे पासवर्ड की तरह समझें। आप इसे Anthropic कुंजी के बजाय अपने कोड में उपयोग करेंगे।

#### चरण 3: एक Claude मॉडल चुनें
OpenRouter Anthropic के Claude मॉडल को निम्नलिखित जैसे IDs के साथ सूचीबद्ध करता है:
- `anthropic/claude-3.5-sonnet` (अधिकांश कार्यों के लिए अनुशंसित; संतुलित और सक्षम)।
- `anthropic/claude-3-opus` (अधिक शक्तिशाली लेकिन महंगा)।
- नए वर्शन (जैसे, Claude 3.7 यदि 2025 में उपलब्ध हो) https://openrouter.ai/models?providers=anthropic पर सूचीबद्ध होंगे।

आप लागत, संदर्भ सीमा और उपलब्धता देखने के लिए मॉडल्स पेज ब्राउज़ कर सकते हैं।

#### चरण 4: अपना एनवायरनमेंट सेट अप करें
- यदि आपके पास Python नहीं है तो इसे इंस्टॉल करें (वर्शन 3.8+ अनुशंसित)।
- OpenAI लाइब्रेरी इंस्टॉल करें: अपने टर्मिनल में `pip install openai` चलाएं।

#### चरण 5: कोड में Claude का उपयोग करें
OpenRouter के बेस URL (`https://openrouter.ai/api/v1`) के साथ OpenAI SDK का उपयोग करें। अपनी रिक्वेस्ट में Claude मॉडल ID निर्दिष्ट करें।

यहां Claude 3.5 Sonnet के साथ चैट करने के लिए एक सरल Python उदाहरण दिया गया है:

```python
from openai import OpenAI

# OpenRouter के एंडपॉइंट और अपनी API कुंजी के साथ क्लाइंट को इनिशियलाइज़ करें
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="YOUR_OPENROUTER_API_KEY_HERE",  # अपनी वास्तविक कुंजी से बदलें
)

# Claude को एक रिक्वेस्ट भेजें
completion = client.chat.completions.create(
    model="anthropic/claude-3.5-sonnet",  # Claude मॉडल ID का उपयोग करें
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, what is the capital of China?"}
    ],
    temperature=0.7,  # वैकल्पिक: रचनात्मकता के लिए समायोजित करें (0-1)
    max_tokens=150    # वैकल्पिक: प्रतिक्रिया की लंबाई सीमित करें
)

# प्रतिक्रिया प्रिंट करें
print(completion.choices[0].message.content)
```

- **स्पष्टीकरण**: यह Claude को एक सिस्टम प्रॉम्प्ट और यूजर मैसेज भेजता है, एक प्रतिक्रिया प्राप्त करता है, और इसे प्रिंट करता है। API कुंजी को बदलें और आवश्यकतानुसार पैरामीटर्स को समायोजित करें।
- **यदि आप रॉ HTTP रिक्वेस्ट पसंद करते हैं** (OpenAI लाइब्रेरी के बिना):

```python
import requests
import json

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer YOUR_OPENROUTER_API_KEY_HERE",
        "Content-Type": "application/json"
    },
    data=json.dumps({
        "model": "anthropic/claude-3.5-sonnet",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, what is the capital of China?"}
        ]
    })
)

# प्रतिक्रिया को पार्स करें और प्रिंट करें
data = response.json()
print(data['choices'][0]['message']['content'])
```

- **सुझाव**:
  - वैकल्पिक हेडर जैसे `"HTTP-Referer": "your-site-url"` और `"X-Title": "Your App Name"` जोड़ें ताकि उपयोग का श्रेय दिया जा सके (लीडरबोर्ड और संभावित फ्री क्रेडिट में मदद करता है)।
  - अप्रत्याशित लागतों से बचने के लिए अपने OpenRouter डैशबोर्ड में उपयोग की निगरानी करें।
  - स्ट्रीमिंग प्रतिक्रियाओं या उन्नत सुविधाओं (जैसे, टूल्स) के लिए, OpenRouter के पूर्ण डॉक्स देखें।
  - यदि आपको रेट लिमिट या एरर्स का सामना करना पड़ता है, तो अपना बैलेंस चेक करें या एक अलग मॉडल आज़माएं।

#### समस्या निवारण
- **API एरर्स**: सुनिश्चित करें कि आपकी कुंजी सही और फंडेड है। पहले एक सस्ते मॉडल के साथ टेस्ट करें।
- **क्षेत्रीय मुद्दे**: यदि कोई ब्लॉक होता है (असंभावित), तो VPN का उपयोग करें, लेकिन OpenRouter को समर्थित मॉडल के लिए ऐसी प्रतिबंधों को दरकिनार करने के लिए डिज़ाइन किया गया है।
- **फ्री विकल्प**: सीमित फ्री एक्सेस के लिए, Puter.js जैसे प्रॉक्सी एक्सप्लोर करें (लेकिन उनकी सीमाएं हो सकती हैं)।

यह सेटअप आपको सीधे Anthropic एक्सेस के बिना प्रोग्रामेटिक रूप से Claude का उपयोग करने देता है। यदि आपको विशिष्ट टूल्स (जैसे, Cursor IDE या Make.com) के साथ इंटीग्रेशन की आवश्यकता है, तो उन पर ट्यूटोरियल्स खोजें।

संदर्भ:  
[OpenRouter डॉक्यूमेंटेशन](https://openrouter.ai/docs)  
[OpenRouter पर Anthropic Claude](https://openrouter.ai/anthropic/claude-3.5-sonnet)  
[चीन में OpenRouter का उपयोग](https://medium.com/ai-simplified-in-plain-english/not-re-inventing-the-wheel-in-ai-2ec3e76ae2bd)  
[चीन में Claude का उपयोग कैसे करें](https://www.comparitech.com/blog/vpn-privacy/how-to-use-claude-in-china/)