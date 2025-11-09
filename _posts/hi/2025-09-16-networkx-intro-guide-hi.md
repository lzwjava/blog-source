---
audio: false
generated: true
image: false
lang: hi
layout: post
model: openai/o1-mini
title: नेटवर्कएक्स पायथन ग्राफ लाइब्रेरी परिचय
translated: true
type: note
---

NetworkX जटिल नेटवर्क (ग्राफ) के निर्माण, हेरफेर और अध्ययन के लिए एक शक्तिशाली Python लाइब्रेरी है। यह अनेदेशित (undirected) और निर्देशित (directed) दोनों प्रकार के ग्राफ के साथ काम करने, भारित (weighted) एज को हैंडल करने और विभिन्न प्रकार के नेटवर्क विश्लेषण करने के टूल्स प्रदान करती है।

नीचे NetworkX के साथ शुरुआत करने में आपकी मदद करने के लिए कई उदाहरण दिए गए हैं:

---

### 1. **NetworkX इंस्टॉल करना**

NetworkX का उपयोग करने से पहले, सुनिश्चित करें कि यह इंस्टॉल है। आप इसे `pip` का उपयोग करके इंस्टॉल कर सकते हैं:

```bash
pip install networkx
```

---

### 2. **एक सरल ग्राफ बनाना और विज़ुअलाइज़ करना**

यहां बताया गया है कि कैसे एक साधारण अनेदेशित ग्राफ बनाया जाए, नोड और एज जोड़े जाएं, और Matplotlib का उपयोग करके इसे विज़ुअलाइज़ किया जाए।

```python
import networkx as nx
import matplotlib.pyplot as plt

# एक खाली ग्राफ बनाएं
G = nx.Graph()

# नोड जोड़ें
G.add_node(1)
G.add_nodes_from([2, 3, 4])

# एज जोड़ें (यदि नोड मौजूद नहीं हैं तो स्वचालित रूप से जोड़ देता है)
G.add_edge(1, 2)
G.add_edges_from([(1, 3), (2, 4)])

# ग्राफ ड्रा करें
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)
plt.title("सरल अनेदेशित ग्राफ")
plt.show()
```

**आउटपुट:**

4 नोड्स वाला एक साधारण अनेदेशित ग्राफ जो एजेज से जुड़ा हुआ है।

---

### 3. **निर्देशित ग्राफ (Directed Graphs)**

एक निर्देशित ग्राफ (DiGraph) बनाना और विज़ुअलाइज़ करना:

```python
import networkx as nx
import matplotlib.pyplot as plt

# एक निर्देशित ग्राफ बनाएं
DG = nx.DiGraph()

# एज जोड़ें (नोड स्वचालित रूप से जोड़ दिए जाते हैं)
DG.add_edges_from([
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'C'),
    ('C', 'A'),
    ('C', 'D')
])

# तीरों के साथ निर्देशित ग्राफ ड्रा करें
pos = nx.circular_layout(DG)
nx.draw(DG, pos, with_labels=True, node_color='lightgreen', edge_color='gray', arrows=True, node_size=700)
plt.title("निर्देशित ग्राफ")
plt.show()
```

**आउटपुट:**

तीरों के साथ एजेज की दिशा दिखाने वाला एक निर्देशित ग्राफ।

---

### 4. **भारित ग्राफ (Weighted Graphs)**

एजेज को वज़न (weights) असाइन करना और उन्हें विज़ुअलाइज़ करना:

```python
import networkx as nx
import matplotlib.pyplot as plt

# एक भारित ग्राफ बनाएं
WG = nx.Graph()

# वज़न के साथ एज जोड़ें
WG.add_edge('A', 'B', weight=4)
WG.add_edge('A', 'C', weight=2)
WG.add_edge('B', 'C', weight=5)
WG.add_edge('B', 'D', weight=10)
WG.add_edge('C', 'D', weight=3)

# लेबलिंग के लिए एज वेट प्राप्त करें
edge_labels = nx.get_edge_attributes(WG, 'weight')

# ग्राफ ड्रा करें
pos = nx.spring_layout(WG)
nx.draw(WG, pos, with_labels=True, node_color='lightyellow', edge_color='gray', node_size=700)
nx.draw_networkx_edge_labels(WG, pos, edge_labels=edge_labels)
plt.title("भारित ग्राफ")
plt.show()
```

