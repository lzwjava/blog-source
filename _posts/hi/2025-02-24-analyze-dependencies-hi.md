---
audio: false
lang: hi
layout: post
title: Java Dependencies का विश्लेषण
translated: true
---

आपके प्रश्न को संबोधित करने के लिए, मैं दिए गए Python स्क्रिप्ट को Java क्लासों के लिए एक निर्भरता ग्राफ बनाने के लिए संशोधित करूँगा, जहां निर्भरताएं एक निर्दिष्ट "स्तर" के पैकेज हायरार्की द्वारा समूहित होती हैं। उदाहरण के लिए, अगर `स्तर=1`, तो पैकेज टॉप स्तर पर समूहित होते हैं (उदाहरण के लिए, "org"), और अगर `स्तर=2`, तो वे दूसरे स्तर पर समूहित होते हैं (उदाहरण के लिए, "org.springframework"). यह अर्थ है कि निर्भरताओं का विश्लेषण करने से पहले, हम क्लासों को उनके पैकेज नामों के पहले `स्तर` हिस्सों के आधार पर समूहों में एकत्रित करते हैं, और ग्राफ इन समूहों के बीच निर्भरताओं को दिखाएगा, न कि व्यक्तिगत क्लासों के बीच।

नीचे संशोधित स्क्रिप्ट है, इसके बाद संशोधनों और यह आपके आवश्यकताओं को कैसे पूरा करता है, के बारे में एक व्याख्या है।

### संशोधित स्क्रिप्ट

```python
import os
import sys
import re
from collections import defaultdict

def get_package(file_path):
    """
    एक .java फ़ाइल से पैकेज नाम निकालें।

    Args:
        file_path (str): .java फ़ाइल का पथ।

    Returns:
        str: पैकेज नाम, या अगर नहीं मिला तो None.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*package\s+([\w.]+);', line)
                if match:
                    return match.group(1)
    except Exception as e:
        print(f"चेतावनी: {file_path} पढ़ा नहीं जा सका: {e}")
    return None

def get_specific_imports(file_path):
    """
    एक .java फ़ाइल से विशेष क्लास इम्पोर्ट निकालें, वाइल्डकार्ड इम्पोर्ट को छोड़कर।

    Args:
        file_path (str): .java फ़ाइल का पथ।

    Returns:
        list: पूर्ण रूप से योग्य इम्पोर्ट किए गए क्लास नामों की सूची।
    """
    imports = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*import\s+([\w.]+);', line)
                if match:
                    imp = match.group(1)
                    # वाइल्डकार्ड इम्पोर्ट (उदाहरण के लिए, import java.util.*;) को छोड़ें
                    if not imp.endswith('.*'):
                        imports.append(imp)
    except Exception as e:
        print(f"चेतावनी: {file_path} पढ़ा नहीं जा सका: {e}")
    return imports

def get_package_group(full_class_name, level):
    """
    पैकेज समूह को प्राप्त करें, पैकेज नाम के पहले 'स्तर' हिस्सों के आधार पर।

    Args:
        full_class_name (str): पूर्ण रूप से योग्य क्लास नाम (उदाहरण के लिए, "org.springframework.boot.App").
        level (int): पैकेज स्तरों की संख्या जो शामिल करनी है (उदाहरण के लिए, 1 के लिए "org", 2 के लिए "org.springframework").

    Returns:
        str: पैकेज समूह (उदाहरण के लिए, "org" या "org.springframework").
    """
    package = '.'.join(full_class_name.split('.')[:-1])  # पैकेज निकालें, क्लास नाम को छोड़कर
    parts = package.split('.')
    if len(parts) <= level:
        return package  # पैकेज का उपयोग करें अगर इसमें स्तरों से कम या बराबर हिस्से हैं
    else:
        return '.'.join(parts[:level])  # पहले 'स्तर' हिस्सों का उपयोग करें

if __name__ == '__main__':
    # कमांड-लाइन तर्कों की जांच करें: root_directory और स्तर
    if len(sys.argv) != 3:
        print("उपयोग: python script.py <root_directory> <स्तर>")
        sys.exit(1)

    root_dir = sys.argv[1]
    try:
        level = int(sys.argv[2])
        if level < 1:
            raise ValueError
    except ValueError:
        print("त्रुटि: स्तर एक धनात्मक पूर्णांक होना चाहिए")
        sys.exit(1)

    all_classes = set()

    # पहला पास: प्रोजेक्ट में सभी पूर्ण रूप से योग्य क्लास नामों को एकत्र करें
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    all_classes.add(full_class_name)

    # पैकेज समूहों के बीच निर्भरताओं को स्टोर करें
    group_dependencies = set()

    # दूसरा पास: पैकेज समूहों के आधार पर निर्भरताओं का विश्लेषण करें
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
                        # केवल प्रोजेक्ट के भीतर क्लासों पर निर्भरताओं को शामिल करें
                        # स्वयं निर्भरताओं को छोड़ें
                        if imp in all_classes and imp != full_class_name:
                            imported_group = get_package_group(imp, level)
                            if imported_group != importer_group:
                                group_dependencies.add((importer_group, imported_group))

    # निर्भरता ग्राफ को DOT प्रारूप में आउटपुट करें
    print('digraph G {')
    for from_group, to_group in sorted(group_dependencies):
        print(f'  "{from_group}" -> "{to_group}";')
    print('}')
```

