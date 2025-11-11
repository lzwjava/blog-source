---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: पायथन क्रिप्टोग्राफ़ी गाइड
translated: true
type: note
---

### क्रिप्टोग्राफी पैकेज का परिचय
`cryptography` पैकेज एक लोकप्रिय Python लाइब्रेरी है जो क्रिप्टोग्राफिक प्रिमिटिव्स और सुरक्षित प्रोटोकॉल के लिए रेसिपी प्रदान करती है। यह उपयोग में आसानी और सुरक्षा पर केंद्रित है, और AES, RSA जैसे मानकों को लागू करती है। यह SSH या TLS जैसे उच्च-स्तरीय प्रोटोकॉल को सीधे लागू करने के लिए नहीं है—इसे एक बिल्डिंग ब्लॉक के रूप में उपयोग करें। सुरक्षा पैच के लिए हमेशा सत्यापित करें कि यह अद्यतन है।

### इंस्टालेशन
pip के माध्यम से इंस्टॉल करें:
```bash
pip install cryptography
```
बेहतर प्रदर्शन के लिए (विशेष रूप से बड़ी कुंजियों या लगातार ऑपरेशन के लिए), OpenSSL सपोर्ट के साथ इंस्टॉल करें:
```bash
pip install cryptography[openssl]
```
नोट: कुछ सिस्टम पर, आपको OpenSSL हेडर अलग से इंस्टॉल करने की आवश्यकता हो सकती है (उदाहरण के लिए, Ubuntu पर `apt install libssl-dev`)।

### बुनियादी अवधारणाएँ
- **प्रिमिटिव्स**: कम-स्तरीय ऑपरेशन जैसे एन्क्रिप्शन/डिक्रिप्शन।
- **रेसिपीज़**: उच्च-स्तरीय, ओपिनियनेटेड फ़ंक्शन (उदाहरण के लिए, सममित एन्क्रिप्शन के लिए Fernet)।
- **खतरे की चेतावनियाँ**: लाइब्रेरी असुरक्षित उपयोग के लिए चेतावनियों का उपयोग करती है—उन पर ध्यान दें।

लाइब्रेरी को इम्पोर्ट करें:
```python
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization, hashes, asyncioc as a
from cryptography.hazmat.primitives.asymmetric import rsa, padding
```

### उदाहरण

#### 1. Fernet के साथ सममित एन्क्रिप्शन (शुरुआती लोगों के लिए सबसे आसान)
Fernet अखंडता के लिए HMAC के साथ CBC मोड में AES-128 का उपयोग करता है। यह एन्क्रिप्टेड डेटा संग्रहीत करने के लिए आदर्श है।

```python
from cryptography.fernet import Fernet

# एक कुंजी जनरेट करें (सुरक्षित रूप से संग्रहीत करें, उदाहरण के लिए, env वेरिएबल में)
key = Fernet.generate_key()
cipher = Fernet(key)

# एन्क्रिप्ट करें
plaintext = b"This is a secret message."
token = cipher.encrypt(plaintext)
print("Encrypted:", token)

# डिक्रिप्ट करें
decrypted = cipher.decrypt(token)
print("Decrypted:", decrypted)
```
- **नोट्स**: कुंजियाँ URL-सुरक्षित base64 (44 वर्ण) होती हैं। कुंजियों को कभी भी हार्डकोड न करें; उन्हें समय-समय पर रोटेट करें।

#### 2. RSA के साथ असममित एन्क्रिप्शन
एक सार्वजनिक/निजी कुंजी जोड़ी जनरेट करें और ऐसे डेटा को एन्क्रिप्ट करें जिसे केवल निजी कुंजी धारक ही डिक्रिप्ट कर सकता है।

