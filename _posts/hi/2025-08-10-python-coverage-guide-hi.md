---
audio: false
generated: true
image: false
lang: hi
layout: post
title: पायथन कवरेज गाइड के मूल तत्व
translated: true
type: note
---

यहाँ **coverage** (coverage.py) पैकेज का एक व्यावहारिक, डेवलपर-केंद्रित परिचय दिया गया है—यह क्या मापता है, इसे अच्छी तरह से कैसे उपयोग करें, और वे मुख्य सेटिंग्स जिनकी आपको वास्तव में आवश्यकता होगी।

# coverage.py क्या है

* एक पायथन टूल जो **मापता है कि टेस्ट या किसी भी एक्सेक्यूशन के दौरान आपके कोड की कौन सी लाइनें और ब्रांचेस चलीं**।
* **टेक्स्ट, HTML, XML, और JSON** रिपोर्ट्स जनरेट करता है ताकि आप कमियाँ देख सकें और इसे CI क्वालिटी गेट्स में इंटीग्रेट कर सकें।
* unittest, pytest, nose, या साधारण स्क्रिप्ट्स के साथ काम करता है।

# मुख्य अवधारणाएँ (सरल भाषा में)

* **लाइन कवरेज**: क्या कोई लाइन कम से कम एक बार चली?
* **ब्रांच कवरेज**: क्या निर्णय (decision) की हर संभव शाखा (ब्रांच) चली? (if/else, बूलियन शॉर्ट-सर्किट, एक्सेप्शन्स, कॉम्प्रिहेंशन्स, आदि)
* **सोर्स चयन**: केवल अपने कोड को मापें ताकि venv/site-packages के शोर से बचा जा सके।
* **डेटा संग्रहण**: रन एक `.coverage` (SQLite) डेटा फाइल बनाते हैं; आप कई रन्स को मर्ज कर सकते हैं।
* **कॉन्टेक्स्ट्स**: एक्सेक्यूशन को लेबल्स के साथ टैग करें (जैसे, प्रति टेस्ट), ताकि आप रिपोर्ट्स को टेस्ट नामों, कमांड्स आदि के आधार पर देख सकें।

# क्विक स्टार्ट

```bash
# 1) इंस्टॉल करें
pip install coverage

# 2) कवरेज के तहत अपने टेस्ट चलाएँ (pytest सिर्फ एक उदाहरण है)
coverage run -m pytest

# 3) एक टर्मिनल रिपोर्ट देखें (गायब लाइन नंबरों के साथ)
coverage report -m

# 4) HTML जनरेट करें (ब्राउज़र में htmlcov/index.html खोलें)
coverage html

# वैकल्पिक: मशीन-रीडेबल रिपोर्ट्स
coverage xml        # CI टूल्स जैसे Sonar, Jenkins, Azure DevOps के लिए
coverage json       # स्क्रिप्टेड एनालिसिस के लिए
```

# अनुशंसित .coveragerc

अपने रेपो रूट पर एक कॉन्फ़िग बनाएँ ताकि रिजल्ट्स लोकल और CI में एक जैसे रहें।

```ini
[run]
# शोर कम रखने के लिए केवल अपने पैकेजेस को मापें
source = src, your_package
branch = True
parallel = True                 # एक से ज़्यादा प्रोसेस/रन को अपना डेटा लिखने की अनुमति दें
relative_files = True           # रिपोर्ट्स में साफ़ पाथ (CI-फ्रेंडली)
concurrency = thread, multiprocessing

# आप फाइल्स या पैटर्न्स को पूरी तरह से बाहर भी कर सकते हैं
omit =
    */tests/*
    */.venv/*
    */site-packages/*
    */migrations/*

[report]
show_missing = True
skip_covered = False            # True सेट करें अगर आपको छोटी रिपोर्ट चाहिए
fail_under = 90                 # CI को फेल कर दे अगर कवरेज 90% से नीचे है
exclude_lines =
    pragma: no cover            # लाइन्स को इग्नोर करने के लिए स्टैंडर्ड प्राग्मा
    if TYPE_CHECKING:
    raise NotImplementedError

[html]
directory = htmlcov
title = Coverage Report

[xml]
output = coverage.xml

[json]
output = coverage.json

[paths]
# अलग-अलग मशीनों/कंटेनर्स से डेटा कॉम्बाइन करते समय उपयोगी
source =
    src
    */workspace/src
    */checkouts/your_repo/src
```

# सबप्रोसेसेस और पैरेलल रन मापना

अगर आपका कोड सबप्रोसेसेस स्पॉन करता है (मल्टीप्रोसेसिंग, CLI टूल्स), तो **सबप्रोसेस कवरेज** सेट अप करें:

1. `[run]` में, `parallel = True` रखें।
2. एक एनवायरनमेंट वेरिएबल एक्सपोर्ट करें ताकि सबप्रोसेसेस ऑटो-स्टार्ट हों उसी कॉन्फ़िग के साथ:

```bash
export COVERAGE_PROCESS_START=$(pwd)/.coveragerc
```

3. अपना प्रोग्राम/टेस्ट नॉर्मली चलाएँ (या फिर भी `coverage run -m ...` के ज़रिए)।
4. सभी रन खत्म होने के बाद, डेटा मर्ज करें और रिपोर्ट बनाएँ:

```bash
coverage combine
coverage report -m
```

> टिप: `concurrency = multiprocessing, thread, gevent, eventlet, greenlet` कवरेज को अलग-अलग एसिंक्रोनस मॉडल्स में हुक करने देता है।

# ब्रांच कवरेज और प्राग्मास

