---
audio: false
generated: true
image: false
lang: hant
layout: post
model: mistralai/mistral-medium-3.1
title: 超越 Graphviz 與 NetworkX 的圖表工具
translated: true
type: note
---

除了 Graphviz 和 NetworkX 的絕佳選擇，依照您偏好的工作方式分類。

文字/領域特定語言「以程式碼繪製圖表」
- PlantUML：完整 UML（時序、類別、元件、部署）、C4 模型、活動圖；龐大生態系。
- Mermaid：輕量級類 Markdown 語法；適用流程圖、時序圖、類別圖、實體關係圖、狀態圖；在 GitHub/GitLab 原生渲染。
- D2（由 Terrastruct 開發）：簡潔通用圖表 DSL，具備優秀自動佈局；支援圖層與大型圖表。
- Structurizr（C4）：模型優先（C4）搭配 DSL；可匯出至 PlantUML/Mermaid；適合架構文件。
- C4-PlantUML：建構於 PlantUML 之上的 C4 模型範本。
- nomnoml：極簡語法，快速繪製類別/關係草圖。
- Kroki：伺服器，可渲染多種 DSL（PlantUML、Mermaid、Graphviz）用於文件流程。

程式碼優先（從程式碼/IaC 生成圖表）
- diagrams（mingrammer，Python）：程式化雲端架構圖（AWS/Azure/GCP/K8s）。
- Terraform 輔助工具：Inframap（從狀態繪製）、Blast Radius（從 Terraform 生成互動式圖表）。
- AWS CDK：cdk-dia 可從 CDK 應用生成架構圖。
- Go/TS 函式庫：GoDiagrams（Go）、ts-graphviz（TypeScript）用於基於程式碼的生成。

網頁視覺化函式庫（互動式圖表）
- Cytoscape.js：大型圖表視覺化，佈局演算法，效能優異。
- D3.js：功能強大但較底層，適用自訂圖表/圖形視覺化。
- vis-network（vis.js）：簡易網絡圖表，具物理效果。
- Sigma.js：針對大型圖表的高速渲染。
- ECharts：通用圖表工具含圖形模組；快速呈現結果。
- pyvis（Python）：透過 Vis.js 實現簡易互動式網絡圖表。

GUI 圖表繪製工具（拖放式）
- diagrams.net（draw.io）：免費、易用、大量圖示庫（UML、雲端圖示）。
- yEd/yFiles：優秀自動佈局；yFiles 為商業 SDK，yEd 為免費桌面版。
- Lucidchart/Miro：協作式網頁工具；適合團隊使用。
- OmniGraffle（macOS）、Visual Paradigm、StarUML、Enterprise Architect：UML/架構工具。

架構專用與領域工具
- C4 模型：Structurizr、C4-PlantUML、Mermaid C4 擴充功能。
- 雲端架構 SaaS：Cloudcraft（AWS）、Hava、Lucidscale、CloudSkew；可從雲端/IaC 匯入。
- BPMN/流程：Camunda Modeler、bpmn.io。
- 時序/時序圖：WebSequenceDiagrams、WaveDrom（時序圖）。
- 實體關係/資料庫圖表：dbdiagram.io、SchemaSpy。

依情境快速選擇
- 標記文件/README 即程式碼：Mermaid。
- 完整 UML + C4 含範本：PlantUML 或 Structurizr。
- 從程式碼/IaC 生成雲端架構：diagrams（Python）、Inframap/Blast Radius（Terraform）、cdk-dia（AWS CDK）。
- 互動式網頁應用圖表：Cytoscape.js 或 vis-network；自訂視覺化則用 D3.js。
- 快速 GUI 繪圖：diagrams.net（draw.io）；需自動佈局則用 yEd。

若您能分享偏好（文字介面 vs GUI、靜態圖片 vs 互動式、使用語言及圖表類型如時序圖/C4/雲端/實體關係圖），我可推薦精選清單與入門範本。