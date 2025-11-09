---
audio: false
date: 2025-09-10
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: एपीआई परीक्षण विशिष्टता और अविचलिता रणनीति
translated: true
type: note
---

बढ़िया सवाल है। आइए पहले व्यापक संदर्भ समझते हैं, फिर API/इंटीग्रेशन टेस्ट में "अनोखेपन" (uniqueness) के बारे में व्यावहारिक बात करते हैं।

# क्या है क्या (त्वरित रिफ्रेशर)

* **URL (पथ + क्वेरी)**

  * पथ आमतौर पर **संसाधन पहचान (resource identity)** होता है: `/orders/123`.
  * क्वेरी पैरामीटर **फ़िल्टर/संशोधक (filters/modifiers)** होते हैं: `/orders?status=PAID&page=2`.

* **मेथड (Method)**

  * `GET/HEAD` सुरक्षित (safe) होते हैं।
  * `PUT` **वर्गसम (Idempotent)** होता है (एक ही कॉल, एक ही परिणाम)।
  * `POST` **वर्गसम नहीं** होता है, जब तक कि आप **Idempotency-Key** योजना न जोड़ें।
  * `PATCH` की वर्गसमता की गारंटी नहीं है।

* **हेडर (Headers)**

  * `Content-Type`: **बॉडी (Body)** को कैसे एनकोड किया गया है।

    * `application/json` → JSON बॉडी।
    * `application/x-www-form-urlencoded` → `a=1&b=2` बॉडी।
    * `multipart/form-data; boundary=----abcd` → फ़ाइल/अपलोड और मिश्रित भाग (parts)।
  * `Content-Disposition` **मल्टीपार्ट के भागों के अंदर** आता है, शीर्ष-स्तरीय रिक्वेस्ट में नहीं। एक विशिष्ट भाग:

    ```
    --Boundary123
    Content-Disposition: form-data; name="file"; filename="x.png"
    Content-Type: image/png

    <binary bytes>
    --Boundary123--
    ```
  * उपयोगी कस्टम हेडर:

    * **Idempotency-Key**: साइड-इफेक्ट वाले POST को डी-डुप्लिकेट (duplicate removal) करने के लिए।
    * **X-Request-ID / Correlation-ID**: सेवाओं में एकल रिक्वेस्ट को ट्रेस/लॉग करने के लिए।

* **बॉडी (Body)**

  * JSON: एक क्रमबद्ध दस्तावेज़ (serialized document)।
  * `form-urlencoded`: क्वेरी स्ट्रिंग की तरह की-वैल्यू जोड़े लेकिन बॉडी में।
  * `multipart/form-data`: `boundary` डिलीमीटर द्वारा अलग किए गए कई "भाग" (parts) (`----WebKitFormBoundary...` एक सामान्य ब्राउज़र स्ट्रिंग है)।

# पहचान कहाँ होनी चाहिए?

* **संसाधन पहचान (Resource identity)** → **URL पथ** में (`/users/{id}`), क्योंकि यह स्थिर और बुकमार्क करने योग्य है।
* **ऑपरेशन संशोधक (Operation modifiers)** → क्वेरी या हेडर में।
* **लिखने के लिए प्रतिनिधित्व/स्थिति (Representation/state)** → बॉडी में।

रिक्वेस्ट की विशिष्टता को केवल URL में एनकोड करने का प्रयास अक्सर राइट ऑपरेशन (जैसे, बड़ी JSON वाला POST) के लिए विफल हो जाता है। इसके बजाय, **दो परतों** में सोचें:

1.  **रिक्वेस्ट पहचान (फिंगरप्रिंट)**:
    निम्नलिखित का एक निर्धारित (deterministic) हैश:

    * HTTP **मेथड**
    * **मानकीकृत पथ (Canonicalized path)** (टेम्पलेट + ठोस मान)
    * **सामान्यीकृत क्वेरी (Normalized query)** (क्रमबद्ध)
    * **चयनित हेडर** (केवल वे जो शब्दार्थ (semantics) को प्रभावित करते हैं, जैसे `Accept`, `Content-Language`, `Date` नहीं)
    * **बॉडी** (मानकीकृत JSON या मल्टीपार्ट के लिए प्रति भाग एक डाइजेस्ट)

