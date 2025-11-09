---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: पिप पैकेजों में निष्पादन योग्य स्क्रिप्ट्स जोड़ना
translated: true
type: note
---

### पायथन पिप पैकेज में एक्जीक्यूटेबल स्क्रिप्ट्स बनाना

पायथन पैकेज में एक्जीक्यूटेबल स्क्रिप्ट्स (यानी कमांड-लाइन टूल्स) शामिल करने के लिए जिन्हें `pip` के माध्यम से इंस्टॉल किया जा सके, आप अपने पैकेज की कॉन्फ़िगरेशन फ़ाइल में **एंट्री पॉइंट्स** परिभाषित करते हैं। इससे उपयोगकर्ता इंस्टॉलेशन के बाद आपकी स्क्रिप्ट्स को सीधे चला सकते हैं (जैसे, टर्मिनल से `my-script`)।

हम एक सरल उदाहरण का उपयोग करेंगे: `mytools` नाम का एक पैकेज जिसमें `greet` नाम की एक स्क्रिप्ट है जो एक अभिवादन प्रिंट करती है।

#### चरण 1: अपनी पैकेज संरचना सेट करें
इस प्रकार की एक डायरेक्टरी संरचना बनाएँ:

```
mytools/
├── pyproject.toml          # आधुनिक कॉन्फ़िग फ़ाइल (setup.py से अधिक अनुशंसित)
├── README.md
└── src/
    └── mytools/
        ├── __init__.py     # इसे एक पैकेज बनाता है
        └── greet.py        # आपका स्क्रिप्ट लॉजिक
```

`src/mytools/__init__.py` में (खाली या वर्जन जानकारी के साथ हो सकता है):
```python
__version__ = "0.1.0"
```

`src/mytools/greet.py` में (वह फ़ंक्शन जिसे आपकी स्क्रिप्ट कॉल करेगी):
```python
import sys

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
```

#### चरण 2: `pyproject.toml` में एंट्री पॉइंट्स कॉन्फ़िगर करें
कंसोल स्क्रिप्ट्स को परिभाषित करने के लिए `[project.scripts]` सेक्शन का उपयोग करें। यह pip को एक्जीक्यूटेबल रैपर बनाने के लिए कहता है।

```toml
[build-system]
requires = ["hatchling"]  # या "setuptools", "flit", आदि।
build-backend = "hatchling.build"

[project]
name = "mytools"
version = "0.1.0"
description = "A simple tool package"
readme = "README.md"
requires-python = ">=3.8"
dependencies = []  # अपनी डिपेंडेंसी यहाँ जोड़ें, जैसे "requests"

[project.scripts]
greet = "mytools.greet:main"  # फॉर्मेट: script_name = package.module:function
```

- `greet` वह कमांड है जिसे उपयोगकर्ता चलाएंगे (जैसे, `greet Alice`)।
- `mytools.greet:main` `greet.py` में `main()` फ़ंक्शन की ओर इशारा करता है।

यदि आप पुराने `setup.py` को प्राथमिकता देते हैं (अभी भी काम करता है लेकिन कम अनुशंसित):
```python
from setuptools import setup, find_packages

setup(
    name="mytools",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "greet = mytools.greet:main"
        ]
    },
    # ... अन्य फ़ील्ड जैसे description, install_requires
)
```

#### चरण 3: पैकेज बनाएँ और इंस्टॉल करें
1. बिल्ड टूल्स इंस्टॉल करें: `pip install build twine` (या `hatchling` अगर उस बैकएंड का उपयोग कर रहे हैं)।

2. पैकेज बनाएँ:
   ```
   python -m build
   ```
   यह `.tar.gz` और `.whl` फ़ाइलों के साथ `dist/` डायरेक्टरी बनाता है।

3. टेस्ट करने के लिए लोकली इंस्टॉल करें:
   ```
   pip install -e .  # एडिटेबल मोड (बदलाव तुरंत दिखाई देते हैं)
   ```
   या क्लीन इंस्टॉलेशन के लिए: `pip install dist/mytools-0.1.0-py3-none-any.whl`।

4. टेस्ट: अपने टर्मिनल में `greet Alice` चलाएँ। इसका आउटपुट "Hello, Alice!" होना चाहिए।

#### चरण 4: वितरित करें (वैकल्पिक)
- PyPI पर अपलोड करें: `twine upload dist/*` (PyPI अकाउंट आवश्यक)।
- उपयोगकर्ता तब `pip install mytools` कर सकते हैं और `greet` चला सकते हैं।

#### सुझाव
- **एकाधिक स्क्रिप्ट्स**: `[project.scripts]` में और लाइनें जोड़ें, जैसे, `another-script = mytools.other:main`।
- **आर्गुमेंट्स**: बेहतर CLI हैंडलिंग के लिए अपने `main()` फ़ंक्शन में `argparse` का उपयोग करें।
- **डिपेंडेंसी**: उन्हें `[project.dependencies]` में सूचीबद्ध करें (जैसे, CLI फ्रेमवर्क के लिए `click`)।
- **वर्चुअल एन्व**: कॉन्फ्लिक्ट से बचने के लिए हमेशा इसका उपयोग करें (`python -m venv env; source env/bin/activate`)।
- **त्रुटियाँ?** विवरण के लिए `pip install --verbose` चेक करें। सुनिश्चित करें कि आपका फ़ंक्शन कोई आर्गुमेंट नहीं लेता (या `sys.argv` को हैंडल करता है)।

अधिक उन्नत सेटअप (जैसे, Poetry या Flit के साथ) के लिए, आधिकारिक डॉक्स देखें।

#### संदर्भ
- [Python Packaging User Guide: Entry Points](https://packaging.python.org/en/latest/guides/writing-entry-points/)
- [PyPI: Building and Publishing](https://packaging.python.org/en/latest/tutorials/packaging-projects/)