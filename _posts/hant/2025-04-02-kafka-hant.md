---
audio: false
generated: true
lang: hant
layout: post
title: 阿帕奇卡夫卡
translated: true
type: note
---

看來您的請求可能存在一些誤解。根據您之前關於 Redis 的提問以及本次提問的上下文，我推測您是想了解關於 **Apache Kafka**（分散式事件串流平台）的綜合指南，而非作家法蘭茲·卡夫卡。如果我理解有誤，請您澄清！目前，我將提供關於 Apache Kafka 的詳細指南。

---

### 什麼是 Apache Kafka？
Apache Kafka 是一個開源的分散式事件串流平台，專為高吞吐量、容錯且可擴展的即時資料處理而設計。最初由 LinkedIn 於 2010 年開發，並於 2011 年捐贈給 Apache 軟體基金會。Kafka 使用 Java 和 Scala 編寫，廣泛用於建置即時資料管道、串流應用程式和事件驅動架構。

主要特性：
- **分散式**：以叢集形式跨多台伺服器運行。
- **事件驅動**：即時處理事件串流。
- **持久性**：將資料持久儲存在磁碟上，並可配置保留策略。
- **可擴展**：每日可處理數萬億事件。

---

### 為什麼使用 Kafka？
Kafka 在需要即時資料處理和高可擴展性的場景中表現卓越。常見使用案例包括：
1. **訊息傳遞**：以更高的吞吐量和容錯能力取代傳統訊息代理（如 RabbitMQ）。
2. **活動追蹤**：即時追蹤使用者操作（如點擊、登入）。
3. **日誌匯總**：從多個來源收集日誌進行集中處理。
4. **串流處理**：支援即時分析或資料轉換。
5. **事件溯源**：記錄應用程式的狀態變更。
6. **指標收集**：監控系統或物聯網裝置。

---

### 主要功能
1. **核心元件**：
   - **主題**：發佈訊息（事件）的類別。
   - **分割區**：主題的細分，用於並行處理和擴展。
   - **生產者**：將訊息傳送至主題的應用程式。
   - **消費者**：從主題讀取訊息的應用程式。
   - **代理**：Kafka 叢集中的伺服器，負責儲存和管理資料。

2. **複製**：透過跨代理複製資料來確保容錯能力。
3. **保留策略**：可配置的資料保留策略（基於時間或大小）。
4. **Kafka Connect**：與外部系統（如資料庫、檔案）整合。
5. **Kafka Streams**：用於即時串流處理的函式庫。
6. **高吞吐量**：以低延遲（例如 2ms）每秒處理數百萬條訊息。

---

### 架構
Kafka 的架構圍繞分散式提交日誌建構：
- **叢集**：一組協同工作的代理。
- **主題與分割區**：訊息寫入主題，主題分割為多個分割區以實現負載平衡和擴展。每個分割區都是一個有序、不可變的日誌。
- **複製**：每個分割區有一個領導者和多個副本；若領導者故障，副本將接管。
- **偏移量**：分割區內訊息的唯一識別碼，允許消費者追蹤其讀取位置。
- **ZooKeeper（或 KRaft）**：傳統上，ZooKeeper 管理叢集中繼資料和協調。自 Kafka 3.3 起，KRaft（Kafka Raft）模式允許自我管理中繼資料，無需依賴 ZooKeeper。

---

### 安裝
以下是在 Linux 系統上安裝 Kafka 的步驟（假設已安裝 Java 8+）：

1. **下載 Kafka**：
   ```bash
   wget https://downloads.apache.org/kafka/3.7.0/kafka_2.13-3.7.0.tgz
   tar -xzf kafka_2.13-3.7.0.tgz
   cd kafka_2.13-3.7.0
   ```

2. **啟動 ZooKeeper**（若未使用 KRaft）：
   ```bash
   bin/zookeeper-server-start.sh config/zookeeper.properties
   ```

3. **啟動 Kafka 伺服器**：
   ```bash
   bin/kafka-server-start.sh config/server.properties
   ```

4. **建立主題**：
   ```bash
   bin/kafka-topics.sh --create --topic mytopic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
   ```

5. **驗證**：
   ```bash
   bin/kafka-topics.sh --list --bootstrap-server localhost:9092
   ```

對於 KRaft 模式（無需 ZooKeeper），生成叢集 ID 並調整 `config/kraft/server.properties`：
```bash
bin/kafka-storage.sh random-uuid
bin/kafka-storage.sh format -t <UUID> -c config/kraft/server.properties
bin/kafka-server-start.sh config/kraft/server.properties
```

