---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: Python 圖表即程式碼工具替代方案
translated: true
type: note
---

以下是適用於 Python 且能輕鬆生成軟體設計/架構圖表的選項（除了 Graphviz 和 NetworkX）。我按使用情境進行分組，並附上簡要說明和小型範例。

圖表即代碼（UML、C4、流程圖、時序圖）
- PlantUML（透過 python-plantuml 或本地 JAR）
  - 非常適合 UML：類別圖、時序圖、元件圖、狀態圖、活動圖、部署圖。
  - 在 CI 和文件編寫中表現良好。
  - 範例：
    @startuml
    class User
    class Order
    User "1" --> "*" Order
    @enduml
- Mermaid（使用 CLI 或 Kroki 伺服器；Python 可調用渲染器）
  - 適用於時序圖、類別圖、流程圖、實體關係圖、狀態圖等的簡潔語法。
  - 在多種文件工具和 wiki 中渲染效果良好。
  - 範例：
    flowchart LR
      API --> DB
- BlockDiag 系列（blockdiag、seqdiag、actdiag、nwdiag）
  - 純 Python 工具，可從簡單文字生成方塊圖、時序圖、活動圖和網絡圖。
  - 範例（seqdiag）：
    seqdiag {
      Client -> API [label = "GET /users"];
      API -> DB [label = "query"];
    }
- Structurizr（C4 模型；社區版 Python 客戶端）
  - 建模軟體架構（Context、Container、Component）並透過 Structurizr/PlantUML 渲染。
  - 非常適合多視圖架構文件和 ADR 工作流程。
- Kroki（圖表即服務；提供 Python 客戶端）
  - 透過單一 HTTP API 從 Python 渲染多種 DSL（PlantUML、Mermaid、Graphviz、BPMN 等）。

雲端和基礎設施架構
- Diagrams（由 mingrammer 開發）
  - 使用官方供應商圖標（AWS、Azure、GCP、K8s、本地部署）的雲端/系統架構圖表即代碼。
  - 在架構概覽圖中非常受歡迎。
  - 範例：
    from diagrams import Diagram
    from diagrams.aws.compute import EC2
    from diagrams.aws.database import RDS
    with Diagram("Web Service", show=False):
        EC2("api") >> RDS("db")

互動式網絡/圖形視覺化（適用於系統地圖、依賴關係）
- PyVis（vis.js）
  - 用極少代碼生成互動式 HTML 圖形。
  - 範例：
    from pyvis.network import Network
    net = Network(); net.add_nodes(["API","DB"]); net.add_edge("API","DB"); net.show("arch.html")
- Dash Cytoscape / ipycytoscape（Cytoscape.js）
  - 適用於 Dash 應用或 Jupyter 中的互動式、可自訂圖形。適合探索依賴關係和流程。
- Plotly
  - 建立具有自訂樣式的互動式節點連結圖；易於嵌入和分享。
- Bokeh / HoloViews
  - 支援網絡的互動式繪圖；適合以 Python 為中心的儀表板。
- python-igraph
  - 具有內建繪圖功能的快速圖形庫；適用於需要佈局算法和可匯出圖表的情況。

文件整合（將圖表與文件緊密結合）
- Sphinx 擴展：sphinxcontrib-plantuml、sphinxcontrib-mermaid、sphinxcontrib-blockdiag
  - 在 reStructuredText/Markdown 中內聯編寫圖表，並在文件管道中構建它們。
- MkDocs 插件（適用於 Mermaid/PlantUML）
  - 適用於現代靜態網站，非常方便。

代碼和架構逆向工程
- pylint 的 pyreverse
  - 從 Python 代碼生成 UML 類別圖和套件圖（通常透過 Graphviz 渲染，但工作流程簡單）。
- pydeps
  - 建立 Python 套件的導入/依賴關係圖，適用於大型代碼庫中的架構地圖。

專業圖表
- SchemDraw
  - 在 Python 中程式化生成電路/邏輯/流程圖；輸出清晰的向量圖。
- railroad-diagrams
  - 生成語法圖（適用於協議/規範文件）。

選擇建議
- 快速 UML/時序圖文件：PlantUML 或 Mermaid。
- 雲端/系統架構海報：Diagrams（mingrammer）。
- 互動式探索和分享：PyVis 或 Dash Cytoscape。
- C4 模型和動態架構文件：Structurizr（透過匯出與 PlantUML/Mermaid 結合）。
- 從代碼自動生成圖表：pyreverse、pydeps。

如果您告訴我目標圖表類型（UML 類別圖、時序圖、C4、雲端架構、數據流圖、套件依賴關係）和輸出格式（PNG/SVG/HTML/嵌入文件），我可以建議最簡設置和入門模板。