---
audio: false
generated: true
lang: hant
layout: post
title: Spring Data REST 模組
translated: true
type: note
---

要使用 **spring-data-rest-core**，你可以利用 Spring Data REST 模組，將 Spring Data 儲存庫暴露為應用程式中的 RESTful 端點。以下是完整的逐步指南：

---

### 1. 添加 Spring Data REST 依賴項
要使用 Spring Data REST，你需要在專案中加入其依賴項。如果你使用 **Spring Boot**（常見情況），請在構建文件中添加以下依賴項：

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

這個 starter 會引入 `spring-data-rest-core` 以及其他必要組件。對於非 Spring Boot 專案，你可以直接引入 `spring-data-rest-core`，但建議使用 Spring Boot starter 以簡化流程。

---

### 2. 定義你的實體
使用持久化技術（如 JPA）定義實體類別來創建你的領域模型。例如：

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

    // 構造函數
    public User() {}
    public User(String name) {
        this.name = name;
    }

    // Getter 和 Setter
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

這個 `User` 實體代表數據庫中的一個簡單表格，包含 `id` 和 `name` 欄位。

---

### 3. 創建儲存庫介面
通過擴展 Spring Data 的儲存庫介面（例如 `JpaRepository`）來為你的實體定義儲存庫介面。例如：

```java
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
}
```

通過擴展 `JpaRepository`，你可以免費獲得基本的 CRUD 操作。Spring Data REST 會自動將此儲存庫暴露為 RESTful 端點。

---

### 4. 運行你的應用程式
添加依賴項並定義實體和儲存庫後，啟動你的 Spring Boot 應用程式。Spring Data REST 會根據你的儲存庫自動生成 REST 端點。對於上述的 `UserRepository`，你可以訪問：

- **GET /users**：檢索所有用戶的列表。
- **GET /users/{id}**：根據 ID 檢索特定用戶。
- **POST /users**：創建新用戶（使用 JSON 負載，例如 `{"name": "Alice"}`）。
- **PUT /users/{id}**：更新現有用戶。
- **DELETE /users/{id}**：刪除用戶。

例如，如果你的應用程式運行在 `localhost:8080`，你可以使用 `curl` 或瀏覽器進行測試：

```bash
curl http://localhost:8080/users
```

響應將包含 HATEOAS 鏈接，允許客戶端動態導航相關資源。

---

### 5. （可選）自定義 REST 端點
你可以使用註解或配置來自定義儲存庫的暴露方式：

- **更改端點路徑**：
  使用 `@RepositoryRestResource` 註解指定自定義路徑：
  ```java
  import org.springframework.data.rest.core.annotation.RepositoryRestResource;

  @RepositoryRestResource(path = "people")
  public interface UserRepository extends JpaRepository<User, Long> {
  }
  ```
  現在，端點將是 `/people` 而不是 `/users`。

- **配置全局設定**：
  通過實現 `RepositoryRestConfigurer` 來自定義基礎路徑或其他設定：
  ```java
  import org.springframework.data.rest.webmvc.config.RepositoryRestConfigurer;
  import org.springframework.context.annotation.Configuration;
  import org.springframework.data.rest.core.config.RepositoryRestConfiguration;

  @Configuration
  public class RestConfig implements RepositoryRestConfigurer {
      @Override
      public void configureRepositoryRestConfiguration(RepositoryRestConfiguration config) {
          config.setBasePath("/api"); // 所有端點將以 /api 開頭
      }
  }
  ```
  這樣，你的用戶將可通過 `/api/users` 訪問。

---

### Spring Data REST 的主要功能
- **HATEOAS 支持**：響應包含超媒體鏈接到相關資源。
- **分頁和排序**：使用查詢參數如 `?page=0&size=10&sort=name,asc` 來分頁和排序結果。
- **篩選**：在儲存庫中添加自定義查詢方法（例如 `findByName(String name)`）以暴露額外端點。

---

### 總結
要使用 `spring-data-rest-core`：
1. 包含 Spring Data REST 依賴項（例如 Spring Boot 的 `spring-boot-starter-data-rest`）。
2. 使用適當註解（例如 JPA 的 `@Entity`）定義你的實體。
3. 創建擴展 Spring Data 介面（例如 `JpaRepository`）的儲存庫介面。
4. 運行你的應用程式以訪問自動生成的 REST 端點。
5. 可根據需要自定義端點路徑或行為。

這種方法讓你能以最少的代碼快速構建 RESTful API，並充分利用 Spring Data REST 的核心功能。