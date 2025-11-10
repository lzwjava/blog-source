---
audio: false
generated: true
image: false
lang: hi
layout: post
title: पायथन 3.11 और pip3.11 इंस्टॉल करें
translated: true
type: note
---

ऐसा लगता है कि आपके Ubuntu सिस्टम पर कई Python और pip वर्ज़न इंस्टॉल हैं, और आप **Python 3.11** और इसके संबंधित **pip (pip3.11)** को इंस्टॉल करना चाहते हैं। यहां बताया गया है कि आप इसे कैसे कर सकते हैं:

---

### **1. Python 3.11 इंस्टॉल करें**
सबसे पहले, अपनी पैकेज लिस्ट को अपडेट करें और Python 3.11 इंस्टॉल करें:

```bash
sudo apt update
sudo apt install python3.11
```

इंस्टॉलेशन को वेरीफाई करें:

```bash
python3.11 --version
```

---

### **2. Python 3.11 के लिए pip इंस्टॉल करें**
Ubuntu की डिफ़ॉल्ट रिपॉजिटरीज में Python 3.11 के लिए `pip` शामिल नहीं हो सकता है। आप इसे निम्नलिखित चरणों का उपयोग करके इंस्टॉल कर सकते हैं:

#### **विकल्प A: apt के माध्यम से pip इंस्टॉल करें (अगर उपलब्ध हो)**
```bash
sudo apt install python3.11-venv python3.11-dev python3-pip
```
अगर `python3-pip` किसी अलग वर्ज़न के लिए pip इंस्टॉल करता है, तो **विकल्प B** पर आगे बढ़ें।

#### **विकल्प B: ensurepip का उपयोग करके pip इंस्टॉल करें**
```bash
python3.11 -m ensurepip --upgrade
```
यह विशेष रूप से Python 3.11 के लिए pip इंस्टॉल करेगा।

#### **विकल्प C: get-pip.py का उपयोग करके pip इंस्टॉल करें**
अगर उपरोक्त तरीके काम नहीं करते हैं, तो ऑफिशियल `get-pip.py` स्क्रिप्ट का उपयोग करें:

```bash
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11
```

---

### **3. pip3.11 इंस्टॉलेशन वेरीफाई करें**
जांचें कि क्या `pip3.11` अब उपलब्ध है:

```bash
pip3.11 --version
```
आपको कुछ इस तरह का आउटपुट दिखना चाहिए:
```
pip 23.x.x from /usr/local/lib/python3.11/site-packages/pip (python 3.11)
```

---

### **4. (वैकल्पिक) एक वर्चुअल एनवायरनमेंट बनाएं**
Python वर्ज़न के बीच कॉन्फ्लिक्ट से बचने के लिए, आप एक वर्चुअल एनवायरनमेंट बना सकते हैं:

```bash
python3.11 -m venv myenv
source myenv/bin/activate
```
अब, वर्चुअल एनवायरनमेंट के अंदर `pip`, Python 3.11 का उपयोग करेगा।

---

### **सारांश तालिका**

| कमांड | उद्देश्य |
|---------|---------|
| `sudo apt update` | पैकेज लिस्ट अपडेट करें |
| `sudo apt install python3.11` | Python 3.11 इंस्टॉल करें |
| `python3.11 -m ensurepip --upgrade` | Python 3.11 के लिए pip इंस्टॉल करें |
| `pip3.11 --version` | pip इंस्टॉलेशन वेरीफाई करें |
| `python3.11 -m venv myenv` | एक वर्चुअल एनवायरनमेंट बनाएं |

---