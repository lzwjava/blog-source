---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: पायथन डिपेंडेंसी मैनेजमेंट विद पोएट्री
translated: true
type: note
---

### Poetry क्या है?

Poetry Python में dependency management और packaging के लिए एक टूल है। यह आपको उन लाइब्रेरीज़ को declare करने की अनुमति देता है जिन पर आपकी परियोजना निर्भर करती है, और यह उन्हें स्वचालित रूप से इंस्टॉल करने, अपडेट करने और resolve करने का काम करता है, साथ ही reproducible environments सुनिश्चित करता है।

### मुख्य उद्देश्य
Poetry एक single configuration file (`pyproject.toml`) के माध्यम से dependencies को manage करके, consistent installations के लिए एक lockfile बनाकर, और distribution (जैसे PyPI पर) के लिए परियोजनाओं के building का समर्थन करके Python project workflows को सरल बनाता है। इसे `pip`, `pipenv`, और `setuptools` जैसे fragmented tools को एक unified, user-friendly approach के साथ बदलने के लिए डिज़ाइन किया गया है।

### मुख्य विशेषताएं
- **Dependency Resolution**: Dependencies को स्वचालित रूप से इंस्टॉल और अपडेट करता है, conflicts को intelligently resolve करता है।
- **Lockfile**: Repeatable builds के लिए exact versions pin करने के लिए `poetry.lock` generate करता है।
- **Virtual Environments**: Global pollution से बचने के लिए प्रति परियोजना isolated environments बनाता है।
- **Packaging**: आसान distribution के लिए wheels या sdists बनाता है।
- **Multi-Platform Support**: Linux, macOS, और Windows पर काम करता है।
- **Shell Integration**: Bash, Fish, और Zsh के लिए tab completion।
- **Python 3.9+ Compatible**: Modern Python versions की आवश्यकता होती है।

### इंस्टॉलेशन
Poetry को एक isolated environment में `pipx` का उपयोग करके इंस्टॉल करें (conflicts के बिना global access के लिए recommended):

1. यदि आवश्यक हो तो `pipx` इंस्टॉल करें (अपने OS package manager के माध्यम से या `python -m pip install --user pipx`)।
2. रन करें: `pipx install poetry`।

अपडेट के लिए: `pipx upgrade poetry`।  
अनइंस्टॉल के लिए: `pipx uninstall poetry`।

Shell completions को सक्षम करें (उदाहरण के लिए, Bash के लिए: `poetry completions bash >> ~/.bash_completion`)।

### बेसिक उपयोग
एक नई परियोजना प्रारंभ करें: `poetry init`।  
एक dependency जोड़ें: `poetry add requests`।  
Lockfile से इंस्टॉल करें: `poetry install`।  
Scripts चलाएं: `poetry run python script.py`।  
Package बनाएं: `poetry build`।

पूरी commands के लिए, documentation देखें।

[Poetry Documentation](https://python-poetry.org/docs/)