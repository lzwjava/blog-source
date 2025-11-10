---
audio: false
generated: true
image: false
lang: hi
layout: post
title: पायथन रिक्वेस्ट्स के साथ सतत HTTP सत्र
translated: true
type: note
---

`Session` पायथन की `requests` लाइब्रेरी में एक ऐसा तरीका है जो कुकीज़, हेडर्स और ऑथेंटिकेशन जैसे कुछ पैरामीटर्स को कई HTTP रिक्वेस्ट्स में बनाए रखता है। यह एक ही सर्वर या संबंधित एंडपॉइंट्स पर बार-बार रिक्वेस्ट भेजने के लिए एक सुविधाजनक इंटरफेस प्रदान करता है, जबकि स्टेट को मेंटेन रखता है, दक्षता बढ़ाता है और कोड को सरल बनाता है। नीचे, मैं समझाऊंगा कि `requests.Session` कैसे काम करता है, इसकी प्रमुख विशेषताएं क्या हैं, और इसके उपयोग को दर्शाने के लिए उदाहरण प्रदान करूंगा।

## `requests.Session` क्या है?

`requests` लाइब्रेरी का व्यापक रूप से पायथन में HTTP रिक्वेस्ट बनाने के लिए उपयोग किया जाता है। जबकि आप स्टैंडअलोन फ़ंक्शन जैसे `requests.get()` या `requests.post()` का उपयोग कर सकते हैं, एक `Session` ऑब्जेक्ट आपको एक लगातार (persistent) सेशन बनाने की अनुमति देता है जो कॉन्फ़िगरेशन (जैसे, कुकीज़, हेडर्स, या ऑथेंटिकेशन क्रेडेंशियल्स) को कई रिक्वेस्ट्स में बरकरार रखता है। यह उन वेबसाइटों या API के साथ इंटरैक्ट करने के लिए विशेष रूप से उपयोगी है जिन्हें स्टेटफुल इंटरैक्शन की आवश्यकता होती है, जैसे कि लॉगिन सेशन को बनाए रखना या TCP कनेक्शन को पुन: उपयोग करना।

एक `Session` ऑब्जेक्ट:
- रिक्वेस्ट्स के बीच कुकीज़ को बनाए रखता है।
- बेहतर प्रदर्शन के लिए एक ही होस्ट पर कई रिक्वेस्ट करते समय अंतर्निहित TCP कनेक्शन (कनेक्शन पूलिंग के माध्यम से) को पुन: उपयोग करता है।
- आपको डिफ़ॉल्ट पैरामीटर (जैसे, हेडर्स, टाइमआउट) सेट करने की अनुमति देता है जो सेशन के साथ की गई सभी रिक्वेस्ट पर लागू होते हैं।
- ऑथेंटिकेशन और कस्टम कॉन्फ़िगरेशन को सपोर्ट करता है।

## `Session` कैसे काम करता है?

जब आप एक `Session` ऑब्जेक्ट बनाते हैं, तो यह आपकी HTTP रिक्वेस्ट के लिए एक कंटेनर के रूप में कार्य करता है। यहां बताया गया है कि यह कैसे कार्य करता है:

1.  **लगातार कुकीज़ (Persistent Cookies)**: जब आप `Session` के साथ एक रिक्वेस्ट करते हैं, तो सर्वर द्वारा सेट की गई कोई भी कुकीज़ (जैसे, लॉग इन करने के बाद सेशन कुकीज़) सेशन में संग्रहीत हो जाती हैं और स्वचालित रूप से बाद की रिक्वेस्ट में भेज दी जाती हैं। यह स्टेट को बनाए रखने, जैसे लॉग इन रहने, के लिए महत्वपूर्ण है।

2.  **कनेक्शन पूलिंग (Connection Pooling)**: एक ही होस्ट पर रिक्वेस्ट के लिए, `Session` एक ही TCP कनेक्शन को पुन: उपयोग करता है, जिससे प्रत्येक रिक्वेस्ट के लिए नए कनेक्शन बनाने की तुलना में विलंबता और ओवरहेड कम हो जाता है।

3.  **डिफ़ॉल्ट पैरामीटर (Default Parameters)**: आप हेडर्स, ऑथेंटिकेशन, या टाइमआउट जैसी विशेषताओं को `Session` ऑब्जेक्ट पर सेट कर सकते हैं, और वे उस सेशन के साथ की गई सभी रिक्वेस्ट पर लागू होंगे, जब तक कि उन्हें ओवरराइड नहीं किया जाता।

