---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: पायथन एक्सएमएल पार्सिंग xml.etree के साथ
translated: true
type: note
---

### Python में xml.etree का अवलोकन

`xml.etree` एक अंतर्निहित Python मॉड्यूल (विशेष रूप से `xml.etree.ElementTree`) है जो XML डेटा को पार्स और मैनिपुलेट करने के लिए है। यह एक ट्री-जैसी संरचना प्रदान करता है जहाँ आप XML एलिमेंट्स को कुशलतापूर्वक पढ़, लिख, संशोधित और नेविगेट कर सकते हैं। यह हल्का है और इसके लिए बाहरी लाइब्रेरीज़ की आवश्यकता नहीं होती, जिससे यह बुनियादी XML कार्यों के लिए आदर्श बन जाता है। इसे `import xml.etree.ElementTree as ET` के साथ इम्पोर्ट करें।

### XML पार्स करना

XML को मेमोरी में लोड करने के लिए, पार्सिंग मेथड्स का उपयोग करें:

- **स्ट्रिंग से**: `ET.fromstring(xml_string)` एक एलिमेंट ऑब्जेक्ट लौटाता है जो रूट को रिप्रेजेंट करता है।
- **फ़ाइल से**: `ET.parse(filename)` एक ElementTree ऑब्जेक्ट लौटाता है, जिसे आप `.getroot()` के माध्यम से एक्सेस कर सकते हैं।

```python
import xml.etree.ElementTree as ET

# स्ट्रिंग से पार्स करें
xml_data = "<root><child>text</child></root>"
root = ET.fromstring(xml_data)

# फ़ाइल से पार्स करें
tree = ET.parse('example.xml')
root = tree.getroot()
```

### एलिमेंट्स को नेविगेट करना

एक बार पार्स हो जाने के बाद, आप XML ट्री को ट्रैवर्स कर सकते हैं:

- **चिल्ड्रन तक पहुँच**: इंडेक्स्ड एक्सेस के लिए `root[0]` का उपयोग करें या `for child in root:` के साथ इटरेट करें।
- **एलिमेंट्स ढूँढें**:
  - `root.find('tag')` पहला मिलान वाला चाइल्ड प्राप्त करता है।
  - `root.findall('tag')` सभी मिलान वाले चिल्ड्रन प्राप्त करता है।
- **टेक्स्ट और एट्रिब्यूट्स तक पहुँच**:
  - टेक्स्ट कंटेंट: `element.text`
  - एट्रिब्यूट्स: `element.attrib` (एक डिक्शनरी)

```python
# उदाहरण XML: <bookstore><book id="1"><title>Python</title></book></bookstore>
for book in root.findall('book'):
    title = book.find('title').text
    book_id = book.attrib['id']
    print(f"Book {book_id}: {title}")
```

### XML को संशोधित करना

एलिमेंट्स को डायनामिक रूप से एडिट करें:

- **एलिमेंट्स जोड़ें**: `ET.SubElement(parent, 'new_tag')` एक नया चाइल्ड बनाता है और अटैच करता है।
- **टेक्स्ट/एट्रिब्यूट्स सेट करें**: `element.text = 'new text'`; `element.set('attr', 'value')`।
- **एलिमेंट्स हटाएँ**: `root.remove(child)`।

```python
new_child = ET.SubElement(root, 'new_element')
new_child.text = 'Added content'
new_child.set('attr', 'value')
```

### XML लिखना

संशोधनों को वापस XML में सेव करने के लिए:

- **स्ट्रिंग में**: `ET.tostring(root, encoding='unicode')`।
- **फ़ाइल में**: `tree.write('output.xml')`।

```python
xml_output = ET.tostring(root, encoding='unicode')
with open('output.xml', 'w') as f:
    f.write(xml_output)

# या सीधे
tree.write('output.xml')
```

### संपूर्ण उदाहरण

यहाँ XML को पार्स, संशोधित और लिखने के लिए एक पूर्ण स्क्रिप्ट है:

```python
import xml.etree.ElementTree as ET

# इनपुट XML स्ट्रिंग
xml_str = """<library>
  <book id="1"><title>1984</title><author>Orwell</author></book>
</library>"""

root = ET.fromstring(xml_str)

# एक नई किताब जोड़ें
new_book = ET.SubElement(root, 'book', id="2")
ET.SubElement(new_book, 'title').text = 'Brave New World'
ET.SubElement(new_book, 'author').text = 'Huxley'

# सभी किताबें प्रिंट करें
for book in root:
    title = book.find('title').text
    author = book.find('author').text
    print(f"{title} by {author}")

# फ़ाइल में लिखें
ET.tostring(root, encoding='unicode')
# या root.write('library.xml')
```

### नोट्स
- नेमस्पेस को `find` क्वेरीज़ में `xmlns='{namespace}'` के साथ हैंडल करें, उदा., `root.find('{http://example.com}tag')`।
- बड़ी फ़ाइलों के लिए, `ET.iterparse()` के साथ इटरेटिव पार्सिंग पर विचार करें।
- XML vulnerabilities जैसे इंजेक्शन से बचने के लिए यूजर-इनपुट XML के साथ सावधान रहें।
- जटिल आवश्यकताओं के लिए, lxml जैसी लाइब्रेरीज़ एक्सटेंडेड फीचर्स ऑफर करती हैं।