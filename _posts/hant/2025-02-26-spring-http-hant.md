---
audio: false
generated: true
lang: hant
layout: post
title: 春季HTTP客戶端
translated: true
type: note
---

要回答「如何使用 FeignClient、Spring RestClient 或 Spring WebClient」這個問題，我將分別說明這些 Spring 工具如何用於發送 HTTP 請求，重點介紹它們的設定步驟和基本用法。這些工具都是 Spring 生態系中用於與 RESTful 服務互動的組件，但根據應用程式的需求各有不同的用途。下面我將為每個工具提供清晰的逐步指南和簡單範例。

---

### **1. 使用 FeignClient**
FeignClient 是 Spring Cloud 提供的宣告式 REST 客戶端。它允許你透過註解定義 HTTP 客戶端介面，特別適用於需要呼叫其他服務的微服務架構。

#### **使用 FeignClient 的步驟**
1. **添加依賴**：在專案中加入 Spring Cloud 依賴。若使用 Maven，請在 `pom.xml` 中添加 Spring Cloud Feign 起步依賴：
   ```xml
   <dependency>
       <groupId>org.springframework.cloud</groupId>
       <artifactId>spring-cloud-starter-openfeign</artifactId>
   </dependency>
   ```
   請確保同時設定了 Spring Cloud 的依賴管理區塊，並指定相容版本。

2. **啟用 Feign Clients**：在主應用程式類別或配置類別上添加 `@EnableFeignClients` 註解以啟動 Feign 支援：
   ```java
   import org.springframework.boot.SpringApplication;
   import org.springframework.boot.autoconfigure.SpringBootApplication;
   import org.springframework.cloud.openfeign.EnableFeignClients;

   @SpringBootApplication
   @EnableFeignClients
   public class MyApplication {
       public static void main(String[] args) {
           SpringApplication.run(MyApplication.class, args);
       }
   }
   ```

3. **定義 FeignClient 介面**：建立一個帶有 `@FeignClient` 註解的介面，指定服務名稱或 URL，並定義對應 REST 端點的方法：
   ```java
   import org.springframework.cloud.openfeign.FeignClient;
   import org.springframework.web.bind.annotation.GetMapping;
   import java.util.List;

   @FeignClient(name = "user-service", url = "http://localhost:8080")
   public interface UserClient {
       @GetMapping("/users")
       List<User> getUsers();
   }
   ```
   此處，`name` 是客戶端的邏輯名稱，`url` 是目標服務的基礎 URL。`@GetMapping` 註解對應到 `/users` 端點。

4. **注入並使用客戶端**：在服務或控制器中自動裝配該介面，並像呼叫本地方法一樣使用：
   ```java
   import org.springframework.beans.factory.annotation.Autowired;
   import org.springframework.stereotype.Service;
   import java.util.List;

   @Service
   public class UserService {
       @Autowired
       private UserClient userClient;

       public List<User> fetchUsers() {
           return userClient.getUsers();
       }
   }
   ```

#### **關鍵點**
- FeignClient 預設為同步模式。
- 在微服務架構中，若結合服務發現（如 Eureka），可省略 `url` 並讓 Spring Cloud 自動解析服務位置。
- 可透過 fallbacks 或斷路器（如 Hystrix 或 Resilience4j）添加錯誤處理機制。

---

### **2. 使用 Spring RestClient**
Spring RestClient 是 Spring Framework 6.1 引入的同步 HTTP 客戶端，作為已棄用的 `RestTemplate` 的現代化替代方案，提供流暢的 API 來建構和執行請求。

#### **使用 RestClient 的步驟**
1. **依賴**：RestClient 包含在 `spring-web` 模組中，該模組是 Spring Boot 的 `spring-boot-starter-web` 的一部分，通常無需額外依賴：
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-web</artifactId>
   </dependency>
   ```

2. **建立 RestClient 實例**：使用靜態方法 `create()` 實例化 `RestClient`，或透過建構器進行自訂設定：
   ```java
   import org.springframework.web.client.RestClient;

   RestClient restClient = RestClient.create();
   ```
   若需自訂配置（如超時設定），請使用 `RestClient.builder()`。

3. **建構並執行請求**：使用流暢 API 指定 HTTP 方法、URI、標頭和主體，然後獲取回應：
   ```java
   import org.springframework.http.MediaType;
   import org.springframework.web.client.RestClient;
   import java.util.List;

   public class UserService {
       private final RestClient restClient;

       public UserService() {
           this.restClient = RestClient.create();
       }

       public List<User> fetchUsers() {
           return restClient.get()
               .uri("http://localhost:8080/users")
               .accept(MediaType.APPLICATION_JSON)
               .retrieve()
               .body(new ParameterizedTypeReference<List<User>>() {});
       }
   }
   ```
   - `get()` 指定 HTTP 方法。
   - `uri()` 設定端點。
   - `accept()` 設定預期內容類型。
   - `retrieve()` 執行請求，`body()` 提取回應，使用 `ParameterizedTypeReference` 處理泛型類型（如列表）。

4. **處理回應**：由於 RestClient 是同步的，回應會直接返回。若需更多控制（如狀態碼），可使用 `toEntity()`：
   ```java
   import org.springframework.http.ResponseEntity;

   ResponseEntity<List<User>> response = restClient.get()
       .uri("http://localhost:8080/users")
       .accept(MediaType.APPLICATION_JSON)
       .retrieve()
       .toEntity(new ParameterizedTypeReference<List<User>>() {});
   List<User> users = response.getBody();
   ```

#### **關鍵點**
- RestClient 為同步客戶端，適用於傳統的阻塞式應用程式。
- 在 HTTP 錯誤時會拋出例外（如 `RestClientException`），可捕獲並處理。
- 是 `RestTemplate` 的替代方案，提供更直觀的 API。

---

### **3. 使用 Spring WebClient**
Spring WebClient 是 Spring WebFlux 引入的反應式、非阻塞 HTTP 客戶端，專為非同步操作設計，並與反應式流（Mono 和 Flux）整合。

#### **使用 WebClient 的步驟**
1. **添加依賴**：在專案中加入 WebFlux 依賴：
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-webflux</artifactId>
   </dependency>
   ```