4.  **अनुकूलन योग्य (Customizable)**: आप प्रॉक्सी, SSL सत्यापन, या यहां तक कि कस्टम एडाप्टर (जैसे, रिट्री या कस्टम ट्रांसपोर्ट के लिए) को कॉन्फ़िगर कर सकते हैं ताकि यह नियंत्रित किया जा सके कि रिक्वेस्ट कैसे हैंडल की जाती हैं।

## बेसिक उपयोग

यहां एक सरल उदाहरण दिया गया है कि `requests.Session` का उपयोग कैसे करें:

```python
import requests

# एक सेशन बनाएं
session = requests.Session()

# इस सेशन में सभी रिक्वेस्ट के लिए डिफ़ॉल्ट हेडर्स सेट करें
session.headers.update({'User-Agent': 'MyApp/1.0'})

# एक GET रिक्वेस्ट करें
response1 = session.get('https://api.example.com/data')
print(response1.json())

# एक और रिक्वेस्ट करें; कुकीज़ और हेडर्स का पुन: उपयोग किया जाता है
response2 = session.post('https://api.example.com/submit', data={'key': 'value'})
print(response2.json())

# संसाधनों को मुक्त करने के लिए सेशन को बंद करें
session.close()
```

इस उदाहरण में:
- एक `Session` बनाया गया है, और सभी रिक्वेस्ट के लिए एक कस्टम `User-Agent` हेडर सेट किया गया है।
- सेशन कुकीज़ को स्वचालित रूप से हैंडल करता है, इसलिए यदि `response1` एक कुकी सेट करती है, तो इसे `response2` के साथ भेजा जाता है।
- सेशन `api.example.com` के कनेक्शन को पुन: उपयोग करता है, जिससे प्रदर्शन में सुधार होता है।

## प्रमुख विशेषताएं और उदाहरण

### 1. **कुकीज़ को बनाए रखना (Persisting Cookies)**
सेशन उन वेबसाइटों के लिए विशेष रूप से उपयोगी होते हैं जो स्टेट को बनाए रखने के लिए कुकीज़ का उपयोग करती हैं, जैसे लॉगिन सेशन।

```python
import requests

# एक सेशन बनाएं
session = requests.Session()

# एक वेबसाइट में लॉग इन करें
login_data = {'username': 'user', 'password': 'pass'}
response = session.post('https://example.com/login', data=login_data)

# एक संरक्षित पेज एक्सेस करें; सेशन स्वचालित रूप से लॉगिन कुकी भेजता है
protected_page = session.get('https://example.com/protected')
print(protected_page.text)

# सेशन को बंद करें
session.close()
```

यहां, सेशन लॉगिन रिक्वेस्ट से ऑथेंटिकेशन कुकी को संग्रहीत करता है और इसे संरक्षित पेज की बाद की रिक्वेस्ट के साथ भेजता है।

### 2. **डिफ़ॉल्ट पैरामीटर सेट करना (Setting Default Parameters)**
आप सेशन में सभी रिक्वेस्ट के लिए डिफ़ॉल्ट हेडर्स, ऑथेंटिकेशन, या अन्य पैरामीटर सेट कर सकते हैं।

```python
import requests
import functools

session = requests.Session()

# डिफ़ॉल्ट हेडर्स सेट करें
session.headers.update({
    'Authorization': 'Bearer my_token',
    'Accept': 'application/json'
})

# डिफ़ॉल्ट टाइमआउट सेट करें
session.request = functools.partial(session.request, timeout=5)

# रिक्वेस्ट करें; हेडर्स और टाइमआउट स्वचालित रूप से लागू हो जाते हैं
response1 = session.get('https://api.example.com/endpoint1')
response2 = session.get('https://api.example.com/endpoint2')

session.close()
```

### 3. **कनेक्शन पूलिंग (Connection Pooling)**
जब एक ही होस्ट पर कई रिक्वेस्ट की जाती हैं, तो `Session` कनेक्शन को पुन: उपयोग करता है, जो स्टैंडअलोन रिक्वेस्ट की तुलना में अधिक कुशल होता है।

```python
import requests
import time

# सेशन के बिना
start = time.time()
for _ in range(5):
    requests.get('https://api.example.com/data')
print(f"Without session: {time.time() - start} seconds")

# सेशन के साथ
session = requests.Session()
start = time.time()
for _ in range(5):
    session.get('https://api.example.com/data')
print(f"With session: {time.time() - start} seconds")
session.close()
```

