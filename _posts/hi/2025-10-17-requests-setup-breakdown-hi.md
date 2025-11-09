---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: अनुरोध सेटअप.पीवाई फ़ाइल विवरण
translated: true
type: note
---

### अवलोकन
यह एक `setup.py` फ़ाइल है, जो एक मानक Python स्क्रिप्ट है जिसका उपयोग `setuptools` के साथ किसी Python पैकेज को परिभाषित और बनाने के लिए किया जाता है। विशेष रूप से, यह **Requests** लाइब्रेरी के लिए है—Python के लिए एक लोकप्रिय HTTP क्लाइंट। यह मेटाडेटा को संभालती है जैसे पैकेज का नाम, संस्करण, निर्भरताएँ और वर्गीकरण (PyPI वितरण के लिए)। जब आप `pip install requests` चलाते हैं, तो यह स्क्रिप्ट (या इसके बिल्ट आर्टिफैक्ट्स) ही है जो पैकेज इंस्टॉल करने के लिए पर्दे के पीछे निष्पादित होती है।

यह स्क्रिप्ट एक एकल `setup()` फ़ंक्शन कॉल के रूप में संरचित है, लेकिन इसमें कुछ गार्ड, हेल्पर्स और अन्य फ़ाइलों से डायनामिक रीड शामिल हैं। मैं इसे अनुभाग दर अनुभाग समझाऊंगा।

### 1. इम्पोर्ट्स और Python वर्जन चेक
```python
#!/usr/bin/env python
import os
import sys
from codecs import open

from setuptools import setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 9)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    # एरर मैसेज और एक्जिट
    sys.exit(1)
```
- **शेबैंग (`#!/usr/bin/env python`)**: यूनिक्स-जैसी सिस्टम्स पर फ़ाइल को एक्जिक्यूटेबल बनाता है, इसे सिस्टम के Python इंटरप्रेटर के साथ चलाता है।
- **इम्पोर्ट्स**: `os` और `sys` को सिस्टम इंटरैक्शन के लिए, `codecs.open` को UTF-8 फ़ाइल रीडिंग के लिए (गैर-ASCII को सुरक्षित रूप से हैंडल करने के लिए), और `setuptools` से `setup` को पैकेज बनाने के लिए लाता है।
- **वर्जन चेक**: यह सुनिश्चित करता है कि उपयोगकर्ता Python 3.9 या उससे ऊपर चला रहा है। यदि नहीं, तो यह एक उपयोगी एरर मैसेज प्रिंट करता है जो अपग्रेड करने या Requests के पुराने वर्जन (<2.32.0) का उपयोग जारी रखने का सुझाव देता है, फिर कोड 1 (फेल्योर) के साथ एक्जिट हो जाता है। यह कम्पैटिबिलिटी को लागू करता है, क्योंकि Requests ने पुराने Python वर्जन के लिए सपोर्ट हटा दिया है।

### 2. पब्लिश शॉर्टकट
```python
if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()
```
- मेंटेनर्स के लिए एक सुविधा: यदि आप `python setup.py publish` चलाते हैं, तो यह:
  - `dist/` फोल्डर में सोर्स डिस्ट्रीब्यूशन (`sdist`) और व्हील (`bdist_wheel`) आर्काइव बनाता है।
  - उन्हें `twine` (एक सिक्योर अपलोडर) का उपयोग करके PyPI पर अपलोड करता है।
- यह मैन्युअल कमांड्स के बिना नया वर्जन रिलीज़ करने का एक त्वरित तरीका है। यह चलने के बाद एक्जिट हो जाता है।

### 3. निर्भरताएँ
```python
requires = [
    "charset_normalizer>=2,<4",
    "idna>=2.5,<4",
    "urllib3>=1.21.1,<3",
    "certifi>=2017.4.17",
]
test_requirements = [
    "pytest-httpbin==2.1.0",
    "pytest-cov",
    "pytest-mock",
    "pytest-xdist",
    "PySocks>=1.5.6, !=1.5.7",
    "pytest>=3",
]
```
- **`requires`**: कोर निर्भरताएँ जो `pip install requests` चलाने पर इंस्टॉल होती हैं। ये एन्कोडिंग (`charset_normalizer`), इंटरनेशनलाइज्ड डोमेन नेम्स (`idna`), HTTP ट्रांसपोर्ट (`urllib3`), और SSL सर्टिफिकेट्स (`certifi`) को संभालती हैं।
- **`test_requirements`**: केवल तब इंस्टॉल होती हैं जब आप टेस्ट चलाते हैं (जैसे, `pip install -e '.[tests]'` के माध्यम से)। इसमें टेस्टिंग टूल्स शामिल हैं जैसे HTTP मॉकिंग, कवरेज और पैरेलल टेस्टिंग के लिए `pytest` वेरिएंट। `PySocks` टेस्ट्स में SOCKS प्रॉक्सी सपोर्ट के लिए है।