2. **建立 WebClient 實例**：使用基礎 URL 或預設設定實例化 `WebClient`：
   ```java
   import org.springframework.web.reactive.function.client.WebClient;

   WebClient webClient = WebClient.create("http://localhost:8080");
   ```
   使用 `WebClient.builder()` 進行自訂配置（如編解碼器、過濾器）。

3. **建構並執行請求**：使用流暢 API 建構請求並獲取反應式回應：
   ```java
   import org.springframework.http.MediaType;
   import org.springframework.web.reactive.function.client.WebClient;
   import reactor.core.publisher.Mono;
   import java.util.List;

   public class UserService {
       private final WebClient webClient;

       public UserService(WebClient webClient) {
           this.webClient = webClient;
       }

       public Mono<List<User>> fetchUsers() {
           return webClient.get()
               .uri("/users")
               .accept(MediaType.APPLICATION_JSON)
               .retrieve()
               .bodyToFlux(User.class)
               .collectList();
       }
   }
   ```
   - `bodyToFlux(User.class)` 處理 `User` 物件流。
   - `collectList()` 將 `Flux<User>` 轉換為 `Mono<List<User>>`。

4. **訂閱回應**：由於 WebClient 是反應式的，必須訂閱 `Mono` 或 `Flux` 以觸發請求：
   ```java
   Mono<List<User>> usersMono = fetchUsers();
   usersMono.subscribe(users -> System.out.println(users));
   ```
   或在反應式管道中鏈接，或使用阻塞呼叫（不建議在反應式情境中使用）：
   ```java
   List<User> users = fetchUsers().block();
   ```

#### **關鍵點**
- WebClient 是非阻塞的，適用於基於 Spring WebFlux 的反應式應用程式。
- 使用 `Mono` 處理單值回應，`Flux` 處理多值回應。
- 可透過運算子如 `onErrorResume()` 或 `retry()` 進行錯誤處理。

---

### **比較與適用場景**
- **FeignClient**：適用於微服務架構中的宣告式、基於介面的客戶端。它是同步的，能簡化服務間呼叫。
- **RestClient**：適用於傳統阻塞式 Spring 應用程式中的同步 HTTP 請求。它是 `RestTemplate` 的現代化替代方案。
- **WebClient**：適用於 WebFlux 基礎的反應式應用程式，或需要處理高併發的非阻塞 HTTP 請求。

---

### **範例：呼叫 POST 端點**
假設你需要透過呼叫 `POST /users` 並傳入 `User` 物件來建立使用者。

#### **FeignClient**
```java
@FeignClient(name = "user-service", url = "http://localhost:8080")
public interface UserClient {
    @PostMapping("/users")
    User createUser(@RequestBody User user);
}

@Service
public class UserService {
    @Autowired
    private UserClient userClient;

    public User createUser(User user) {
        return userClient.createUser(user);
    }
}
```

#### **RestClient**
```java
@Service
public class UserService {
    private final RestClient restClient = RestClient.create();

    public User createUser(User user) {
        return restClient.post()
            .uri("http://localhost:8080/users")
            .contentType(MediaType.APPLICATION_JSON)
            .body(user)
            .retrieve()
            .body(User.class);
    }
}
```

#### **WebClient**
```java
@Service
public class UserService {
    private final WebClient webClient;

    public UserService(WebClient webClient) {
        this.webClient = WebClient.create("http://localhost:8080");
    }

    public Mono<User> createUser(User user) {
        return webClient.post()
            .uri("/users")
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(user)
            .retrieve()
            .bodyToMono(User.class);
    }
}
```

---

### **總結**
- **FeignClient**：定義介面，啟用後即可像本地 Bean 一樣使用。
- **RestClient**：透過流暢方式建構請求，並同步獲取回應。
- **WebClient**：透過流暢方式建構請求，獲取反應式流，並非同步處理。

請根據應用程式架構選擇：FeignClient 用於微服務，RestClient 用於阻塞式應用，WebClient 用於反應式應用。每種工具都遵循如上所示的直覺設定和使用模式。