---
audio: false
generated: true
image: false
lang: hant
layout: post
title: WAS Spring JDBC 超時排查指南
translated: true
type: note
---

以下是運作模型與快速排查指南。

# 運作原理 (WAS + Spring + JDBC)

1. **DataSource 位於 WAS 中**

   * 您需在 WAS 管理控制台中定義 JDBC Provider 和 **DataSource**（通常全域交易使用 `XA`，或非 XA）。
   * WAS 負責管理 **JCA 連接池** 並分配 JDBC 連接。

2. **Spring 透過 JNDI 取得 DataSource**

   * 您的 Spring 應用程式會查詢伺服器的 DataSource（例如 `java:comp/env/jdbc/MyDS`）並對其進行封裝：

     * 純 JDBC：`JdbcTemplate` 使用該 DataSource。
     * JPA/Hibernate：`EntityManagerFactory` 使用它。
   * 交易通常為 **容器 JTA**（`WebSphereUowTransactionManager` 或標準 JTA）。Spring 的 `@Transactional` 會加入容器交易。

3. **呼叫路徑**

   * Web 請求 → WebContainer 執行緒 → Spring 服務 → 交易開始 (JTA) → 從 **WAS 池** 呼叫 `DataSource.getConnection()` → 透過驅動程式執行 SQL → 資料庫。
   * 逾時可能發生在多個層級（Spring、JPA、WAS 池、JTA 交易、JDBC 驅動程式/資料庫、網路）。

# 發生逾時時 — 識別類型

從四個面向思考。錯誤訊息/堆疊追蹤通常會告訴您是哪一種。

1. **連接取得逾時**
   症狀：等待池化連接。
   尋找關於池耗盡或 `J2CA0086W / J2CA0030E` 的訊息。
   常見調校參數：*Maximum Connections*、*Connection Timeout*、*Aged Timeout*、*Purge Policy*。

2. **交易逾時 (JTA)**
   症狀：`WTRN`/`Transaction` 訊息；類似 *「Transaction timed out after xxx seconds」* 的例外。
   常見調校參數：**Total transaction lifetime timeout**。即使資料庫仍在運作，也可能終止長時間的資料庫操作。

3. **查詢/陳述式逾時**
   症狀：`java.sql.SQLTimeoutException`、Hibernate/JPA 「query timeout」，或 Spring `QueryTimeoutException`。
   調校參數：

   * Spring：`JdbcTemplate.setQueryTimeout(...)`、Hibernate `javax.persistence.query.timeout` / `hibernate.jdbc.timeout`。
   * WAS DataSource 自訂屬性（DB2 範例）：`queryTimeout`、`queryTimeoutInterruptProcessingMode`。
   * 驅動程式/資料庫端的陳述式逾時。

4. **Socket/讀取逾時 / 網路問題**
   症狀：在長時間擷取過程中閒置一段時間後發生；低階 `SocketTimeoutException` 或供應商代碼。
   調校參數：驅動程式 `loginTimeout`/`socketTimeout`、防火牆/NAT 閒置設定、資料庫 keepalive。

# 檢查位置（依層級）

**WAS Admin Console 路徑 (傳統 WAS)**

* JDBC Provider / DataSource：
  資源 → JDBC → Data sources → *您的DS* →

  * *Connection pool properties*：**Connection timeout**、**Maximum connections**、**Reap time**、**Unused timeout**、**Aged timeout**、**Purge policy**。
  * *Custom properties*：供應商特定屬性（例如 DB2 的 `queryTimeout`、`currentSQLID`、`blockingReadConnectionTimeout`、`queryTimeoutInterruptProcessingMode`）。
  * *JAAS – J2C*（如果驗證別名有關）。
* Transactions：
  Application servers → *server1* → Container Settings → **Container Services → Transaction Service** → **Total transaction lifetime timeout**、**Maximum transaction timeout**。
* WebContainer：
  執行緒池大小（如果請求堆積）。

**日誌與追蹤**

* 傳統 WAS：`<profile_root>/logs/<server>/SystemOut.log` 和 `SystemErr.log`。
  關鍵元件：`RRA`（資源配接器）、`JDBC`、`ConnectionPool`、`WTRN`（交易）。
  啟用追蹤（簡潔起始設定）：

  ```
  RRA=all:WTRN=all:Transaction=all:JDBC=all:ConnectionPool=all
  ```

  尋找：

  * `J2CA0086W`、`J2CA0114W`（池/連接問題）
  * `WTRN0037W`、`WTRN0124I`（交易逾時/回滾）
  * 帶有供應商 SQL 代碼的 `DSRA`/`SQL` 例外。
* Liberty：`wlp/usr/servers/<server>/logs/` 下的 `messages.log`。

**PMI / 監控**

