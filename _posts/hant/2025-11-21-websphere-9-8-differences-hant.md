---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: WebSphere 9.0 與 8.0 主要差異
translated: true
type: note
---

### IBM WebSphere Application Server (WAS) 9.0 與 8.0 的主要差異

IBM WebSphere Application Server (WAS) 是一款企業級 Java EE 應用程式伺服器。版本 8.0（於 2011 年發佈）引入了 Java EE 6 相容性，而版本 9.0（於 2017 年發佈）則升級至 Java EE 7，重點在於將傳統配置檔案現代化，以符合輕量級、雲端友好的運行環境，例如 Liberty。以下我將根據 IBM 官方文件和版本說明，以表格形式列出關鍵差異，涵蓋 Java 支援、標準相容性、架構和部署等方面。

| 面向                  | WAS 8.0                                                                 | WAS 9.0                                                                 |
|-------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **Java SE 支援**    | 預設使用 Java SE 6；可透過配置選擇性支援 Java SE 7。 | 預設以 Java SE 8 為主要平台，使用 IBM SDK Java 8 以完全相容 Oracle Java 8。這使得 lambda 表達式、串流和其他 SE 8 功能得以實現。 |
| **Java EE 相容性** | 完整支援 Java EE 6，包括 JPA 2.0、JSF 2.0 和 Servlet 3.0。    | 完整支援 Java EE 7，新增了 WebSocket 1.0、JSON-P 1.0、Batch 1.0 和增強並行工具等功能。這使得傳統版本與 Liberty 早期版本的功能持平。 |
| **Liberty Profile 整合** | Liberty 在 8.5 版本中引入（不在 8.0 核心中）；8.0 僅專注於傳統完整配置檔案。 | 深度整合 Liberty 運行環境（版本 16.0.0.2）作為輕量級、模組化的替代方案，優化雲端原生應用。Liberty 已捆綁並支援持續交付。 |
| **部署模式**   | 主要為本地部署；透過 Installation Manager 安裝，提供 Base 和 Network Deployment (ND) 等版本以支援叢集。 | 首次同時發佈為本地部署和 IBM Cloud 上的服務形式。支援混合雲部署，並提供更好的容器化掛鉤。 |
| **效能與管理** | 相比 WAS 7 吞吐量提升高達 20-26%；ND 版本具備智能管理功能。 | 在 8.0 基礎上進一步優化資源效率；增強管理工具以支援遷移和配置比較。 |
| **支援終止日期**     | 延伸支援已於 2019 年結束；不再接收修復程式。              | 活躍支援至少持續至 2027 年，並定期發佈修復套件（例如 9.0.5.x）以解決安全性和相容性問題。 |
| **遷移考量** | 不適用（基準）。                                                        | 透過工具（如 Configuration Comparison Tool）更輕鬆地從 8.x 遷移；自動連接埠對齊和棄用 API 處理以支援 Java SE 8 過渡。 |

#### 關鍵要點
- **最大躍進**：轉向 Java EE 7 和 Java SE 8 是最重要的變化，實現了現代 Java 功能和標準，這些功能早期已在 Liberty 中預覽。如果您運行傳統 Java EE 6 應用程式，遷移至 9.0 是直接的，但可能需要測試 SE 8 特定變更。
- **何時升級**：若需要雲端/混合雲功能或 EE 7 特性，請選擇 9.0；僅在短期維護舊應用程式時才繼續使用 8.0（或修補至 8.5.5）。
- 詳細遷移指南，請查閱 IBM 官方文件。

**參考資料**：
- [IBM WebSphere Application Server Wikipedia](https://en.wikipedia.org/wiki/IBM_WebSphere_Application_Server)
- [Java SE 8 in WAS Traditional V9](https://www.ibm.com/docs/en/was/9.0.5?topic=waso-java-se-8-in-websphere-application-server-traditional-v9)
- [WAS Version Comparison Slides](https://www.slideshare.net/ejlp12/ibm-websphere-application-server-version-to-version-comparison)
- [WAS Configuration Comparison Tool](https://www.ibm.com/support/pages/websphere-application-server-configuration-comparison-tool)