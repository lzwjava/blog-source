---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: पायथन पैकेजिंग गाइड पीईपी ५१७
translated: true
type: note
---

PEP 517, जिसे 2016 में स्वीकार किया गया था, Python पैकेज बनाने के लिए एक मानकीकृत इंटरफेस को परिभाषित करता है जो बिल्ड बैकएंड (डिस्ट्रीब्यूशन बनाने का तर्क) को फ्रंटएंड (pip जैसे टूल जो प्रक्रिया को ऑर्केस्ट्रेट करते हैं) से अलग करता है। यह डेवलपर्स को पुराने सिस्टम जैसे कि setuptools के `setup.py` में लॉक हुए बिना आधुनिक बिल्ड टूल्स का उपयोग करने की अनुमति देता है। PEP 518 (जो बिल्ड निर्भरताओं को निर्दिष्ट करता है) के साथ संयुक्त, यह स्रोत ट्री या स्रोत डिस्ट्रीब्यूशन (sdists) से विश्वसनीय, अलग-थलग बिल्ड सक्षम करता है। 2025 तक, PEP 517 आधुनिक Python पैकेजिंग की आधारशिला है, जिसे pip (PEP 518 के लिए संस्करण 10 और पूर्ण PEP 517 के लिए 19 के बाद से) और Poetry, Flit, और PDM जैसे टूल्स द्वारा समर्थित किया जाता है।

यह गाइड प्रेरणा, मुख्य अवधारणाओं, विशिष्टता, वर्कफ़्लो, कार्यान्वयन और सर्वोत्तम प्रथाओं को कवर करती है।

## प्रेरणा और पृष्ठभूमि

Python पैकेजिंग `distutils` (Python 1.6, 2000 में पेश) से `setuptools` (2004) में विकसित हुई, जिसने निर्भरता प्रबंधन जोड़ा लेकिन समस्याएं पैदा कीं:
- **अनिवार्य और नाजुक**: बिल्ड `python setup.py` नामक एक मनमाना स्क्रिप्ट को निष्पादित करने पर निर्भर थे, जो पर्यावरणीय धारणाओं (जैसे, एक्सटेंशन के लिए गुम Cython) के कारण विफल हो सकते थे।
- **कोई बिल्ड निर्भरताएं नहीं**: बिल्डिंग के लिए आवश्यक टूल (जैसे, कंपाइलर, Cython) घोषित नहीं किए गए थे, जिससे मैन्युअल इंस्टॉलेशन और संस्करण संघर्ष होते थे।
- **कड़ा जुड़ाव**: Pip ने `setup.py` इनवोकेशन को हार्डकोड किया, जिससे Flit या Bento जैसे वैकल्पिक बिल्ड सिस्टम अवरुद्ध हो गए।
- **होस्ट एनवायरनमेंट प्रदूषण**: बिल्ड उपयोगकर्ता के वैश्विक Python वातावरण का उपयोग करते थे, जिससे साइड इफेक्ट का जोखिम रहता था।

इन समस्याओं ने नवाचार को रोका और स्रोत इंस्टॉल (जैसे, Git से) के दौरान त्रुटियाँ पैदा कीं। PEP 517 इसे एक न्यूनतम इंटरफेस को मानकीकृत करके हल करता है: फ्रंटएंड अलग-थलग वातावरण में बैकएंड हुक को कॉल करते हैं। व्हील (पूर्व-निर्मित बाइनरी, 2014 में पेश) वितरण को सरल बनाते हैं—बैकएंड्स केवल अनुपालन व्हील/sdists का उत्पादन करते हैं। PEP 518 `pyproject.toml` में बिल्ड आवश्यकताओं को घोषित करके, अलगाव को सक्षम करके इसका पूरक है।

परिणाम: एक घोषणात्मक, विस्तार योग्य पारिस्थितिकी तंत्र जहां `setup.py` वैकल्पिक है, और pip जैसे टूल बिना लीगेसी फॉलबैक के किसी भी अनुपालन परियोजना का निर्माण कर सकते हैं।

## मुख्य अवधारणाएँ

