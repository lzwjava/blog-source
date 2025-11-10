---
audio: false
generated: true
image: false
lang: hi
layout: post
title: कार्यप्रवाह आरेखों के लिए पायथन लाइब्रेरियाँ
translated: true
type: note
---

यदि आप Python लाइब्रेरीज़ की तलाश कर रहे हैं जो वर्कफ़्लो या फ़्लो ग्राफ़ बनाना आसान बनाती हैं—जैसे **maniod** जैसे टूल जो डायग्राम बनाने को सरल बनाते हैं—तो यहां कुछ उत्कृष्ट विकल्प हैं जिन्हें एक्सप्लोर करने लायक है:

---

### वर्कफ़्लो और फ़्लो डायग्राम के लिए अनुशंसित Python पैकेज

#### **1. Graphviz (Python के माध्यम से)**

* डॉट लैंग्वेज में परिभाषित ग्राफ़ बनाने के लिए एक व्यापक रूप से उपयोग होने वाला ओपन-सोर्स टूल।
* कई लेआउट स्टाइल प्रदान करता है जैसे लेयर्ड (`dot`), सर्कुलर (`circo`), रेडियल (`twopi`), और फ़ोर्स-डायरेक्टेड (`neato`, `fdp`) ([विकिपीडिया][1])।
* Python में, आप `graphviz` या `pygraphviz` रैपर का उपयोग नोड्स और एज को प्रोग्रामेटिक रूप से परिभाषित करने के लिए कर सकते हैं—DSL-स्टाइल में।

> "मैंने ऐसी चीज़ों के लिए GraphViz का उपयोग किया है। मुख्य कारण जो मुझे इसे पसंद है, वह यह है कि यह फ़्लो चार्ट बनाने के लिए GUI की बजाय एक DSL ज़्यादा है।" ([Reddit][2])

#### **2. NetworkX**

* ग्राफ़ निर्माण, विश्लेषण और Matplotlib या Graphviz लेआउट के माध्यम से विज़ुअलाइज़ेशन के लिए एक Python-नेटिव लाइब्रेरी ([विकिपीडिया][3])।
* डायरेक्टेड ग्राफ़, मल्टी-एज और विभिन्न लेआउट एल्गोरिदम जैसे स्प्रिंग-लेआउट, मल्टीपार्टाइट (लेयर्ड वर्कफ़्लो के लिए बढ़िया), सर्कुलर लेआउट आदि को सपोर्ट करता है ([विकिपीडिया][3])।
* डेटा-ड्रिवन वर्कफ़्लो डायग्राम जेनरेट करने के लिए परफेक्ट, जहां ग्राफ़ स्ट्रक्चर डायनामिक हो।

#### **3. Pyvis (VisJS के साथ)**

* आपको Python का उपयोग करके नोटबुक या वेब में इंटरैक्टिव वर्कफ़्लो विज़ुअलाइज़ेशन बनाने देता है।
* VisJS पर बना हुआ; अत्यधिक कस्टमाइज़ेबल इंटरैक्टिविटी, लेआउट फ़िज़िक्स, टूलटिप्स—एक्सप्लोरेटरी डायग्राम के लिए रिस्पॉन्सिव और यूजर-फ्रेंडली ([GitHub][4], [arXiv][5])।

#### **4. Graph-tool**

* ग्राफ़ मैनिपुलेशन और विज़ुअलाइज़ेशन के लिए एक हाई-परफॉर्मेंस Python/C++ लाइब्रेरी।
* Cairo या Graphviz के माध्यम से अच्छे एक्सपोर्ट ऑफर करती है और कॉम्प्लेक्स ग्राफ़ एल्गोरिदम को सपोर्ट करती है यदि आपको एनालिटिक प्लस विज़ुअल क्षमताओं की आवश्यकता है ([विकिपीडिया][6])।

#### **5. igraph**

* एक फास्ट, स्केलेबल ग्राफ़ लाइब्रेरी (C कोर के साथ Python इंटरफेस)।
* परफॉर्मेंस-हैवी वर्कलोड और इंटरैक्टिव प्लॉटिंग सपोर्ट के साथ लार्ज-स्केल ग्राफ़ के लिए बढ़िया ([arXiv][7])।

#### **6. pyflowsheet**

* इंजीनियरिंग संदर्भों में **प्रोसेस फ़्लो डायग्राम** के लिए तैयार।
* आपको कोड से फ़्लोशीट जेनरेट करने देता है—न्यूनतम परेशानी, प्रोसेस इंजीनियरों के लिए आदर्श ([GitHub][4])।

#### **7. Plotly Sankey Diagram**

* मात्रात्मक मात्राओं वाले फ़्लो को दर्शाने के लिए—Sankey डायग्राम चरणों के बीच फ़्लो वॉल्यूम दिखाने के लिए एरो की चौड़ाई का उपयोग करते हैं।
* उपयोगी जब आपको सिर्फ़ स्ट्रक्चर ही नहीं बल्कि चरणों के बीच फ़्लो का परिमाण भी दिखाने की आवश्यकता हो ([Plotly][8])।

---

### अन्य उल्लेखित टूल

