---
audio: false
generated: true
lang: hi
layout: post
title: एक्सएमएल रेगेक्स स्क्रिप्ट
translated: true
type: note
---

मैं स्क्रिप्ट को कमांड-लाइन आर्गुमेंट्स को हैंडल करने के लिए `argparse` का उपयोग करने के लिए मॉडिफाई करूंगा। इससे आप स्क्रिप्ट को रन करते समय फ़ाइल पाथ सीधे पास कर सकेंगे:

```python
import xml.etree.ElementTree as ET
import re
import argparse

def extract_look_tags(xml_file):
    # XML फ़ाइल कंटेंट को पढ़ें
    with open(xml_file, 'r') as file:
        xml_content = file.read()
    
    # regex का उपयोग करके सभी <c:look> टैग्स ढूंढें
    pattern = r'<c:look>(\d+)</c:look>'
    matches = re.findall(pattern, xml_content)
    
    # नंबर्स प्रिंट करें
    for number in matches:
        print(number)

def main():
    # आर्गुमेंट पार्सर सेट अप करें
    parser = argparse.ArgumentParser(description='XML फ़ाइल में <c:look> टैग्स से नंबर्स एक्सट्रैक्ट करें')
    parser.add_argument('file_path', help='XML फ़ाइल का पाथ')
    
    # आर्गुमेंट्स पार्स करें
    args = parser.parse_args()
    
    # फ़ाइल प्रोसेस करें
    extract_look_tags(args.file_path)

if __name__ == "__main__":
    main()

```

अब आप स्क्रिप्ट को कमांड लाइन से इस तरह रन कर सकते हैं:

```
python script_name.py path/to/your/xml_file.xml
```

स्क्रिप्ट यह करेगी:
1. फ़ाइल पाथ के लिए कमांड-लाइन आर्गुमेंट को हैंडल करने के लिए `argparse` का उपयोग करेगी
2. सभी `<c:look>` टैग्स ढूंढने के लिए XML फ़ाइल को पार्स करेगी
3. इन टैग्स के अंदर के नंबर्स को एक्सट्रैक्ट और प्रिंट करेगी

यह तरीका स्क्रिप्ट को अधिक यूजर-फ्रेंडली और स्क्रिप्टिंग या बैच प्रोसेसिंग के लिए उपयुक्त बनाता है।