---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: WebSphere 應用程式伺服器中的 JMS 佇列
translated: true
type: note
---

### Java Message Service (JMS) 概述
Java Message Service (JMS) 是一個用於在 Java 應用程式之間傳送訊息的標準 API，實現了非同步通訊。它支援兩種主要的訊息傳遞模式：點對點（使用佇列）和發佈-訂閱（使用主題）。在 IBM WebSphere Application Server (WAS) 中，JMS 被整合用於處理企業應用程式內的訊息傳遞，通常使用內建的預設訊息提供者或外部提供者（如 IBM MQ）。

### JMS 中的佇列
在 JMS 中，**佇列**是一種用於**點對點訊息傳遞**的目的地類型。以下是詳細說明：
- **用途**：傳送到佇列的訊息只會交付給一個消費者（接收者）。它適用於需要由單一應用程式或元件處理訊息的場景，例如任務分配或請求-回應模式。
- **關鍵特性**：
  - **FIFO（先進先出）**：訊息通常按照到達順序處理，但 JMS 允許優先級設定。
  - **持久性**：訊息可以是持久的（永久儲存）或非持久的，確保在故障情況下的可靠性。
  - **消費者**：多個消費者可以連接到佇列，但每條訊息只會被一個消費者處理。如果沒有可用消費者，訊息會排隊直到被處理。
- **涉及的元件**：
  - **佇列傳送者/生產者**：將訊息傳送到佇列。
  - **佇列接收者/消費者**：輪詢或監聽佇列上的訊息。
  - **連接工廠**：用於建立與 JMS 提供者的連接。

### IBM WebSphere Application Server 中的佇列
在 IBM WAS 中，JMS 佇列被配置為伺服器訊息基礎架構內的資源。WAS 支援：
- **預設訊息提供者**：內建的 JMS 引擎，用於輕量級訊息傳遞。
- **與 IBM MQ 整合**：用於更強大、可擴展的佇列功能。

#### 配置基礎
在 WAS 中使用佇列：
1. **建立 JMS 匯流排**：用於訊息路由的伺服器邏輯分組。
2. **新增匯流排成員**：將應用程式伺服器加入匯流排。
3. **建立佇列目的地**：定義佇列（例如名稱、JNDI 綁定）並將其連結到匯流排。
4. **設定連接工廠**：供生產者/消費者連接使用。
5. **啟動規格**：用於訊息驅動 Bean (MDB) 自動從佇列消費訊息。

可以透過 WAS 管理控制台監控佇列的深度、存留時間和吞吐量。例如，您可以建立一個名為 `MyApp.Queue` 的佇列，並使用如 `jms/queue/MyQueue` 的 JNDI 名稱供程式碼查詢。

#### 使用範例
在銀行應用程式中，佇列可以處理交易請求：前端將訊息傳送到佇列，後端 MDB 一次處理一條訊息，確保沒有重複處理。

有關詳細設定，請參閱 IBM 的文件。

### 參考資料
- [為 WebSphere Application Server 配置 Java Message Service](https://www.ibm.com/docs/en/mfci/7.6.2?topic=clusters-configuring-jms-websphere-application-server)
- [WebSphere Application Server 中的佇列集合](https://www.ibm.com/docs/en/was/8.5.5?topic=s-queue-collection)