### 4. डायनामिक मेटाडेटा लोडिंग
```python
about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "src", "requests", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)

with open("README.md", "r", "utf-8") as f:
    readme = f.read()
```
- **`about` डिक्शनरी**: `exec()` का उपयोग करके `src/requests/__version__.py` (जैसे, `__title__`, `__version__`, `__description__`, आदि) से मेटाडेटा पढ़ता है। यह वर्जन जानकारी को केंद्रीकृत रखता है—इसे एक बार अपडेट करें, और `setup.py` इसे अंदर खींच लेता है।
- **`readme`**: PyPI पर पैकेज के लंबे विवरण के रूप में पूरी `README.md` फ़ाइल को एक स्ट्रिंग के रूप में लोड करता है।

### 5. मुख्य `setup()` कॉल
यह फ़ाइल का दिल है। यह पैकेज को बिल्ड/इंस्टॉलेशन के लिए कॉन्फ़िगर करता है:
```python
setup(
    name=about["__title__"],  # उदा., "requests"
    version=about["__version__"],  # उदा., "2.32.3"
    description=about["__description__"],  # संक्षिप्त सारांश
    long_description=readme,  # पूरा README
    long_description_content_type="text/markdown",  # PyPI पर मार्कडाउन के रूप में रेंडर होता है
    author=about["__author__"],  # उदा., "Kenneth Reitz"
    author_email=about["__author_email__"],
    url=about["__url__"],  # उदा., GitHub रेपो
    packages=["requests"],  # 'requests' पैकेज इंस्टॉल करता है
    package_data={"": ["LICENSE", "NOTICE"]},  # गैर-Python फ़ाइलें शामिल करता है
    package_dir={"": "src"},  # सोर्स कोड 'src/' में है
    include_package_data=True,  # सभी डेटा फ़ाइलों को अंदर खींचता है
    python_requires=">=3.9",  # वर्जन चेक को दोहराता है
    install_requires=requires,  # पहले से
    license=about["__license__"],  # उदा., "Apache 2.0"
    zip_safe=False,  # इंस्टॉल की गई फ़ाइलों को एडिट करने की अनुमति देता है (लाइब्स के लिए आम)
    classifiers=[  # खोजने में आसानी के लिए PyPI श्रेणियाँ
        "Development Status :: 5 - Production/Stable",
        # ... (पूरी सूची में Python वर्जन, OS, विषय शामिल हैं)
    ],
    tests_require=test_requirements,  # `pip install -e '.[tests]'` के लिए
    extras_require={  # वैकल्पिक निर्भरताएँ
        "security": [],  # खाली—शायद भविष्य के उपयोग के लिए
        "socks": ["PySocks>=1.5.6, !=1.5.7"],  # SOCKS प्रॉक्सी सपोर्ट
        "use_chardet_on_py3": ["chardet>=3.0.2,<6"],  # लेगेसी कैरेक्टर सेट फॉलबैक
    },
    project_urls={  # PyPI पेज पर लिंक्स
        "Documentation": "https://requests.readthedocs.io",
        "Source": "https://github.com/psf/requests",
    },
)
```
- **मुख्य आर्ग्युमेंट्स**:
  - **नाम/वर्जन/विवरण**: आसान मेंटेनेंस के लिए `__version__.py` से लिए गए हैं।
  - **पैकेजेस/पैकेज डिर**: setuptools को बताता है कि पैकेज `src/requests/` के अंदर है और इसे `import requests` के रूप में इंस्टॉल करना है।
  - **क्लासिफायर्स**: स्ट्रिंग्स की एक सूची जो पैकेज को वर्गीकृत करती है (जैसे, स्टेबल, Python 3.9+, Apache लाइसेंस, वेब/HTTP विषय)। यह उपयोगकर्ताओं को इसे PyPI पर खोजने में मदद करती है।
  - **एक्स्ट्रास रिक्वायर**: उपयोगकर्ताओं को वैकल्पिक फीचर्स इंस्टॉल करने देता है, जैसे `pip install requests[socks]` प्रॉक्सी सपोर्ट के लिए।
  - **प्रोजेक्ट URLs**: PyPI पेज पर डॉक्स और सोर्स के क्लिक करने योग्य लिंक जोड़ता है।

### व्यवहार में यह कैसे काम करता है
- **इंस्टॉलेशन**: `pip install .` (रेपो से) या `pip install requests` (PyPI से) फ़ाइलों को कॉपी करने, निर्भरताएँ इंस्टॉल करने और पैकेज सेटअप करने के लिए इसे चलाता है।
- **बिल्डिंग**: `python setup.py sdist` वितरण योग्य आर्काइव बनाता है।
- **यह संरचना क्यों?** यह एक "src लेआउट" (कोड `src/` में) है, जो डेवलपमेंट के दौरान आकस्मिक इम्पोर्ट्स से बचने के लिए एक आधुनिक बेस्ट प्रैक्टिस है। फ़ाइल स्वयं-निहित है लेकिन विवरणों को `__version__.py` जैसी अन्य फ़ाइलों को सौंपती है।

यह setup.py आधिकारिक Requests रेपो से है और वर्षों में ज्यादा नहीं बदली है—यह विश्वसनीयता के लिए परखी हुई है।

### संदर्भ
- [Requests डॉक्यूमेंटेशन](https://requests.readthedocs.io/en/latest/)
- [Requests GitHub रिपॉजिटरी](https://github.com/psf/requests)
- [Python पैकेजिंग यूजर गाइड](https://packaging.python.org/en/latest/tutorials/packaging-projects/)