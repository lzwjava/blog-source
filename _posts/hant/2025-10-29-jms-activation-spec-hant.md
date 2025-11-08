---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: WebSphere 中的 JMS 啟用規範
translated: true
type: note
---

### IBM WebSphere Application Server (WAS) 中的 JMS 啟動規格

在 IBM WebSphere Application Server (WAS) 中，**啟動規格**是 Java Message Service (JMS) 中用於處理入站消息的關鍵配置組件，特別適用於**消息驅動 Bean (MDB)**。它作為 JMS 目的地（例如隊列或主題）與 MDB 之間的橋樑，定義應用程式伺服器如何連接到消息提供者（例如 WebSphere MQ 或內建的默認消息引擎），以異步方式接收和處理消息。

#### 主要目的與角色
- **標準化消息傳遞**：通過聲明式方式（透過 XML 描述符或管理控制台）配置 MDB 的消息消費，確保可靠傳遞而無需顯式輪詢。
- **連接管理**：指定 JMS 提供者、目的地類型（隊列或主題）、連接工廠、身份驗證和會話池等詳細信息，以優化資源使用。
- **J2C 集成**：啟動規格是 WAS 中 Java EE Connector Architecture (JCA/J2C) 資源適配器的一部分。它們使伺服器能夠根據傳入消息激活（實例化並分派消息到）MDB 實例。

#### 常見配置元素
在 WAS 中設置啟動規格時（透過管理控制台中的**資源 > JMS > 啟動規格**）：
- **常規屬性**：名稱、描述、JMS 提供者（例如 WebSphere MQ 或默認消息）。
- **連接設置**：主機、端口、傳輸類型（例如客戶端或伺服器模式）。
- **目的地設置**：隊列/主題名稱、目的地的 JNDI 查找。
- **高級屬性**：消息選擇器（用於過濾）、確認模式、事務支持和並發控制（例如最大並發 MDB）。
- **安全性**：用戶 ID、密碼或容器管理身份驗證。

#### 示例用例
對於基於 WebSphere MQ 的設置：
1. 安裝 WebSphere MQ 資源適配器。
2. 創建一個作用於您的伺服器/集群的啟動規格。
3. 在應用程式的部署描述符（例如 `ejb-jar.xml`，包含 `<messaging-type>` 和 `<activation-config>`）中將其鏈接到 MDB。
4. 部署應用程式 — MDB 將自動從指定隊列消費消息。

此設置對於 WAS 環境中可擴展的企業級消息傳遞至關重要，支持跨消息引擎的負載平衡等功能。

有關配置的更多詳細信息，請參閱官方 IBM 文檔。

#### 參考資料
- [JMS 啟動規格 [設置] - IBM](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=settings-jms-activation-specification)
- [為 WebSphere MQ 消息提供者配置啟動規格 - IBM](https://www.ibm.com/docs/SSAW57_8.5.5/com.ibm.websphere.nd.doc/ae/tmj_adm20.html)
- [WebSphere MQ 消息提供者啟動規格設置 - IBM](https://www.ibm.com/docs/SSEQTP_8.5.5/com.ibm.websphere.base.doc/ae/umj_pasm.html)