### स्रोत ट्री और डिस्ट्रीब्यूशन
- **स्रोत ट्री**: एक निर्देशिका (जैसे, VCS चेकआउट) जिसमें पैकेज कोड और `pyproject.toml` होता है। `pip install .` जैसे टूल इससे बनाते हैं।
- **स्रोत डिस्ट्रीब्यूशन (Sdist)**: एक gzipped tarball (`.tar.gz`) जैसे `package-1.0.tar.gz`, जो `pyproject.toml` और मेटाडेटा (PKG-INFO) के साथ एक `{name}-{version}` निर्देशिका में अनपैक होता है। इसका उपयोग रिलीज़ और डाउनस्ट्रीम पैकेजिंग (जैसे, Debian) के लिए किया जाता है।
- **व्हील**: एक `.whl` बाइनरी डिस्ट्रीब्यूशन—पूर्व-निर्मित, प्लेटफ़ॉर्म-विशिष्ट, और संकलन के बिना इंस्टॉल करने योग्य। PEP 517 पुनरुत्पादनशीलता के लिए व्हील को अनिवार्य करता है।

लीगेसी sdists (PEP 517 से पहले) निष्पादन योग्य ट्री में अनपैक होते हैं लेकिन अनुपालन के लिए अब `pyproject.toml` शामिल करना होगा।

### pyproject.toml
यह TOML फ़ाइल कॉन्फ़िगरेशन को केंद्रीकृत करती है। `[build-system]` सेक्शन (PEP 518/517 से) निर्दिष्ट करता है:
- `requires`: बिल्ड के लिए PEP 508 निर्भरताओं की सूची (जैसे, `["setuptools>=40.8.0", "wheel"]`)।
- `build-backend`: बैकएंड का एंट्री पॉइंट (जैसे, `"setuptools.build_meta"` या `"poetry.masonry.api"`)।
- `backend-path` (वैकल्पिक): सेल्फ-होस्टेड बैकएंड के लिए `sys.path` में जोड़े गए इन-ट्री पाथ (जैसे, `["src/backend"]`)।

उदाहरण न्यूनतम कॉन्फ़िग:
```
[build-system]
requires = ["setuptools>=40.8.0", "wheel"]
build-backend = "setuptools.build_meta"
```

आवश्यकताएं एक DAG बनाती हैं (कोई चक्र नहीं; फ्रंटएंड पता लगाते हैं और विफल होते हैं)। अन्य सेक्शन जैसे `[project]` (PEP 621) या `[tool.poetry]` मेटाडेटा/निर्भरताएं रखते हैं।

### बिल्ड बैकएंड और फ्रंटएंड
- **बैकएंड**: हुक (कॉल करने योग्य फ़ंक्शन) के माध्यम से बिल्ड लॉजिक लागू करता है। अलगाव के लिए एक सबप्रोसेस में चलता है।
- **फ्रंटएंड**: ऑर्केस्ट्रेट करता है (जैसे, pip)। अलगाव सेट करता है, आवश्यकताएं इंस्टॉल करता है, हुक को कॉल करता है।
- **डिकपलिंग**: फ्रंटएंड मानकीकृत हुक को कॉल करते हैं, `setup.py` को नहीं। यह pip परिवर्तनों के बिना विविध बैकएंड का समर्थन करता है।

हुक `config_settings` (फ्लैग्स के लिए dict, जैसे `{"--debug": true}`) का उपयोग करते हैं और stdout/stderr (UTF-8) पर आउटपुट दे सकते हैं।

## विशिष्टता

### [build-system] विवरण
- `requires`: PEP 508 स्ट्रिंग्स (जैसे, `">=1.0; sys_platform == 'win32'"`)।
- `build-backend`: `module:object` (जैसे, `flit_core.buildapi` `flit_core` को इम्पोर्ट करता है; `backend = flit_core.buildapi`)।
- कोई sys.path प्रदूषण नहीं—बैकएंड अलगाव के माध्यम से इम्पोर्ट करते हैं।

### हुक
बैकएंड इन्हें विशेषताओं के रूप में एक्सपोज़ करते हैं:

**अनिवार्य:**
- `build_wheel(wheel_directory, config_settings=None, metadata_directory=None) -> str`: `wheel_directory` में व्हील बनाता है, बेसनेम लौटाता है (जैसे, `"myproj-1.0-py3-none-any.whl"`)। प्रदान किए गए prior मेटाडेटा का उपयोग करता है। टेम्प के माध्यम से रीड-ओनली स्रोतों को हैंडल करता है।
- `build_sdist(sdist_directory, config_settings=None) -> str`: `sdist_directory` में sdist बनाता है (pax फॉर्मेट, UTF-8)। असंभव होने पर `UnsupportedOperation` उठाता है (जैसे, कोई VCS नहीं)।

**वैकल्पिक (डिफ़ॉल्ट `[]` या फॉलबैक):**
- `get_requires_for_build_wheel(config_settings=None) -> list[str]`: अतिरिक्त व्हील निर्भरताएं (जैसे, `["cython"]`)।
- `prepare_metadata_for_build_wheel(metadata_directory, config_settings=None) -> str`: `{pkg}-{ver}.dist-info` मेटाडेटा (व्हील स्पेक के अनुसार, कोई RECORD नहीं) लिखता है। बेसनेम लौटाता है; फ्रंटएंड गुम होने पर व्हील से निकालते हैं।
- `get_requires_for_build_sdist(config_settings=None) -> list[str]`: अतिरिक्त sdist निर्भरताएं।

हुक त्रुटियों के लिए एक्सेप्शन उठाते हैं। फ्रंटएंड अलग-थलग एनव में कॉल करते हैं (जैसे, केवल stdlib + आवश्यकताओं के साथ venv)।

### बिल्ड एनवायरनमेंट
- अलग-थलग venv: `get_requires_*` के लिए बूटस्ट्रैप, बिल्ड के लिए पूर्ण।
- CLI टूल (जैसे, `flit`) PATH में।
- कोई stdin नहीं; हुक प्रति सबप्रोसेस।

## बिल्ड प्रक्रिया कैसे काम करती है

### चरण-दर-चरण वर्कफ़्लो
`pip install .` (स्रोत ट्री) या sdist इंस्टॉल के लिए:

1.  **डिस्कवरी**: फ्रंटएंड `pyproject.toml` पढ़ता है।
2.  **अलगाव सेटअप**: venv बनाएं; `requires` इंस्टॉल करें।
3.  **आवश्यकताएं क्वेरी**: `get_requires_for_build_wheel` को कॉल करें (एक्स्ट्रा इंस्टॉल करें)।
4.  **मेटाडेटा प्रिप**: `prepare_metadata_for_build_wheel` को कॉल करें (या व्हील बनाएं और निकालें)।
5.  **व्हील बिल्ड**: अलग-थलग एनव में `build_wheel` को कॉल करें; परिणामी व्हील इंस्टॉल करें।
6.  **फॉलबैक**: यदि sdist असमर्थित है, तो व्हील बनाएं; यदि कोई हुक नहीं है, तो लीगेसी `setup.py`।

Sdists के लिए: अनपैक करें, स्रोत ट्री के रूप में व्यवहार करें। डेवलपर वर्कफ़्लो (जैसे, `pip wheel .`):
1.  एनव को अलग करें।
2.  व्हील/sdist के लिए बैकएंड हुक को कॉल करें।

### बिल्ड आइसोलेशन (PEP 518)
बिल्ड के लिए अस्थायी venv बनाता है, होस्ट प्रदूषण से बचता है। Pip का `--no-build-isolation` अक्षम करता है (सावधानी से उपयोग करें)। tox जैसे टूल डिफ़ॉल्ट रूप से अलगाव का उपयोग करते हैं।

पुराना बनाम नया:
-   **पुराना**: होस्ट एनव में `python setup.py install`—संघर्ष का जोखिम।
-   **नया**: अलग-थलग हुक—पुनरुत्पादनशील, सुरक्षित।

## एक बिल्ड बैकएंड लागू करना

एक बनाने के लिए:
1.  हुक के साथ एक मॉड्यूल परिभाषित करें (जैसे, `mybackend.py`)।
2.  `build-backend` को इसकी ओर इशारा करें।