### संशोधनों की व्याख्या

1. **कमांड-लाइन तर्क**:
   - **मूल**: `python script.py <root_directory>`
   - **संशोधित**: `python script.py <root_directory> <स्तर>`
   - एक दूसरे तर्क, `स्तर`, जो पैकेज हायरार्की स्तर को निर्दिष्ट करता है, के लिए समर्थन जोड़ा गया है। स्क्रिप्ट यह सुनिश्चित करता है कि ठीक दो तर्क दिए गए हैं और `स्तर` एक धनात्मक पूर्णांक है।

2. **नया फंक्शन: `get_package_group`**:
   - एक फंक्शन जो एक क्लास के लिए पैकेज समूह को संशोधित `स्तर` के आधार पर कंप्यूट करता है, जोड़ा गया है।
   - एक पूर्ण रूप से योग्य क्लास नाम (उदाहरण के लिए, "org.springframework.boot.App") के लिए, यह पैकेज ("org.springframework.boot") निकालता है, इसे हिस्सों में विभाजित करता है ("org", "springframework", "boot"), और पहले `स्तर` हिस्सों को लेता है:
     - अगर `स्तर=1`: "org" लौटाता है।
     - अगर `स्तर=2`: "org.springframework" लौटाता है।
     - अगर पैकेज में स्तरों से कम हिस्से हैं (उदाहरण के लिए, "com.example" के साथ `स्तर=3`), तो यह पूर्ण पैकेज ("com.example") लौटाता है।

3. **निर्भरता समूहण**:
   - **मूल**: `defaultdict(set)` का उपयोग करके व्यक्तिगत क्लासों के बीच निर्भरताओं को स्टोर किया गया था।
   - **संशोधित**: एक `set` (`group_dependencies`) का उपयोग करके पैकेज समूहों के बीच निर्देशित एजेस को ट्यूपल के रूप में स्टोर करता है `(from_group, to_group)`.
   - प्रत्येक क्लास के लिए:
     - `get_package_group` का उपयोग करके इसका पैकेज समूह (`importer_group`) कंप्यूट करता है।
     - प्रत्येक विशेष इम्पोर्ट जो प्रोजेक्ट के भीतर है (`imp in all_classes`) और क्लास खुद नहीं है (`imp != full_class_name`):
       - इम्पोर्ट किए गए क्लास का पैकेज समूह (`imported_group`) कंप्यूट करता है।
       - अगर समूह अलग हैं (`imported_group != importer_group`), तो एक एज `group_dependencies` में जोड़ता है।
   - `set` एकता सुनिश्चित करता है, इसलिए समान समूहों के बीच कई निर्भरताएं एक एज में परिणामित होती हैं।

