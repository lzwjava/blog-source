---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: नेटवर्कएक्स और मैटप्लॉटलिब ग्राफ़ ट्यूटोरियल
translated: true
type: note
---

### लाइब्रेरी इंस्टॉल करना

डायग्राम बनाने के लिए NetworkX और Matplotlib का उपयोग करने हेतु, यदि आवश्यक हो तो उन्हें इंस्टॉल करें:

- **NetworkX**: ग्राफ बनाने और उसमें हेरफेर करने का काम करती है।
- **Matplotlib**: प्लॉटिंग क्षमताएँ प्रदान करती है।

pip के माध्यम से इंस्टॉल करें:
```bash
pip install networkx matplotlib
```

तेज़ रेंडरिंग के लिए, Matplotlib NumPy इंस्टॉल करने की सलाह देती है (`pip install numpy`)।

### बेसिक सेटअप और उदाहरण

1. **लाइब्रेरीज़ इम्पोर्ट करें**:
   ```python
   import networkx as nx
   import matplotlib.pyplot as plt
   ```

2. **एक ग्राफ बनाएँ**:
   एक साधारण अनडायरेक्टेड ग्राफ बनाने के लिए NetworkX का उपयोग करें (आप इसे डायरेक्टेड ग्राफ, वेटेड एज आदि के साथ कस्टमाइज़ कर सकते हैं):
   ```python
   G = nx.Graph()  # एक खाली ग्राफ बनाएँ
   G.add_nodes_from([1, 2, 3, 4, 5])  # नोड जोड़ें (उदाहरण के लिए, 5 नोड)
   G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])  # एज जोड़ें (कनेक्शन)
   ```

3. **डायग्राम बनाएँ और दिखाएँ**:
   विज़ुअलाइज़ेशन के लिए Matplotlib के बैकएंड का उपयोग करें:
   ```python
   nx.draw(G, with_labels=True)  # नोड लेबल्स के साथ ग्राफ बनाएँ
   plt.show()  # प्लॉट डिस्प्ले करें
   ```

यह ग्राफ का एक बेसिक सर्कुलर लेआउट बनाता है (5 नोड्स वाला एक साइकिल)।

### एडवांस्ड कस्टमाइज़ेशन

- **लेआउट्स**: नोड की पोजीशन को नियंत्रित करें (जैसे, रैंडम, स्प्रिंग लेआउट):
  ```python
  pos = nx.spring_layout(G)  # यथार्थवादी नेटवर्क के लिए फोर्स-डायरेक्टेड लेआउट
  nx.draw(G, pos=pos, with_labels=True, node_color='lightblue', edge_color='gray')
  plt.title("Network Diagram")
  plt.show()
  ```
- **नोड और एज स्टाइल्स**: दिखावट को कस्टमाइज़ करें:
  ```python
  nx.draw(G, pos=pos, node_size=500, node_color='red', edge_width=2, font_size=10)
  ```
- **डायरेक्टेड ग्राफ**: हायरार्किकल रिलेशनशिप के लिए, `nx.DiGraph` का उपयोग करें।
  ```python
  DG = nx.DiGraph()
  DG.add_edges_from([('A', 'B'), ('B', 'C')])
  nx.draw(DG, with_labels=True, arrows=True)
  plt.show()
  ```
- **डायग्राम सेव करना**: डिस्प्ले करने के बजाय फाइल में एक्सपोर्ट करें:
  ```python
  plt.savefig('diagram.png')
  ```

### टिप्स और रिसोर्सेज

- ग्राफ प्रकार जैसे ट्री या ग्रिड के लिए NetworkX डॉक्स (networkx.org) देखें।
- GUI या सबप्लॉट में एम्बेड करने के लिए Matplotlib डॉक्स (matplotlib.org) देखें।
- बड़े ग्राफ (>100 नोड्स) के लिए, बेहतर परफॉर्मेंस हेतु `nx.draw_networkx` या Graphviz जैसे एक्सटर्नल टूल्स का उपयोग करें।
- इंटरएक्टिव प्लॉटिंग के लिए Jupyter नोटबुक में एक्सपेरिमेंट करें। यदि कोई समस्या आती है, तो आम त्रुटियाँ मिसिंग बैकएंड से उत्पन्न होती हैं (इंटरएक्टिव विंडोज़ के लिए `pip install pyqt5` या इसी तरह के पैकेज इंस्टॉल करें)।