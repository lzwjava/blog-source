---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 在 Spring Boot 中使用 H2 數據庫進行測試
translated: true
type: note
---

### 在 Spring Boot 的 JUnit 測試中使用 H2 數據庫

H2 是一款輕量級的內存數據庫，非常適合 Java 應用程式（特別是 Spring Boot）的單元測試和整合測試。它能讓您快速執行測試，無需設置外部數據庫。以下步驟假設您正在使用 Spring Boot 項目並搭配 JPA/Hibernate。如果您未使用 Spring，可以通過純 JDBC 使用 H2（請參閱文末說明）。

#### 步驟 1：添加 H2 依賴
在您的 `pom.xml`（Maven）或 `build.gradle`（Gradle）中加入 H2 依賴。請將其範圍設定為 `test`，以避免包含在生產環境中。

**Maven (`pom.xml`):**
```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>test</scope>
</dependency>
```

**Gradle (`build.gradle`):**
```gradle
testImplementation 'com.h2database:h2'
```

這將僅在測試執行時引入 H2 JAR。

#### 步驟 2：在測試屬性中配置 H2
創建或更新 `src/test/resources/application.properties`（或 `application-test.yml`），將其指向 H2。這將覆蓋生產數據庫的設定。

**application.properties:**
```
# H2 數據庫配置
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=

# H2 控制台（可選，用於調試）
spring.h2.console.enabled=true

# JPA/Hibernate 設定
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.jpa.hibernate.ddl-auto=create-drop
spring.jpa.show-sql=true
```

- `mem:testdb`：名為 "testdb" 的內存數據庫。
- `create-drop`：在啟動時自動創建表格，並在關閉時刪除它們。
- 在測試期間啟用 H2 控制台，網址為 `http://localhost:8080/h2-console`（使用 JDBC URL: `jdbc:h2:mem:testdb`）以便檢查。

如果使用配置檔，請在測試類中使用 `@ActiveProfiles("test")` 來激活。

#### 步驟 3：編寫 JUnit 測試
使用 `@SpringBootTest` 進行完整上下文測試，或使用 `@DataJpaTest` 進行以儲存庫為重點的測試。使用 `@Test` 註解並搭配 JUnit 5（`@ExtendWith(SpringExtension.class)`）。

**範例：測試 JPA 儲存庫**
假設您有一個 `Entity`，例如 `User`，以及一個擴展 `JpaRepository` 的 `UserRepository`。

```java
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.test.context.ActiveProfiles;

import static org.assertj.core.api.Assertions.assertThat;

@DataJpaTest  // 僅加載與 JPA 相關的 bean，以加快測試速度
@ActiveProfiles("test")  // 激活測試配置檔
public class UserRepositoryTest {

    @Autowired
    private UserRepository userRepository;

    @Test
    public void shouldSaveAndFindUser() {
        // Given
        User user = new User("John Doe", "john@example.com");
        userRepository.save(user);

        // When
        User foundUser = userRepository.findByEmail("john@example.com").orElse(null);

        // Then
        assertThat(foundUser).isNotNull();
        assertThat(foundUser.getName()).isEqualTo("John Doe");
    }
}
```

- `@DataJpaTest`：自動配置 H2 並在每個測試後回滾事務。
- 使用 `AssertJ` 或 `JUnit` 斷言進行驗證。
- 對於服務層測試，請使用 `@SpringBootTest` 並注入服務/儲存庫。

使用 `mvn test` 或您的 IDE 測試運行器來執行。每個測試都會從一個全新的數據庫開始。

#### 步驟 4：進階提示
- **Flyway/Liquibase 遷移**：如果使用架構遷移，請將其添加到 `src/test/resources`，H2 將會應用它們。
- **真實性測試**：H2 模擬大多數 SQL 方言，但可能與生產環境（例如 PostgreSQL）有所不同。為了更接近真實環境，可以考慮使用 Testcontainers 搭配真實的數據庫容器。
- **排除生產配置**：在 `pom.xml` 中，使用配置檔來排除測試中的真實數據庫驅動程式：
  ```xml
  <profile>
      <id>test</id>
      <dependencies>
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-data-jpa</artifactId>
              <exclusions>
                  <exclusion>
                      <groupId>mysql</groupId>  <!-- 或您的生產數據庫 -->
                      <artifactId>mysql-connector-java</artifactId>
                  </exclusion>
              </exclusions>
          </dependency>
      </dependencies>
  </profile>
  ```
- **疑難排解**：如果測試使用了生產數據庫，請確保 `spring.profiles.active=test` 或使用 `@TestPropertySource`。

#### 獨立 JUnit（無 Spring）
對於不使用 Spring 的純 JDBC：
1. 添加 H2 依賴（如上所述）。
2. 在您的測試中：
```java
import org.h2.jdbcx.JdbcDataSource;
import org.junit.jupiter.api.Test;

public class StandaloneH2Test {
    @Test
    public void testH2Connection() throws Exception {
        JdbcDataSource ds = new JdbcDataSource();
        ds.setURL("jdbc:h2:mem:test;DB_CLOSE_DELAY=-1");
        ds.setUser("sa");
        ds.setPassword("");

        try (Connection conn = ds.getConnection();
             Statement stmt = conn.createStatement()) {
            stmt.execute("CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(255))");
            stmt.execute("INSERT INTO users VALUES (1, 'Test User')");
            ResultSet rs = stmt.executeQuery("SELECT * FROM users");
            assertTrue(rs.next());
        }
    }
}
```
這將為每個測試創建一個內存數據庫。

更多詳細資訊，請參閱以下參考資料。

[Setting Up H2 for Testing in Spring Boot](https://medium.com/@paulkunda/setting-up-h2-for-testing-in-spring-boot-245d3a98e405)  
[Self-Contained Testing Using an In-Memory Database | Baeldung](https://www.baeldung.com/spring-jpa-test-in-memory-database)  
[Setting Up H2 for Testing in Spring Boot application](https://medium.com/@akshatakanaje08/setting-up-h2-for-testing-in-spring-boot-application-7f016220a475)  
[Test Spring Data Repositories with H2 in-memory database](https://www.geekyhacker.com/test-spring-data-repositories-with-h2-in-memory-database/)