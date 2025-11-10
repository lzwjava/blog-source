---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 工作流程圖的Python庫
translated: true
type: note
---

若你正在尋找能輕鬆繪製工作流程或流程圖的 Python 函式庫——例如像 **maniod** 這類簡化圖表繪製的工具——以下精選了一些值得探索的優秀選項：

---

### 推薦用於工作流程與流程圖的 Python 套件

#### **1. Graphviz (透過 Python)**

* 一個廣泛使用的開源工具，用於繪製以 DOT 語言定義的圖表。
* 提供多種佈局樣式，如分層 (`dot`)、圓形 (`circo`)、放射狀 (`twopi`) 和力導向 (`neato`, `fdp`) ([維基百科][1])。
* 在 Python 中，你可以使用 `graphviz` 或 `pygraphviz` 包裝器以程式方式定義節點和邊——類似 DSL 風格。

> 「我曾用 GraphViz 處理這類需求。我喜歡它的主要原因是它更像是一種 DSL，而非用於製作流程圖的 GUI。」 ([Reddit][2])

#### **2. NetworkX**

* 一個原生 Python 函式庫，用於透過 Matplotlib 或 Graphviz 佈局來建立、分析和視覺化圖表 ([維基百科][3])。
* 支援有向圖、多邊以及各種佈局演算法，如彈簧佈局、多部分佈局（非常適合分層工作流程）、圓形佈局等 ([維基百科][3])。
* 非常適合生成資料驅動、圖形結構動態的工作流程圖。

#### **3. Pyvis (使用 VisJS)**

* 讓你能在筆記本或網頁中使用 Python 建立互動式工作流程視覺化。
* 基於 VisJS 建構；高度可自訂的互動性、佈局物理效果、工具提示——對於探索性圖表來說反應靈敏且使用者友好 ([GitHub][4], [arXiv][5])。

#### **4. Graph-tool**

* 一個高效能的 Python/C++ 函式庫，用於圖形操作與視覺化。
* 透過 Cairo 或 Graphviz 提供良好的匯出功能，並支援複雜的圖形演算法，如果你需要分析加上視覺化能力 ([維基百科][6])。

#### **5. igraph**

* 一個快速、可擴展的圖形函式庫（核心為 C，提供 Python 介面）。
* 非常適合效能要求高的工作負載和大規模圖形，並支援互動式繪圖 ([arXiv][7])。

#### **6. pyflowsheet**

* 專為工程情境中的**工藝流程圖**量身打造。
* 讓你可以從程式碼生成流程圖——麻煩最少，非常適合製程工程師 ([GitHub][4])。

#### **7. Plotly Sankey Diagram**

* 用於表示具有定量屬性的流程——Sankey 圖使用箭頭寬度顯示流量。
* 當你不僅需要顯示結構，還需要顯示步驟之間流量的大小時非常有用 ([Plotly][8])。

---

### 其他提及的工具

* **Schemdraw**：專為電路圖設計，但包含流程圖模組。圖表精美，但佈局必須手動指定 ([Stack Overflow][9])。
* **VisTrails**：一個基於 UI 的科學工作流程工具（未積極維護），用於視覺化管理、視覺化和探索管道 ([維基百科][10])。
* **PM4Py**：專注於**流程挖掘**而非繪製任意工作流程。更多是關於分析事件日誌 ([arXiv][11])。

---

以下是一個快速分類，幫助你選擇：

* **想要 DSL 風格、靜態的流程圖？** → **Graphviz**
* **需要動態/自訂的圖形結構？** → **NetworkX** (+ Matplotlib 或 Graphviz)
* **想要在筆記本/網頁中實現互動性？** → **Pyvis**
* **處理大型、對效能敏感的圖形？** → **igraph** 或 **graph-tool**
* **需要從程式碼生成工程風格的流程圖？** → **pyflowsheet**
* **需要表示階段之間的定量流動？** → **Plotly Sankey**

---

### 程式碼片段範例

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

### 總結

* **Graphviz** 適用於簡潔、由 DSL/程式碼定義的工作流程。
* **NetworkX** 適用於透過 Python 實現的靈活、佈局驅動的圖表。
* **Pyvis** 適用於在筆記本或網頁中實現互動式、豐富的視覺化。
* **igraph** / **graph-tool** 適用於效能要求高的圖形任務。
* **pyflowsheet** 適用於工藝流程圖。
* **Plotly Sankey** 如果你需要流量大小視覺化。

如果你需要任何特定函式庫的協助或範例實現，請告訴我！

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