---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 整合 Liquibase 與 Spring Boot
translated: true
type: note
---

## 整合 Liquibase 與 Spring Boot

Liquibase 是一個流行的開源工具，用於以版本控制的方式管理數據庫結構變更（遷移）。Spring Boot 為 Liquibase 提供了出色的自動配置支持，使其易於整合。本指南假設您使用 Spring Boot 3.x（截至 2025 年最新版本）與 Maven，但概念同樣適用於 Gradle。我們將逐步介紹基礎知識。

### 先決條件
- 已設置好的 Spring Boot 專案（例如透過 Spring Initializr）。
- 已在 `application.properties` 中配置的數據庫（例如測試用 H2，生產環境用 PostgreSQL/MySQL）。

### 步驟 1：添加 Liquibase 依賴
在您的 `pom.xml` 中包含 Liquibase Spring Boot starter。這將引入 Liquibase 並無縫整合。

```xml
<dependency>
    <groupId>org.liquibase</groupId>
    <artifactId>liquibase-core</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-jdbc</artifactId> <!-- 用於數據庫連接 -->
</dependency>
```

對於 Gradle，請添加到 `build.gradle`：
```groovy
implementation 'org.liquibase:liquibase-core'
implementation 'org.springframework.boot:spring-boot-starter-jdbc'
```

執行 `mvn clean install`（或 `./gradlew build`）以下載依賴項。

### 步驟 2：配置 Liquibase
如果您將變更日誌文件放在預設位置，Spring Boot 會自動檢測 Liquibase。可透過 `application.properties`（或等效的 `.yml` 文件）進行自定義。

範例 `application.properties`：
```properties
# 數據庫設置（根據您的數據庫調整）
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driver-class-name=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=

# Liquibase 配置
spring.liquibase.change-log=classpath:db/changelog/db.changelog-master.xml
spring.liquibase.enabled=true  # 預設為 true
spring.liquibase.drop-first=false  # 在開發環境中設置為 true 以在啟動時刪除結構描述
```

- `change-log`：您的主變更日誌文件的路徑（預設：`db/changelog/db.changelog-master.xml`）。
- 使用 `spring.liquibase.enabled` 啟用/停用。
- 對於上下文/配置文件，使用 `spring.liquibase.contexts=dev` 來執行特定變更。

### 步驟 3：建立變更日誌文件
Liquibase 使用「變更日誌」來定義結構描述變更。在 `src/main/resources` 下建立目錄結構：
```
src/main/resources/
└── db/
    └── changelog/
        ├── db.changelog-master.xml  # 包含其他文件的主文件
        └── changes/
            ├── 001-create-users-table.xml  # 單獨的變更
            └── 002-add-email-column.xml
```

#### 主變更日誌 (`db.changelog-master.xml`)
此文件包含其他變更日誌：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog
    xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
                        http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.24.xsd">

    <include file="changes/001-create-users-table.xml"/>
    <include file="changes/002-add-email-column.xml"/>
</databaseChangeLog>
```

#### 範例變更 (`001-create-users-table.xml`)
定義一個建立表格的變更：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
                                       http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.24.xsd">

    <changeSet id="001" author="yourname">
        <createTable tableName="users">
            <column name="id" type="bigint">
                <constraints primaryKey="true" nullable="false"/>
            </column>
            <column name="name" type="varchar(255)">
                <constraints nullable="false"/>
            </column>
        </createTable>
    </changeSet>
</databaseChangeLog>
```

- 使用 XML、YAML、JSON 或 SQL 格式作為變更日誌。
- 每個 `<changeSet>` 是一個遷移，具有 ID（用於追蹤）。
- 執行 `java -jar target/your-app.jar` 以啟動應用程式 — Liquibase 會在啟動時自動應用變更。

### 步驟 4：執行與測試
- **啟動時**：Spring Boot 在您的應用程式完全啟動之前執行 Liquibase。
- **回滾**：使用 `spring.liquibase.rollback-file` 或 CLI 進行測試。
- **CLI 整合**：對於手動執行，添加 Liquibase Maven 插件：
  ```xml
  <plugin>
      <groupId>org.liquibase</groupId>
      <artifactId>liquibase-maven-plugin</artifactId>
      <version>4.24.0</version>
      <configuration>
          <changeLogFile>src/main/resources/db/changelog/db.changelog-master.xml</changeLogFile>
          <url>jdbc:h2:mem:testdb</url>
          <username>sa</username>
          <password></password>
      </configuration>
  </plugin>
  ```
  然後執行 `mvn liquibase:update`。

- **驗證**：啟用 `spring.liquibase.validate-on-migrate=true` 以檢查變更日誌。

### 常見提示
- **配置文件**：如有需要，在 bean 上使用 `@Profile("dev")`，但除非進行過濾，否則 Liquibase 會全域執行。
- **前置條件**：在變更集中添加 `<preConditions>` 以檢查數據庫狀態。
- **SQL 格式**：對於原始 SQL，建立 `.sql` 文件並包含它們：`<sqlFile path="changes/create-users.sql" relativeToChangelogFile="true"/>`。
- **疑難排解**：檢查日誌中的錯誤（例如以 `liquibase` 為前綴的日誌）。確保數據庫 URL 正確。
- **生產環境**：如果您偏好，可以使用 Flyway，但 Liquibase 在處理複雜變更和多數據庫支持方面表現出色。

有關高級功能（如標記回滾或自定義擴展），請參閱文檔。

### 參考資料
- [Spring Boot Liquibase 自動配置](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#io.liquibase)
- [Liquibase 官方文檔](https://docs.liquibase.com/start/home.html)
- [Baeldung Spring Boot + Liquibase 教程](https://www.baeldung.com/liquibase-refactor-schema-of-jpa-entity-in-spring-boot)