```python
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# निजी कुंजी जनरेट करें
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# संग्रहण के लिए सीरियलाइज़ करें
pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()  # पासवर्ड सुरक्षा के लिए BestAvailableEncryption() का उपयोग करें
)

# सार्वजनिक कुंजी प्राप्त करें और सीरियलाइज़ करें
public_key = private_key.public_key()
pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# सार्वजनिक कुंजी के साथ एन्क्रिप्ट करें
plaintext = b"Secret message"
ciphertext = public_key.encrypt(
    plaintext,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)

# निजी कुंजी के साथ डिक्रिप्ट करें
decrypted = private_key.decrypt(
    ciphertext,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)
print("Decrypted:", decrypted)
```
- **नोट्स**: RSA बड़े डेटा के लिए धीमा है; इसका उपयोग कुंजी विनिमय या छोटे संदेशों के लिए करें। OAEP पैडिंग हमलों को रोकती है।

#### 3. हैश जनरेट करना और उपयोग करना
अखंडता जांच या पासवर्ड हैशिंग के लिए।

```python
from cryptography.hazmat.primitives import hashes

# डेटा हैश करें
digest = hashes.Hash(hashes.SHA256())
digest.update(b"Some data")
hash_result = digest.finalize()
print("SHA256 Hash:", hash_result.hex())
```

पासवर्ड के लिए, कुंजी व्युत्पत्ति के लिए `cryptography.hazmat.primitives.kdf.pbkdf2` का उपयोग करें (उदाहरण के लिए, धीमे, नमकीन हैशिंग के लिए PBKDF2)।

#### 4. RSA के साथ डिजिटल हस्ताक्षर
प्रामाणिकता साबित करने के लिए डेटा पर हस्ताक्षर करें।

```python
# पहले से बनी RSA कुंजियों का उपयोग करना
message = b"Data to sign"
signature = private_key.sign(
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256()
)

# सार्वजनिक कुंजी के साथ सत्यापित करें
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    print("Signature valid")
except Exception:
    print("Signature invalid")
```

### सर्वोत्तम अभ्यास
- **कुंजी प्रबंधन**: कुंजियों को सुरक्षित रूप से संग्रहीत करें (उदाहरण के लिए, AWS KMS, हार्डवेयर सुरक्षा मॉड्यूल का उपयोग करके)। कुंजियों का पुन: उपयोग कभी न करें।
- **पैडिंग और मोड**: हमेशा सुरक्षित पैडिंग का उपयोग करें (उदाहरण के लिए, RSA के लिए OAEP, AES के लिए GCM)।
- **यादृच्छिकता**: बीज के लिए `os.urandom()` या `secrets` मॉड्यूल का उपयोग करें; `random` से बचें।
- **अपडेट**: क्रिप्टोग्राफी विकसित होती है—अपने उपयोग में कमजोरियों की जांच करें।
- **अपना खुद का न बनाएँ**: जटिल आवश्यकताओं के लिए, रेसिपी का उपयोग करें या उच्च-स्तरीय लाइब्रेरी जैसे `pyjwt` या `boto3` के साथ एकीकृत करें।
- **टेस्टिंग**: त्रुटि हैंडलिंग के लिए लाइब्रेरी के कॉन्स्टेंट और एक्सेप्शन का उपयोग करें।

### आगे पढ़ने के लिए
- [आधिकारिक दस्तावेज़ीकरण](https://cryptography.io/en/latest/) – विस्तृत API संदर्भ और ट्यूटोरियल।
- [PyPI पेज](https://pypi.org/project/cryptography/) – संस्करण इतिहास और एकीकरण।
- उन्नत विषयों के लिए, `cryptography` विकी या RFCs (उदाहरण के लिए, PKCS#1 के लिए RFC 8017) का अन्वेषण करें।

यदि आपके पास कोई विशिष्ट उपयोग मामला है (उदाहरण के लिए, फ़ाइलों को एन्क्रिप्ट करना या API सुरक्षा), तो तैयार किए गए उदाहरणों के लिए अधिक विवरण प्रदान करें।