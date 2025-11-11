---
audio: false
generated: true
lang: hi
layout: post
title: पायथन अनुरोध पुस्तकालय
translated: true
type: note
---

Postman को पूरी तरह से Python `requests` लाइब्रेरी से बदलने के लिए, आप सभी सामान्य HTTP ऑपरेशन कर सकते हैं जैसे कि विभिन्न प्रकार के requests भेजना, headers को हैंडल करना, JSON डेटा के साथ काम करना, फ़ाइलें अपलोड करना, proxies का उपयोग करना और responses पर assertion लगाना। नीचे, मैं आपको इनमें से प्रत्येक functionality के लिए उदाहरणों के साथ चरण-दर-चरण मार्गदर्शन करूंगा, यह सुनिश्चित करते हुए कि आपके पास एक पूर्ण और व्यावहारिक गाइड है।

### चरण 1: Requests लाइब्रेरी इंस्टॉल करें
शुरू करने से पहले, सुनिश्चित करें कि `requests` लाइब्रेरी इंस्टॉल है। अपने टर्मिनल में यह कमांड चलाएँ:

```bash
pip install requests
```

अब, उदाहरणों में गोता लगाते हैं।

---

### HTTP Requests भेजना
`requests` लाइब्रेरी सभी HTTP methods जैसे GET, POST, PUT, DELETE, आदि को सपोर्ट करती है। यहाँ एक साधारण GET और POST request भेजने का तरीका बताया गया है:

#### GET Request
```python
import requests

# एक GET request भेजें
response = requests.get('https://api.example.com/data')

# status code और response body प्रिंट करें
print("Status Code:", response.status_code)
print("Response Body:", response.text)
```

#### POST Request
```python
# बिना डेटा के एक POST request भेजें
response = requests.post('https://api.example.com/submit')

print("Status Code:", response.status_code)
print("Response Body:", response.text)
```

---

### Headers जोड़ना
Headers का उपयोग अक्सर authentication, content types, या custom metadata के लिए किया जाता है। उन्हें `headers` पैरामीटर को एक dictionary के रूप में पास करें।

```python
# custom headers को परिभाषित करें
headers = {
    'Authorization': 'Bearer my_token',
    'Content-Type': 'application/json',
    'User-Agent': 'MyApp/1.0'
}

# headers के साथ एक GET request भेजें
response = requests.get('https://api.example.com/data', headers=headers)

print("Status Code:", response.status_code)
print("Response Headers:", response.headers)
print("Response Body:", response.text)
```

---

### JSON डेटा भेजना
एक POST request में JSON डेटा भेजने के लिए (जैसे Postman के body टैब में JSON चुनना), `json` पैरामीटर का उपयोग करें। यह स्वचालित रूप से `Content-Type` को `application/json` पर सेट कर देता है।

```python
# JSON डेटा को परिभाषित करें
data = {
    'key1': 'value1',
    'key2': 'value2'
}

# JSON डेटा के साथ एक POST request भेजें
response = requests.post('https://api.example.com/submit', json=data, headers=headers)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
```

---

### फ़ाइलें अपलोड करना
फ़ाइलें अपलोड करने के लिए (Postman के form-data विकल्प के समान), `files` पैरामीटर का उपयोग करें। फ़ाइलों को binary mode (`'rb'`) में खोलें और वैकल्पिक रूप से अतिरिक्त form data शामिल करें।

#### सरल फ़ाइल अपलोड
```python
# अपलोड के लिए फ़ाइल तैयार करें
files = {
    'file': open('myfile.txt', 'rb')
}

# फ़ाइल के साथ POST request भेजें
response = requests.post('https://api.example.com/upload', files=files)

print("Status Code:", response.status_code)
print("Response Body:", response.text)

# फ़ाइल को मैन्युअल रूप से बंद करें
files['file'].close()
```

#### Form Data के साथ फ़ाइल अपलोड (अनुशंसित तरीका)
`with` स्टेटमेंट का उपयोग करने से यह सुनिश्चित होता है कि फ़ाइल स्वचालित रूप से बंद हो जाती है:
```python
# अतिरिक्त form data
form_data = {
    'description': 'My file upload'
}

# फ़ाइल को खोलें और अपलोड करें
with open('myfile.txt', 'rb') as f:
    files = {
        'file': f
    }
    response = requests.post('https://api.example.com/upload', data=form_data, files=files)

print("Status Code:", response.status_code)
print("Response Body:", response.text)
```

---

