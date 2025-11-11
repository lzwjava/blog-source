---
audio: false
generated: true
lang: hi
layout: post
title: जावा निर्भरताओं का विश्लेषण करें
translated: true
type: note
---

आपके प्रश्न के समाधान के लिए, मैं प्रदान किए गए Python स्क्रिप्ट को संशोधित करूंगा ताकि यह Java कक्षाओं के लिए एक निर्भरता ग्राफ उत्पन्न कर सके, जहां निर्भरताओं को पैकेज पदानुक्रम के एक निर्दिष्ट "स्तर" द्वारा समूहीकृत किया जाता है। उदाहरण के लिए, यदि `स्तर=1`, तो पैकेज शीर्ष स्तर पर समूहीकृत होते हैं (जैसे, "org"), और यदि `स्तर=2`, तो वे दूसरे स्तर पर समूहीकृत होते हैं (जैसे, "org.springframework")। इसका मतलब है कि निर्भरताओं का विश्लेषण करने से पहले, हम उनके पैकेज नामों के पहले `स्तर` भागों के आधार पर कक्षाओं को समूहों में संचित करते हैं, और ग्राफ अलग-अलग कक्षाओं के बजाय इन समूहों के बीच की निर्भरताओं को दिखाएगा।

नीचे संशोधित स्क्रिप्ट दी गई है, उसके बाद परिवर्तनों की व्याख्या और यह कैसे आपकी आवश्यकताओं को पूरा करती है।

### संशोधित स्क्रिप्ट

```python
import os
import sys
import re
from collections import defaultdict

def get_package(file_path):
    """
    .java फ़ाइल से पैकेज नाम निकालें।

    Args:
        file_path (str): .java फ़ाइल का पथ।

    Returns:
        str: पैकेज नाम, या None यदि नहीं मिला।
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*package\s+([\w.]+);', line)
                if match:
                    return match.group(1)
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}")
    return None

def get_specific_imports(file_path):
    """
    .java फ़ाइल से विशिष्ट कक्षा आयात निकालें, वाइल्डकार्ड आयातों को छोड़कर।

    Args:
        file_path (str): .java फ़ाइल का पथ।

    Returns:
        list: पूर्णतः योग्य आयातित कक्षा नामों की सूची।
    """
    imports = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*import\s+([\w.]+);', line)
                if match:
                    imp = match.group(1)
                    # वाइल्डकार्ड आयातों को छोड़ें (जैसे, import java.util.*;)
                    if not imp.endswith('.*'):
                        imports.append(imp)
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}")
    return imports

def get_package_group(full_class_name, level):
    """
    पैकेज नाम के पहले 'स्तर' भागों के आधार पर पैकेज समूह प्राप्त करें।

    Args:
        full_class_name (str): पूर्णतः योग्य कक्षा नाम (जैसे, "org.springframework.boot.App")।
        level (int): शामिल करने के लिए पैकेज स्तरों की संख्या (जैसे, 1 के लिए "org", 2 के लिए "org.springframework")।

    Returns:
        str: पैकेज समूह (जैसे, "org" या "org.springframework")।
    """
    package = '.'.join(full_class_name.split('.')[:-1])  # कक्षा नाम को छोड़कर पैकेज निकालें
    parts = package.split('.')
    if len(parts) <= level:
        return package  # पूर्ण पैकेज का उपयोग करें यदि इसके भाग स्तर से कम या बराबर हैं
    else:
        return '.'.join(parts[:level])  # पहले 'स्तर' भागों का उपयोग करें

if __name__ == '__main__':
    # कमांड-लाइन तर्कों के लिए जांच: root_directory और level
    if len(sys.argv) != 3:
        print("Usage: python script.py <root_directory> <level>")
        sys.exit(1)

    root_dir = sys.argv[1]
    try:
        level = int(sys.argv[2])
        if level < 1:
            raise ValueError
    except ValueError:
        print("Error: level must be a positive integer")
        sys.exit(1)

    all_classes = set()

    # प्रथम पास: प्रोजेक्ट में सभी पूर्णतः योग्य कक्षा नाम एकत्रित करें
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    all_classes.add(full_class_name)

    # पैकेज समूहों के बीच निर्भरताएं संग्रहीत करें
    group_dependencies = set()

    # द्वितीय पास: पैकेज समूहों के आधार पर निर्भरताओं का विश्लेषण करें
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    importer_group = get_package_group(full_class_name, level)
                    imports = get_specific_imports(file_path)
                    for imp in imports:
                        # केवल प्रोजेक्ट के भीतर की कक्षाओं पर निर्भरताएं शामिल करें
                        # स्व-निर्भरताओं को छोड़ें
                        if imp in all_classes and imp != full_class_name:
                            imported_group = get_package_group(imp, level)
                            if imported_group != importer_group:
                                group_dependencies.add((importer_group, imported_group))

    # DOT प्रारूप में निर्भरता ग्राफ आउटपुट करें
    print('digraph G {')
    for from_group, to_group in sorted(group_dependencies):
        print(f'  "{from_group}" -> "{to_group}";')
    print('}')
```

