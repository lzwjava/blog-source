---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: एनवी में पायथन रिक्वेस्ट्स प्रॉक्सी कॉन्फ़िगर करें
translated: true
type: note
---

### `.env` फ़ाइल का उपयोग करके Python Requests के लिए HTTP/HTTPS प्रॉक्सी सेट करना

Python में `requests` लाइब्रेरी प्रॉक्सी कॉन्फ़िगरेशन के लिए `HTTP_PROXY` और `HTTPS_PROXY` जैसे मानक पर्यावरण चर (environment variables) का स्वचालित रूप से पालन करती है। इन्हें सुरक्षित रूप से प्रबंधित करने (जैसे, आपकी स्क्रिप्ट में हार्डकोड किए बिना) के लिए, आप इन्हें एक `.env` फ़ाइल में संग्रहीत कर सकते हैं और `python-dotenv` लाइब्रेरी का उपयोग करके लोड कर सकते हैं। यह संवेदनशील प्रॉक्सी विवरणों को आपके कोड से बाहर रखता है।

#### चरण 1: आवश्यक पैकेज इंस्टॉल करें
आपको `.env` फ़ाइल लोड करने के लिए `requests` (यदि पहले से इंस्टॉल नहीं है) और `python-dotenv` की आवश्यकता होगी।

```bash
pip install requests python-dotenv
```

#### चरण 2: एक `.env` फ़ाइल बनाएँ
अपने प्रोजेक्ट रूट में, `.env` नामक एक फ़ाइल बनाएँ (कोई एक्सटेंशन नहीं) और अपनी प्रॉक्सी सेटिंग्स जोड़ें। प्रॉक्सी URL के लिए `http://` या `https://` फॉर्मेट का उपयोग करें, यदि आवश्यक हो तो उपयोगकर्ता नाम/पासवर्ड सहित।

`.env` सामग्री का उदाहरण:
```
HTTP_PROXY=http://username:password@proxy-host:port
HTTPS_PROXY=https://username:password@proxy-host:port
NO_PROXY=localhost,127.0.0.1,example.com  # वैकल्पिक: प्रॉक्सी से डोमेन को बाहर करें
```

- `HTTP_PROXY`: HTTP ट्रैफ़िक के लिए।
- `HTTPS_PROXY`: HTTPS ट्रैफ़िक के लिए (अक्सर HTTP_PROXY के समान)।
- `NO_PROXY`: प्रॉक्सी को बायपास करने के लिए होस्ट/आईपी की अल्पविराम-पृथक्कृत सूची।
- नोट: पर्यावरण चर केस-इनसेंसिटिव होते हैं, लेकिन अपरकेस पारंपरिक है।

संवेदनशील जानकारी को कमिट करने से बचने के लिए `.env` को अपने `.gitignore` में जोड़ें।

#### चरण 3: अपनी Python स्क्रिप्ट में `.env` फ़ाइल लोड करें
अपनी स्क्रिप्ट के शीर्ष पर, पर्यावरण चर लोड करें:

```python
from dotenv import load_dotenv
import requests

# .env फ़ाइल से चर लोड करें
load_dotenv()  # डिफ़ॉल्ट रूप से वर्तमान निर्देशिका में .env की तलाश करता है

# अब एक रिक्वेस्ट करें – प्रॉक्सी स्वचालित रूप से लागू हो जाते हैं
response = requests.get('https://httpbin.org/ip')
print(response.json())
```

- `load_dotenv()` `.env` फ़ाइल को पढ़ता है और `os.environ` में चर सेट करता है।
- `requests` स्वचालित रूप से `HTTP_PROXY`/`HTTPS_PROXY` का पता लगा लेगा—जब तक कि ओवरराइड न करना हो, `proxies` डिक्शनरी पास करने की कोई आवश्यकता नहीं है।

#### चरण 4: प्रॉक्सी उपयोग सत्यापित करें (वैकल्पिक)
यह पुष्टि करने के लिए कि प्रॉक्सी काम कर रहे हैं, httpbin.org जैसी सेवा के साथ परीक्षण करें:

```python
import requests
from dotenv import load_dotenv

load_dotenv()

proxies = requests.utils.get_environ_proxies('https://httpbin.org/ip')  # लोड किए गए प्रॉक्सी का निरीक्षण करें
print("Loaded proxies:", proxies)

response = requests.get('https://httpbin.org/ip')
print("Your IP via proxy:", response.json())
```

यदि सही ढंग से कॉन्फ़िगर किया गया है तो इसमें प्रॉक्सी सर्वर का आईपी दिखाई देना चाहिए।

#### सामान्य समस्याएँ और सुझाव
- **प्रॉक्सी प्रमाणीकरण**: यदि आवश्यक हो तो URL में `username:password@` शामिल करें।
- **SOCKS प्रॉक्सी**: `socks5://` उपसर्ग का उपयोग करें (`requests[socks]` एक्स्ट्रा की आवश्यकता होती है: `pip install requests[socks]`)।
- **प्रति-अनुरोध ओवरराइड करना**: यदि आपको किसी विशिष्ट कॉल के लिए अलग-अलग प्रॉक्सी की आवश्यकता है, तो एक डिक्शनरी पास करें:
  ```python:disable-run
  proxies = {'http': 'http://custom-proxy:port', 'https': 'https://custom-proxy:port'}
  response = requests.get('url', proxies=proxies)
  ```
- **पर्यावरण**: Windows/Linux/macOS पर काम करता है। Windows पर, cmd में `set` या PowerShell समकक्षों का उपयोग करें।
- **सुरक्षा**: `.env` को वर्जन कंट्रोल में कभी कमिट न करें।

यह सेटअप सरल, सुरक्षित है और पर्यावरण-आधारित कॉन्फ़िगरेशन के लिए सर्वोत्तम प्रथाओं का पालन करता है।

[Requests Documentation: Proxies](https://requests.readthedocs.io/en/latest/user/advanced/#proxies)  
[python-dotenv Documentation](https://github.com/theskumar/python-dotenv)