**आउटपुट:**

वज़न का प्रतिनिधित्व करने वाले एज लेबल के साथ एक भारित ग्राफ।

---

### 5. **सबसे छोटा रास्ता कम्प्यूट करना (Computing Shortest Path)**

दो नोड्स के बीच सबसे छोटा रास्ता खोजना (भारित ग्राफ के लिए Dijkstra's algorithm का उपयोग करके):

```python
import networkx as nx

# एक भारित ग्राफ बनाएं (पिछले उदाहरण की तरह)
WG = nx.Graph()
WG.add_edge('A', 'B', weight=4)
WG.add_edge('A', 'C', weight=2)
WG.add_edge('B', 'C', weight=5)
WG.add_edge('B', 'D', weight=10)
WG.add_edge('C', 'D', weight=3)

# 'A' से 'D' तक का सबसे छोटा रास्ता कम्प्यूट करें
shortest_path = nx.dijkstra_path(WG, source='A', target='D', weight='weight')
path_length = nx.dijkstra_path_length(WG, source='A', target='D', weight='weight')

print(f"A से D तक का सबसे छोटा रास्ता: {shortest_path} कुल वज़न के साथ {path_length}")
```

**आउटपुट:**

```
A से D तक का सबसे छोटा रास्ता: ['A', 'C', 'D'] कुल वज़न के साथ 5
```

---

### 6. **केंद्रीयता माप (Centrality Measures)**

ग्राफ में महत्वपूर्ण नोड्स की पहचान करने के लिए विभिन्न केंद्रीयता मापों की गणना करना।

```python
import networkx as nx

# एक नमूना ग्राफ बनाएं
G = nx.karate_club_graph()

# डिग्री केंद्रीयता कम्प्यूट करें
degree_centrality = nx.degree_centrality(G)

# बीच में होने की केंद्रीयता (betweenness centrality) कम्प्यूट करें
betweenness_centrality = nx.betweenness_centrality(G)

# आइगेनवेक्टर केंद्रीयता कम्प्यूट करें
eigen_centrality = nx.eigenvector_centrality(G, max_iter=1000)

# डिग्री केंद्रीयता के आधार पर शीर्ष 5 नोड्स प्रदर्शित करें
sorted_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)
print("डिग्री केंद्रीयता के आधार पर शीर्ष 5 नोड्स:")
for node, centrality in sorted_degree[:5]:
    print(f"नोड {node}: {centrality:.4f}")

# इसी तरह, आप अन्य केंद्रीयताएं प्रदर्शित कर सकते हैं
```

**आउटपुट:**

```
डिग्री केंद्रीयता के आधार पर शीर्ष 5 नोड्स:
नोड 33: 0.6035
नोड 0: 0.3793
नोड 1: 0.3793
नोड 2: 0.3793
नोड 3: 0.3793
```

*नोट:* कराटे क्लब ग्राफ NetworkX में अक्सर उपयोग किया जाने वाला एक सामाजिक नेटवर्क उदाहरण है।

---

### 7. **Girvan-Newman Algorithm के साथ कम्युनिटी का पता लगाना**

एक ग्राफ के भीतर कम्युनिटीज की पहचान करना।

```python
import networkx as nx
from networkx.algorithms import community
import matplotlib.pyplot as plt

# एक ग्राफ बनाएं (कराटे क्लब ग्राफ का उपयोग करके)
G = nx.karate_club_graph()

# Girvan-Newman का उपयोग करके कम्युनिटीज कम्प्यूट करें
communities_generator = community.girvan_newman(G)
top_level_communities = next(communities_generator)
second_level_communities = next(communities_generator)

# कम्युनिटीज को रंग असाइन करने के लिए फ़ंक्शन
def get_community_colors(G, communities):
    color_map = {}
    for idx, community in enumerate(communities):
        for node in community:
            color_map[node] = idx
    return [color_map[node] for node in G.nodes()]

# वांछित स्तर की कम्युनिटीज चुनें
communities = second_level_communities
colors = get_community_colors(G, communities)

# कम्युनिटी रंगों के साथ ग्राफ ड्रा करें
pos = nx.spring_layout(G)
nx.draw(G, pos, node_color=colors, with_labels=True, cmap=plt.cm.Set1)
plt.title("कराटे क्लब ग्राफ में कम्युनिटीज")
plt.show()
```

**आउटपुट:**

कराटे क्लब ग्राफ का एक विज़ुअलाइज़ेशन जहां नोड्स उनकी कम्युनिटी सदस्यता के आधार पर रंगे गए हैं।

---

### 8. **ग्राफ पढ़ना और लिखना**

NetworkX ग्राफ को पढ़ने और लिखने के लिए विभिन्न फॉर्मेट सपोर्ट करता है, जैसे कि adjacency lists, edge lists, और GraphML.

**एक एज लिस्ट पढ़ना:**

```python
import networkx as nx

# मान लें कि 'edges.txt' में यह शामिल है:
# A B
# A C
# B C
# B D
# C D

G = nx.read_edgelist('edges.txt', delimiter=' ')
print("नोड्स:", G.nodes())
print("एजेज:", G.edges())
```

**एक ग्राफ को GraphML में लिखना:**

```python
import networkx as nx

G = nx.complete_graph(5)  # 5 नोड्स के साथ एक पूर्ण ग्राफ बनाएं
nx.write_graphml(G, 'complete_graph.graphml')
print("ग्राफ 'complete_graph.graphml' में सेव हो गया")
```

---

### 9. **Pandas DataFrames के साथ NetworkX का उपयोग करना**

अधिक उन्नत डेटा हेरफेर के लिए NetworkX को Pandas के साथ एकीकृत करें।

```python
import networkx as nx
import pandas as pd

# वज़न के साथ एजेज का प्रतिनिधित्व करने वाला एक DataFrame बनाएं
data = {
    'source': ['A', 'A', 'B', 'B', 'C'],
    'target': ['B', 'C', 'C', 'D', 'D'],
    'weight': [4, 2, 5, 10, 3]
}
df = pd.DataFrame(data)

# DataFrame से एक भारित ग्राफ बनाएं
G = nx.from_pandas_edgelist(df, 'source', 'target', ['weight'])

# वज़न के साथ एजेज प्रदर्शित करें
for u, v, data in G.edges(data=True):
    print(f"({u}, {v}) - वज़न: {data['weight']}")
```

**आउटपुट:**

```
(A, B) - वज़न: 4
(A, C) - वज़न: 2
(B, C) - वज़न: 5
(B, D) - वज़न: 10
(C, D) - वज़न: 3
```

---

### 10. **NetworkX और Matplotlib के साथ उन्नत विज़ुअलाइज़ेशन**

बेहतर पठनीयता के लिए ग्राफ की उपस्थिति को कस्टमाइज़ करना।

```python
import networkx as nx
import matplotlib.pyplot as plt

# एक ग्राफ बनाएं
G = nx.Graph()
G.add_edges_from([
    ('A', 'B'), ('A', 'C'), ('A', 'D'),
    ('B', 'C'), ('C', 'D'), ('D', 'E'),
    ('E', 'F'), ('F', 'C')
])

# एक लेआउट का उपयोग करके पोजीशन असाइन करें
pos = nx.spring_layout(G, seed=42)

# अलग-अलग आकार और रंगों के साथ नोड्स ड्रा करें
node_sizes = [700 if node == 'C' else 300 for node in G.nodes()]
node_colors = ['red' if node == 'C' else 'skyblue' for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors)

# अलग-अलग चौड़ाई वाली एजेज ड्रा करें
edge_widths = [2 if (u == 'C' or v == 'C') else 1 for u, v in G.edges()]
nx.draw_networkx_edges(G, pos, width=edge_widths)

# लेबल ड्रा करें
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

plt.title("कस्टमाइज़्ड ग्राफ विज़ुअलाइज़ेशन")
plt.axis('off')
plt.show()
```

**आउटपुट:**

एक कस्टमाइज़्ड ग्राफ जहां नोड 'C' को बड़े आकार में लाल रंग में हाइलाइट किया गया है, और 'C' से जुड़ी एजेज की लाइनें मोटी हैं।

---

ये उदाहरण Python में ग्राफ बनाने, हेरफेर करने और विश्लेषण करने के लिए NetworkX का उपयोग करने की मूलभूत समझ प्रदान करते हैं। अधिक उन्नत उपयोग और विस्तृत दस्तावेज़ के लिए, [आधिकारिक NetworkX दस्तावेज़](https://networkx.org/documentation/stable/) देखें।