### परिवर्तनों की व्याख्या

1. **कमांड-लाइन तर्क**:
   - **मूल**: `python script.py <root_directory>`
   - **संशोधित**: `python script.py <root_directory> <level>`
   - दूसरे तर्क, `level`, के लिए समर्थन जोड़ा गया, जो पैकेज पदानुक्रम स्तर निर्दिष्ट करता है। स्क्रिप्ट जांचती है कि ठीक दो तर्क प्रदान किए गए हैं और `level` एक धनात्मक पूर्णांक है।

2. **नया फ़ंक्शन: `get_package_group`**:
   - निर्दिष्ट `level` के आधार पर कक्षा के लिए पैकेज समूह की गणना करने के लिए एक फ़ंक्शन जोड़ा गया।
   - एक पूर्णतः योग्य कक्षा नाम (जैसे, "org.springframework.boot.App") के लिए, यह पैकेज ("org.springframework.boot") निकालता है, इसे भागों ("org", "springframework", "boot") में विभाजित करता है, और पहले `level` भाग लेता है:
     - यदि `level=1`: "org" लौटाता है।
     - यदि `level=2`: "org.springframework" लौटाता है।
     - यदि पैकेज में `level` से कम भाग हैं (जैसे, `level=3` के साथ "com.example"), तो यह पूर्ण पैकेज ("com.example") लौटाता है।

3. **निर्भरता समूहीकरण**:
   - **मूल**: अलग-अलग कक्षाओं के बीच निर्भरताएं संग्रहीत करने के लिए `defaultdict(set)` का उपयोग किया गया।
   - **संशोधित**: पैकेज समूहों के बीच निर्देशित किनारों को टुपल्स `(from_group, to_group)` के रूप में संग्रहीत करने के लिए एक `set` (`group_dependencies`) का उपयोग करता है।
   - प्रत्येक कक्षा के लिए:
     - `get_package_group` का उपयोग करके इसके पैकेज समूह (`importer_group`) की गणना करता है।
     - प्रत्येक विशिष्ट आयात के लिए जो प्रोजेक्ट के भीतर है (`imp in all_classes`) और स्वयं कक्षा नहीं है (`imp != full_class_name`):
       - आयातित कक्षा के पैकेज समूह (`imported_group`) की गणना करता है।
       - यदि समूह भिन्न हैं (`imported_group != importer_group`), तो `group_dependencies` में एक किनारा जोड़ता है।
   - `set` विशिष्टता सुनिश्चित करता है, इसलिए एक ही समूहों के बीच कई निर्भरताएं एक ही किनारे में परिणत होती हैं।

