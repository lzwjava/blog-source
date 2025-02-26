---
audio: false
lang: hi
layout: post
title: Python Requests Library का अनुवाद
translated: true
---

Postman को Python `requests` लाइब्रेरी से पूरी तरह से बदलने के लिए, आप सभी आम HTTP ऑपरेशन जैसे विभिन्न प्रकार के अनुरोध भेजना, हेडर्स को संभालना, JSON डेटा के साथ काम करना, फाइलें अपलोड करना, प्रॉक्सी का उपयोग करना, और जवाबों को दावा करना कर सकते हैं। नीचे, मैं आपको प्रत्येक इन सुविधाओं के लिए उदाहरणों के साथ चरण-दर-चरण मार्गदर्शन करूँगा, ताकि आप एक पूर्ण और व्यावहारिक मार्गदर्शन प्राप्त करें।

### चरण 1: Requests लाइब्रेरी को इंस्टॉल करें
आरंभ करने से पहले, सुनिश्चित करें कि `requests` लाइब्रेरी इंस्टॉल है। अपने टर्मिनल में इस कमांड को चलाएं:

```bash
pip install requests
```

अब, हम उदाहरणों में डूबते हैं।

---

### HTTP अनुरोध भेजना
`requests` लाइब्रेरी सभी HTTP विधियों जैसे GET, POST, PUT, DELETE आदि को समर्थन करती है। यहाँ एक सरल GET और POST अनुरोध भेजने का तरीका है:

#### GET अनुरोध
```python
import requests

# एक GET अनुरोध भेजें
response = requests.get('https://api.example.com/data')

# स्थिति कोड और जवाब शरीर को प्रिंट करें
print("स्थिति कोड:", response.status_code)
print("जवाब शरीर:", response.text)
```

#### POST अनुरोध
```python
# कोई डेटा के साथ POST अनुरोध भेजें
response = requests.post('https://api.example.com/submit')

print("स्थिति कोड:", response.status_code)
print("जवाब शरीर:", response.text)
```

---

### हेडर्स जोड़ना
हेडर्स अक्सर प्रमाणन, सामग्री प्रकारों, या कस्टम मेटाडेटा के लिए उपयोग किए जाते हैं। उन्हें `headers` पैरामीटर के रूप में एक डिक्शनरी के रूप में पास करें।

```python
# कस्टम हेडर्स को परिभाषित करें
headers = {
    'Authorization': 'Bearer my_token',
    'Content-Type': 'application/json',
    'User-Agent': 'MyApp/1.0'
}

# हेडर्स के साथ एक GET अनुरोध भेजें
response = requests.get('https://api.example.com/data', headers=headers)

print("स्थिति कोड:", response.status_code)
print("जवाब हेडर्स:", response.headers)
print("जवाब शरीर:", response.text)
```

---

### JSON डेटा भेजना
एक POST अनुरोध में JSON डेटा भेजने के लिए (जैसे Postman के बॉडी टैब में JSON का चयन), `json` पैरामीटर का उपयोग करें। यह स्वचालित रूप से `Content-Type` को `application/json` पर सेट करता है।

```python
# JSON डेटा को परिभाषित करें
data = {
    'key1': 'value1',
    'key2': 'value2'
}

# JSON डेटा के साथ एक POST अनुरोध भेजें
response = requests.post('https://api.example.com/submit', json=data, headers=headers)

print("स्थिति कोड:", response.status_code)
print("जवाब JSON:", response.json())
```

---

### फाइलें अपलोड करना
फाइलें अपलोड करने के लिए (Postman के form-data विकल्प के समान), `files` पैरामीटर का उपयोग करें। फाइलें बाइनरी मोड (`'rb'`) में खोलें और विकल्प रूप से अतिरिक्त फॉर्म डेटा शामिल करें।

#### सरल फाइल अपलोड
```python
# अपलोड के लिए फाइल तैयार करें
files = {
    'file': open('myfile.txt', 'rb')
}

# फाइल के साथ POST अनुरोध भेजें
response = requests.post('https://api.example.com/upload', files=files)

print("स्थिति कोड:", response.status_code)
print("जवाब शरीर:", response.text)

# फाइल को मैन्युअल रूप से बंद करें
files['file'].close()
```

#### फाइल अपलोड के साथ फॉर्म डेटा (सिफारिशित तरीका)
एक `with` स्टेटमेंट का उपयोग करके सुनिश्चित करें कि फाइल स्वचालित रूप से बंद हो जाए:

```python
# अतिरिक्त फॉर्म डेटा
form_data = {
    'description': 'My file upload'
}

# फाइल खोलें और अपलोड करें
with open('myfile.txt', 'rb') as f:
    files = {
        'file': f
    }
    response = requests.post('https://api.example.com/upload', data=form_data, files=files)

print("स्थिति कोड:", response.status_code)
print("जवाब शरीर:", response.text)
```

---

### प्रॉक्सी का उपयोग करना
अनुरोधों को एक प्रॉक्सी के माध्यम से रूट करने के लिए (Postman के प्रॉक्सी सेटिंग्स के समान), एक डिक्शनरी के साथ `proxies` पैरामीटर का उपयोग करें।

```python
# प्रॉक्सी सेटिंग्स को परिभाषित करें
proxies = {
    'http': 'http://myproxy:8080',
    'https': 'https://myproxy:8080'
}

# एक प्रॉक्सी के माध्यम से एक अनुरोध भेजें
response = requests.get('https://api.example.com/data', proxies=proxies)

print("स्थिति कोड:", response.status_code)
print("जवाब शरीर:", response.text)
```

---

