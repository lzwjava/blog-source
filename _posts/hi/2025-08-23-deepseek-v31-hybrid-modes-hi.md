---
audio: false
generated: true
image: false
lang: hi
layout: post
title: डीपसीक वी3.1 हाइब्रिड मोड्स की व्याख्या
translated: true
type: note
---

यहां बताया गया है कि **DeepSeek V3.1 API** अपनी नई हाइब्रिड इन्फ़रेंस आर्किटेक्चर ("थिंक" बनाम "नॉन‑थिंक" मोड) को कैसे हैंडल करती है:

---

### API में हुए बदलावों का सिंहावलोकन

#### 1. **दो अलग-अलग एंडपॉइंट (मोड)**

* **`deepseek-chat`** **नॉन‑थिंकिंग मोड** से मेल खाता है—जो त्वरित प्रतिक्रियाओं के लिए ऑप्टिमाइज़्ड है।
* **`deepseek-reasoner`** **थिंकिंग मोड** से मेल खाता है—जो अधिक विचारशील, मल्टी-स्टेप रीज़निंग टास्क्स के लिए बनाया गया है।
  दोनों एंडपॉइंट अब 128K टोकन कॉन्टेक्स्ट विंडो वाले एक ही V3.1 मॉडल पर चलते हैं। ([DeepSeek API Docs][1], [Data Science Dojo][2])

#### 2. **विस्तारित कॉन्टेक्स्ट सपोर्ट**

* दोनों मोड विस्तारित 128K टोकन कॉन्टेक्स्ट को सपोर्ट करते हैं, जो एक बड़ा अपग्रेड है और बहुत लंबे इनपुट को हैंडल करने की अनुमति देता है। ([DeepSeek API Docs][1], [Hugging Face][3])

#### 3. **बेहतर फॉर्मेट और क्षमताएं**

* **Anthropic API कम्पैटिबिलिटी** अब सपोर्टेड है, जिससे DeepSeek को Anthropic-स्टाइल क्लाइंट लाइब्रेरीज़ के साथ इंटीग्रेट करना आसान हो गया है। ([DeepSeek API Docs][1])
* **स्ट्रिक्ट फंक्शन कॉलिंग** (बीटा में) सपोर्टेड है, जो API के माध्यम से अधिक रोबस्ट और वैलिडेटेड टूल इनवोकेशन की अनुमति देती है। ([DeepSeek API Docs][1])

#### 4. **UI टॉगल बनाम API इनवोकेशन**

* उनके वेब UI ("DeepThink" बटन) पर, यूज़र इंटरैक्टिव तरीके से मोड के बीच स्विच कर सकते हैं।
* **API** में, आपको `model` पैरामीटर को या तो `"deepseek-chat"` (नॉन‑थिंकिंग के लिए) या `"deepseek-reasoner"` (थिंकिंग के लिए) सेट करके मोड को एक्सप्लिसिटली चुनना होगा। ([DeepSeek API Docs][1])

#### 5. **अन्य एन्हांसमेंट्स**

* **अधिक API रिसोर्सेज** और एक समग्र रूप से स्मूद डेवलपर एक्सपीरियंस पेश किया गया है। ([DeepSeek API Docs][1])
* अंतर्निहित टोकनाइज़र और चैट टेम्पलेट्स को मोड-आधारित व्यवहार (जैसे `` टोकन्स को उचित रूप से इन्सर्ट करना) को सपोर्ट करने के लिए अपडेट किया गया है। ([Hugging Face][3])

---

### सारांश: क्या बदला है — बिना टेबल के

* **नए नाम**:

  * `deepseek-chat` → नॉन‑थिंकिंग मोड
  * `deepseek-reasoner` → थिंकिंग मोड

* **साझा आर्किटेक्चर**: दोनों एक ही 671B-पैरामीटर मॉडल पर बने हैं जिसमें लंबी 128K-टोकन कॉन्टेक्स्ट विंडो है।

* **बेहतर इंटीग्रेशन विकल्प**:

  * Anthropic-स्टाइल APIs को सपोर्ट करता है।
  * स्ट्रिक्ट फंक्शन कॉलिंग (बीटा) ऑफ़र करता है, जो सुरक्षित, स्कीमा-आधारित टूल इंटरैक्शन को सक्षम बनाता है।

* **टेम्पलेट अपडेट**: API अब मोड को अलग करने के लिए प्रॉम्प्ट्स में विशेष टोकन (``) का उपयोग करता है, और चैट टेम्प्लेटिंग लॉजिक को रिवैम्प किया है।

* **डेवलपर एक्सपीरियंस**: प्लेटफ़ॉर्म में अधिक संसाधन, अपडेटेड डॉक्स और एक समग्र रूप से स्मूद इंटीग्रेशन प्रक्रिया शामिल है।

---

### उदाहरण उपयोग (Python/HTTP)

**नॉन-थिंकिंग (फास्ट रिस्पॉन्सेज):**

```python
import openai  # or DeepSeek-compatible SDK
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role":"user","content":"Tell me a joke."}],
)
```

**थिंकिंग (गहन रीज़निंग):**

```python
response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role":"user","content":"Explain why the sky is blue."}],
)
```

**फंक्शन कॉलिंग (स्ट्रिक्ट मोड, बीटा):**
आप JSON स्कीमा के साथ फ़ंक्शन (टूल्स) को डिफ़ाइन कर सकते हैं और मॉडल को उन्हें इनवोक करने दे सकते हैं, स्ट्रक्चर्ड कॉल प्राप्त कर सकते हैं जिन्हें आप एक्सेक्यूट कर सकते हैं और फीड बैक कर सकते हैं—ऑटोनोमस एजेंट्स बनाने के लिए बढ़िया। ([DeepSeek API Docs][1], [Reddit][4], [apidog][5])

---

मुझे बताएं कि क्या आप टूल यूज़ के लिए प्रॉम्प्ट्स तैयार करने, लागत या गति के लिए ऑप्टिमाइज़ करने, या Anthropic-कम्पैटिबल इंटरफेस को और अधिक विस्तार से एक्सप्लोर करने में सहायता चाहेंगे!

[1]: https://api-docs.deepseek.com/news/news250821?utm_source=chatgpt.com "DeepSeek-V3.1 Release"
[2]: https://datasciencedojo.com/blog/deep-seek-v3-1/?utm_source=chatgpt.com "Deep Seek v3.1: The Next Leap in Open-Source Large ..."
[3]: https://huggingface.co/deepseek-ai/DeepSeek-V3.1?utm_source=chatgpt.com "deepseek-ai/DeepSeek-V3.1"
[4]: https://www.reddit.com/r/LocalLLaMA/comments/1munvj6/the_new_design_in_deepseek_v31/?utm_source=chatgpt.com "The new design in DeepSeek V3.1 : r/LocalLLaMA"
[5]: https://apidog.com/blog/deepseek-v3-1-api/?utm_source=chatgpt.com "How to Use DeepSeek-V3.1 API ?"