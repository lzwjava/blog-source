---
audio: false
generated: true
lang: hant
layout: post
title: 存取 Spring 應用程式上下文
translated: true
type: note
---

要使用 Spring 的 `ApplicationContextAware` 介面在普通 Java 物件（例如 Kafka 消費者）中存取 `ApplicationContext`，您需要一種橋接 Spring 管理 Bean 與普通物件的方法。以下是實現方式：

### 通用方法
`ApplicationContextAware` 介面允許 Spring 管理的 Bean 自動從 Spring 接收 `ApplicationContext`。您可以使用此功能讓非 Spring 管理（即不是由 Spring 容器建立的 Bean）的普通 Java 物件也能使用該上下文。

#### 存取 ApplicationContext 的步驟
1. **建立 Spring 管理的輔助類別**：
   定義一個實作 `ApplicationContextAware` 並由 Spring 管理的類別（例如使用 `@Component` 註解）。此類別將在 Spring 應用程式啟動時接收 `ApplicationContext`。

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

   - `@Component` 確保 Spring 管理此 Bean。
   - `setApplicationContext` 由 Spring 呼叫以注入 `ApplicationContext`。
   - 靜態 `context` 變數和 getter 方法允許從任何地方存取。

2. **在普通 Java 物件中存取上下文**：
   在您的普通 Java 物件（例如手動建立的 Kafka 消費者）中，使用輔助類別取得 `ApplicationContext`，並用它來獲取 Spring 管理的 Bean。

   ```java
   public class MyKafkaConsumer {
       public void processMessage() {
           ApplicationContext context = ApplicationContextProvider.getApplicationContext();
           SomeService service = context.getBean(SomeService.class);
           // 按需使用服務或其他 Bean
       }
   }
   ```

   - 此方法有效是因為 `ApplicationContextProvider` 在啟動時由 Spring 初始化，使上下文可透過靜態方式取得。

3. **替代方法：明確傳遞上下文**：
   如果您的普通 Java 物件是由 Spring 管理的 Bean 所建立，您可以將 `ApplicationContext` 自動裝配到該 Bean 中，並透過建構函式或 setter 傳遞給普通物件。

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

   - 此方法避免了靜態變數，使依賴關係更明確並提高可測試性。

### Kafka 消費者專屬解決方案
如果您正在使用 Kafka 消費者並採用 **Spring Kafka**，建議的方法是直接將消費者整合到 Spring 生態系統中，而不是將其視為普通 Java 物件。

#### 使用 `@KafkaListener`
將您的 Kafka 消費者定義為帶有 `@KafkaListener` 方法的 Spring 管理 Bean。這允許您直接自動裝配 `ApplicationContext` 或其他 Bean。

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
        SomeService service = context.getBean(SomeService.class); // 如有需要
        someService.process(message);
    }
}
```

- Spring Kafka 管理消費者的生命週期，包括執行緒和輪詢。
- 在大多數情況下，自動裝配消除了手動取得上下文的需求。

#### 手動建立 Kafka 消費者
如果必須手動建立 `KafkaConsumer`（例如直接使用 Kafka 客戶端庫），請在 Spring 管理的 Bean 中建立，並將 `ApplicationContext` 傳遞給它，如上文所述的明確傳遞方法。

### 建議
- **對於 Kafka 消費者**：盡可能使用 Spring Kafka 的 `@KafkaListener` 並將其定義為 Spring 管理的 Bean。這能充分利用 Spring 與 Kafka 的整合，並簡化對 `ApplicationContext` 和其他 Bean 的存取。
- **對於一般普通 Java 物件**：使用靜態 `ApplicationContextProvider` 方法或從 Spring 管理的 Bean 明確傳遞 `ApplicationContext`。在可行的情况下，優先選擇明確傳遞方法，因為它避免了靜態狀態並提高了可測試性。

透過這些方法，您可以根據具體設定，有效利用 `ApplicationContextAware` 讓 Spring 上下文可供您的普通 Java 物件（包括 Kafka 消費者）使用。