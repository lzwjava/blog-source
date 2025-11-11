---
audio: false
generated: true
lang: hant
layout: post
title: 在 Java 中使用 Apache Kafka
translated: true
type: note
---

在 Java 中使用 Apache Kafka 需要在應用程式中設定 Kafka 客戶端來生產和消費訊息。Kafka 是一個分散式串流平台，其 Java 客戶端函式庫讓整合變得簡單直接。以下我將引導您完成基本入門步驟。

首先，您需要設定環境。請確保已在您的系統或伺服器上安裝並執行 Kafka。您可以從 Apache Kafka 官方網站下載，並使用提供的腳本啟動 ZooKeeper 和 Kafka 伺服器。為簡化說明，我假設您使用預設設定在本機運行 Kafka（例如使用 `localhost:9092` 作為引導伺服器）。

接下來，將 Kafka 客戶端依賴項加入您的 Java 專案。若使用 Maven，請在 `pom.xml` 中加入以下內容：

```xml
<dependency>
    <groupId>org.apache.kafka</groupId>
    <artifactId>kafka-clients</artifactId>
    <version>3.6.0</version> <!-- 請使用最新版本 -->
</dependency>
```

現在讓我們編寫一些程式碼。我將示範如何建立簡單的生產者和消費者。

### Kafka 生產者範例
生產者會向 Kafka 主題發送訊息。以下是基本範例：

```java
import org.apache.kafka.clients.producer.*;
import java.util.Properties;

public class SimpleProducer {
    public static void main(String[] args) {
        // 設定生產者屬性
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092"); // Kafka 伺服器位址
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        // 建立生產者實例
        try (Producer<String, String> producer = new KafkaProducer<>(props)) {
            // 傳送訊息至名為 "test-topic" 的主題
            String topic = "test-topic";
            for (int i = 0; i < 10; i++) {
                String key = "key" + i;
                String value = "Hello, Kafka " + i;
                ProducerRecord<String, String> record = new ProducerRecord<>(topic, key, value);

                producer.send(record, (metadata, exception) -> {
                    if (exception == null) {
                        System.out.println("Sent message: " + value + " to partition " + metadata.partition());
                    } else {
                        exception.printStackTrace();
                    }
                });
            }
        }
    }
}
```

此程式碼中：
- `bootstrap.servers` 指定 Kafka 運行位置
- 序列化器定義了鍵與值（此處皆為字串）如何轉換為位元組
- `ProducerRecord` 代表訊息，`send()` 透過回呼機制非同步發送並處理成功或失敗狀態

### Kafka 消費者範例
消費者會訂閱主題並讀取訊息。以下是範例：

```java
import org.apache.kafka.clients.consumer.*;
import java.util.Collections;
import java.util.Properties;

public class SimpleConsumer {
    public static void main(String[] args) {
        // 設定消費者屬性
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("group.id", "test-group"); // 消費者群組 ID
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("auto.offset.reset", "earliest"); // 從主題起始點開始讀取

        // 建立消費者實例
        try (KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props)) {
            // 訂閱主題
            consumer.subscribe(Collections.singletonList("test-topic"));

            // 輪詢訊息
            while (true) {
                ConsumerRecords<String, String> records = consumer.poll(1000); // 逾時設定（毫秒）
                for (ConsumerRecord<String, String> record : records) {
                    System.out.printf("Received: key=%s, value=%s, partition=%d, offset=%d%n",
                            record.key(), record.value(), record.partition(), record.offset());
                }
            }
        }
    }
}
```

此處：
- `group.id` 用於識別協調用的消費者群組
- 反序列化器將位元組資料轉回字串
- `poll()` 在迴圈中獲取訊息，`auto.offset.reset` 確保在無提交偏移量時從最早訊息開始讀取

### 執行程式碼
1. **啟動 Kafka**：確保 ZooKeeper 與 Kafka 正在運行（例如在類 Unix 系統使用 `bin/zookeeper-server-start.sh config/zookeeper.properties` 與 `bin/kafka-server-start.sh config/server.properties`）
2. **建立主題**：使用 Kafka 命令列工具建立 `test-topic`（若不存在）：`bin/kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`
3. **執行生產者**：運行 `SimpleProducer` 類別來發送訊息
4. **執行消費者**：運行 `SimpleConsumer` 類別來查看訊息消費情況

### 實用提示
- **錯誤處理**：在正式環境程式碼中請加入 try-catch 區塊或日誌記錄
- **組態設定**：根據需求調整如 `acks`（生產者可靠性）或 `max.poll.records`（消費者批次大小）等屬性
- **函式庫**：複雜應用可考慮使用 Spring Kafka 來簡化組態與使用

這是幫助您入門的基本設定。若想深入了解特定功能如分區、錯誤處理或與大型應用整合，請隨時告訴我！