* **Schemdraw**: सर्किट स्कीमैटिक्स के लिए तैयार, लेकिन इसमें फ़्लोचार्टिंग मॉड्यूल है। शानदार डायग्राम, लेकिन लेआउट मैन्युअल रूप से निर्दिष्ट करना होगा ([Stack Overflow][9])।
* **VisTrails**: एक UI-आधारित साइंटिफिक वर्कफ़्लो टूल (सक्रिय रूप से मेंटेन नहीं) जो पाइपलाइन को विज़ुअली मैनेज, विज़ुअलाइज़ और एक्सप्लोर करने के लिए है ([विकिपीडिया][10])।
* **PM4Py**: मनमाने वर्कफ़्लो ड्रॉ करने के बजाय **प्रोसेस माइनिंग** पर केंद्रित। इवेंट लॉग का विश्लेषण करने के बारे में ज़्यादा ([arXiv][11])।

---

आपकी पसंद में मदद के लिए एक त्वरित विवरण:

* **DSL-जैसे, स्टैटिक फ़्लोचार्ट चाहते हैं?** → **Graphviz**
* **डायनामिक/कस्टम ग्राफ़ स्ट्रक्चर चाहिए?** → **NetworkX** (+ Matplotlib या Graphviz)
* **नोटबुक/वेब में इंटरैक्टिविटी चाहते हैं?** → **Pyvis**
* **बड़े, परफॉर्मेंस-सेंसिटिव ग्राफ़ के साथ काम कर रहे हैं?** → **igraph** या **graph-tool**
* **कोड से इंजीनियरिंग-स्टाइल फ़्लोशीट चाहिए?** → **pyflowsheet**
* **चरणों के बीच मात्रात्मक फ़्लो का प्रतिनिधित्व करना है?** → **Plotly Sankey**

---

### उदाहरण स्निपेट

**Graphviz (Python)**

```python
from graphviz import Digraph

dot = Digraph()
dot.node('A', 'Start')
dot.node('B', 'Process')
dot.node('C', 'End')
dot.edge('A', 'B')
dot.edge('B', 'C')

dot.render('flowchart', view=True)
```

**NetworkX**

```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edge('A', 'B')
G.add_edge('B', 'C')

pos = nx.multipartite_layout(G, subset_key=lambda n: {'A':0,'B':1,'C':2}[n])
nx.draw(G, pos, with_labels=True, arrows=True)
plt.show()
```

**Plotly Sankey**

```python
import plotly.graph_objects as go

fig = go.Figure(go.Sankey(
    node = dict(label=["Start","Process","End"], pad=15, thickness=20),
    link = dict(source=[0,1], target=[1,2], value=[1,1])
))
fig.show()
```

---

### संक्षेप (TL;DR)

* **Graphviz** साफ़, DSL/कोड-परिभाषित वर्कफ़्लो के लिए।
* **NetworkX** Python के माध्यम से फ्लेक्सिबल, लेआउट-ड्रिवन डायग्राम के लिए।
* **Pyvis** नोटबुक या वेब में इंटरैक्टिव, रिच विज़ुअलाइज़ेशन के लिए।
* **igraph** / **graph-tool** परफॉर्मेंस-हैवी ग्राफ़ टास्क के लिए।
* **pyflowsheet** प्रोसेस फ़्लोशीट के लिए।
* **Plotly Sankey** यदि आपको फ़्लो मैग्नीट्यूड विज़ुअल की आवश्यकता है।

मुझे बताएं यदि आप किसी विशिष्ट लाइब्रेरी या सैंपल इम्प्लीमेंटेशन के लिए मदद चाहते हैं!

[1]: https://en.wikipedia.org/wiki/Graphviz?utm_source=chatgpt.com "Graphviz"
[2]: https://www.reddit.com/r/Python/comments/ewbku/recommended_methodsapps_for_making_flowcharts/?utm_source=chatgpt.com "Recommended methods/apps for making flowcharts? : r/Python"
[3]: https://en.wikipedia.org/wiki/NetworkX?utm_source=chatgpt.com "NetworkX"
[4]: https://github.com/Nukleon84/pyflowsheet?utm_source=chatgpt.com "Nukleon84/pyflowsheet: A python package for drawing process flow ..."
[5]: https://arxiv.org/abs/2006.04951?utm_source=chatgpt.com "Network visualizations with Pyvis and VisJS"
[6]: https://en.wikipedia.org/wiki/Graph-tool?utm_source=chatgpt.com "Graph-tool"
[7]: https://arxiv.org/abs/2311.10260?utm_source=chatgpt.com "igraph enables fast and robust network analysis across programming languages"
[8]: https://plotly.com/python/sankey-diagram/?utm_source=chatgpt.com "Sankey diagram in Python - Plotly"
[9]: https://stackoverflow.com/questions/22920433/python-library-for-drawing-flowcharts-and-illustrated-graphs?utm_source=chatgpt.com "Python library for drawing flowcharts and illustrated graphs"
[10]: https://en.wikipedia.org/wiki/VisTrails?utm_source=chatgpt.com "VisTrails"
[11]: https://arxiv.org/abs/1905.06169?utm_source=chatgpt.com "Process Mining for Python (PM4Py): Bridging the Gap Between Process- and Data Science"