### Proxies का उपयोग करना
Requests को एक proxy के माध्यम से रूट करने के लिए (Postman की proxy settings के समान), `proxies` पैरामीटर का उपयोग एक dictionary के साथ करें।

```python
# proxy settings को परिभाषित करें
proxies = {
    'http': 'http://myproxy:8080',
    'https': 'https://myproxy:8080'
}

# एक proxy के माध्यम से request भेजें
response = requests.get('https://api.example.com/data', proxies=proxies)

print("Status Code:", response.status_code)
print("Response Body:", response.text)
```

---

### Responses को हैंडल करना और Assertion लगाना
`requests` लाइब्रेरी response details जैसे status codes, JSON data, headers, और cookies तक आसान पहुंच प्रदान करती है। आप responses को validate करने के लिए Python के `assert` स्टेटमेंट का उपयोग कर सकते हैं, जो Postman के test scripts के समान है।

#### JSON Responses को पार्स करना
```python
response = requests.get('https://api.example.com/data')

# status code की जांच करें और JSON को पार्स करें
if response.status_code == 200:
    data = response.json()  # response को Python dict/list में बदलता है
    print("JSON Data:", data)
else:
    print("Error:", response.status_code)
```

#### Response Details पर Assertion लगाना
```python
response = requests.get('https://api.example.com/data')

# status code पर assertion लगाएं
assert response.status_code == 200, f"Expected 200, got {response.status_code}"

# JSON को पार्स करें और content पर assertion लगाएं
data = response.json()
assert 'key' in data, "Key not found in response"
assert data['key'] == 'expected_value', "Value does not match"

# response headers की जांच करें
assert 'Content-Type' in response.headers, "Content-Type header missing"
assert response.headers['Content-Type'] == 'application/json', "Unexpected Content-Type"

# cookies की जांच करें
cookies = response.cookies
assert 'session_id' in cookies, "Session ID cookie missing"

print("All assertions passed!")
```

#### Errors को हैंडल करना
नेटवर्क या HTTP errors को पकड़ने के लिए requests को `try-except` ब्लॉक में लपेटें:
```python
try:
    response = requests.get('https://api.example.com/data')
    response.raise_for_status()  # 4xx/5xx errors के लिए एक exception उठाता है
    data = response.json()
    print("Data:", data)
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
```

---

### व्यापक उदाहरण
यहाँ headers, फ़ाइल अपलोड, proxies, और response assertions को जोड़ने वाला एक पूर्ण उदाहरण दिया गया है:

```python
import requests

# headers को परिभाषित करें
headers = {
    'Authorization': 'Bearer my_token'
}

# Form data और फ़ाइल
form_data = {
    'description': 'My file upload'
}

# Proxy settings
proxies = {
    'http': 'http://myproxy:8080',
    'https': 'https://myproxy:8080'
}

# फ़ाइल अपलोड के साथ request भेजें
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
        response.raise_for_status()  # HTTP errors की जांच करें

        # response को पार्स करें और assertion लगाएं
        data = response.json()
        assert 'upload_id' in data, "Upload ID not found in response"
        print("Upload successful, ID:", data['upload_id'])

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
```

---

### पुन: प्रयोज्य Functions (Postman Collections को बदलना)
Postman के saved requests या collections की नकल करने के लिए, लॉजिक को functions में encapsulate करें:

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
            assert 'upload_id' in data, "Upload ID not found"
            return data['upload_id']
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return None

# Usage
upload_id = upload_file('myfile.txt', 'My file upload', 'my_token', 'http://myproxy:8080')
if upload_id:
    print("Upload successful, ID:", upload_id)
```

---

### अतिरिक्त विशेषताएँ
- **Sessions**: requests में cookies या headers को बनाए रखने के लिए `requests.Session()` का उपयोग करें।
- **Timeouts**: लटकने से बचने के लिए requests में `timeout=5` (सेकंड) जोड़ें।
- **Redirects**: `allow_redirects=True/False` के साथ नियंत्रित करें।

---

### सारांश
`requests` लाइब्रेरी के साथ, आप यह कर सकते हैं:
- HTTP requests भेजें (`get`, `post`, आदि)
- headers, JSON डेटा, और फ़ाइल अपलोड शामिल करें
- proxies का उपयोग करें
- responses को पार्स करें और assertion लगाएं (status, JSON, headers, cookies)
- कोड को पुन: प्रयोज्य functions में व्यवस्थित करें

यह आपको Postman का एक प्रोग्रामेटिक, लचीला विकल्प देता है, जो स्क्रिप्टिंग और automation के लिए उपयुक्त है!