---

### 基本操作
Kafka 使用命令列介面或用戶端函式庫。以下透過 `kafka-console-*` 工具示例：

#### 生產訊息
```bash
bin/kafka-console-producer.sh --topic mytopic --bootstrap-server localhost:9092
> Hello, Kafka!
> Another message
```

#### 消費訊息
```bash
bin/kafka-console-consumer.sh --topic mytopic --from-beginning --bootstrap-server localhost:9092
```
輸出：`Hello, Kafka!` `Another message`

#### 關鍵命令
- 列出主題：`bin/kafka-topics.sh --list --bootstrap-server localhost:9092`
- 描述主題：`bin/kafka-topics.sh --describe --topic mytopic --bootstrap-server localhost:9092`

---

### 使用 Kafka 編程
Kafka 透過用戶端函式庫支援多種語言。以下是使用 `kafka-python` 的 Python 示例：

1. **安裝函式庫**：
   ```bash
   pip install kafka-python
   ```

2. **生產者示例**：
   ```python
   from kafka import KafkaProducer

   producer = KafkaProducer(bootstrap_servers='localhost:9092')
   producer.send('mytopic', b'Hello, Kafka!')
   producer.flush()
   ```

3. **消費者示例**：
   ```python
   from kafka import KafkaConsumer

   consumer = KafkaConsumer('mytopic', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
   for message in consumer:
       print(message.value.decode('utf-8'))
   ```

---

### 進階概念
1. **消費者群組**：
   - 群組內的多個消費者共享分割區；每條訊息在群組內僅處理一次。
   - 示例：在消費者配置中設定 `group.id=mygroup`。

2. **複製與容錯**：
   - 設定 `replication-factor` > 1 以確保資料在代理故障時不會遺失。
   - 示例：`--replication-factor 3`。

3. **Kafka Streams**：
   - 即時處理資料（如聚合、連接）。
   - Java 示例：
     ```java
     StreamsBuilder builder = new StreamsBuilder();
     KStream<String, String> stream = builder.stream("mytopic");
     stream.foreach((key, value) -> System.out.println(value));
     ```

4. **Kafka Connect**：
   - 匯入/匯出資料（如從 MySQL 到 Kafka）。
   - 示例：使用 JDBC 來源連接器。

5. **保留與壓縮**：
   - `log.retention.hours=168`（預設 7 天）。
   - 日誌壓縮保留每個鍵的最新值。

---

### 效能優化技巧
1. **分割**：增加分割區以實現並行處理，但避免過度分割（例如每個主題 10-100 個）。
2. **批次處理**：調整 `batch.size` 和 `linger.ms` 以提高吞吐量。
3. **壓縮**：啟用 `compression.type=gzip`。
4. **監控**：使用 Kafka Manager 或 Prometheus + Grafana 等工具。

---

### 安全性
- **身份驗證**：啟用 SASL（例如 `sasl.mechanism=PLAIN`）。
- **授權**：透過 `kafka-acls.sh` 使用 ACL。
- **加密**：配置 SSL（`security.protocol=SSL`）。
- **限制存取**：在 `server.properties` 中綁定特定 IP。

---

### Kafka 與其他技術的比較
- **Kafka vs. RabbitMQ**：Kafka 提供更高的吞吐量和持久性；RabbitMQ 更適合傳統訊息傳遞。
- **Kafka vs. Redis**：Kafka 用於事件串流；Redis 用於記憶體快取/鍵值儲存。
- **Kafka vs. AWS Kinesis**：Kafka 需自行管理且更可自訂；Kinesis 為全託管服務。

---

### 限制
- **複雜性**：叢集配置和調優的學習曲線較陡峭。
- **資源密集**：需要大量記憶體和磁碟空間。
- **無原生查詢功能**：依賴外部工具（如 Kafka Streams）進行處理。

---

### 資源
- **官方網站**：[kafka.apache.org](https://kafka.apache.org)
- **文件**：[kafka.apache.org/documentation](https://kafka.apache.org/documentation)
- **Confluent**：[confluent.io](https://www.confluent.io)（教程、託管 Kafka 服務）

---

本指南涵蓋了 Kafka 的基礎知識及更多內容。如果您想深入了解特定領域（如叢集、Streams 或使用案例），請告訴我！