2.  **ऑपरेशन पहचान (व्यवसाय वर्गसमता)**:
    साइड-इफेक्ट वाले ऑपरेशन (create/charge/transfer) के लिए **Idempotency-Key** (एक UUID प्रति *व्यवसाय इरादा*) का उपयोग करें। सर्वर पहला परिणाम उस Key के तहत संग्रहीत करता है और रिट्राइज के लिए उसे वापस लौटाता है।

ये अलग-अलग समस्याओं को हल करते हैं: फिंगरप्रिंट आपके **टेस्ट** और **अवलोकन (observability)** में मदद करते हैं; Idempotency Key **प्रोडक्शन** को डुप्लिकेट प्रभावों से बचाते हैं।

# "अनोखेपन" के लिए टेस्टिंग रणनीति

1.  **एक रिक्वेस्ट फिंगरप्रिंट फ़ंक्शन परिभाषित करें** (क्लाइंट/टेस्ट साइड)। उदाहरण लॉजिक:

    * हेडर नामों को लोअरकेस करें; केवल एक सुरक्षित allowlist शामिल करें।
    * क्वेरी पैरामीटर्स को सॉर्ट करें; बॉडी को स्थिर JSON स्ट्रिंगिफाई करें (व्हाइटस्पेस हटाएं, कीज़ को सॉर्ट करें)।
    * `METHOD\nPATH\nQUERY\nHEADERS\nBODY` पर SHA-256।

2.  **प्रत्येक टेस्ट को एक Correlation ID दें**

    * प्रति टेस्ट केस एक UUID जेनरेट करें: `X-Request-ID: test-<suite>-<uuid>`।
    * इसे सर्वर-साइड लॉग करें ताकि आप लॉग्स को एक टेस्ट से जोड़ सकें।

3.  **जहाँ आवश्यक हो Idempotency-Key का उपयोग करें**

    * ऐसे POSTs के लिए जो संसाधन बनाते हैं या पैसे चार्ज करते हैं:

      * `Idempotency-Key: <uuid>`
      * सर्वर को एक ही रिटेंशन विंडो के भीतर एक ही Key वाली रिट्राइज के लिए एक ही 200/201 और बॉडी वापस करनी चाहिए।

4.  **टेस्ट डेटा को अद्वितीय लेकिन न्यूनतम रखें**

    * सीडेड, निर्धारित ID (जैसे, ईमेल `user+T001@example.com`) का उपयोग करें या टेस्ट UUID के साथ सफ़िक्स लगाएं।
    * साफ़ करें, या बेहतर है, टेस्ट को **वर्गसम (Idempotent)** बनाने के लिए डिज़ाइन करें, जहाँ संभव हो अपने सीडेड ID के खिलाफ PUT/DELETE का उपयोग करके।

5.  **सही स्तर पर असर्शन (Assert) करें**

    * **वर्गसम (Idempotent)** ऑपरेशन के लिए: **स्टेटस**, **प्रतिनिधित्व (representation)**, और **साइड इफेक्ट्स** (जैसे, दोहराने पर रिकॉर्ड काउंट अपरिवर्तित) का असर्शन करें।
    * **गैर-वर्गसम (Non-idempotent)** POSTs के लिए Idempotency-Key के साथ: पहली कॉल के लिए 201, बाद की रिट्राइ के लिए समान बॉडी के साथ 200 (या समान संसाधन के साथ 201 दोहराया गया) का असर्शन करें।

# व्यावहारिक स्निपेट्स (Snippets)

**cURL उदाहरण**

* JSON POST:

  ```bash
  curl -X POST https://api.example.com/orders \
    -H 'Content-Type: application/json' \
    -H 'Idempotency-Key: 4b6f2d1a-...' \
    -H 'X-Request-ID: test-orders-create-...' \
    -d '{"customerId":"C123","items":[{"sku":"ABC","qty":1}]}'
  ```
* मल्टीपार्ट अपलोड:

  ```bash
  curl -X POST https://api.example.com/uploads \
    -H 'X-Request-ID: test-upload-...' \
    -F 'file=@/path/pic.png' \
    -F 'meta={"purpose":"avatar"};type=application/json'
  ```

  (curl स्वचालित रूप से `Content-Type: multipart/form-data; boundary=----...` सेट कर देता है और प्रत्येक भाग की अपनी `Content-Disposition` होती है।)

