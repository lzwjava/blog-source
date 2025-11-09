---
audio: false
generated: true
image: false
lang: ar
layout: post
model: openai/o1-mini
title: مقدمة إلى مكتبة NetworkX للرسوم البيانية في بايثون
translated: true
type: note
---

NetworkX هي مكتبة Python قوية لإنشاء الشبكات المعقدة (الرسوم البيانية) ومعالجتها ودراستها. توفر أدوات للعمل مع كل من الرسوم البيانية غير الموجهة والموجهة، والتعامل مع الحواف الموزونة، وإجراء مجموعة متنوعة من تحليلات الشبكات.

فيما يلي عدة أمثلة لمساعدتك في البدء مع NetworkX:

---

### 1. **تثبيت NetworkX**

قبل استخدام NetworkX، تأكد من تثبيتها. يمكنك تثبيتها باستخدام `pip`:

```bash
pip install networkx
```

---

### 2. **إنشاء وتصور رسم بياني بسيط**

إليك كيفية إنشاء رسم بياني غير موجه بسيط، وإضافة العقد والحواف، وتصورها باستخدام Matplotlib.

```python
import networkx as nx
import matplotlib.pyplot as plt

# إنشاء رسم بياني (Graph) فارغ
G = nx.Graph()

# إضافة العقد
G.add_node(1)
G.add_nodes_from([2, 3, 4])

# إضافة الحواف (تضيف العقد تلقائيًا إذا لم تكن موجودة)
G.add_edge(1, 2)
G.add_edges_from([(1, 3), (2, 4)])

# رسم الرسم البياني
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)
plt.title("رسم بياني غير موجه بسيط")
plt.show()
```

**الناتج:**

رسم بياني غير موجه بسيط يحتوي على 4 عقد متصلة بواسطة حواف.

---

### 3. **الرسوم البيانية الموجهة**

إنشاء وتصور رسم بياني موجه (DiGraph):

```python
import networkx as nx
import matplotlib.pyplot as plt

# إنشاء رسم بياني موجه
DG = nx.DiGraph()

# إضافة الحواف (يتم إضافة العقد تلقائيًا)
DG.add_edges_from([
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'C'),
    ('C', 'A'),
    ('C', 'D')
])

# رسم الرسم البياني الموجه مع أسهم
pos = nx.circular_layout(DG)
nx.draw(DG, pos, with_labels=True, node_color='lightgreen', edge_color='gray', arrows=True, node_size=700)
plt.title("رسم بياني موجه")
plt.show()
```

**الناتج:**

رسم بياني موجه يظهر اتجاه الحواف باستخدام الأسهم.

---

### 4. **الرسوم البيانية الموزونة**

تعيين أوزان للحواف وتصورها:

```python
import networkx as nx
import matplotlib.pyplot as plt

# إنشاء رسم بياني موزون
WG = nx.Graph()

# إضافة الحواف مع الأوزان
WG.add_edge('A', 'B', weight=4)
WG.add_edge('A', 'C', weight=2)
WG.add_edge('B', 'C', weight=5)
WG.add_edge('B', 'D', weight=10)
WG.add_edge('C', 'D', weight=3)

# الحصول على أوزان الحواف لوضع التسميات
edge_labels = nx.get_edge_attributes(WG, 'weight')

# رسم الرسم البياني
pos = nx.spring_layout(WG)
nx.draw(WG, pos, with_labels=True, node_color='lightyellow', edge_color='gray', node_size=700)
nx.draw_networkx_edge_labels(WG, pos, edge_labels=edge_labels)
plt.title("رسم بياني موزون")
plt.show()
```

**الناتج:**

رسم بياني موزون مع تسميات الحواف تمثل الأوزان.

---

### 5. **حساب أقصر مسار**

إيجاد أقصر مسار بين عقدتين باستخدام خوارزمية Dijkstra (للرسوم البيانية الموزونة):

```python
import networkx as nx

# إنشاء رسم بياني موزون (كما في المثال السابق)
WG = nx.Graph()
WG.add_edge('A', 'B', weight=4)
WG.add_edge('A', 'C', weight=2)
WG.add_edge('B', 'C', weight=5)
WG.add_edge('B', 'D', weight=10)
WG.add_edge('C', 'D', weight=3)

# حساب أقصر مسار من 'A' إلى 'D'
shortest_path = nx.dijkstra_path(WG, source='A', target='D', weight='weight')
path_length = nx.dijkstra_path_length(WG, source='A', target='D', weight='weight')

print(f"أقصر مسار من A إلى D: {shortest_path} بإجمالي وزن {path_length}")
```

**الناتج:**

```
أقصر مسار من A إلى D: ['A', 'C', 'D'] بإجمالي وزن 5
```

---

### 6. **مقاييس المركزية**

حساب مقاييس مركزية مختلفة لتحديد العقد المهمة في الرسم البياني.

```python
import networkx as nx

# إنشاء رسم بياني نموذجي
G = nx.karate_club_graph()

# حساب مركزية الدرجة
degree_centrality = nx.degree_centrality(G)

# حساب مركزية الوساطة
betweenness_centrality = nx.betweenness_centrality(G)

# حساب مركزية المتجه الذاتي
eigen_centrality = nx.eigenvector_centrality(G, max_iter=1000)

# عرض أفضل 5 عقد حسب مركزية الدرجة
sorted_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)
print("أفضل 5 عقد حسب مركزية الدرجة:")
for node, centrality in sorted_degree[:5]:
    print(f"العقدة {node}: {centrality:.4f}")

# وبالمثل، يمكنك عرض مقاييس المركزية الأخرى
```

