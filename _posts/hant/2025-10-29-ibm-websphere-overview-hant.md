---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: IBM WebSphere 應用伺服器概覽
translated: true
type: note
---

### IBM WebSphere Application Server (WAS) 概覽

IBM WebSphere Application Server 是一款穩健的企業級 Java 應用伺服器，作為中介軟體平台，用於託管、部署和管理基於 Java 的 Web 及企業應用程式。它充當 Java EE（現為 Jakarta EE）容器，為關鍵任務工作負載提供安全、高效能的運行環境。WAS 支援三層式架構，負責處理應用邏輯層，使客戶端能夠與資料資源和服務互動。憑藉其可靠性與可擴展性，WAS 廣泛應用於金融、醫療保健和政府等行業，並支援地端部署、雲端、混合及容器化環境。

### 主要功能
WAS 專注於 Java 應用程式的完整生命週期，從開發、部署到運行時管理與現代化。主要功能包括：

- **應用程式部署與託管**：部署 Java EE/Jakarta EE 應用程式，包括 servlet、JSP、EJB、Web 服務和微服務。它支援在「單元」架構中跨多個作業系統實例進行分散式運算，並透過 XML 檔案和 Deployment Manager 進行集中配置。
  
- **運行時管理**：透過叢集、負載平衡和智能路由提供高可用性。會話管理、資源池（例如 JDBC 連線）和滾動更新等功能確保維護期間的停機時間最小化。

- **安全性與整合**：實作 Java EE 安全模型，支援身份驗證（例如表單驗證、Kerberos、LDAP）、授權和加密。可與 Apache HTTP、IIS 和 IBM HTTP Server 等網頁伺服器整合，並支援 WS-Security 和 JACC 等標準。

- **效能與擴展性**：透過動態叢集、快取（例如 ObjectGrid）和批次處理等功能，針對大規模操作進行優化。支援在大型主機（z/OS）上垂直擴展，並在雲端環境中水平擴展。

- **現代化工具**：自動遷移至現代運行環境，如 WebSphere Liberty（輕量級配置檔）或容器（例如 Docker、Kubernetes），降低舊版應用程式更新的風險。

- **監控與管理**：提供統一控制台進行配置、效能監控和故障排除，包括健康檢查和診斷功能。

### 主要特性
- **標準合規性**：全面支援 Java EE 8（及更早版本）、Java SE 最高至 11（於 Liberty）、Servlet 4.0、EJB 3.2、JMS 2.0、JPA 2.1，以及適用於雲原生應用的 MicroProfile。
- **輕量級選項（Liberty 配置檔）**：模組化、快速啟動（3 秒內）的運行環境，適用於 Web/行動應用程式，並透過 OSGi 實現動態功能載入。自 2017 年起開源為 Open Liberty，並提供持續交付更新。
- **平台多樣性**：可運行於 Windows、Linux、AIX、z/OS、IBM i、Solaris 等平台；支援虛擬機器、實體伺服器和雲端環境（例如 AWS、Azure）。
- **進階功能**：內嵌 JMS、OSGi 應用支援、智能管理（例如應用程式版本控制），以及 z/OS 專用功能，如 Workload Manager 和 RACF 整合。

### 版本與使用場景
WAS 提供多種版本以滿足不同需求：
- **Traditional（基礎版/網路部署版）**：提供完整的企業功能，如叢集和邊緣快取；適合資料中心內的單體式應用程式。
- **Liberty**：輕量級版本，適用於開發測試、微服務和雲原生部署；適合現代化應用程式的敏捷團隊。
- **z/OS**：針對大型主機工作負載優化，具備交易完整性和高負載處理能力。

常見使用場景包括電子商務平台、金融交易系統、醫療保健入口網站和混合雲遷移。截至 2025 年，WAS 已整合至 IBM 的 Enterprise Application Runtimes 和 JSphere Suite，強調容器化和 AI 輔助的現代化。

最新詳細資訊，請查閱官方資源。

[IBM WebSphere Application Server 產品頁面](https://www.ibm.com/products/websphere-application-server)  
[WebSphere Application Server 文件](https://www.ibm.com/docs/en/was/9.0.5?topic=websphere-application-server-overview)  
[維基百科：IBM WebSphere Application Server](https://en.wikipedia.org/wiki/IBM_WebSphere_Application_Server)