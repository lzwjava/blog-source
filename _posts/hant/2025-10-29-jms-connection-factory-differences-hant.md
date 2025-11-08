---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: JMS 連接工廠差異
translated: true
type: note
---

在 IBM WebSphere Application Server (WAS) 中，連接工廠（connection factories）和佇列連接工廠（queue connection factories）都是用於建立與 JMS 提供者連接的 JMS（Java Message Service）資源，以實現訊息傳遞。然而，它們在適用範圍、API 相容性以及基於 JMS 領域模型（點對點與發佈/訂閱）的使用方式上有所不同。以下為詳細說明：

### 主要差異

| 面向                  | 連接工廠                                                                 | 佇列連接工廠                                                                 |
|-----------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **主要用途**          | 建立與目的地的 JMS 連接，用於**同時**支援點對點（佇列）和發佈/訂閱（主題）訊息傳遞。支援 JMS 1.1 引入的統一「經典」API。 | **專門**為點對點訊息傳遞與佇列建立 JMS 連接。基於 JMS 1.0 的舊有領域特定 API。 |
| **API 層級結構**      | 基礎介面（`javax.jms.ConnectionFactory`）。可動態建立 `Queue` 或 `Topic` 目的地，並在同一連接/工作階段中處理。 | `ConnectionFactory` 的子類（`javax.jms.QueueConnectionFactory`）。僅建立 `QueueConnection` 和 `QueueSession` 物件；無法處理主題。 |
| **靈活性**            | 對現代應用程式更為靈活。允許在同一交易/工作單元中混合佇列和主題操作（JMS 1.1+）。適用於需要在不重新配置的情況下切換訊息傳遞風格的程式碼。 | 靈活性較低；僅限於佇列。適用於舊版 JMS 1.0 程式碼或僅需點對點傳遞的嚴格職責分離場景。 |
| **在 WAS 中的配置**    | 在管理主控台的 **Resources > JMS > Connection factories** 下配置。與 JMS 提供者關聯（例如預設訊息傳遞、WebSphere MQ）。 | 在 **Resources > JMS > Queue connection factories** 下配置。僅與佇列特定提供者（如 IBM MQ 或預設訊息傳遞）綁定，用於點對點傳遞。 |
| **使用時機**          | 建議用於新開發或使用 JMS 1.1+ 的應用程式。當應用程式可能需要同時與佇列和主題互動時使用。 | 用於與 JMS 1.0 領域特定程式碼向後相容，或明確限制僅使用佇列時（例如在 WebSphere MQ 設置中為了效能/安全隔離）。 |
| **效能/安全性**       | 通常相當，但跨領域使用可能需要額外設置。 | 可針對僅佇列使用進行優化（例如在 MQ 中使用綁定傳輸以提高吞吐量，約 30% 的提升）。 |

### 程式碼使用範例
- **使用連接工廠**（統一、靈活）：
  ```java
  ConnectionFactory factory = (ConnectionFactory) context.lookup("jms/ConnectionFactory");
  Connection conn = factory.createConnection();
  Session session = conn.createSession(false, Session.AUTO_ACKNOWLEDGE);
  // 可建立以下任一項：
  Queue queue = session.createQueue("myQueue");
  Topic topic = session.createTopic("myTopic");
  ```

- **使用佇列連接工廠**（僅限佇列）：
  ```java
  QueueConnectionFactory qFactory = (QueueConnectionFactory) context.lookup("jms/QueueConnectionFactory");
  QueueConnection qConn = qFactory.createQueueConnection();
  QueueSession qSession = qConn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
  Queue queue = qSession.createQueue("myQueue");
  // 此處無法建立主題。
  ```

總結而言，在 WAS 上的現代 JMS 應用程式中，為追求多功能性應選擇通用連接工廠，而佇列連接工廠則是針對以佇列為中心或舊有場景的專門保留選項。

[連接工廠集合 - IBM](https://www.ibm.com/docs/en/was-nd/8.5.5?topic=settings-connection-factory-collection)  
[佇列連接工廠集合 - IBM](https://www.ibm.com/docs/en/was-nd/8.5.5?topic=settings-queue-connection-factory-collection)  
[JMS QueueConnectionFactory 與 ConnectionFactory - Stack Overflow](https://stackoverflow.com/questions/30121654/jms-queueconnectionfactory-vs-connectionfactory)  
[佇列連接工廠 VS 連接工廠 - MQSeries.net](https://mqseries.net/phpBB/viewtopic.php?p=102901)