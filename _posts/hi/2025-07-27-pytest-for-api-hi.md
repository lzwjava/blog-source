---
audio: false
generated: true
image: false
lang: hi
layout: post
title: पायथन एपीआई परीक्षण फ्रेमवर्क
translated: true
type: note
---

### API एंडपॉइंट टेस्टिंग के लिए अनुशंसित Python टेस्ट फ्रेमवर्क

Java (जैसे, Spring Boot) में लिखे गए सर्वर एंडपॉइंट्स का परीक्षण करने के लिए, आप HTTP रिक्वेस्ट्स (जैसे GET, POST, PUT, DELETE, आदि) भेजने और प्रतिक्रिया कोड, हेडर और बॉडी सामग्री को सत्यापित करने के लिए Python फ्रेमवर्क का उपयोग कर सकते हैं। चूंकि सर्वर Java में है, इसे एक ब्लैक-बॉक्स API की तरह समझें और इसके साथ इंटरैक्ट करने के लिए Python की HTTP क्लाइंट लाइब्रेरीज (जैसे `requests` या `httpx`) का उपयोग करें। सबसे आम सेटअप में एक टेस्ट रनर फ्रेमवर्क शामिल होता है जो एक HTTP लाइब्रेरी के साथ संयुक्त होता है।

आपके उपयोग के मामले के लिए लोकप्रियता और उपयुक्तता के आधार पर (2025 तक की हालिया सिफारिशों पर आधारित), यहां कुछ मजबूत विकल्प दिए गए हैं। मैं उन पर ध्यान केंद्रित करूंगा जो आसान HTTP इंटरैक्शन और प्रतिक्रिया सत्यापन का समर्थन करते हैं:

#### 1. **pytest (requests या httpx लाइब्रेरी के साथ)**
   - **यह अच्छा क्यों है**: pytest यूनिट, इंटीग्रेशन और API टेस्ट के लिए सबसे लोकप्रिय Python टेस्टिंग फ्रेमवर्क है। यह लचीला है, इसका सिंटैक्स सरल है, और यह सेटअप/टीयरडाउन (जैसे, एक टेस्ट सर्वर शुरू करना या मॉकिंग) के लिए फिक्स्चर का समर्थन करता है। आप स्टेटस कोड (जैसे, 200 OK) और JSON प्रतिक्रियाओं पर दावा करने के लिए GET/POST रिक्वेस्ट भेजने के लिए टेस्ट लिख सकते हैं। यह `pytest-httpx` जैसे प्लगइन्स के साथ एक्स्टेंसिबल है जो एसिंक टेस्टिंग के लिए है।
   - **आपके परिदृश्य के लिए उपयोग कैसे करें**:
     - इंस्टॉल करें: `pip install pytest requests` (या एसिंक के लिए `pip install pytest httpx`)।
     - उदाहरण टेस्ट:
       ```python
       import requests
       import pytest

       @pytest.fixture
       def base_url():
           return "http://your-java-server:8080"

       def test_get_endpoint(base_url):
           response = requests.get(f"{base_url}/api/resource")
           assert response.status_code == 200
           assert "expected_key" in response.json()

       def test_post_endpoint(base_url):
           data = {"key": "value"}
           response = requests.post(f"{base_url}/api/resource", json=data)
           assert response.status_code == 201
           assert response.json()["status"] == "created"
       ```
     - फायदे: पठनीय, कम्युनिटी प्लगइन्स, समानांतर निष्पादन, CI/CD के लिए बढ़िया।
     - नुकसान: इसमें कुछ कोडिंग की आवश्यकता होती है; विशुद्ध रूप से डिक्लेरेटिव नहीं है।
   - सबसे अच्छा: इंटीग्रेशन टेस्ट के लिए जहां आपको कस्टम लॉजिक की आवश्यकता हो।

#### 2. **Tavern**
   - **यह अच्छा क्यों है**: Tavern, RESTful API टेस्टिंग के लिए विशेष रूप से एक pytest प्लगइन है। यह टेस्ट को डिक्लेरेटिव तरीके से परिभाषित करने के लिए YAML फाइलों का उपयोग करता है, जिससे बहुत अधिक Python कोड के बिना HTTP मेथड्स, पेलोड और अपेक्षित प्रतिक्रियाओं को निर्दिष्ट करना आसान हो जाता है। स्टेटस कोड और JSON स्कीमा जांच सहित एंडपॉइंट वैलिडेशन के लिए आदर्श।
   - **आपके परिदृश्य के लिए उपयोग कैसे करें**:
     - इंस्टॉल करें: `pip install tavern`।
     - उदाहरण YAML टेस्ट फाइल:
       ```yaml
       test_name: Test GET endpoint
       stages:
         - name: Get resource
           request:
             url: http://your-java-server:8080/api/resource
             method: GET
           response:
             status_code: 200
             json:
               expected_key: expected_value

       test_name: Test POST endpoint
       stages:
         - name: Post resource
           request:
             url: http://your-java-server:8080/api/resource
             method: POST
             json: { "key": "value" }
           response:
             status_code: 201
             json:
               status: created
       ```
     - `pytest your_test.yaml` के साथ रन करें।
   - फायदे: मानव-पठनीय YAML, pytest के साथ एकीकृत, स्वचालित रिट्री और वैलिडेशन।
   - नुकसान: शुद्ध Python की तुलना में जटिल लॉजिक के लिए कम लचीला।
   - सबसे अच्छा: एंडपॉइंट्स पर केंद्रित त्वरित, डिक्लेरेटिव API टेस्ट के लिए।

