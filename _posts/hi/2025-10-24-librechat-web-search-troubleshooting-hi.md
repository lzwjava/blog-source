---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: लिबरेचैट वेब खोज समस्या निवारण
translated: true
type: note
---

आइए इस समस्या को ध्यान से हल करें — जब **LibreChat में वेब खोज काम नहीं करती**, भले ही आपने **Firecrawl**, **SerpApi**, और **Jina API** कुंजियाँ जोड़ दी हों, तो समस्या लगभग हमेशा इनमें से एक होती है: कॉन्फ़िगरेशन में गलतियाँ, बैकएंड में सक्षम फ़्लैग्स का गायब होना, या UI को गलत समझना।

यहाँ एक स्पष्ट विवरण दिया गया है जिसका आप पालन कर सकते हैं (टेबल नहीं, सिर्फ स्पष्टीकरण):

---

### 1. **जाँचें कि क्या बैकएंड कॉन्फ़िग में "वेब खोज" सक्षम है**

अपनी LibreChat सर्वर कॉन्फ़िग फ़ाइल (आमतौर पर `.env` या `api/config.yaml` आपके सेटअप के आधार पर) खोलें और पुष्टि करें कि आपके पास कुछ इस तरह है:

```
# .env के लिए
SEARCH_ENABLED=true
```

या, यदि YAML का उपयोग कर रहे हैं:

```yaml
features:
  search: true
```

यदि `SEARCH_ENABLED` या `search` स्पष्ट रूप से `true` पर सेट नहीं है, तो UI बटन दिखाई दे सकता है लेकिन वास्तव में खोज नहीं करेगा।

---

### 2. **पुष्टि करें कि API कुंजियाँ सही नामित हैं**

प्रत्येक प्रदाता विशिष्ट पर्यावरण चर नामों की अपेक्षा करता है। उदाहरण के लिए:

* **SerpApi** के लिए:

  ```
  SERPAPI_API_KEY=your_key_here
  ```
* **Firecrawl** के लिए:

  ```
  FIRECRAWL_API_KEY=your_key_here
  ```
* **Jina** के लिए:

  ```
  JINA_API_KEY=your_key_here
  ```

यह भी सुनिश्चित करें कि ये निर्यात किए गए हैं या चल रही `backend` प्रक्रिया के समान वातावरण में लोड किए गए हैं।

जाँचने के लिए:

```bash
echo $SERPAPI_API_KEY
```

यदि यह खाली लौटाता है, तो आपका बैकएंड इसे नहीं देख रहा है।

---

### 3. **कुंजियाँ संपादित करने के बाद LibreChat को पुनरारंभ करें**

LibreChat पर्यावरण चर को हॉट-रीलोड नहीं करता है। चलाएँ:

```bash
docker compose down
docker compose up -d
```

(या `npm run start` फिर से यदि आप Docker का उपयोग नहीं कर रहे हैं)।

---

### 4. **पुष्टि करें कि LibreChat वास्तव में किस खोज प्रदाता का उपयोग कर रहा है**

LibreChat कॉन्फ़िग क्रम के आधार पर एक डिफ़ॉल्ट वेब खोज बैकएंड चुनता है।

यदि आप चाहते हैं कि यह SerpApi का उपयोग करे, उदाहरण के लिए, आपको निर्दिष्ट करना होगा:

```
SEARCH_PROVIDER=serpapi
```

वैकल्पिक रूप से, यदि आप Jina चाहते हैं:

```
SEARCH_PROVIDER=jina
```

यदि आपने केवल कुंजियाँ सेट की हैं लेकिन यह परिभाषित नहीं किया है कि किस प्रदाता का उपयोग करना है, तो LibreChat डिफ़ॉल्ट रूप से किसी का भी उपयोग नहीं कर सकता है।

---

### 5. **बैकएंड लॉग देखें**

चलाएँ:

```bash
docker logs librechat-backend
```

या

```bash
npm run start:debug
```

इस तरह के संदेशों की तलाश करें:

```
[Search] SerpApi key missing or invalid
```

या

```
Search provider not configured
```

ये सबसे अच्छे सुराग हैं।

---

### 6. **API को सीधे टेस्ट करें**

यह सुनिश्चित करने के लिए कि आपकी कुंजियाँ वास्तव में काम करती हैं:

**SerpApi टेस्ट:**

```bash
curl "https://serpapi.com/search.json?q=chatgpt&api_key=YOUR_KEY"
```

**Firecrawl टेस्ट:**

```bash
curl "https://api.firecrawl.dev/v1/search?q=chatgpt" -H "Authorization: Bearer YOUR_KEY"
```

**Jina टेस्ट:**

```bash
curl "https://r.jina.ai/chatgpt" -H "Authorization: Bearer YOUR_KEY"
```

यदि ये विफल होते हैं, तो कुंजियाँ स्वयं अमान्य हैं या रेट-सीमित हैं।

---

### 7. **फ्रंटएंड वर्जन मिसमैच**

यदि आपने हाल ही में LibreChat अपडेट किया है (विशेष रूप से pre-v0.7 से v0.8+ पर), तो फ्रंटएंड `Web Search` टॉगल मौजूद हो सकता है, भले ही आपका बैकएंड वर्जन अभी तक एकीकृत Firecrawl/Jina खोज मॉड्यूल का समर्थन नहीं करता हो।
चलाएँ:

```bash
git pull
```

और रीबिल्ड करें:

```bash
docker compose build --no-cache
docker compose up -d
```

---

### 8. **अंतिम जाँच — वेब UI से पुष्टि करें**

UI खोलें, **Settings → Features** पर जाएँ, और पुष्टि करें:

* "Web Search" टॉगल ON है
* आपका चुना हुआ प्रदाता सूचीबद्ध है (SerpApi, Firecrawl, या Jina)

यदि यह *"No provider available"* कहता है, तो बैकएंड आपकी कुंजियाँ नहीं पढ़ रहा है।

---

यदि आप चाहें, तो आप अपनी प्रासंगिक `.env` फ़ाइल (कुंजियों को छुपाकर) पेस्ट कर सकते हैं और मैं बिल्कुल सटीक बता दूंगा कि कौन सी लाइन गायब है या गलत नामित है।

क्या आप मुझे वह स्निपेट दिखाना चाहेंगे?