4. **DOT आउटपुट**:
   - **मूल**: व्यक्तिगत क्लासों के बीच एजेस (उदाहरण के लिए, "org.springframework.boot.App" -> "org.apache.commons.IOUtils") को प्रिंट किया गया था।
   - **संशोधित**: पैकेज समूहों के बीच एजेस (उदाहरण के लिए, "org.springframework" -> "org.apache" के लिए `स्तर=2`) को प्रिंट करता है।
   - एजेस को सॉर्ट किया जाता है, सुसंगत आउटपुट के लिए।

### यह आपके आवश्यकताओं को कैसे पूरा करता है

- **स्तरों का समर्थन**: स्क्रिप्ट अब एक `स्तर` पैरामीटर स्वीकार करता है, जो पैकेज हायरार्की स्तर के आधार पर पैकेजों को समूहित करने के लिए है।
- **स्तर = 1**: सभी क्लासों को उनके टॉप-स्तर पैकेज (उदाहरण के लिए, "org") द्वारा समूहित करता है। उदाहरण के लिए, "org.springframework.boot.App" और "org.apache.commons.IOUtils" दोनों "org" समूह में हैं, इसलिए उनके बीच "org" के भीतर इम्पोर्ट्स को एजेस के रूप में नहीं दिखाया जाता है।
- **स्तर = 2**: क्लासों को पहले दो पैकेज स्तरों (उदाहरण के लिए, "org.springframework") द्वारा समूहित करता है। उदाहरण के लिए, "org.springframework.boot.App" से "org.apache.commons.IOUtils" तक का एक इम्पोर्ट "org.springframework" से "org.apache" तक का एक एज बनाता है।
- **निर्भरताओं का विश्लेषण से पहले पैकेजों को एकत्रित करें**: स्क्रिप्ट प्रत्येक क्लास के पैकेज समूह को `स्तर` के आधार पर निर्धारित करता है, निर्भरताओं का विश्लेषण करने से पहले, सुनिश्चित करता है कि निर्भरताएं समूहों के बीच हैं, न कि व्यक्तिगत क्लासों के बीच।
- **उदाहरण अनुपालन**: आपके उदाहरण एज के लिए:
  - मूल: `"org.springframework.boot.web.servlet.server.Session" -> "org.springframework.boot.convert.DurationUnit"`
  - `स्तर=2` के साथ: दोनों क्लास "org.springframework" में हैं, इसलिए कोई एज जोड़ा नहीं जाता है (समान समूह).
  - `स्तर=3` के साथ: "org.springframework.boot.web" -> "org.springframework.boot.convert", इन अलग-अलग समूहों के बीच एक एज जोड़ता है।

### उपयोग उदाहरण

- **कमांड**: `python script.py /path/to/project 1`
  - समूह: "org", "com", आदि।
  - आउटपुट में शामिल हो सकता है: `"org" -> "com"` अगर एक "org" पैकेज में एक क्लास एक "com" पैकेज में एक क्लास को इम्पोर्ट करता है।

- **कमांड**: `python script.py /path/to/project 2`
  - समूह: "org.springframework", "org.apache", आदि।
  - आउटपुट में शामिल हो सकता है: `"org.springframework" -> "org.apache"` अगर एक "org.springframework" पैकेज में एक क्लास एक "org.apache" पैकेज में एक क्लास को इम्पोर्ट करता है।

### नोट्स

- स्क्रिप्ट मूल व्यवहार को बनाए रखता है, केवल प्रोजेक्ट के भीतर निर्भरताओं (`all_classes` के भीतर इम्पोर्ट) को शामिल करता है और वाइल्डकार्ड इम्पोर्ट और स्वयं निर्भरताओं को छोड़ देता है।
- पैकेज घोषणा के बिना क्लास को छोड़ दिया जाता है, मूल स्क्रिप्ट के साथ एकरूपता बनाए रखते हुए।
- आउटपुट एक निर्देशित ग्राफ DOT प्रारूप में है, जो Graphviz जैसे टूल्स के साथ देखे जा सकते हैं।

यह संशोधित स्क्रिप्ट आपके अनुरोध को पूरी तरह से पूरा करेगी, जो पैकेज स्तर हायरार्की के आधार पर निर्भरताओं को समूहित करने के लिए है।