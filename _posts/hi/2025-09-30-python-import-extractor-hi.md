---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: पायथन पैकेज आयात निष्कर्षक
translated: true
type: note
---

### सभी आयातित पैकेज निकालने के लिए पायथन स्क्रिप्ट

यह स्क्रिप्ट एक निर्दिष्ट डायरेक्टरी और उसकी उप-डायरेक्टरीज़ में चलती है, सभी पायथन फाइलें (`.py`) ढूंढती है, और पायथन के `ast` मॉड्यूल का उपयोग करके उनके आयात स्टेटमेंट्स को पार्स करती है (सुरक्षित, सिंटैक्स-अवेयर पार्सिंग के लिए), और सभी अद्वितीय बेस मॉड्यूल नाम एकत्र करती है (जैसे, `import os` से `os`, या `from collections import defaultdict` से `collections`)। यह बिल्ट-इन मॉड्यूल्स को नज़रअंदाज करती है और बाहरी मॉड्यूल्स पर ध्यान केंद्रित करती है।

इसे एक `.py` फाइल के रूप में सेव करें (जैसे, `extract_imports.py`) और इसे एक डायरेक्टरी पथ के साथ आर्ग्युमेंट के रूप में चलाएं, जैसे `python extract_imports.py /path/to/directory`.

```python
import os
import ast
import sys

def extract_imports_from_file(file_path):
    """
    Parses a Python file and extracts imported module names.
    Handles 'import mod' and 'from mod import item' styles.
    """
    modules = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read(), filename=file_path)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    modules.add(alias.name.split('.')[0])  # Get base module (e.g., 'import os.path' -> 'os')
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules.add(node.module.split('.')[0])  # Get base module from 'from mod.sub import ...'
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
    
    return modules

def get_all_imported_modules(directory):
    """
    Walks through the directory and subdirectories, collects all unique imported modules.
    """
    all_modules = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                modules = extract_imports_from_file(file_path)
                all_modules.update(modules)
    
    # Exclude common builtins (optional, as they are rarely external packages)
    excluded = {'sys', 'os', 're', 'math', 'random', 'json', 'time', 'datetime', 'collections', 'itertools', 'functools'}
    all_modules -= excluded
    
    return sorted(all_modules)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_imports.py <directory_path>")
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)
    
    modules = get_all_imported_modules(directory)
    print("All unique imported packages:")
    for mod in modules:
        print(mod)
```

### यह कैसे काम करती है
- **डायरेक्टरी ट्रैवर्सल**: सभी उप-डायरेक्टरीज़ और फाइलों को रिकर्सिवली विज़िट करने के लिए `os.walk` का उपयोग करती है।
- **फाइल फिल्टरिंग**: केवल `.py` फाइलों को प्रोसेस करती है।
- **आयात पार्सिंग**: सोर्स कोड को सुरक्षित रूप से पार्स करने और `Import` और `ImportFrom` नोड्स की पहचान करने के लिए `ast` का उपयोग करती है। टॉप-लेवल मॉड्यूल (जैसे `import numpy.linalg` से `numpy`) को कैप्चर करने के लिए `.` पर स्प्लिट करती है।
- **एकत्रीकरण**: विशिष्टता के लिए मॉड्यूल्स को एक सेट में एकत्र करती है, फिर उन्हें सॉर्ट और प्रिंट करती है।
- **एज केस**: बिल्ट-इन मॉड्यूल्स को स्किप करती है (आप `excluded` सेट को कस्टमाइज़ कर सकते हैं), सिंटैक्स एरर्स को सहजता से हैंडल करती है, और यूनिकोड फाइलों को सपोर्ट करती है।
- **आउटपुट**: अद्वितीय पैकेज नामों की एक सॉर्टेड सूची। यदि आप इसे अपनी खुद की प्रोजेक्ट डायरेक्टरी पर चलाते हैं, तो यह `requests`, `pandas` आदि जैसे पैकेजों को सूचीबद्ध करेगी, जिन्हें आपको इंस्टॉल करने की आवश्यकता होगी।

यह दृष्टिकोण कोडबेस विश्लेषण के लिए कुशल है और संभावित असुरक्षित कोड को एक्सेक्यूट करने से बचाता है। यदि आपको सुधार की आवश्यकता है (जैसे, रिलेटिव आयात को अलग तरह से हैंडल करना या एक requirements.txt जनरेट करना), अधिक विवरण प्रदान करें!