### जवाबों को संभालना और दावा करना
`requests` लाइब्रेरी आसानी से जवाब विवरणों जैसे स्थिति कोड, JSON डेटा, हेडर्स, और कुकीज तक पहुंच प्रदान करती है। आप Python के `assert` स्टेटमेंट का उपयोग करके जवाबों को वैधता जांच सकते हैं, जो Postman के टेस्ट स्क्रिप्ट्स के समान हैं।

#### JSON जवाबों को पर्स करना
```python
response = requests.get('https://api.example.com/data')

# स्थिति कोड जांचें और JSON पर्स करें
if response.status_code == 200:
    data = response.json()  # जवाब को Python dict/list में बदलता है
    print("JSON डेटा:", data)
else:
    print("त्रुटि:", response.status_code)
```

#### जवाब विवरणों को दावा करना
```python
response = requests.get('https://api.example.com/data')

# स्थिति कोड दावा करें
assert response.status_code == 200, f"200 की अपेक्षा थी, {response.status_code} मिला"

# JSON पर्स करें और सामग्री दावा करें
data = response.json()
assert 'key' in data, "जवाब में कुंजी नहीं मिली"
assert data['key'] == 'expected_value', "मूल्य मेल नहीं खाता"

# जवाब हेडर्स जांचें
assert 'Content-Type' in response.headers, "Content-Type हेडर गायब है"
assert response.headers['Content-Type'] == 'application/json', "अनपेक्षित Content-Type"

# कुकीज जांचें
cookies = response.cookies
assert 'session_id' in cookies, "सेशन आईडी कुकी गायब है"

print("सभी दावे पास हो गए!")
```

#### त्रुटियों को संभालना
अनुरोधों को एक `try-except` ब्लॉक में लपेटें ताकि नेटवर्क या HTTP त्रुटियों को पकड़ सकें:

```python
try:
    response = requests.get('https://api.example.com/data')
    response.raise_for_status()  # 4xx/5xx त्रुटियों के लिए एक अपवाद उठाता है
    data = response.json()
    print("डेटा:", data)
except requests.exceptions.RequestException as e:
    print("अनुरोध विफल:", e)
```

---

### व्यापक उदाहरण
यहाँ एक पूर्ण उदाहरण है जो हेडर्स, फाइल अपलोड, प्रॉक्सी, और जवाब दावों को संयोजित करता है:

```python
import requests

# हेडर्स को परिभाषित करें
headers = {
    'Authorization': 'Bearer my_token'
}

# फॉर्म डेटा और फाइल
form_data = {
    'description': 'My file upload'
}

# प्रॉक्सी सेटिंग्स
proxies = {
    'http': 'http://myproxy:8080',
    'https': 'https://myproxy:8080'
}

# फाइल अपलोड के साथ अनुरोध भेजें
try:
    with open('myfile.txt', 'rb') as f:
        files = {'file': f}
        response = requests.post(
            'https://api.example.com/upload',
            headers=headers,
            data=form_data,
            files=files,
            proxies=proxies
        )
        response.raise_for_status()  # HTTP त्रुटियों की जांच करें

        # जवाब पर्स करें और दावा करें
        data = response.json()
        assert 'upload_id' in data, "जवाब में अपलोड आईडी नहीं मिली"
        print("अपलोड सफल, आईडी:", data['upload_id'])

except requests.exceptions.RequestException as e:
    print("अनुरोध विफल:", e)
```

---

### पुन: उपयोगी फंक्शन्स (Postman संग्रहों को बदलना)
Postman के सेट अनुरोधों या संग्रहों को नकल करने के लिए, तर्क को फंक्शन्स में कैप्सूलेट करें:

```python
def upload_file(file_path, description, token, proxy=None):
    headers = {'Authorization': f'Bearer {token}'}
    data = {'description': description}
    proxies = {'http': proxy, 'https': proxy} if proxy else None

    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(
                'https://api.example.com/upload',
                headers=headers,
                data=data,
                files=files,
                proxies=proxies
            )
            response.raise_for_status()
            data = response.json()
            assert 'upload_id' in data, "अपलोड आईडी नहीं मिली"
            return data['upload_id']
    except requests.exceptions.RequestException as e:
        print("अनुरोध विफल:", e)
        return None

# उपयोग
upload_id = upload_file('myfile.txt', 'My file upload', 'my_token', 'http://myproxy:8080')
if upload_id:
    print("अपलोड सफल, आईडी:", upload_id)
```

---

### अतिरिक्त सुविधाएँ
- **सेशन**: `requests.Session()` का उपयोग करें ताकि अनुरोधों के बीच कुकीज या हेडर्स को स्थायी बनाएं।
- **समय सीमा**: अनुरोधों में `timeout=5` (सेकंड) जोड़ें ताकि लटकने से बचा जा सके।
- **रेडायरेक्ट**: `allow_redirects=True/False` के साथ नियंत्रित करें।

---

### सारांश
`requests` लाइब्रेरी के साथ, आप:
- HTTP अनुरोध भेज सकते हैं (`get`, `post`, आदि)
- हेडर्स, JSON डेटा, और फाइल अपलोड शामिल कर सकते हैं
- प्रॉक्सी का उपयोग कर सकते हैं
- जवाबों को पर्स और दावा कर सकते हैं (स्थिति, JSON, हेडर्स, कुकीज)
- कोड को पुन: उपयोगी फंक्शन्स में संगठित कर सकते हैं

यह आपको एक प्रोग्रामेटिक, फ्लेक्सिबल विकल्प प्रदान करता है जो Postman के लिए उपयुक्त है, जो स्क्रिप्टिंग और ऑटोमेशन के लिए उपयुक्त है!