4. **DOT आउटपुट**:
   - **मूल**: अलग-अलग कक्षाओं के बीच किनारे प्रिंट करता था (जैसे, "org.springframework.boot.App" -> "org.apache.commons.IOUtils")।
   - **संशोधित**: पैकेज समूहों के बीच किनारे प्रिंट करता है (जैसे, `level=2` के लिए "org.springframework" -> "org.apache")।
   - सुसंगत आउटपुट के लिए किनारों को क्रमबद्ध किया जाता है।

### यह आपकी आवश्यकताओं को कैसे पूरा करता है

- **स्तरों के लिए समर्थन**: स्क्रिप्ट अब निर्भरताओं का विश्लेषण करने से पहले पैकेजों को समूहीकृत करने के लिए एक `level` पैरामीटर स्वीकार करती है।
- **स्तर = 1**: सभी कक्षाओं को उनके शीर्ष-स्तरीय पैकेज (जैसे, "org") द्वारा समूहीकृत करता है। उदाहरण के लिए, "org.springframework.boot.App" और "org.apache.commons.IOUtils" दोनों "org" समूह से संबंधित हैं, इसलिए "org" के भीतर उनके बीच आयात किनारे के रूप में नहीं दिखाए जाते।
- **स्तर = 2**: कक्षाओं को पहले दो पैकेज स्तरों (जैसे, "org.springframework") द्वारा समूहीकृत करता है। उदाहरण के लिए, "org.springframework.boot.App" से "org.apache.commons.IOUtils" का आयात "org.springframework" से "org.apache" तक एक किनारा बनाता है।
- **निर्भरता विश्लेषण से पहले पैकेज संचित करना**: स्क्रिप्ट निर्भरताओं का विश्लेषण करने से पहले `level` के आधार पर प्रत्येक कक्षा के पैकेज समूह का निर्धारण करती है, यह सुनिश्चित करते हुए कि निर्भरताएं समूहों के बीच हैं, न कि अलग-अलग कक्षाओं के बीच।
- **उदाहरण अनुपालन**: आपके उदाहरण किनारे के लिए:
  - मूल: `"org.springframework.boot.web.servlet.server.Session" -> "org.springframework.boot.convert.DurationUnit"`
  - `level=2` के साथ: दोनों कक्षाएं "org.springframework" में हैं, इसलिए कोई किनारा नहीं जोड़ा जाता (समान समूह)।
  - `level=3` के साथ: "org.springframework.boot.web" -> "org.springframework.boot.convert", इन विशिष्ट समूहों के बीच एक किनारा जोड़ता है।

### उपयोग उदाहरण

- **कमांड**: `python script.py /path/to/project 1`
  - समूह: "org", "com", आदि।
  - आउटपुट में शामिल हो सकता है: `"org" -> "com"` यदि "org" पैकेज में एक कक्षा "com" पैकेज में एक कक्षा आयात करती है।

- **कमांड**: `python script.py /path/to/project 2`
  - समूह: "org.springframework", "org.apache", आदि।
  - आउटपुट में शामिल हो सकता है: `"org.springframework" -> "org.apache"`।

### नोट्स

- स्क्रिप्ट केवल प्रोजेक्ट-आंतरिक निर्भरताओं (`all_classes` के भीतर आयात) को शामिल करने और वाइल्डकार्ड आयातों और स्व-निर्भरताओं को छोड़ने के मूल व्यवहार को बनाए रखती है।
- बिना पैकेज घोषणा वाली कक्षाओं को छोड़ दिया जाता है, जो मूल स्क्रिप्ट के अनुरूप है।
- आउटपुट DOT प्रारूप में एक निर्देशित ग्राफ है, जिसे Graphviz जैसे टूल्स के साथ देखा जा सकता है।

यह संशोधित स्क्रिप्ट पैकेज स्तर पदानुक्रम द्वारा निर्भरताओं को समूहीकृत करने के आपके अनुरोध को पूरी तरह से संतुष्ट करनी चाहिए।