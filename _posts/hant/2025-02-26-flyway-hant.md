---
audio: false
generated: true
lang: hant
layout: post
title: Spring Boot 中使用 Flyway 進行數據庫遷移
translated: true
type: note
---

這是一份簡明實用的指南，說明如何在 Spring Boot 應用程式中使用 Flyway 來管理資料庫結構：

---

### 什麼是 Flyway？
Flyway 是一款資料庫遷移工具，可協助您對資料庫結構進行版本控制。它會按特定順序執行 SQL 指令碼（遷移）來演進資料庫，非常適合需要保持一致性與自動化的 Spring Boot 專案。

---

### 步驟 1：加入 Flyway 相依性
首先，將 Flyway 加入您的專案。若使用 **Maven**，請更新 `pom.xml`：

```xml
<dependency>
    <groupId>org.flywaydb</groupId>
    <artifactId>flyway-core</artifactId>
</dependency>
```

若使用 **Gradle**，請在 `build.gradle` 中加入：

```groovy
implementation 'org.flywaydb:flyway-core'
```

這會將 Flyway 引入您的 Spring Boot 應用程式。

---

### 步驟 2：設定資料庫連線
Flyway 需要知道要管理哪個資料庫。請在 `application.properties`（或 `application.yml`）中定義資料庫連線。以 PostgreSQL 為例：

```properties
spring.datasource.url=jdbc:postgresql://localhost:5432/mydb
spring.datasource.username=myuser
spring.datasource.password=mypassword
```

Spring Boot 會自動設定 Flyway 使用此資料來源，因此無需額外設定。

---

### 步驟 3：建立遷移指令碼
Flyway 使用版本化 SQL 指令碼來更新資料庫。請將這些指令碼放置在預設目錄：`src/main/resources/db/migration`。每個指令檔名必須遵循此命名模式：`V<版本號>__<描述>.sql`。版本號可確保遷移按順序執行。

例如，建立名為 `V1__create_users_table.sql` 的檔案：

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);
```

將其儲存於 `src/main/resources/db/migration`。

---

### 步驟 4：執行應用程式
啟動您的 Spring Boot 應用程式（例如透過 `mvn spring-boot:run` 或 IDE）。Flyway 將會：
- 檢查資料庫中的遷移歷史記錄
- 依序套用所有待處理的遷移（例如 `V1__create_users_table.sql`）

由於 Spring Boot 的整合，這會在啟動時自動完成，無需手動介入。

---

### 步驟 5：自訂 Flyway（可選）
您可以在 `application.properties` 中透過屬性調整 Flyway 的行為。以下是一些常用選項：

```properties
spring.flyway.locations=classpath:db/migration  # 指令碼位置
spring.flyway.baseline-on-migrate=true          # 處理現有資料庫
spring.flyway.enabled=true                      # 開關 Flyway
```

這些設定可讓您根據專案需求調整 Flyway。

---

### 進階功能
Flyway 不僅提供基本遷移功能：
- **Java 遷移**：可編寫 Java 遷移指令碼處理複雜邏輯
- **可重複遷移**：使用 `R__<描述>.sql` 作為變更時重新執行的指令碼（例如視圖）
- **復原遷移**：可回滾變更（需 Flyway Pro）

詳情請查閱 [Flyway 官方文件](https://flywaydb.org/documentation/)。

---

### 總結
在 Spring Boot 中使用 Flyway 的步驟：
1. 將 Flyway 相依性加入專案
2. 在 `application.properties` 中設定資料庫連線
3. 在 `src/main/resources/db/migration` 中編寫版本化 SQL 指令碼
4. 啟動應用程式 — Flyway 將自動套用遷移

Flyway 透過版本控制與自動化簡化了資料庫結構管理，完美契合 Spring Boot 的流暢開發體驗。