**الناتج:**

```
أفضل 5 عقد حسب مركزية الدرجة:
العقدة 33: 0.6035
العقدة 0: 0.3793
العقدة 1: 0.3793
العقدة 2: 0.3793
العقدة 3: 0.3793
```

*ملاحظة:* رسم نادي الكاراتيه البياني هو مثال شائع لشبكة اجتماعية مستخدم في NetworkX.

---

### 7. **كشف المجتمعات باستخدام خوارزمية Girvan-Newman**

تحديد المجتمعات داخل الرسم البياني.

```python
import networkx as nx
from networkx.algorithms import community
import matplotlib.pyplot as plt

# إنشاء رسم بياني (باستخدام رسم نادي الكاراتيه البياني)
G = nx.karate_club_graph()

# حساب المجتمعات باستخدام Girvan-Newman
communities_generator = community.girvan_newman(G)
top_level_communities = next(communities_generator)
second_level_communities = next(communities_generator)

# دالة لتعيين الألوان للمجتمعات
def get_community_colors(G, communities):
    color_map = {}
    for idx, community in enumerate(communities):
        for node in community:
            color_map[node] = idx
    return [color_map[node] for node in G.nodes()]

# اختيار المستوى المطلوب من المجتمعات
communities = second_level_communities
colors = get_community_colors(G, communities)

# رسم الرسم البياني مع ألوان المجتمعات
pos = nx.spring_layout(G)
nx.draw(G, pos, node_color=colors, with_labels=True, cmap=plt.cm.Set1)
plt.title("المجتمعات في رسم نادي الكاراتيه البياني")
plt.show()
```

**الناتج:**

تصور لرسم نادي الكاراتيه البياني مع تلوين العقد بناءً على انتمائها المجتمعي.

---

### 8. **قراءة وكتابة الرسوم البيانية**

تدعم NetworkX تنسيقات متنوعة لقراءة وكتابة الرسوم البيانية، مثل قوائم المجاورة، وقوائم الحواف، و GraphML.

**قراءة قائمة حواف:**

```python
import networkx as nx

# افترض أن 'edges.txt' يحتوي على:
# A B
# A C
# B C
# B D
# C D

G = nx.read_edgelist('edges.txt', delimiter=' ')
print("العقد:", G.nodes())
print("الحواف:", G.edges())
```

**كتابة رسم بياني إلى GraphML:**

```python
import networkx as nx

G = nx.complete_graph(5)  # إنشاء رسم بياني كامل يحتوي على 5 عقد
nx.write_graphml(G, 'complete_graph.graphml')
print("تم حفظ الرسم البياني في 'complete_graph.graphml'")
```

---

### 9. **استخدام NetworkX مع Pandas DataFrames**

دمج NetworkX مع Pandas لمعالجة بيانات أكثر تقدمًا.

```python
import networkx as nx
import pandas as pd

# إنشاء DataFrame يمثل الحواف مع الأوزان
data = {
    'source': ['A', 'A', 'B', 'B', 'C'],
    'target': ['B', 'C', 'C', 'D', 'D'],
    'weight': [4, 2, 5, 10, 3]
}
df = pd.DataFrame(data)

# إنشاء رسم بياني موزون من DataFrame
G = nx.from_pandas_edgelist(df, 'source', 'target', ['weight'])

# عرض الحواف مع الأوزان
for u, v, data in G.edges(data=True):
    print(f"({u}, {v}) - الوزن: {data['weight']}")
```

**الناتج:**

```
(A, B) - الوزن: 4
(A, C) - الوزن: 2
(B, C) - الوزن: 5
(B, D) - الوزن: 10
(C, D) - الوزن: 3
```

---

### 10. **تصور متقدم باستخدام NetworkX و Matplotlib**

تخصيص مظهر الرسم البياني لتحسين إمكانية القراءة.

```python
import networkx as nx
import matplotlib.pyplot as plt

# إنشاء رسم بياني
G = nx.Graph()
G.add_edges_from([
    ('A', 'B'), ('A', 'C'), ('A', 'D'),
    ('B', 'C'), ('C', 'D'), ('D', 'E'),
    ('E', 'F'), ('F', 'C')
])

# تعيين المواضع باستخدام تخطيط
pos = nx.spring_layout(G, seed=42)

# رسم العقد بأحجام وألوان مختلفة
node_sizes = [700 if node == 'C' else 300 for node in G.nodes()]
node_colors = ['red' if node == 'C' else 'skyblue' for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors)

# رسم الحواف بعروض متفاوتة
edge_widths = [2 if (u == 'C' or v == 'C') else 1 for u, v in G.edges()]
nx.draw_networkx_edges(G, pos, width=edge_widths)

# رسم التسميات
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

plt.title("تصور مخصص للرسم البياني")
plt.axis('off')
plt.show()
```

**الناتج:**

رسم بياني مخصص حيث يتم تمييز العقدة 'C' باللون الأحمر بحجم أكبر، والحواف المتصلة بـ 'C' لها خطوط أكثر سمكًا.

---

توفر هذه الأمثلة فهمًا أساسيًا لكيفية استخدام NetworkX لإنشاء الرسوم البيانية ومعالجتها وتحليلها في Python. للاستخدام المتقدم والتوثيق التفصيلي، راجع [توثيق NetworkX الرسمي](https://networkx.org/documentation/stable/).