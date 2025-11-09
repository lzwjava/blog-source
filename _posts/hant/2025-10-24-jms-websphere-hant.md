---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: WebSphere Application Server 中的 JMS
translated: true
type: note
---

### IBM WebSphere Application Server (WAS) 中的 JMS 運作原理

JMS（Java Message Service）是一個標準 API，用於以解耦、非同步的方式在 Java 應用程式之間傳送和接收訊息。在 WAS 中，JMS 是透過**預設訊息提供者**來實現的，該提供者使用**服務整合匯流排 (SIBus)** 作為其底層訊息引擎。SIBus 是一個內建、可擴展的匯流排，負責處理訊息路由、佇列和傳遞，無需外部軟體。

#### 關鍵組件與流程
1. **服務整合匯流排 (SIBus)**：這是核心基礎架構。它就像一個虛擬網絡，訊息引擎（每個伺服器或叢集一個）在其中處理訊息。您可以建立一個匯流排，將伺服器添加為成員，並在其上定義目的地（佇列或主題）。
   
2. **連線工廠**：作為入口點。您的 Java 應用程式透過 JNDI（例如 `jms/MyConnectionFactory`）查找此工廠，以建立與 SIBus 的 JMS 連線。

3. **目的地（佇列/主題）**：佇列用於點對點訊息傳遞（一個傳送者，一個接收者）。一旦建立並綁定到匯流排，它們就會持久儲存訊息（使用檔案儲存或資料庫，可配置）。

4. **訊息流程**：
   - **傳送**：應用程式透過連線工廠建立 JMS 工作階段，透過 JNDI 取得佇列參考，並傳送訊息（例如 `TextMessage`）。SIBus 將其路由到目標訊息引擎，該引擎將其放入佇列。
   - **接收**：消費者（例如另一個應用程式或 Message-Driven Bean）以類似方式連接，並輪詢或監聽訊息。SIBus 可靠地傳遞訊息，處理重試、確認和交易。
   - SIBus 支援叢集以實現高可用性、負載平衡，以及用於與其他系統整合的外部匯流排連結。

WAS 管理生命週期：啟動/停止引擎、監控佇列，並根據您的配置（例如持久性與非持久性訊息）確保耐久性。

#### 建立 JMS 佇列是否啟用 Java 應用程式傳送/接收訊息？
是的，正是如此。設定完成後（如前所述：匯流排、成員、連線工廠、佇列），您的 Java 應用程式可以：
- 使用標準 JMS API (`javax.jms.*`) 傳送/接收。
- 在應用程式伺服器上下文中透過 JNDI 查找資源。
- 傳送訊息的範例程式碼片段：
  ```java
  InitialContext ctx = new InitialContext();
  QueueConnectionFactory qcf = (QueueConnectionFactory) ctx.lookup("jms/MyConnectionFactory");
  Queue queue = (Queue) ctx.lookup("jms/MyQueue");
  QueueConnection conn = qcf.createQueueConnection();
  QueueSession session = conn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
  QueueSender sender = session.createSender(queue);
  TextMessage msg = session.createTextMessage("Hello JMS!");
  sender.send(msg);
  // 關閉資源...
  ```
接收訊息類似，使用 `QueueReceiver` 或 MDB。無需為匯流排編寫自訂程式碼——所有這些都被抽象化了。

#### WAS 是否正確處理佇列？
絕對正確。SIBus 負責：
- **持久性**：訊息在重啟後仍然保留（檔案/資料庫儲存）。
- **可靠性**：保證傳遞，失敗時使用死信佇列。
- **可擴展性**：處理高吞吐量、叢集。
- **監控**：在管理控制台中查看統計資料（例如訊息計數、積壓）。
如果出現問題（例如佇列已滿），可以查看日誌和警報。它已為企業使用做好生產準備。

#### 我們是否需要像 Kafka 這樣的額外外掛？
不需要，無需類似 Kafka 的東西——SIBus 完全整合到 WAS 中（除了 WAS 本身之外，無需單獨安裝或授權）。Kafka 是一個不同的分散式串流平台；SIBus 是 JMS 專用的，對於 WAS 應用程式來說更簡單。如果您需要類似 Kafka 的功能（例如串流），可以透過外部匯流排連結進行整合，但對於標準的 JMS 佇列，請堅持使用預設提供者。

如需深入了解，請查閱 IBM 文件：[使用預設訊息提供者管理訊息傳遞](https://www.ibm.com/docs/en/was/9.0.5?topic=resources-managing-messaging-default-messaging-provider) 和 [JMS 應用程式如何連接到匯流排上的訊息引擎](https://www.ibm.com/docs/en/was-nd/8.5.5?topic=messaging-how-jms-applications-connect-engine-bus)。