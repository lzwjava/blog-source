---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Flyway 數據庫遷移指南
translated: true
type: note
---

### Flyway 簡介
Flyway 是一款熱門的開源工具，用於以版本控制方式管理數據庫結構遷移。它能讓你以可重複且安全的方式，對數據庫應用增量變更（例如建立資料表、修改欄位或插入資料）。在 Java 應用程式中，Flyway 可透過其 API 整合，通常在應用程式啟動時執行，以確保在程式碼與數據庫互動前，其結構已處於最新狀態。它透過 JDBC 與大多數數據庫協同工作（例如 PostgreSQL、MySQL、Oracle）。

### 步驟 1：加入 Flyway 相依項目
將 Flyway 加入至你的建置檔案。除非需要企業版功能，否則請使用開源版本。

**Maven (`pom.xml`)**：
```xml
<dependencies>
    <dependency>
        <groupId>org.flywaydb</groupId>
        <artifactId>flyway-core</artifactId>
        <version>11.14.1</version> <!-- 請檢查最新版本 -->
    </dependency>
    <!-- 加入你的數據庫 JDBC 驅動程式，例如 PostgreSQL -->
    <dependency>
        <groupId>org.postgresql</groupId>
        <artifactId>postgresql</artifactId>
        <version>42.7.3</version>
    </dependency>
</dependencies>
```

**Gradle (`build.gradle`)**：
```groovy
dependencies {
    implementation 'org.flywaydb:flyway-core:11.14.1'
    // 加入你的數據庫 JDBC 驅動程式
    implementation 'org.postgresql:postgresql:42.7.3'
}
```

你還需要目標數據庫的 JDBC 驅動程式。

### 步驟 2：設定 Flyway
Flyway 使用流暢 API 進行設定。關鍵設定包括數據庫連線詳細資料、遷移腳本的位置，以及可選的回呼設定。

在你的 Java 程式碼中，建立一個 `Flyway` 實例：
```java
import org.flywaydb.core.Flyway;

public class DatabaseMigration {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/mydb";
        String user = "username";
        String password = "password";

        Flyway flyway = Flyway.configure()
                .dataSource(url, user, password)
                .locations("classpath:db/migration")  // 存放 SQL 腳本的資料夾（預設：db/migration）
                .load();
    }
}
```
- `locations`：指向存放遷移檔案的位置（例如，classpath 中的 `src/main/resources/db/migration`）。
- 其他常見設定：`.baselineOnMigrate(true)` 用於基線化現有結構，或 `.table("flyway_schema_history")` 用於自訂歷史記錄資料表。

### 步驟 3：撰寫遷移腳本
遷移腳本是 SQL 檔案，放置於設定的位置（例如 `src/main/resources/db/migration`）。Flyway 會依序應用這些腳本。

#### 命名慣例
- **版本化遷移**（用於一次性結構變更）：`V<版本>__<描述>.sql`（例如 `V1__Create_person_table.sql`、`V2__Add_age_column.sql`）。
  - 版本格式：使用底線分隔區段（例如 `V1_1__Initial.sql`）。
- **可重複遷移**（用於持續性任務，例如視圖）：`R__<描述>.sql`（例如 `R__Update_view.sql`）。這些腳本在內容變更時每次都會執行。
- 檔案依字典順序應用。

#### 範例腳本
在 `src/main/resources/db/migration` 中建立以下檔案。

**V1__Create_person_table.sql**：
```sql
CREATE TABLE person (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO person (id, name) VALUES (1, 'John Doe');
```

**V2__Add_age_column.sql**：
```sql
ALTER TABLE person ADD COLUMN age INT;
```

**R__Populate_names.sql**（可重複）：
```sql
UPDATE person SET name = CONCAT(name, ' (Updated)') WHERE id = 1;
```

Flyway 在 `flyway_schema_history` 資料表中追蹤已應用的遷移。

對於不適合使用 SQL 的複雜邏輯，可使用基於 Java 的遷移（實作 `org.flywaydb.core.api.migration.java.JavaMigration`）。

### 步驟 4：以程式方式執行遷移
呼叫 `migrate()` 來應用待處理的遷移。將此整合至你的應用程式啟動流程中（例如在 `main()` 或 Spring 的 `@PostConstruct` 中）。

```java
import org.flywaydb.core.Flyway;
import org.flywaydb.core.api.FlywayException;

public class DatabaseMigration {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/mydb";
        String user = "username";
        String password = "password";

        Flyway flyway = Flyway.configure()
                .dataSource(url, user, password)
                .locations("classpath:db/migration")
                .load();

        try {
            flyway.migrate();  // 應用所有待處理的遷移
            System.out.println("數據庫遷移成功！");
        } catch (FlywayException e) {
            System.err.println("遷移失敗：" + e.getMessage());
            // 處理錯誤（例如退出或回滾）
        }

        // 現在啟動應用程式的其餘部分
    }
}
```

- `migrate()`：依序應用版本化遷移，然後是可重複遷移。
- 其他指令：`flyway.info()` 用於檢查狀態，`flyway.repair()` 用於修復問題，`flyway.validate()` 用於檢查一致性。
- 在進行任何數據庫操作前執行此步驟，以確保結構相容性。

### 最佳實踐
- 保持遷移的冪等性（可安全重新執行）。
- 在生產數據的副本上測試遷移。
- 對遷移檔案使用版本控制。
- 對於 Spring Boot，請加入 `spring-boot-starter-jdbc` 並在 `application.properties` 中設定 `spring.flyway.enabled=true` 以啟用自動設定。

### 參考資料
- [Flyway API (Java) 文件](https://documentation.red-gate.com/fd/api-java-277579358.html)
- [Flyway 遷移文件](https://documentation.red-gate.com/fd/migrations-271585107.html)
- [Flyway 入門指南](https://documentation.red-gate.com/fd/getting-started-with-flyway-184127223.html)