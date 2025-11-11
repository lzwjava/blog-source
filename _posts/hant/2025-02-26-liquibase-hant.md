---
audio: false
generated: true
lang: hant
layout: post
title: Liquibase：數據庫結構管理
translated: true
type: note
---

這是一份關於如何在 Spring Boot 應用程式中使用 **Liquibase** 來有效管理數據庫結構變更的完整指南：

---

### 1. 添加 Liquibase 依賴
首先，您需要在專案中加入 Liquibase 依賴。如果您使用 **Maven**，請在 `pom.xml` 中加入：

```xml
<dependency>
    <groupId>org.liquibase</groupId>
    <artifactId>liquibase-core</artifactId>
</dependency>
```

如果您使用 **Gradle**，請在 `build.gradle` 中加入：

```groovy
implementation 'org.liquibase:liquibase-core'
```

這會將 Liquibase 核心函式庫加入您的專案。

---

### 2. 配置 Liquibase
Liquibase 使用 **changelog 檔案** 來管理數據庫結構變更。預設情況下，Spring Boot 會在 classpath 中尋找名為 `db/changelog/db.changelog-master.yaml`、`db/changelog/db.changelog-master.xml` 或 `db/changelog/db.changelog-master.sql` 的檔案。您可以透過在 `application.properties`（或 `application.yml`）中加入以下屬性來自訂此位置：

```properties
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

這會告訴 Spring Boot 您的 changelog 檔案位置。

---

### 3. 建立 Changelog 檔案
Changelog 檔案定義了您要應用於數據庫的變更。您可以使用 XML、YAML 或 SQL 格式編寫。以下是一個位於 `src/main/resources/db/changelog/db.changelog-master.xml` 的 **XML changelog** 檔案範例：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog
    xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
        http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-3.8.xsd">

    <changeSet id="1" author="your-name">
        <createTable tableName="users">
            <column name="id" type="int">
                <constraints primaryKey="true" nullable="false"/>
            </column>
            <column name="username" type="varchar(255)"/>
            <column name="email" type="varchar(255)"/>
        </createTable>
    </changeSet>

</databaseChangeLog>
```

此範例建立了一個包含三個欄位（`id`、`username` 和 `email`）的 `users` 資料表。每個 `<changeSet>` 代表一組要應用的變更。

---

### 4. 運行 Spring Boot 應用程式
當您啟動 Spring Boot 應用程式時，Liquibase 會自動：
- 讀取 changelog 檔案。
- 檢查哪些 changeset 已被應用（記錄在名為 `DATABASECHANGELOG` 的資料表中）。
- 對您的數據庫執行任何新的 changeset。

無需額外程式碼——Spring Boot 的自動配置會為您處理。

---

### 5. 自訂 Liquibase（可選）
您可以使用 `application.properties` 中的屬性來調整 Liquibase 的行為。以下是一些常用選項：

```properties
spring.liquibase.enabled=true          # 啟用或停用 Liquibase
spring.liquibase.drop-first=false      # 在應用變更前刪除數據庫（請謹慎使用）
spring.liquibase.contexts=dev,prod     # 僅在特定環境中運行 changeset
```

這些設定可讓您根據環境或工作流程調整 Liquibase。

---

### 6. 運用進階功能
Liquibase 提供強大的功能來增強結構管理：
- **Contexts 與 Labels**：控制哪些 changeset 在特定環境中運行（例如 `dev` 與 `prod`）。
- **Preconditions**：確保在應用 changeset 前符合特定條件（例如資料表存在）。
- **Rollbacks**：定義如何撤銷 changeset（如有需要）。
- **Refactoring**：使用內建支援處理複雜的數據庫變更（例如重新命名欄位）。

例如，為 changeset 加入 context：

```xml
<changeSet id="2" author="your-name" context="dev">
    <addColumn tableName="users">
        <column name="created_at" type="timestamp"/>
    </addColumn>
</changeSet>
```

此 changeset 僅在 `dev` context 中運行。

---

### 7. 使用記憶體數據庫進行測試
為了測試，可將 Liquibase 與 H2 等記憶體數據庫搭配使用。加入 H2 依賴：

```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>
```

然後為測試配置 `application.properties`：

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

Liquibase 會在測試期間將您的變更應用到記憶體數據庫。

---

### 8. 將 Changelog 納入版本控制
將您的 changelog 檔案與應用程式代碼一起儲存在版本控制系統（例如 Git）中。這可確保您的數據庫結構與代碼庫同步演進，使部署和回滾更加可預測。

---

### 總結
在 Spring Boot 應用程式中使用 Liquibase 的步驟：
1. 加入 Liquibase 依賴。
2. 配置 changelog 檔案位置。
3. 建立包含數據庫變更的 changelog 檔案。
4. 運行應用程式——Liquibase 會處理後續工作。

Liquibase 是一個強大的工具，能以結構化、版本控制的方式管理數據庫結構變更，並與 Spring Boot 無縫整合。