न्यूनतम उदाहरण (शुद्ध Python पैकेज):
```python
# mybackend.py
from zipfile import ZipFile
import os
from pathlib import Path

def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    # स्रोत को व्हील डिर में कॉपी करें, .whl के रूप में ज़िप करें
    dist = Path(wheel_directory) / "myproj-1.0-py3-none-any.whl"
    with ZipFile(dist, 'w') as z:
        for src in Path('.').rglob('*'):
            z.write(src, src.relative_to('.'))
    return str(dist.relative_to(wheel_directory))

# वैकल्पिक हुक
def get_requires_for_build_wheel(config_settings=None):
    return []

def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    # METADATA, आदि लिखें।
    return "myproj-1.0.dist-info"
```

`pyproject.toml` में:
```
[build-system]
requires = []
build-backend = "mybackend:build_wheel"  # वास्तव में मॉड्यूल ऑब्जेक्ट की ओर इशारा करता है
```

बॉयलरप्लेट के लिए `pyproject-hooks` जैसी लाइब्रेरीज़ का उपयोग करें। एक्सटेंशन के लिए, `config_settings` के माध्यम से C कंपाइलर को एकीकृत करें।

## टूल्स के साथ PEP 517 का उपयोग करना

-   **pip**: `pyproject.toml` को स्वचालित रूप से पहचानता है; `--use-pep517` का उपयोग करें (19.1 के बाद से डिफ़ॉल्ट)। संपादन योग्य के लिए: `pip install -e .` हुक को कॉल करता है।
-   **Poetry**: घोषणात्मक टूल। उत्पन्न करता है:
    ```
    [build-system]
    requires = ["poetry-core>=1.0.0"]
    build-backend = "poetry.core.masonry.api"
    ```
    `poetry build` के माध्यम से इंस्टॉल करता है; pip-संगत।
-   **Flit**: शुद्ध Python के लिए सरल। उपयोग करता है:
    ```
    [build-system]
    requires = ["flit_core >=3.2,<4"]
    build-backend = "flit_core.buildapi"
    ```
    `flit publish` बनाता है/अपलोड करता है।
-   **Setuptools**: लीगेसी ब्रिज:
    ```
    [build-system]
    requires = ["setuptools>=40.8.0", "wheel"]
    build-backend = "setuptools.build_meta"
    ```
    घोषणात्मक मेटाडेटा के लिए `setup.cfg` का समर्थन करता है।

लीगेसी माइग्रेट करें: `[build-system]` जोड़ें; `setup.py` कॉल हटाएं।

## त्रुटि हैंडलिंग और सर्वोत्तम प्रथाएं

-   **त्रुटियाँ**: हुक उठाते हैं (जैसे, अमान्य कॉन्फ़िग के लिए `ValueError`)। चक्र: फ्रंटएंड संदेश के साथ विफल। असमर्थित sdist: व्हील पर फॉलबैक।
-   **सर्वोत्तम प्रथाएं**:
    -   घोषणात्मक (`setup.cfg` या `[project]`) को प्राथमिकता दें।
    -   सटीक बिल्ड निर्भरताएं घोषित करें (जैसे, `cython==0.29`)।
    -   अलगाव का परीक्षण करें: डीबगिंग के लिए `pip wheel . --no-build-isolation`।
    -   इन-ट्री बैकएंड के लिए: `backend-path` का उपयोग करें; चक्रों से बचें।
    -   सुरक्षा: सबप्रोसेस में हुक; कोई मनमाना कोड नहीं।
    -   संगतता: पुराने टूल के लिए `setup.py` शामिल करें।

2025 तक, setuptools हावी है (सर्वेक्षणों के अनुसार), लेकिन सरलता के लिए Poetry/Flit का अपनाना बढ़ रहा है।

## संदर्भ
-   [PEP 517 – A build-system independent format for source trees](https://peps.python.org/pep-0517/)
-   [PEP 517 and 518 in Plain English](https://chadsmith-software.medium.com/pep-517-and-518-in-plain-english-47208ca8b7a6)
-   [Python packaging - Past, Present, Future](https://bernat.tech/posts/pep-517-518/)
-   [What is PEP 517/518 compatibility?](https://pydevtools.com/handbook/explanation/what-is-pep-517/)
-   [Modern pip build process (–use-pep517)](https://fromkk.com/posts/modern-pip-build-process-use-pep517/)
-   [What is a build backend?](https://pydevtools.com/handbook/explanation/what-is-a-build-backend/)