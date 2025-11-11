---
audio: false
generated: true
lang: hant
layout: post
title: 視覺化依賴關係
translated: true
type: note
---

要視覺化由提供的 Python 腳本生成的 Maven 依賴關係圖，您可以使用 **Graphviz**，這是一個廣泛使用且簡單直接的圖形工具，能渲染以 DOT 語言描述的圖形。該腳本以 DOT 格式輸出依賴關係圖，將您 Maven 專案中模組間的依賴關係表示為有向圖，節點以 `artifactId` 標記，邊線則顯示依賴關係。以下是使用 Graphviz 繪製和視覺化此圖的步驟，同時也提及如 Polyglot 或其他替代工具，以供您選擇不同選項。

---

### 使用 Graphviz（推薦方法）

Graphviz 在此處非常理想，因為腳本直接生成 DOT 格式輸出，而 Graphviz 原生支援此格式。請遵循以下步驟：

1. **執行腳本**  
   執行 Python 腳本，並提供您 Maven 專案的根目錄作為參數。這將生成依賴關係圖的 DOT 輸出。
   ```bash
   python script.py /path/to/maven/project
   ```

2. **將 DOT 輸出儲存至檔案**  
   將腳本的輸出重定向到一個檔案，例如 `dependencies.dot`。該檔案將包含 DOT 格式的圖形描述。
   ```bash
   python script.py /path/to/maven/project > dependencies.dot
   ```

3. **安裝 Graphviz（如果尚未安裝）**  
   Graphviz 適用於 Windows、macOS 和 Linux。請使用您的套件管理器進行安裝：
   - **Ubuntu/Debian**：  
     ```bash
     sudo apt-get install graphviz
     ```
   - **macOS（使用 Homebrew）**：  
     ```bash
     brew install graphviz
     ```
   - **Windows**：從 [Graphviz 網站](https://graphviz.org/download/)下載並安裝。

4. **生成視覺化圖像**  
   使用 Graphviz 的 `dot` 指令將 DOT 檔案轉換為圖像。例如，建立一個 PNG 檔案：
   ```bash
   dot -Tpng dependencies.dot -o dependencies.png
   ```
   - 您可以根據偏好將 `-Tpng` 替換為其他格式，如 `-Tsvg` 用於 SVG 或 `-Tpdf` 用於 PDF。

5. **檢視圖形**  
   使用任何圖片檢視器開啟生成的 `dependencies.png` 檔案，即可看到依賴關係圖。每個節點代表一個模組的 `artifactId`，箭頭則表示模組間的依賴關係。

---

### 替代工具

如果您不想使用 Graphviz 或希望探索其他常見的圖形工具，以下是一些選項：

#### Polyglot Notebooks（例如與 Jupyter 搭配使用）
Polyglot Notebooks 不直接視覺化 DOT 檔案，但您可以在 Jupyter notebook 環境中整合 Graphviz：
- **步驟**：
  1. 安裝 Graphviz 和 `graphviz` Python 套件：
     ```bash
     pip install graphviz
     sudo apt-get install graphviz  # 對於 Ubuntu，請根據您的作業系統調整
     ```
  2. 修改腳本，使用 Python 的 `graphviz` 庫代替直接輸出原始 DOT。在腳本末尾加入以下程式碼：
     ```python
     from graphviz import Digraph

     dot = Digraph()
     for from_module, to_module in sorted(dependencies):
         dot.edge(from_module, to_module)
     dot.render('dependencies', format='png', view=True)
     ```
  3. 執行修改後的腳本，直接生成並顯示 `dependencies.png`。
- **注意**：此方法底層仍依賴 Graphviz，因此並非完全獨立的工具。

#### Gephi
Gephi 是一個開源的網絡視覺化工具，可以匯入 DOT 檔案：
- **步驟**：
  1. 從 [gephi.org](https://gephi.org/) 下載並安裝 Gephi。
  2. 執行腳本並將 DOT 輸出儲存至 `dependencies.dot`。
  3. 開啟 Gephi，前往 `檔案 > 匯入 > 圖形檔案`，並選擇 `dependencies.dot`。
  4. 調整佈局（例如 ForceAtlas 2）並進行互動式視覺化。
- **優點**：適用於大型圖形，並提供進階佈局選項。
- **缺點**：需要手動匯入和設定。

#### 線上 Graphviz 工具
如需快速且無需安裝的選項：
- **步驟**：
  1. 執行腳本並複製 DOT 輸出（從 `digraph G {` 到 `}`）。
  2. 訪問線上工具，如 [GraphvizOnline](https://dreampuf.github.io/GraphvizOnline/)。
  3. 貼上 DOT 內容並點擊以渲染圖形。
- **優點**：無需安裝。
- **缺點**：需要網路連線；對輸出格式的控制較少。

#### yEd
yEd 是一個免費的圖形編輯器，但不原生支援 DOT：
- **步驟**：
  1. 使用工具（如 `dot`）將 DOT 檔案轉換為 GraphML 或其他支援的格式（例如 `dot -Tgraphml dependencies.dot -o dependencies.graphml`）。
  2. 開啟 yEd，匯入 GraphML 檔案，並調整佈局。
- **缺點**：需要額外的轉換步驟。

---

### 為何 Graphviz 在此處是最佳選擇
腳本的輸出專為 DOT 格式設計，使 Graphviz 成為最直接且高效的選擇。它輕量、基於命令列，且廣泛支援。生成的圖形將大致如下（概念上）：
- 節點：每個模組的 `artifactId（例如 `"module-a"`、`"module-b"`）。
- 邊線：箭頭如 `"module-a" -> "module-b"`，顯示 `module-a` 依賴於 `module-b`。

如果您的圖形較大，可以使用 Graphviz 選項調整佈局（例如使用 `dot -Kneato` 進行不同排列），但上述基本步驟應已足夠。

---

### 最終建議
要視覺化來自您腳本的 Maven 依賴關係圖：
1. 執行：`python script.py /path/to/maven/project > dependencies.dot`
2. 如有需要，安裝 Graphviz。
3. 轉換為圖像：`dot -Tpng dependencies.dot -o dependencies.png`
4. 開啟 `dependencies.png` 檢視您的圖形。

此方法簡單，使用常見工具（Graphviz），並與您腳本的輸出完美契合。如果您需要互動性或替代格式，請嘗試 Gephi 或線上工具。