* `[run]` में `branch = True` इनेबल करें। यह छूटे हुए `else` ब्लॉक्स, शॉर्ट-सर्किट्स, एक्सेप्शन पाथ्स, आदि को पकड़ता है।
* अनटेस्टेबल लाइन्स को ट्रेलिंग कमेंट के साथ इग्नोर करें:

  * `# pragma: no cover` — उस लाइन को कवरेज से बाहर कर देता है।
  * ट्रिकी ब्रांचेस के लिए, प्राग्मास का ज़्यादा इस्तेमाल करने के बजाय कोड को रिफैक्टर करें।

# कॉन्टेक्स्ट्स (कवरेज को टेस्ट या टास्क के हिसाब से स्लाइस करें)

कॉन्टेक्स्ट्स एक्सेक्यूट की गई लाइन्स से लेबल्स जोड़ते हैं ताकि आप यह जवाब दे सकें: "यह कोड कौन से टेस्ट्स कवर करते हैं?"

* Pytest के साथ सबसे आसान:

  * `.coveragerc` में `dynamic_context = test_function` ऐड करें।
  * फिर `coverage html --show-contexts` चलाएँ या प्रति-कॉन्टेक्स्ट डेटा इंस्पेक्ट करें यह देखने के लिए कि कौन सा टेस्ट किस लाइन को छूता है।
* आप `dynamic_context = test` (टेस्ट nodeid) भी सेट कर सकते हैं या कस्टम रनर्स में env के ज़रिए `dynacontext` सेट कर सकते हैं।

# Pytest इंटीग्रेशन

दो कॉमन पैटर्न:

**A. नेटिव coverage CLI (सरल और फास्ट)**

```bash
coverage run -m pytest -q
coverage report -m
```

**B. pytest-cov प्लगइन (CLI में अतिरिक्त सुविधाएँ जोड़ता है)**

```bash
pip install pytest-cov
pytest --cov=your_package --cov-branch --cov-report=term-missing --cov-report=html
```

दोनों ही अंततः coverage.py का इस्तेमाल करते हैं; जो भी आपकी टीम की कन्वेंशन्स से मेल खाता हो, उसे इस्तेमाल करें।

# टिपिकल CI वायरिंग (GitHub Actions स्केच)

```yaml
- name: Install
  run: pip install -U pip coverage pytest

- name: Test with coverage
  run: |
    coverage run -m pytest -q
    coverage report -m
    coverage xml
- name: Enforce threshold
  run: coverage report --fail-under=90
- name: Upload HTML
  if: always()
  uses: actions/upload-artifact@v4
  with:
    name: htmlcov
    path: htmlcov/
```

# कॉमन पिटफॉल्स और फिक्सेस

* **बहुत बड़ी/धीमी रिपोर्ट्स**: `source=` को रिस्ट्रिक्ट करें और venv, टेस्ट्स, जनरेटेड कोड को स्किप करने के लिए `omit=` का इस्तेमाल करें।
* **CI बनाम लोकल पर अलग-अलग पाथ**: `[paths]` सेक्शन ऐड करें ताकि `coverage combine` डेटासेट्स को मर्ज कर सके।
* **सबप्रोसेसेस नहीं मापे जा रहे**: `COVERAGE_PROCESS_START` सेट करें और `parallel = True` रखें, फिर `coverage combine` चलाएँ।
* **Async फ्रेमवर्क्स**: `concurrency = ...` में रिलेवेंट एंट्री ऐड करें।
* **C एक्सटेंशन्स**: coverage.py पायथन को मापता है, नेटिव कोड को नहीं—पायथन बाउंड्री के आसपास हार्नेस टेस्ट्स लिखें।
* **अनरीचेबल कोड पर फॉल्स नेगेटिव्स**: `# pragma: no cover` से मार्क करें, लेकिन बिहेवियर को टेस्टेबल बनाने के लिए रिफैक्टर करने पर विचार करें।

# हैंडी कमांड्स जिनका आप वास्तव में इस्तेमाल करेंगे

```bash
coverage erase                       # पिछला डेटा साफ़ करें
coverage run -m pytest               # डेटा कलेक्ट करें
coverage report -m                   # टेक्स्ट सारांश गायब लाइन्स के साथ
coverage html                        # htmlcov/index.html खोलें
coverage xml                         # CI पार्सर्स
coverage json                        # स्क्रिप्ट्स/ऑटोमेशन
coverage combine                     # पैरेलल/सबप्रोसेस डेटा मर्ज करें
coverage annotate                    # प्रति-लाइन .py, दिखाता है कि कौन सी लाइनें चलीं
```

# ट्यूनिंग कब रोकें

एक **मायने रखने वाली थ्रेशोल्ड** (जैसे, 80–95%) का लक्ष्य रखें, इसे `fail_under` के साथ एनफोर्स करें, और रिव्यूज़ को **डिफ कवरेज** (क्या नई/बदली हुई लाइन्स टेस्ट की गई हैं?) पर फोकस करें। उस कोड पर 100% का पीछा न करें जिसे टेस्ट करना मुश्किल है (फीचर फ्लैग्स, डिफेंसिव गार्ड्स)—प्राग्मास का कम इस्तेमाल करें और सरल, टेस्टेबल डिज़ाइन को प्राथमिकता दें।

अगर आप चाहें, तो मैं एक मिनिमल उदाहरण रेपो लेआउट जनरेट कर सकता हूँ जिसमें एक रेडी-टू-रन `.coveragerc`, pytest कॉन्फ़िग, और एक फेलिंग थ्रेशोल्ड गेट हो, जिसे आप अपने प्रोजेक्ट्स में ड्रॉप कर सकते हैं।