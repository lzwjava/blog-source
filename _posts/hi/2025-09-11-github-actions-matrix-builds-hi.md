---
audio: false
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: GitHub एक्शन्स मैट्रिक्स बिल्ड गाइड
translated: true
type: note
---

ऐसा लगता है कि आप **GitHub Actions** मैट्रिक्स बिल्ड्स का उपयोग करके टेस्ट को समानांतर में चलाने और मैट्रिक्स स्ट्रैटेजी में `fail-fast` ऑप्शन का उपयोग करने के बारे में पूछ रहे हैं। मैं आपको इसे समझाता हूं।

---

### GitHub Actions में मैट्रिक्स बिल्ड्स
**मैट्रिक्स स्ट्रैटेजी** आपको एक ही जॉब को अलग-अलग पैरामीटर्स के साथ समानांतर में चलाने की सुविधा देती है—उदाहरण के लिए, कई Python या Node वर्जन पर, या अलग-अलग ऑपरेटिंग सिस्टम पर टेस्ट चलाना।

एक मिनिमल उदाहरण:

```yaml
name: CI

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, 3.10]
        os: [ubuntu-latest, windows-latest]
      fail-fast: false
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
```

---

### मुख्य बिंदु

- **`matrix`:** जॉब कॉम्बिनेशन बनाने के लिए वेरिएबल्स को डिफाइन करता है।  
  ऊपर दिया गया उदाहरण (`python-version`, `os`) के सभी कॉम्बिनेशन के लिए टेस्ट चलाता है।

- **समानांतर एक्सेक्यूशन:** मैट्रिक्स द्वारा जेनरेट की गई प्रत्येक जॉब डिफॉल्ट रूप से **समानांतर में चलती है**।

- **`fail-fast`:**
  - डिफॉल्ट `true` होता है। इसका मतलब है कि अगर एक जॉब फेल हो जाती है, तो बाकी मैट्रिक्स जॉब्स कैंसल कर दी जाती हैं।
  - अगर आप चाहते हैं कि एक जॉब के फेल होने पर भी सभी मैट्रिक्स जॉब्स चलती रहें, तो `fail-fast: false` सेट करें।

  उदाहरण:
  ```yaml
  strategy:
    matrix:
      node: [14, 16, 18]
    fail-fast: false
  ```

- **कुल जॉब्स को सीमित करना:** आप कुछ कॉम्बिनेशन को बाहर कर सकते हैं:
  ```yaml
  strategy:
    matrix:
      python-version: [3.8, 3.9, 3.10]
      os: [ubuntu-latest, windows-latest]
    exclude:
      - python-version: 3.8
        os: windows-latest
  ```

---

### समानांतर में टेस्ट चलाना
- प्रत्येक **मैट्रिक्स जॉब अपने रनर पर समानांतर में चलती है**, इसलिए आपको कुछ खास करने की जरूरत नहीं है।
- प्रत्येक जॉब के अंदर, अगर आप **समानांतर टेस्ट एक्सेक्यूशन** चाहते हैं (जैसे, pytest `-n auto`), तो आप इसे टेस्ट कमांड लेवल पर एड कर सकते हैं।

उदाहरण:
```yaml
- name: Run pytest in parallel
  run: pytest -n auto
```

---

✅ **सारांश:**
- अलग-अलग पैरामीटर कॉम्बिनेशन को डिफाइन करने के लिए `strategy.matrix` का उपयोग करें।
- अगर आप चाहते हैं कि एक जॉब के फेल होने पर भी सभी मैट्रिक्स जॉब्स चलती रहें, तो `fail-fast: false` सेट करें।
- मैट्रिक्स जॉब्स ऑटोमैटिकली समानांतर में चलती हैं।
- प्रत्येक जॉब के अंदर रनटाइम को तेज करने के लिए, टेस्ट फ्रेमवर्क की समानांतर सुविधा (जैसे pytest-xdist) का उपयोग करें।

---

क्या आप **Node/JavaScript टेस्ट चलाने** के लिए मैट्रिक्स (मल्टीपल Node वर्जन, `fail-fast: false`, `npm test` के साथ समानांतर टेस्ट) का एक रियल-वर्ल्ड उदाहरण देखना चाहेंगे?