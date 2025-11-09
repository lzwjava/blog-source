---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Java 訊息系統概覽
translated: true
type: note
---

### 什麼是 Java 中的訊息系統？

Java 中的訊息系統實現了應用程式、服務或組件之間的異步通訊。與直接同步呼叫（如方法調用）不同，訊息被發送到中央中介層（**訊息代理**或**佇列**），隨後由接收方處理。這種方式解耦了生產者（發送方）和消費者（接收方），提升了分散式系統的可擴展性、容錯性和可靠性。

主要優勢：
- **異步處理**：生產者無需等待立即回應，實現非阻塞操作。
- **負載平衡**：訊息可分配給多個消費者處理。
- **可靠性**：訊息可持續保存直至被確認，即使遇到系統崩潰或網路問題也不遺失。
- **解耦**：系統中某部分的變更不會影響其他部分。

常見應用場景包括微服務通訊、事件驅動架構、任務佇列（如後台作業）以及整合舊有系統。

#### JMS（Java Message Service）：標準 API
JMS 是 Java EE（現為 Jakarta EE）規範的一部分，提供了與訊息系統交互的廠商中立 API。它抽象了底層代理（如 Apache ActiveMQ、RabbitMQ、IBM MQ），使你的程式碼能在不同實現中通用。

JMS 支援兩種主要**訊息傳遞領域**：
- **點對點（PTP）**：使用佇列。一個生產者發送至佇列；一個消費者接收（先進先出）。適合任務分配。
- **發布-訂閱（Pub/Sub）**：使用主題。生產者發布至主題；多個訂閱者接收副本。適合事件廣播。

##### 核心組件
- **ConnectionFactory**：建立與代理的連線。
- **Connection**：管理與代理的會話。
- **Session**：處理交易和訊息建立。
- **Destination**：訊息發送的佇列或主題。
- **MessageProducer**：發送訊息至目的地。
- **MessageConsumer**：從目的地接收訊息。
- **Message**：承載內容，包含標頭（如優先級、時間戳）和屬性。

訊息可以是文字、物件、映射或串流。

##### 簡單範例
以下是使用佇列的基本 JMS 生產者和消費者（偽代碼；需 JMS 提供者如 ActiveMQ）。

**生產者（發送方）**：
```java
import javax.jms.*;

public class JMSProducer {
    public static void main(String[] args) throws JMSException {
        ConnectionFactory factory = new ActiveMQConnectionFactory("tcp://localhost:61616");
        Connection connection = factory.createConnection();
        connection.start();
        Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
        Queue queue = session.createQueue("exampleQueue");
        MessageProducer producer = session.createProducer(queue);
        
        TextMessage message = session.createTextMessage("Hello, JMS!");
        producer.send(message);
        
        producer.close();
        session.close();
        connection.close();
    }
}
```

**消費者（接收方）**：
```java
import javax.jms.*;

public class JMSConsumer {
    public static void main(String[] args) throws JMSException {
        ConnectionFactory factory = new ActiveMQConnectionFactory("tcp://localhost:61616");
        Connection connection = factory.createConnection();
        connection.start();
        Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
        Queue queue = session.createQueue("exampleQueue");
        MessageConsumer consumer = session.createConsumer(queue);
        
        consumer.setMessageListener(msg -> {
            try {
                System.out.println("Received: " + ((TextMessage) msg).getText());
            } catch (JMSException e) {
                e.printStackTrace();
            }
        });
        
        // 保持運行以監聽訊息
        try { Thread.sleep(5000); } catch (InterruptedException e) {}
        consumer.close();
        session.close();
        connection.close();
    }
}
```

運行此代碼需添加 JMS 依賴（例如透過 Maven：`javax.jms:javax.jms-api` 及 ActiveMQ 客戶端）。

##### 現代替代方案
儘管 JMS 是基礎，Java 開發者常使用更輕量級的框架：
- **Spring Boot with JMS**：簡化配置。
- **Apache Kafka**：適用於高吞吐量串流處理（不完全符合 JMS 標準但可整合）。
- **RabbitMQ/AMQP**：基於協議，提供 Java 客戶端。

深入學習可查閱官方 Jakarta JMS 文檔。

[Jakarta Messaging 規範](https://jakarta.ee/specifications/messaging/)  
[ActiveMQ 文檔](https://activemq.apache.org/)