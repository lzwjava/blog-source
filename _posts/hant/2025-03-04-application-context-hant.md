---
audio: false
generated: true
lang: hant
layout: post
title: 獲取Spring的ApplicationContext
translated: true
---

要使用 Spring 的 `ApplicationContextAware` 介面來訪問 `ApplicationContext` 於一個普通的 Java 物件，例如 Kafka 消費者，你需要一種方法來橋接 Spring 管理的 bean 與你的普通物件。以下是如何做到的：

### 一般方法
`ApplicationContextAware` 介面允許一個 Spring 管理的 bean 自動從 Spring 接收 `ApplicationContext`。你可以使用這個來使上下文可用於一個不由 Spring 管理的普通 Java 物件（即不是由 Spring 容器創建的 bean）。

#### 訪問 ApplicationContext 的步驟
1. **創建一個 Spring 管理的幫助類**：
   定義一個實現 `ApplicationContextAware` 並由 Spring 管理的類（例如，使用 `@Component` 注解）。這個類將在 Spring 應用啟動時接收 `ApplicationContext`。

   ```java
   import org.springframework.context.ApplicationContext;
   import org.springframework.context.ApplicationContextAware;
   import org.springframework.stereotype.Component;

   @Component
   public class ApplicationContextProvider implements ApplicationContextAware {
       private static ApplicationContext context;

       @Override
       public void setApplicationContext(ApplicationContext applicationContext) {
           context = applicationContext;
       }

       public static ApplicationContext getApplicationContext() {
           return context;
       }
   }
   ```

   - `@Component` 確保 Spring 管理這個 bean。
   - `setApplicationContext` 由 Spring 請求來注入 `ApplicationContext`。
   - 靜態的 `context` 變數和 getter 允許從任何地方訪問。

2. **在你的普通 Java 物件中訪問上下文**：
   在你的普通 Java 物件（例如，手動創建的 Kafka 消費者）中，使用幫助類來獲取 `ApplicationContext`，並使用它來獲取 Spring 管理的 bean。

   ```java
   public class MyKafkaConsumer {
       public void processMessage() {
           ApplicationContext context = ApplicationContextProvider.getApplicationContext();
           SomeService service = context.getBean(SomeService.class);
           // 使用服務或其他 bean 如需
       }
   }
   ```

   - 這樣做是因為 `ApplicationContextProvider` 在啟動時由 Spring 初始化，使上下文靜態可用。

3. **替代方法：明確傳遞上下文**：
   如果你的普通 Java 物件由一個 Spring 管理的 bean 創建，你可以將 `ApplicationContext` 自動注入到該 bean 中，並通過構造函數或設置器將其傳遞給普通物件。

   ```java
   import org.springframework.beans.factory.annotation.Autowired;
   import org.springframework.context.ApplicationContext;
   import org.springframework.stereotype.Component;

   @Component
   public class KafkaConsumerCreator {
       @Autowired
       private ApplicationContext context;

       public MyKafkaConsumer createConsumer() {
           return new MyKafkaConsumer(context);
       }
   }

   public class MyKafkaConsumer {
       private final ApplicationContext context;

       public MyKafkaConsumer(ApplicationContext context) {
           this.context = context;
       }

       public void processMessage() {
           SomeService service = context.getBean(SomeService.class);
           // 使用服務
       }
   }
   ```

   - 這樣可以避免靜態變數，使依賴明確並提高可測試性。

### Kafka 消費者特定解決方案
如果你正在使用 Kafka 消費者並使用 **Spring Kafka**，建議的方法是將消費者直接整合到 Spring 生態系統中，而不是將其視為普通 Java 物件。

#### 使用 `@KafkaListener`
將你的 Kafka 消費者定義為一個帶有 `@KafkaListener` 方法的 Spring 管理 bean。這樣可以直接自動注入 `ApplicationContext` 或其他 bean。

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

@Component
public class MyKafkaConsumer {
    @Autowired
    private ApplicationContext context;

    @Autowired
    private SomeService someService;

    @KafkaListener(topics = "my-topic")
    public void consume(String message) {
        // 直接使用 context 或 someService
        SomeService service = context.getBean(SomeService.class); // 如果需要
        someService.process(message);
    }
}
```

- Spring Kafka 管理消費者生命週期，包括線程和輪詢。
- 自動注入消除了手動獲取上下文的需求。

#### 手動 Kafka 消費者
如果你必須手動創建 `KafkaConsumer`（例如，直接使用 Kafka 客戶端庫），請在一個 Spring 管理的 bean 中進行，並將 `ApplicationContext` 傳遞給它，如上述明確傳遞方法所示。

### 建議
- **對於 Kafka 消費者**：在可能的情況下，使用 Spring Kafka 的 `@KafkaListener` 在一個 Spring 管理的 bean 中。這樣可以利用 Spring 與 Kafka 的整合，並簡化訪問 `ApplicationContext` 和其他 bean。
- **對於一般的普通 Java 物件**：使用靜態的 `ApplicationContextProvider` 方法或從一個 Spring 管理的 bean 明確傳遞 `ApplicationContext`。當可行時，明確傳遞方法是首選，因為它避免了靜態狀態並提高了可測試性。

通過這些方法，你可以有效地使用 `ApplicationContextAware` 使 Spring 上下文可用於你的普通 Java 物件，包括 Kafka 消費者，具體取決於你的設置。