* 為 JDBC Connection Pools 和 Transaction 指標啟用 **PMI**。監控：

  * 池大小、使用中計數、等待者、等待時間、逾時。
  * 交易逾時/回滾計數。

**Spring/JPA 應用程式日誌**

* 在應用程式中啟用 SQL + 計時（`org.hibernate.SQL`、`org.hibernate.type`、Spring JDBC debug）以對持續時間與逾時進行關聯分析。

**資料庫與驅動程式**

* DB2：`db2diag.log`、`MON_GET_PKG_CACHE_STMT`、活動事件監視器、陳述式層級逾時。
* WAS DataSource 或 `DriverManager` 中的驅動程式屬性（如果在 WAS 上未使用容器 DS，則不典型）。

**網路**

* 具有閒置逾時的中介裝置。作業系統 keepalive / 驅動程式 keepalive 設定。

# 快速排查流程

1. **分類逾時類型**

   * *連接等待？* 尋找 `J2CA` 池警告。如果是，增加 **Maximum connections**、修復洩漏、調校池、對於中毒事件設定 **Purge Policy = EntirePool**。
   * *交易逾時？* `WTRN` 訊息。增加 **Total transaction lifetime timeout** 或減少每個交易的工作量；避免將大型批次作業包在單一交易中。
   * *查詢逾時？* `SQLTimeoutException` 或 Spring/Hibernate `QueryTimeout`。將 **Spring/Hibernate** 逾時與 **WAS DS** 和 **DB** 逾時對齊；避免設定衝突。
   * *Socket/讀取逾時？* 網路/驅動程式訊息。檢查驅動程式的 `socketTimeout`/`loginTimeout`、資料庫 keepalive 和防火牆。

2. **關聯時間點**

   * 比較失敗持續時間與設定的閾值（例如「在 ~30 秒時失敗」→ 尋找任何 30 秒的設定：Spring 查詢逾時 30 秒？交易生命週期逾時 30 秒？池等待 30 秒？）。

3. **檢查池健康狀態**

   * PMI：**waiters** 是否 > 0？**in-use** 是否接近 **max**？有長時間持有的連接嗎？考慮啟用 **connection leak detection**（RRA 追蹤顯示誰取走了連接）。

4. **資料庫可見性**

   * 在資料庫上確認：陳述式是否仍在執行？是否被取消？有任何鎖定等待嗎？如果有鎖定 → 考慮鎖定逾時與陳述式逾時。

# 實用調校參數與注意事項 (WAS + DB2 範例)

* **Total transaction lifetime timeout**（伺服器層級）會終止長時間查詢，即使您設定了更高的 Spring/Hibernate 逾時。請保持這些設定一致。
* **queryTimeoutInterruptProcessingMode**（DB2 的 DataSource 自訂屬性）：控制 DB2 應如何中斷逾時的查詢（協同/強制）。有助於避免執行緒在逾時後卡住。
* **Purge policy**：`EntirePool` 可以從嚴重的 SQL 狀態（例如資料庫重啟）中更快恢復，但代價是會有一個小波動。
* **Aged/Unused timeout**：淘汰過時的連接以避免防火牆/NAT 閒置問題。
* **Validation**：啟用 **validation by SQL** 或 **validation timeout**，以便在使用前檢測到失效的連接。
* **Thread pools**：如果 WebContainer 執行緒飽和，*症狀會類似逾時*。確保 WebContainer 和 Default 執行緒池的大小設定適當。

# 最小 Spring 設定範例

**JNDI DataSource (XML)**

```xml
<jee:jndi-lookup id="dataSource" jndi-name="java:comp/env/jdbc/MyDS" expected-type="javax.sql.DataSource"/>
<bean id="txManager" class="org.springframework.transaction.jta.JtaTransactionManager"/>
<tx:annotation-driven transaction-manager="txManager"/>
```

**JdbcTemplate 查詢逾時 (Java)**

```java
@Bean JdbcTemplate jdbcTemplate(DataSource ds) {
  JdbcTemplate jt = new JdbcTemplate(ds);
  jt.setQueryTimeout(60); // 秒
  return jt;
}
```

**Hibernate/JPA 逾時**

```properties
javax.persistence.query.timeout=60000  # 毫秒
hibernate.jdbc.timeout=60              # 秒
```

# 提報問題時需提供的資訊

* 確切的例外文字 + 堆疊追蹤。
* 時間戳記：請求開始、交易開始、查詢開始、錯誤發生時間。
* WAS DS 池配置（截圖或數值）、Transaction Service 逾時設定。
* PMI 快照（池等待者、使用中數量、逾時計數）。
* 失敗時資料庫的工作階段/陳述式視圖。
* 網路拓撲備註（防火牆、代理、閒置計時器）。

如果您貼上特定的例外片段（J2CA/WTRN/SQL 狀態），我可以精確定位到具體層級以及對應需要調整的設定。