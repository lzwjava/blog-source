---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: NetworkX 與 Matplotlib 圖形教學
translated: true
type: note
---

### 安裝程式庫
若要使用 NetworkX 和 Matplotlib 繪製圖表，請按需安裝：
- NetworkX：處理圖形建立與操作
- Matplotlib：提供繪圖功能

透過 pip 安裝：
```bash
pip install networkx matplotlib
```

為獲得更快渲染速度，Matplotlib 建議安裝 NumPy（`pip install numpy`）。

### 基本設定與範例
1. **匯入程式庫**：  
   ```python
   import networkx as nx
   import matplotlib.pyplot as plt
   ```

2. **建立圖形**：  
   使用 NetworkX 建立簡單無向圖（可自訂為有向圖、加權邊等）：
   ```python
   G = nx.Graph()  # 建立空圖形
   G.add_nodes_from([1, 2, 3, 4, 5])  # 添加節點（例如 5 個節點）
   G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])  # 添加邊（連接關係）
   ```

3. **繪製並顯示圖表**：  
   使用 Matplotlib 後端進行視覺化：
   ```python
   nx.draw(G, with_labels=True)  # 繪製帶有節點標籤的圖形
   plt.show()  # 顯示繪圖
   ```

這將產生圖形的基本環形佈局（包含 5 個節點的循環圖）。

### 進階自訂功能
- **佈局**：控制節點位置（例如隨機、彈簧佈局）：
  ```python
  pos = nx.spring_layout(G)  # 力導向佈局，適用於真實網絡
  nx.draw(G, pos=pos, with_labels=True, node_color='lightblue', edge_color='gray')
  plt.title("網絡圖表")
  plt.show()
  ```
- **節點與邊樣式**：自訂外觀：
  ```python
  nx.draw(G, pos=pos, node_size=500, node_color='red', edge_width=2, font_size=10)
  ```
- **有向圖**：適用於層級關係，使用 `nx.DiGraph`：
  ```python
  DG = nx.DiGraph()
  DG.add_edges_from([('A', 'B'), ('B', 'C')])
  nx.draw(DG, with_labels=True, arrows=True)
  plt.show()
  ```
- **儲存圖表**：匯出至檔案而非顯示：
  ```python
  plt.savefig('diagram.png')
  ```

### 提示與資源
- NetworkX 文檔（networkx.org）提供樹狀圖或網格圖等圖形類型
- Matplotlib 文檔（matplotlib.org）提供嵌入 GUI 或子圖的相關資訊
- 處理大型圖形（>100 個節點）時，建議使用 `nx.draw_networkx` 或外部工具如 Graphviz 以獲得更好效能
- 可在 Jupyter notebook 中進行互動式繪圖測試。若遇問題，常見錯誤通常源自缺少後端（可透過 `pip install pyqt5` 或類似指令安裝以啟用互動視窗）