सेशन-आधारित रिक्वेस्ट आमतौर पर तेज़ होती हैं क्योंकि वे TCP कनेक्शन का पुन: उपयोग करती हैं।

### 4. **ऑथेंटिकेशन (Authentication)**
सेशन ऑथेंटिकेशन को हैंडल करना सरल बनाते हैं, जैसे HTTP Basic Auth या कस्टम टोकन-आधारित ऑथेंटिकेशन।

```python
import requests
from requests.auth import HTTPBasicAuth

session = requests.Session()
session.auth = HTTPBasicAuth('user', 'pass')

# सभी रिक्वेस्ट में Basic Auth शामिल होगा
response = session.get('https://api.example.com/protected')
print(response.json())

session.close()
```

### 5. **कस्टम एडाप्टर (Custom Adapters)**
आप रिट्री या कनेक्शन पूलिंग व्यवहार जैसी चीजों को नियंत्रित करने के लिए कस्टम एडाप्टर माउंट कर सकते हैं।

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()

# रिट्री कॉन्फ़िगर करें
retries = Retry(total=3, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
session.mount('https://', HTTPAdapter(max_retries=retries))

# रिट्री लॉजिक के साथ एक रिक्वेस्ट करें
response = session.get('https://api.example.com/unstable_endpoint')
print(response.json())

session.close()
```

यह उदाहरण विशिष्ट HTTP एरर कोड के लिए स्वचालित रिट्री सेट करता है।

## `Session` का उपयोग कब करें

`requests.Session` का उपयोग करें जब:
- आपको कई रिक्वेस्ट्स में स्टेट (जैसे, कुकीज़) बनाए रखने की आवश्यकता हो, जैसे ऑथेंटिकेशन के लिए।
- आप एक ही होस्ट पर कई रिक्वेस्ट कर रहे हों और कनेक्शन पूलिंग का लाभ उठाना चाहते हों।
- आप रिक्वेस्ट्स में सुसंगत कॉन्फ़िगरेशन (हेडर्स, टाइमआउट, आदि) लागू करना चाहते हों।
- आप ऐसे API या वेबसाइटों के साथ इंटरैक्ट कर रहे हों जिन्हें सेशन-आधारित इंटरैक्शन की आवश्यकता हो।

यदि आप एकल रिक्वेस्ट कर रहे हैं या स्टेट को बनाए रखने की आवश्यकता नहीं है, तो स्टैंडअलोन `requests.get()` या `requests.post()` पर्याप्त है।

## एक सेशन को बंद करना (Closing a Session)

जब आपका काम पूरा हो जाए तो संसाधनों (जैसे, कनेक्शन) को मुक्त करने के लिए हमेशा सेशन को बंद करें:

```python
session.close()
```

वैकल्पिक रूप से, यह सुनिश्चित करने के लिए कि यह स्वचालित रूप से बंद हो जाए, एक सेशन को कॉन्टेक्स्ट मैनेजर के रूप में उपयोग करें:

```python
with requests.Session() as session:
    session.headers.update({'User-Agent': 'MyApp/1.0'})
    response = session.get('https://api.example.com/data')
    print(response.json())
# ब्लॉक से बाहर निकलने पर सेशन स्वचालित रूप से बंद हो जाता है
```

## एडवांस्ड नोट्स
- **थ्रेड सेफ्टी (Thread Safety)**: `Session` ऑब्जेक्ट थ्रेड-सेफ नहीं हैं। यदि आप मल्टीथ्रेडिंग का उपयोग कर रहे हैं, तो प्रत्येक थ्रेड के लिए एक अलग `Session` बनाएं।
- **प्रॉक्सी (Proxies)**: आप एक सेशन पर प्रॉक्सी सेट कर सकते हैं: `session.proxies = {'http': 'http://proxy.com', 'https': 'https://proxy.com'}`।
- **SSL सत्यापन (SSL Verification)**: डिफ़ॉल्ट रूप से, `Session` SSL सर्टिफिकेट सत्यापित करता है। इसे अक्षम करने के लिए (प्रोडक्शन के लिए अनुशंसित नहीं), `session.verify = False` का उपयोग करें।

## संदर्भ (References)
[Requests Documentation](https://requests.readthedocs.io/en/latest/)  
[Requests Session Objects](https://requests.readthedocs.io/en/latest/user/advanced/#session-objects)