**पायथन टेस्ट-साइड रिक्वेस्ट फिंगरप्रिंट (उदाहरण स्वरूप):**

```python
import hashlib, json, urllib.parse

def canonical_json(obj):
    return json.dumps(obj, separators=(',', ':'), sort_keys=True)

def normalize_query(url):
    parsed = urllib.parse.urlsplit(url)
    q = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    q.sort()
    return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, urllib.parse.urlencode(q), '')), q

def request_fingerprint(method, url, headers=None, body_bytes=b''):
    headers = headers or {}
    # allowlist headers that affect semantics
    allow = {'accept', 'content-type', 'content-language'}
    norm_headers = {k.lower(): v.strip() for k, v in headers.items() if k.lower() in allow}
    header_line = '\n'.join(f'{k}:{norm_headers[k]}' for k in sorted(norm_headers))
    url_no_query, q_pairs = normalize_query(url)
    query_line = '&'.join(f'{k}={v}' for k, v in q_pairs)
    h = hashlib.sha256()
    h.update((method.upper() + '\n').encode())
    h.update((url_no_query + '\n').encode())
    h.update((query_line + '\n').encode())
    h.update((header_line + '\n').encode())
    h.update(body_bytes or b'')
    return h.hexdigest()
```

* JSON बॉडी के लिए, `body_bytes=canonical_json(payload).encode()` पास करें।
* मल्टीपार्ट के लिए, बाउंडरी शोर से बचने के लिए प्रत्येक भाग को हैश करें फिर संयोजन को हैश करें।

# आपके मूल विचार का उत्तर

> "अगर URL यूनिक है तो रिक्वेस्ट्स यूनिक हैं; पैराम/बॉडी फिर भी बहुत योगदान देते हैं—API/इंटीग्रेशन टेस्ट के लिए uniqueness के बारे में कैसे सोचें?"

* **URL अकेले** को टेस्ट में uniqueness के लिए **अपर्याप्त** मानें, क्योंकि हेडर और बॉडी शब्दार्थ (semantics) को भौतिक रूप से बदलते हैं।
* टेस्ट में डीडप/ट्रेस के लिए ऊपर बताए अनुसार एक **रिक्वेस्ट फिंगरप्रिंट** बनाएं।
* **POSTs** के व्यवसाय-स्तरीय डी-डुप्लिकेशन के लिए, URL पर नहीं, **Idempotency-Key** पर भरोसा करें।
* स्पष्टता और बेहतर टेस्ट निर्धारण (determinism) के लिए **संसाधन पहचान (resource identity)** को पथ में रखें।

# छोटी चेकलिस्ट जिसे आप आज से अपना सकते हैं

* [ ] प्रत्येक टेस्ट रिक्वेस्ट में `X-Request-ID` (UUID) जोड़ें।
* [ ] ऐसे POSTs में जो create/charge करते हैं, `Idempotency-Key` जोड़ें।
* [ ] एक टेस्ट हेल्पर लागू करें जो रिक्वेस्ट फिंगरप्रिंट की गणना करे और इसे प्रत्येक असर्शन के साथ लॉग करे।
* [ ] हैश करने से पहले JSON को मानक (Canonicalize) करें; क्वेरी पैरामीटर्स को सॉर्ट करें; शब्दार्थ हेडर की allowlist बनाएं।
* [ ] टेस्ट को वर्गसम बनाने के लिए अपसर्ट (upserts) के लिए PUT को प्राथमिकता दें; सच्चे क्रिएट (creates) के लिए POST रिज़र्व करें।
* [ ] मल्टीपार्ट के लिए, कच्चे बाउंडरी बाइट्स के बजाय **सर्वर-पार्स किए गए भागों** (नाम, फ़ाइलनाम, कंटेंट टाइप) पर असर्शन करें।

यदि आप अपना वर्तमान टेस्ट स्टैक (pytest/unittest + requests/httpx, या Java/Kotlin) साझा करते हैं, तो मैं उसके अनुरूप एक तैयार-से-उपयोग हेल्पर प्रदान कर सकता हूं।