#### 3. **PyRestTest**
   - **यह अच्छा क्यों है**: YAML या JSON कॉन्फ़िग का उपयोग करके REST API टेस्टिंग के लिए एक हल्का Python टूल। यह बुनियादी टेस्ट के लिए कोड-मुक्त है, बेंचमार्किंग का समर्थन करता है, और आपके Java एंडपॉइंट्स जैसे बाहरी सर्वरों से HTTP प्रतिक्रियाओं को मान्य करने के लिए बढ़िया है।
   - **आपके परिदृश्य के लिए उपयोग कैसे करें**:
     - इंस्टॉल करें: `pip install pyresttest`।
     - उदाहरण YAML:
       ```yaml
       - config:
           url: http://your-java-server:8080
       - test:
           name: GET test
           url: /api/resource
           method: GET
           expected_status: [200]
           validators:
             - {jsonpath_mini: 'expected_key', expected: 'expected_value'}
       - test:
           name: POST test
           url: /api/resource
           method: POST
           body: '{"key": "value"}'
           expected_status: [201]
           validators:
             - {jsonpath_mini: 'status', expected: 'created'}
       ```
     - `pyresttest http://base-url test.yaml` के साथ रन करें।
   - फायदे: सरल सेटअप, बॉयलरप्लेट कोड की आवश्यकता नहीं, पोर्टेबल।
   - नुकसान: pytest की तुलना में सीमित कम्युनिटी; पुराना टूल लेकिन अभी भी मेंटेन किया गया।
   - सबसे अच्छा: माइक्रो-बेंचमार्किंग और सरल इंटीग्रेशन टेस्ट के लिए।

#### 4. **Robot Framework (RequestsLibrary के साथ)**
   - **यह अच्छा क्यों है**: स्वीकृति और API टेस्टिंग के लिए एक कीवर्ड-चालित फ्रेमवर्क। `RequestsLibrary` के साथ, यह HTTP रिक्वेस्ट्स को मूल रूप से संभालता है और इंटीग्रेशन टेस्ट के लिए एक्स्टेंसिबल है। पठनीय, गैर-कोड टेस्ट पसंद करने वाली टीमों के लिए अच्छा है।
   - **आपके परिदृश्य के लिए उपयोग कैसे करें**:
     - इंस्टॉल करें: `pip install robotframework robotframework-requests`।
     - उदाहरण टेस्ट फाइल:
       ```
       *** Settings ***
       Library    RequestsLibrary

       *** Test Cases ***
       Test GET Endpoint
           Create Session    mysession    http://your-java-server:8080
           ${response}=    GET On Session    mysession    /api/resource
           Status Should Be    200    ${response}
           ${json}=    To Json    ${response.content}
           Should Be Equal    ${json['expected_key']}    expected_value

       Test POST Endpoint
           Create Session    mysession    http://your-java-server:8080
           ${data}=    Create Dictionary    key=value
           ${response}=    POST On Session    mysession    /api/resource    json=${data}
           Status Should Be    201    ${response}
           ${json}=    To Json    ${response.content}
           Should Be Equal    ${json['status']}    created
       ```
     - `robot your_test.robot` के साथ रन करें।
   - फायदे: कीवर्ड-आधारित (गैर-डेवलपर्स के लिए आसान), रिपोर्टिंग अंतर्निहित।
   - नुकसान: वर्बोस सिंटैक्स; Python शुद्धतावादियों के लिए सीखने में अधिक मुश्किल।
   - सबसे अच्छा: BDD-शैली के इंटीग्रेशन टेस्ट के लिए।

#### अतिरिक्त सुझाव
- **सामान्य लाइब्रेरी: requests**: लगभग सभी फ्रेमवर्क HTTP कॉल के लिए इसके साथ अच्छी तरह से जोड़े जाते हैं। यह सरल है (`response = requests.get(url)`), JSON को स्वचालित रूप से संभालता है, और बैटल-टेस्टेड है।
- **requests का विकल्प: httpx**: यदि आपको एसिंक सपोर्ट की आवश्यकता है (जैसे, हाई-थ्रूपुट टेस्ट के लिए) तो इसका उपयोग करें। `pip install httpx` के माध्यम से इंस्टॉल करें।
- **Java सर्वर के लिए सेटअप**: सुनिश्चित करें कि आपका Java सर्वर स्थानीय रूप से या दूरस्थ रूप से चल रहा है। इंटीग्रेशन टेस्ट के लिए, CI/CD में Spring Boot ऐप को स्पिन अप करने के लिए Docker पर विचार करें।
- **सर्वश्रेष्ठ समग्र पिक**: लचीलेपन के लिए pytest + requests से शुरुआत करें। यदि आप डिक्लेरेटिव टेस्ट पसंद करते हैं, तो Tavern या PyRestTest चुनें।
- **विचारणीय बातें**: ये क्रॉस-लैंग्वेज काम करते हैं क्योंकि वे मानक HTTP का उपयोग करते हैं। स्कीमा वैलिडेशन के लिए, `jsonschema` जैसी लाइब्रेरीज जोड़ें। Jenkins या GitHub Actions जैसे टूल्स के साथ CI/CD में रन करें।

### संदर्भ
[Top Python Testing Frameworks in 2025 You Should Switch To](https://medium.com/@hadiyolworld007/top-python-testing-frameworks-in-2025-you-should-switch-to-6ddeb679ccd5)  
[10 Best Python Testing Frameworks To Look For In 2025](https://www.lambdatest.com/blog/top-python-testing-frameworks/)  
[Top 14 Best Python Automation Tools for Testing in 2025](https://apidog.com/blog/best-python-testing-tools-2025/)  
[The Best Open Source API Testing Tools for 2025](https://testguild.com/12-open-source-api-testing-tools-rest-soap-services/)