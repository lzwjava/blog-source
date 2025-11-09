---
audio: false
generated: true
image: false
lang: hi
layout: post
model: mistralai/mistral-medium-3.1
title: नेटवर्कएक्स ग्राफ निर्माण और विश्लेषण उदाहरण
translated: true
type: note
---

NetworkX जटिल नेटवर्क बनाने, विश्लेषण करने और विज़ुअलाइज़ करने के लिए एक शक्तिशाली Python लाइब्रेरी है। यहां इसकी क्षमताओं को दर्शाने वाले कई उदाहरण दिए गए हैं:

## 1. बेसिक ग्राफ निर्माण और विज़ुअलाइज़ेशन

```python
import networkx as nx
import matplotlib.pyplot as plt

# एक खाली ग्राफ बनाएं
G = nx.Graph()

# नोड जोड़ें
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_nodes_from(range(4, 7))

# एज जोड़ें
G.add_edge(1, 2)
G.add_edges_from([(2, 3), (3, 4), (4, 5), (5, 6), (6, 1)])

# ग्राफ विज़ुअलाइज़ करें
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()
```

## 2. डायरेक्टेड ग्राफ उदाहरण

```python
# एक डायरेक्टेड ग्राफ बनाएं
D = nx.DiGraph()

# एज जोड़ें (स्वचालित रूप से नोड जोड़ता है)
D.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

# अलग-अलग नोड रंगों के साथ ड्रा करें
pos = nx.spring_layout(D)
nx.draw(D, pos, with_labels=True, node_color='lightgreen',
        edge_color='red', node_size=1000, arrowsize=20)
plt.show()
```

## 3. ग्राफ विश्लेषण उदाहरण

```python
# एक ग्राफ बनाएं
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)])

# बेसिक ग्राफ गुण
print("नोड्स की संख्या:", G.number_of_nodes())
print("एज की संख्या:", G.number_of_edges())
print("नोड्स:", G.nodes())
print("एज:", G.edges())
print("नोड 2 की डिग्री:", G.degree(2))
print("नोड 2 के पड़ोसी:", list(G.neighbors(2)))
print("क्या ग्राफ कनेक्टेड है?", nx.is_connected(G))
print("1 से 5 तक का शॉर्टेस्ट पाथ:", nx.shortest_path(G, 1, 5))
```

## 4. वेटेड ग्राफ उदाहरण

```python
# एक वेटेड ग्राफ बनाएं
G = nx.Graph()

# वेटेड एज जोड़ें
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'C', weight=2)
G.add_edge('A', 'C', weight=1)
G.add_edge('C', 'D', weight=5)

# वेट दिखाने वाले एज लेबल के साथ ड्रा करें
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightcoral')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
```

## 5. सोशल नेटवर्क विश्लेषण उदाहरण

```python
# एक सोशल नेटवर्क ग्राफ बनाएं
social = nx.Graph()

# लोग और उनके कनेक्शन जोड़ें
people = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
social.add_nodes_from(people)

connections = [('Alice', 'Bob'), ('Alice', 'Charlie'),
               ('Bob', 'Charlie'), ('Bob', 'David'),
               ('Charlie', 'Eve'), ('David', 'Eve')]
social.add_edges_from(connections)

# सेंट्रलिटी माप की गणना करें
degree_centrality = nx.degree_centrality(social)
betweenness_centrality = nx.betweenness_centrality(social)
closeness_centrality = nx.closeness_centrality(social)

print("डिग्री सेंट्रलिटी:", degree_centrality)
print("बिटवीननेस सेंट्रलिटी:", betweenness_centrality)
print("क्लोजनेस सेंट्रलिटी:", closeness_centrality)

# विज़ुअलाइज़ करें
nx.draw(social, with_labels=True, node_color='lightgreen', node_size=2000)
plt.show()
```

## 6. रैंडम ग्राफ जनरेशन

```python
# एक Erdős–Rényi रैंडम ग्राफ बनाएं
random_graph = nx.erdos_renyi_graph(10, 0.3)  # 10 नोड्स, 30% एज प्रोबेबिलिटी

# विज़ुअलाइज़ करें
nx.draw(random_graph, with_labels=True, node_color='skyblue')
plt.show()
```

## 7. ग्राफ एल्गोरिदम उदाहरण

```python
# एक ग्राफ बनाएं
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 6), (5, 6)])

# दो नोड्स के बीच सभी साधारण पाथ खोजें
print("1 से 6 तक के सभी पाथ:", list(nx.all_simple_paths(G, 1, 6)))

# मिनिमम स्पैनिंग ट्री
T = nx.minimum_spanning_tree(G)
print("MST में एज:", T.edges())

# कम्युनिटी डिटेक्शन (python-louvain पैकेज की आवश्यकता है)
# pip install python-louvain
try:
    import community as community_louvain
    partition = community_louvain.best_partition(G)
    print("कम्युनिटी पार्टीशन:", partition)
except ImportError:
    print("कम्युनिटी डिटेक्शन के लिए python-louvain इंस्टॉल करें")
```

ये उदाहरण बेसिक ग्राफ निर्माण, विज़ुअलाइज़ेशन, विश्लेषण और कुछ सामान्य एल्गोरिदम को कवर करते हैं। NetworkX जटिल नेटवर्क के साथ काम करने के लिए कई और फीचर्स प्रदान करता है।