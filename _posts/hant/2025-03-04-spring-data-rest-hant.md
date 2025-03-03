---
audio: false
generated: true
lang: hant
layout: post
title: Spring Data REST 模組
translated: true
---

要使用 **spring-data-rest-core**，你可以利用 Spring Data REST 模組將你的 Spring Data 存儲庫暴露為應用程式中的 RESTful 端點。以下是一個完整的、逐步指南，幫助你開始：

---

### 1. 添加 Spring Data REST 依賴
要使用 Spring Data REST，你需要在項目中包含其依賴。如果你使用 **Spring Boot**（常見情況），將以下依賴添加到你的構建文件中：

- **Maven**：
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-data-rest</artifactId>
  </dependency>
  ```

- **Gradle**：
  ```gradle
  implementation 'org.springframework.boot:spring-boot-starter-data-rest'
  ```

這個啟動器會帶來 `spring-data-rest-core` 以及其他必要的組件。對於非 Spring Boot 專案，你可以直接包含 `spring-data-rest-core`，但建議使用 Spring Boot 啟動器以簡化操作。

---

### 2. 定義你的實體
通過使用持久化技術（如 JPA）來定義實體類，創建你的域模型。例如：

```java
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.GeneratedValue;

@Entity
public class User {
    @Id
    @GeneratedValue
    private Long id;
    private String name;

    // 建構函數
    public User() {}
    public User(String name) {
        this.name = name;
    }

    // Getters 和 Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

這個 `User` 實體代表數據庫中的簡單表，包含 `id` 和 `name`。

---

### 3. 創建存儲庫介面
通過擴展 Spring Data 的存儲庫介面（如 `JpaRepository`）來定義實體的存儲庫介面。例如：

```java
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
}
```

通過擴展 `JpaRepository`，你可以免費獲得基本的 CRUD（創建、讀取、更新、刪除）操作。Spring Data REST 會自動將這個存儲庫暴露為 RESTful 端點。

---

### 4. 運行你的應用程式
添加依賴並定義實體和存儲庫後，啟動你的 Spring Boot 應用程式。Spring Data REST 會根據你的存儲庫自動生成 REST 端點。對於上述的 `UserRepository`，你可以訪問：

- **GET /users**：檢索所有用戶的列表。
- **GET /users/{id}**：通過 ID 檢索特定用戶。
- **POST /users**：創建新用戶（使用 JSON 載荷，例如 `{"name": "Alice"}`）。
- **PUT /users/{id}**：更新現有用戶。
- **DELETE /users/{id}**：刪除用戶。

例如，如果你的應用程式運行在 `localhost:8080`，你可以使用工具（如 `curl`）或瀏覽器進行測試：

```bash
curl http://localhost:8080/users
```

響應將包括 HATEOAS 鏈接，允許客戶端動態導航相關資源。

---

### 5. （可選）自定義 REST 端點
你可以使用註解或配置來自定義存儲庫的暴露方式：

- **更改端點路徑**：
  使用 `@RepositoryRestResource` 注解來指定自定義路徑：
  ```java
  import org.springframework.data.rest.core.annotation.RepositoryRestResource;

  @RepositoryRestResource(path = "people")
  public interface UserRepository extends JpaRepository<User, Long> {
  }
  ```
  現在，端點將是 `/people` 而不是 `/users`。

- **配置全局設置**：
  通過實現 `RepositoryRestConfigurer` 來自定義基礎路徑或其他設置：
  ```java
  import org.springframework.data.rest.webmvc.config.RepositoryRestConfigurer;
  import org.springframework.context.annotation.Configuration;
  import org.springframework.data.rest.core.config.RepositoryRestConfiguration;

  @Configuration
  public class RestConfig implements RepositoryRestConfigurer {
      @Override
      public void configureRepositoryRestConfiguration(RepositoryRestConfiguration config) {
          config.setBasePath("/api"); // 所有端點都將以 /api 開頭
      }
  }
  ```
  使用這個配置，你的用戶將可在 `/api/users` 訪問。

---

### Spring Data REST 的關鍵功能
- **HATEOAS 支持**：響應包括超媒體鏈接到相關資源。
- **分頁和排序**：使用查詢參數（如 `?page=0&size=10&sort=name,asc`）來分頁和排序結果。
- **篩選**：在存儲庫中添加自定義查詢方法（例如 `findByName(String name)`）以暴露額外的端點。

---

### 總結
要使用 `spring-data-rest-core`：
1. 包含 Spring Data REST 依賴（例如，對於 Spring Boot，使用 `spring-boot-starter-data-rest`）。
2. 使用適當的註解（例如，對於 JPA，使用 `@Entity`）來定義你的實體。
3. 創建擴展 Spring Data 介面（例如 `JpaRepository`）的存儲庫介面。
4. 運行你的應用程式以訪問自動生成的 REST 端點。
5. 根據需要自定義端點路徑或行為。

這種方法允許你快速構建 RESTful API，利用 Spring Data REST 的核心功能。